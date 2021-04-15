import pandas as pd
from flask import Flask, render_template, request, Response, url_for
from model import model
app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/result', methods=['POST','GET'])
def result():
    name = request.form.get("var_2", type=str)
    name1 = request.form.get("var_3", type=str)
    ret = model(name,name1)
    return render_template('index.html', pred="{}".format(ret))


if __name__ == '_main_':
    app.run(debug=True)