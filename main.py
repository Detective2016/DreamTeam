import logging
import rec_eng as re
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, Response, jsonify
from werkzeug.exceptions import BadRequest, NotFound, UnsupportedMediaType, Unauthorized

# This defines a Flask application
app = Flask(__name__, static_url_path='')

# variables to adjust, setting to default initially and change based on request
criterias = {"Age": 25,  # (16 - 99)
             "Behavior": 3,  # (0 - 3)
             "Location": "New York",  # (0 - 3)
             "Parking Space": 3,  # (0 - 14)
             "Purpose": "Traveling",  # (0 - 62)
             "Usage": 25}  # (1 - 30)
recommendation = {"Keyloss": 0,
                  "Paint": 0,
                  "Tires": 1,
                  "Windshield":0,
                  "User":["Windshield"]}
recommendation_details = "97% people like you bought this package"

def get_json_criteria():
    return jsonify(
        keyloss=recommendation["Keyloss"],
        paint=recommendation["Paint"],
        tires=recommendation["Tires"],
        windshield=recommendation["Windshield"]
    )

def get_final_criteria():
    recommendation['details'] = "people like this"
    print(recommendation['details'])
    return jsonify(
        keyloss=recommendation["Keyloss"],
        paint=recommendation["Paint"],
        tires=recommendation["Tires"],
        details=recommendation["details"],
        windshield=recommendation["Windshield"],
        users=recommendation["User"]
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

@app.route("/location", methods=['POST'])
def input_location():
    if not request.is_json:
        raise UnsupportedMediaType()

    body = request.get_json()
    location = body.get('location')
    if location is None:
        raise BadRequest('missing location')

    print("location: " + location)
    criterias['Location'] = location

    return get_json_criteria()

@app.route("/driving_style", methods=['POST'])
def input_driving_style():
    if not request.is_json:
        raise UnsupportedMediaType()

    body = request.get_json()
    behavior = body.get('driving_style')
    if behavior is None:
        raise BadRequest('missing driving_style')
    print("driving style: " + behavior)

    if (int(behavior) <= 33):
        criterias['Behavior'] = 1
    elif (int(behavior) <= 66):
        criterias['Behavior'] = 2
    else:
        criterias['Behavior'] = 3

    return get_json_criteria()

@app.route("/driving_hours", methods=['POST'])
def input_driving_hours():
    if not request.is_json:
        raise UnsupportedMediaType()

    body = request.get_json()
    usage = body.get('driving_hours')
    if usage is None:
        raise BadRequest('missing driving_hours')
    print("driving hours: " + usage)
    criterias['Usage'] = usage

    if (int(usage) == 1):
        criterias['Usage'] = 5
    elif (int(usage) == 2):
        criterias['Usage'] = 15
    else:
        criterias['Usage'] = 25

    return get_json_criteria()

@app.route("/age", methods=['POST'])
def input_age():
    if not request.is_json:
        raise UnsupportedMediaType()

    body = request.get_json()
    age = body.get('age')
    if age is None:
        raise BadRequest('missing age')

    if (int(age) == 1):
        criterias['Age'] = 20
    elif (int(age) == 2):
        criterias['Age'] = 30
    else:
        criterias['Age'] = 60

    print("age: " + age)

    return get_json_criteria()

@app.route("/parking_style", methods=['POST'])
def input_parking_style():
    if not request.is_json:
        raise UnsupportedMediaType()

    body = request.get_json()
    parking = body.get('parking_style')
    if body.get('parking_style') is None:
        raise BadRequest('missing parking_style')
    print("parking style: " + parking)
    criterias['Parking Space'] = int(parking)

    return get_json_criteria()

@app.route("/car_usage", methods=['POST'])
def input_car_usage():
    if not request.is_json:
        raise UnsupportedMediaType()

    body = request.get_json()
    purpose = body.get('car_usage')
    if purpose is None:
        raise BadRequest('missing car_usage')
    print("car usage purpose: " + purpose)

    if (int(purpose) == 1):
        criterias['Purpose'] = 'Traveling'
    elif (int(purpose) == 2):
        criterias['Purpose'] = 'Working'
    elif (int(purpose) == 3):
        criterias['Purpose'] = 'Commuting'
    elif (int(purpose) == 4):
        criterias['Purpose'] = 'Racing'
    else:
        criterias['Purpose'] = 'Leisure'
    print(criterias)
    return get_final_criteria()

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

