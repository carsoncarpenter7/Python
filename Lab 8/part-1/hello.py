# Carson Carpenter
# CPSC 223P-03
# 2020-11-19
# carson.carpenter7@csu.fullerton.edu
#
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/<name>')
@app.route('/', methods=['GET','POST'])
def hello_world(name='World!'):
    return render_template('home.html', templatename=name)
    #return '<html>Hello World!</html>'
    #return '<html><h1>Hello, World!</h1><p>This is so cool!</p></html>'
