# -*- coding: utf-8 -*-

from flask import Flask, request, url_for, render_template, session, redirect, flash
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
    if request.method == 'POST':
        if request.form['username'] != USERNAME:
            error = 'Invalid username'
        elif request.form['password'] != PASSWORD:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
    return render_template('login.html', error=error, title=TITLE)

@app.route('/logout', methods=['GET'])
def logout():
    if session.get('logged_in'):
        session.pop('logged_in', None)
        return render_template(url_for('show_feed'), 200)
    
posts= [] # get all posts from db

post_content={ }

#after successful login the user is redirected to the news feed
@app.route('/', methods=['GET'])
def show_feed():
    #get data from dbms
    posts = fetch_posts()
    return render_template("index.html", title=TITLE, posts=posts)

#invoked while adding a new post
@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method=='GET':
        return render_template('post.html')
    else:
        title= request.form['title']
        text= request.form['text']
        username = USERNAME
        from datetime import date
        to = date.today()
        date=to.strftime("%B %d %Y")
        
        post = {
                'title':title, 'text':text,
                'date':date, 'username':username              
                }
        
        insert_post(post)
        
        render_template('post.html', post=post)

@app.route('/contact', methods=['GET'])
def contact():
    return render_template("contact.html", title=TITLE)

@app.route('/about', methods=['GET'])
def about():
    return render_template("about.html", title=TITLE)

@app.route('/dashboard', methods=['GET'])
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        return render_template("dashboard.html")

@app.route('/post/<postid>')
def show_post(postid):
    post_content = fetch_post_by_id(postid)
    return render_template("show_post.html",post=post_content)
