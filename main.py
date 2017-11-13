import logging
import recommendation as re
from flask import Flask, render_template

# This defines a Flask application
app = Flask(__name__)

# variables to adjust
dictionary = {'Age': 16, 'Behavior': 0, 'Location': 'NY', 'Parking': 'Indoor', 'Purpose': 0, 'Usage': 0}
package = {'Keyloss': 1, 'Paint': 1, 'Tires': 1, "Windshield": 1, "User": ['Andreas just bought keyloss protection']}

# Magical annotations define URL routing via the Flask application
@app.route('/')
def hello():
    return render_template('index.html')

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

def process_input(dict):
    recommended_package = re.provide_recommendation(dict)
    for key, value in recommended_package.items():
        print("key: " + key + " value: " + value)
        package[key] = value



# This allows you to run locally.
# When run in GCP, Gunicorn is used instead (see entrypoint in app.yaml) to
# Access the Flack app via WSGI
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
