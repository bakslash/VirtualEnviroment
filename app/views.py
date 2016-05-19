from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'Miguel'} # fake user
    posts = [# fake array of posts
        {
          'author': {'nickname':'john'},
          'body': 'Beautiful day in portland'
        },
        {
           'author': {'nickname':'susan'},  
           'body': 'The Avengers movies was so cool!'
        }  
   ]
    return render_template("index.html",title='Home',user=user,posts=posts)
 
