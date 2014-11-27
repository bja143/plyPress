from flask import Flask, request, redirect, url_for
from flask.templating import render_template


app = Flask('flyPress')

#when the application is run for the first time it has to set up files on the system
#this is the function used to do so

#implement the installer later

# @app.route('/install', methods=['GET', 'POST'])
# def install_flyPress():
#     if request.method == 'POST':
#         pass
#     else:
#         render_template("installer.html")

#when the user logs into the system this method is executed
@app.route('/login', methods=['GET', 'POST'])

def valid_login(username, password):
    pass


def login():
    error = None
    if request.method=='POST':
        if valid_login(request.form['username'], request.form['password']):
            return redirect(url_for('home'))
        else:
            error = 'Invalid credentials'
    
    
    return render_template('login.html', error=error)

#after successful login the user is redirected to the news feed
@app.route('/home', methods=['GET'])
def show_feed():
    #get data from dbms
    render_template("home.html")

#invoked while adding a new post
@app.route('new', methods=['GET'])
def new_post():
    render_template('new_post.html')
    
    
if __name__=='__main__':
    app.run(debug=True)