curl -XPOST localhost:9200/people -d '{
    "settings" : {
        "number_of_shards" : 2
    },
    "mappings" : {
        "person" : {
		"properties" : {
		    "interests" : {
		        "type" : "multi_field",
		        "fields" : {
		            "interests" : {"type" : "string", "index" : "analyzed"},
		            "interests_untouched" : {"type" : "string", "index" : "not_analyzed"}
		        }
		    },
		    "name" :{
		          "type" : "string",
		          "index" : "not_analyzed"
		    },
		    "link" :{
		          "type" : "string",
		          "index" : "not_analyzed"
		    },
		    "department" :{
		          "type" : "string",
		          "index" : "not_analyzed"
		    },
                    "publications_authors" :{
		          "type" : "string",
		          "index" : "not_analyzed"
		    }, 
                    "publications" :{
		          "type" : "string",
		          "index" : "analyzed"
		    }
		}
	}
    }

}'
