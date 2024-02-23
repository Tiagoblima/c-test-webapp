from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__, template_folder='dist')


@app.route('/')
def index():
  
    return render_template('index.html')

@app.route('/projects')
def projects():
  
    return render_template('projects.html')


@app.route('/resume')
def resume():
  
    return render_template('resume.html')


@app.route('/contact')
def contact():
  
    return render_template('contact.html')