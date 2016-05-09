#!/usr/bin/python

from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'nickname':'Marcus'}
    return '''
<html>
   <head>
    <title>Home Page</title>
    </head>
    <body>
    <h1>Hello, ''' + user['nickname'] +'''</h1>
   </body>
  </html>
'''  
