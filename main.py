from flask import Flask, render_template
from script import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("inkwell.html")
    
@app.route("/decode")
def decode_page():
    return render_template("decode.html",decoded_text="Votre texte s'affichera ici.")

@app.route("/encode")
def encode_page():
    return render_template("encode.html")

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/encodage/<dropdown_value>/<textarea_value>")
def my_route(dropdown_value,textarea_value):
    d = {'peche':'1.png','riviere':'2.png','hiver':'3.png'}
    encode_text(textarea_value,'static/'+d[dropdown_value])
    return "Success"

@app.route("/decodage/<dropdown_value>")
def my_route2(dropdown_value):
    d = {'peche':'1.png','riviere':'2.png','hiver':'3.png'}
    print("Function detected")
    decoded=decode_text('static/'+d[dropdown_value])
    print(decoded)
    return decoded

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8080)