from flask import Flask, request, url_for, render_template, session
import config


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
    if request.method=='POST':
        if valid_login(request.form['username'], request.form['password']):
            #session['logged_in'] = True
            return render_template("dashboard.html")
        else:
            error = 'Invalid credentials'
            return render_template('dashboard.html', error=error)
    else:
        return render_template('login.html', title=TITLE)

def valid_login(username, password):
    if username== USERNAME and password==PASSWORD:
        return True
    else:
        return False

#after successful login the user is redirected to the news feed
@app.route("/")
@app.route('/home', methods=['GET'])
def show_feed():
    #get data from dbms
    return render_template("index.html", title=TITLE)

#invoked while adding a new post
@app.route('/new', methods=['GET'])
def new_post():
    return render_template('post.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template("contact.html", title=TITLE)

@app.route('/about', methods=['GET'])
def about():
    return render_template("about.html", title=TITLE)

@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template("dashboard.html")

@app.route("/post/<postid>")
def show_post(postid=None):
    if postid==None:
        return render_template("404.html", 404)
    
    return render_template("show_post.html")

