#!/usr/bin/python

from app import app
@app.route('/')
@app.route('/index')

def index():
    user = {'nickname':'Miguel'}#fake user
   
    return '''
<html>
 <head>
   <title>Home page</title>
 </head>
 <body>
  <h1>hello, ''' + user['nickname'] + '''</h1>
 </body>
</html>
 ''' 
                           
              
