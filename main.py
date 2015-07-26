# -*- coding: utf-8 -*-
import sys
from flask import Flask, redirect, request, render_template
from wtforms import Form, TextField
from wtforms.validators import Required
from hotpepper import hotpepper
from geocoding import geocoding
reload(sys)
sys.setdefaultencoding("utf-8")

app = Flask(__name__)

class addressform(Form):
    address = TextField('input_address', validators=[Required()])

@app.route('/')
def index():
    form = addressform()
    return render_template('index.html',form=form,shop=0) 

@app.route('/post', methods=["POST"])
def post():
    form = addressform(request.form)
    latlng = geocoding(form.address.data)
    if request.method == 'POST' and form.validate() and latlng!=0:
        food,shop = hotpepper(latlng)
        address = form.address.data
        form = addressform()
        return render_template('index.html',form=form,address=address,food=food,shop=shop)
    else:
        form=addressform()
        return render_template('index.html',form=form,shop=0,address=0)
        
def main(address):
    hotpepper(geocoding(address))

if "__main__" == __name__:
    #main(sys.argv[1].encode("utf-8"))
    app.run(debug=True)
