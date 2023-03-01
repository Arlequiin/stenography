from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("inkwell.html")
    
@app.route("/decode")
def decode():
    return render_template("decode.html")

@app.route("/encode")
def encode():
    return render_template("encode.html")
    

if __name__ == "__main__":
    app.run(debug=True)