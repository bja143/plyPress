# -*- coding: utf-8 -*-

from flask import Flask, request, url_for, render_template, session, redirect
from plySrc.models import fetch_posts, insert_post, fetch_post_by_id
from plySrc import app
from plySrc.config import PASSWORD, USERNAME, TITLE, secret_key

app.secret_key = secret_key

#implement the installer later

# @app.route('/install', methods=['GET', 'POST'])
# def install_flyPress():
#     if request.method == 'POST':
#         pass
#     else:
#         render_template("installer.html")

#when the user logs into the system this method is executed
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method=='POST' and session['logged_in'] == False:
        if valid_login(request.form['username'], request.form['password']):
            session['logged_in'] = True
            return render_template("dashboard.html")
        else:
            error = 'Invalid credentials'
            return render_template('dashboard.html', error=error)
    elif session['logged_in']==True:
        redirect(url_for(dashboard, 400))
    else:
        return render_template('login.html', title=TITLE)

@app.route('/logout', methods=['GET'])
def logout():
    session.pop(USERNAME)
    session['logged_in'] = False
    
def valid_login(username, password):
    if username== USERNAME and password==PASSWORD:
        return True
    else:
        return False
    
posts= [] # get all posts from db

post_content={ }

#after successful login the user is redirected to the news feed
@app.route("/")
@app.route('/home', methods=['GET'])
def show_feed():
    #get data from dbms
    posts = fetch_posts()
    return render_template("index.html", title=TITLE, posts=posts)

#invoked while adding a new post
@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if session['logged_in']==True:
        
        if request.method=='GET':
            return render_template('post.html')
        else:
            title= request.form['title']
            subtitle= request.form['subtitle']
            text= request.form['text']
            username = USERNAME
            from datetime import date
            to = date.today()
            date=to.strftime("%B %d %Y")
            
            post = {
                    'title':title, 'subtitle':subtitle, 'text':text,
                    'date':date, 'username':username              
                    }
            
            insert_post(post)
            
            render_template('post.html', post=post)
    else:
        redirect(url_for(login, 403))
        

@app.route('/contact', methods=['GET'])
def contact():
    return render_template("contact.html", title=TITLE)

@app.route('/about', methods=['GET'])
def about():
    return render_template("about.html", title=TITLE)

@app.route('/dashboard', methods=['GET'])
def dashboard():
    if session['logged_in']==True:
        return render_template("dashboard.html")
    else:
        redirect(url_for(login), 403)

@app.route('/post/<postid>')
def show_post(postid):
    post_content = fetch_post_by_id(postid)
    return render_template("show_post.html",post=post_content)
