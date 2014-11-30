from flask import Flask
import config
import models
import views


#create the application
app = Flask(__name__)
app.config.from_object(__name__)

if __name__=='__main__':
    app.run(debug=True)

