import requests
import json
from flask import Flask, render_template


app = Flask(__name__, template_folder='template')


@app.route("/", methods=['GET'])
def index():
    req = requests.get('https://api.unsplash.com/search/photos?query=affirmation&client_id=6yk_In27AcY3hxuqRfm_p4kpv1tZHm109oUy_UJE22g')
    data = json.loads(req.content)

    return render_template('userHomePage.html', data=data['results'])


app.run(debug=True)
