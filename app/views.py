from flask import render_template, flash, redirect
from app import app
from.forms import LoginForm

# index view function suppressed for brevity

@app.route('/login', methods=['GET','POST'])
def index():
    form = LoginForm()
    return render_template('login.html',title='Sign In',form=form)
 
