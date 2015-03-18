require "wombat"
# Wombat.crawl do
#     base_url "http://www.researchgate.net/profile/Eachan_Johnson"
#     keywords "css=a.keyword-list-token-text", :list
# end
require 'json'
require 'elasticsearch'


def crawl_profile(url)
    sleep 5
    data = Wombat.crawl do
        base_url "http://www.researchgate.net"
        path "/#{url}"
        interests "css=a.keyword-list-token-text", :list
    end
    sleep 5
    pubs = Wombat.crawl do
        base_url "http://www.researchgate.net"
        path "/#{url}/publications"
        publications "css=span.publication-title", :list
        publications_authors 'xpath=//a[@class="authors"]/@href', :list
    end
    data = data.merge(pubs)
    return data
end





def crawl(dep, page)
    done_pages = []
    data = Wombat.crawl do
       base_url "http://www.researchgate.net"
       path "/institution/University_of_Oxford/department/#{dep}/members/#{page}"
       people "css=div.indent-content>h5", :iterator do
          name "css=a"
          link xpath: "a/@href"
       end
    end
    return data
end




depts = [
"Department_of_Chemistry",
"Department_of_Physiology_Anatomy_and_Genetics",
"Department_of_Biochemistry",
"Nuffield_Department_of_Clinical_Medicine",
"Nuffield_Department_of_Clinical_Neurosciences",
"Department_of_Psychiatry",
"Wellcome_Trust_Centre_for_Human_Genetics2",
"Division_of_Medical_Sciences",
"Weatherall_Institute_of_Molecular_Medicine",
"Department_of_Pharmacology",
"Department_of_Oncology",
"Jenner_Institute",
"Nuffield_Division_of_Clinical_Laboratory_Sciences",
"Division_of_Structural_Biology_STRUBI",
"Kennedy_Institute_of_Rheumatology",
"Clinical_Trial_Service_Unit_and_Epidemiological_Studies_Unit_CTSU",
"Institute_of_Biomedical_Engineering",
"Structural_Genomics_Consortium_SGC",
"SGC_Oxford_Structural_Genomics_Consortium",
"Centre_for_Cellular_and_Molecular_Physiology_CCMP",
"Sir_William_Dunn_School_of_Pathology"]



full_data = []
client = Elasticsearch::Client.new

for dep in depts
    puts dep
    depmembers = Hash.new
    for page in 1..30
    	data = crawl(dep, page)
        newcount = 0
        for person in data["people"]
            if !depmembers.has_key?(person["link"])
                person["department"] = dep
		begin
		    persondata = crawl_profile(person["link"])
                rescue  ResponseCodeError
                    sleep 120
                    begin
                         persondata = crawl_profile(person["link"])
                    rescue  ResponseCodeError
                         next
                    end
		end
		puts person
                person = person.merge(persondata)

                newcount += 1
                client.index  index: 'people', type: 'person', id: person["link"], body: person
                depmembers[person["link"]] = person
            end
        end
        if newcount == 0
           break
        end
    end
end


#full_data.push({"dept" => depts[0], "members" => crawl(depts[0]) })


