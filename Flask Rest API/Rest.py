from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Index!"

@app.route("/hello")
def hellp():
        return "Hello World!"

@app.route("/members")
def members():
        return "Members"

#@app.route("/members/<members:name>/")
#def getMember(name):
        return name<members:name\>

if __name__ == "__main__": app.run()
