import flask

from src.person_service import PersonService


app = flask.Flask(__name__)


@app.route('/health', methods=['GET', ])
def health() -> tuple:
    return flask.jsonify({'status': 'ok'}), 200


@app.route('/person', methods=['GET', ])
def get_registered_persons() -> tuple:
    persons = PersonService().get_person_by_csv_file()

    persons = [person.to_dict() for person in persons]

    return flask.jsonify(persons), 200


@app.route('/index', methods=['GET', ])
def index() -> tuple:
    return flask.render_template('index.html')
