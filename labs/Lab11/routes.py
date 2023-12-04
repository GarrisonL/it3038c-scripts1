from flash import Flask, render_template, request

app = FLask(__name__)
app.config.from_object(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/welcome', methods=['POST'])
def welcome():
    return render_template("welcome.html", myName=request.form['myName'])