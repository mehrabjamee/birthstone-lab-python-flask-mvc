# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
import model


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/birthstone', methods=['GET', 'POST'])
def birthstone():
    print(request.form)
    props = model.get_stone(request.form)
    return render_template('results.html', props=props)
