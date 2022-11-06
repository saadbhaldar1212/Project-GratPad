from flask import Flask, render_template


app = Flask(__name__, template_folder='template')


@app.route("/")
def index():
    
    return render_template('userHomePage.html')


app.run(debug=True)
