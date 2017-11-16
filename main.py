import logging
import rec_eng as re
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, Response, jsonify
from werkzeug.exceptions import BadRequest, NotFound, UnsupportedMediaType, Unauthorized

# This defines a Flask application
app = Flask(__name__, static_url_path='')

# variables to adjust
criterias = {"Age": 25,  # (16 - 99)
             "Behavior": "Neutral",  # (0 - 3)
             "Location": "S",  # (0 - 3)
             "Parking Space": "Parkinglot/R|Parkinglot",  # (0 - 14)
             "Purpose": "Working|Commuting|Racing",  # (0 - 62)
             "Usage": 10}  # (1 - 30)
recommendation = {}

def translate_to_json():
    return jsonify(
        age=criterias["Age"]
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recom.html')
def recom():
    return render_template('recom.html')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('images', path)

@app.route('/us-map-1.0.1/<path:path>')
def send_maps(path):
    return send_from_directory('us-map-1.0.1', path)

@app.route('/recommendation.html')
def recommendation():
    return render_template('recommendation.html')

@app.route('/population.csv')
def population():
    return render_template('population.csv')

@app.route("/driving_style", methods=['POST'])
def input_driving_style():
    if not request.is_json:
        raise UnsupportedMediaType()

    body = request.get_json()
    if body.get('driving_style') is None:
        raise BadRequest('missing driving_style')
    print("driving style: " + body.get('driving_style'))

    return translate_to_json()

@app.route("/driving_hours", methods=['POST'])
def input_driving_hours():
    if not request.is_json:
        raise UnsupportedMediaType()

    body = request.get_json()
    if body.get('driving_hours') is None:
        raise BadRequest('missing driving_hours')
    print("driving hours: " + body.get('driving_hours'))

    return translate_to_json()

@app.route("/parking_style", methods=['POST'])
def input_parking_style():
    if not request.is_json:
        raise UnsupportedMediaType()

    body = request.get_json()
    if body.get('parking_style') is None:
        raise BadRequest('missing parking_style')
    print("parking style: " + body.get('parking_style'))

    return translate_to_json()

@app.route("/car_usage", methods=['POST'])
def input_car_usage():
    if not request.is_json:
        raise UnsupportedMediaType()

    body = request.get_json()
    if body.get('car_usage') is None:
        raise BadRequest('missing car_usage')
    print("car usage: " + body.get('car_usage'))

    return translate_to_json()

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


def process_input(test):
    return re.get_rec(test)

if __name__ == '__main__':
    recommendation = process_input(criterias)
    print(recommendation)
    app.run(host='127.0.0.1', port=8080)

