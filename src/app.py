from flask import Flask, jsonify, render_template, url_for, request
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Learn Flask API's"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


@app.route("/")
def index():
    return render_template('welcome.html')


@app.route("/getInfo")
def getInfo():
    return jsonify({'msg': 'Hello World!'})


@app.route("/postInfo", methods=['POST'])
def postInfo():
    if request.method == 'POST':
        posted_data = request.get_json()
        data = posted_data['data']
        return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
