from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET"])
def get_form():
    return render_template("survey.html")