import github3
import os

@route('/issues/create', method='POST')
def create_issue():

    labels   = request.forms.get('labels')
    upload     = request.files.get('upload')
    repo = request.forms.get('repo')
    name, ext = os.path.splitext(upload.filename)
    gh.create_issue( "strets123", repo, title, body=body, assignee=None,
                     milestone=None, labels=["dsadszdfsdf","fdsfdsfgkdflgj"])
    return 'OK'
    
    
run(app, host='localhost', port=8999)