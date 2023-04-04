from flask import Flask,render_template

x = Flask(__name__,template_folder ="template")
@x.route("/")

def com():
    return "Welcome to python"

@x.route("/com2")

def com2():
    return "Welcome to flask"

@x.route("/com3")

def com3():
    name="manvitha"
    return render_template("index.html",index_variable = name)
 
x.run(debug=True)