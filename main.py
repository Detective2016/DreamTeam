import logging
import rec_eng as re
from flask import Flask, render_template, request, redirect, url_for, send_from_directory

# This defines a Flask application
app = Flask(__name__, static_url_path='')

# Magical annotations define URL routing via the Flask application
@app.route('/')
def root():
    return render_template('index.html')

@app.route('/js/<path:path>')
def send_js(path):
    print(path)
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

@app.route("/login")
def do_login():
    username = "foo"
    return username

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


def process_input(test):
    return re.get_rec(test)


# This allows you to run locally.
# When run in GCP, Gunicorn is used instead (see entrypoint in app.yaml) to
# Access the Flack app via WSGI

# variables to adjust
test = {"Age": 25,  # (16 - 99)
           "Behavior": "Neutral",  # (0 - 3)
           "Location": "S",  # (0 - 3)
           "Parking Space": "Parkinglot/R|Parkinglot",  # (0 - 14)
           "Purpose": "Working|Commuting|Racing",  # (0 - 62)
           "Usage": 10}  # (1 - 30)

if __name__ == '__main__':

    print(process_input(test))

    app.run(host='127.0.0.1', port=8080)

