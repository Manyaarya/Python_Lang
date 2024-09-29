from flask import Flask, render_template
## Responsible for redirecting to entire webpage.
'''
It creates an instance of the flask Class,
which will be your WSGI (Web Server gateway Interface) application.
'''
### WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/index")
def index():
    return "Hola! Bonjour "

@app.route("/about")
def about():
    return render_template("about.html")


if __name__=="__main__":   ## Entry point of this particular application
    app.run(debug=True)