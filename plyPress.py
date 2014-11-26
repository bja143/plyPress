from flask import Flask, request
from flask.templating import render_template


app = Flask('flyPress')

@app.route('/install', methods=['GET', 'POST'])
def install_flyPress():
    if request == 'POST':
        pass
    else:
        render_template("installer.html") 