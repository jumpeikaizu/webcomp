import sys
from flask import Flask, redirect, request, render_template, url_for
from wtforms import Form, StringField
from wtforms.validators import DataRequired
from hotpepper import hotpepper
from geocoding import geocoding
reload(sys)
sys.setdefaultencoding("utf-8")

app = Flask(__name__)

class addressform(Form):
    address = StringField('input_address', validators=[DataRequired()])

@app.route('/')
def index():
    form = addressform()
    return render_template('index.html',form=form,flag=0) 

@app.route('/post', methods=["POST"])
def post():
    form = addressform(request.form)
    shop = hotpepper(geocoding(form.address.data))
    return render_template('index.html',form=form,shop=shop,flag=1)

def main(address):
    hotpepper(geocoding(address))

if "__main__" == __name__:
    #main(sys.argv[1].encode("utf-8"))
    app.run(debug=True)
