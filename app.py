from flask import Flask, jsonify, make_response, request, Response


def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET', 'POST'])
    def index():

        return make_response(jsonify({'message': 'Hello World'}), 200)

    return app
