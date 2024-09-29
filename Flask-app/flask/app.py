from flask import Flask
'''
It creates an instance of the flask Class,
which will be your WSGI (Web Server gateway Interface) application.
'''
### WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to Flask Framework. Woahh !! "

@app.route("/index")
def index():
    return "Hola! Bonjour "


if __name__=="__main__":   ## Entry point of this particular application
    app.run(debug=True)