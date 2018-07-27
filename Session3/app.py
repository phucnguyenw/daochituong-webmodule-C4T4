from flask import Flask

app=Flask(__name__)
@app.route("/hello/<name>")
def index(name):
    return "Hello {0}".format(name)

@app.route("/add/<int:a>/<int:b>")
def sum(a,b):
    return "{0} + {1} = {2}".format(a,b,a+b)
       

if __name__ == "__main__":
    app.run(debug=True)

