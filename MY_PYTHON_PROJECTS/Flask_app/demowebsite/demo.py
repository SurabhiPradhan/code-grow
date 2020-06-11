#importing flask class from flask framework
from flask import Flask, render_template

# variable to store object instance of Flask class
app = Flask(__name__)

@app.route('/')                                           # This is a decorator. '/' means homepage
def homepage():
    return render_template("homepage.html")               # The output that this function produces will be mapped to the above url


@app.route('/about_Me/')
def about():
    return render_template("aboutpage.html")

if __name__ =="__main__":
    app.run(debug=True)
