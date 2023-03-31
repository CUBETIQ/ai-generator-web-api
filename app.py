from flask import Flask, jsonify, make_response, request, Response
from marvin import ai_fn


@ai_fn
def get_emoji(text: str) -> str:
    """
    Returns an emoji that describes the provided text.
    """


def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET', 'POST'])
    def index():

        return make_response(jsonify({'message': 'Hello World'}), 200)

    @app.route('/generator', methods=['GET', 'POST'])
    def generator():
        fn = request.args.get('fn') or request.form.get('fn')
        if fn:
            # Check by fn name and invoke the function
            if fn == 'emoji':
                text = request.args.get('text') or request.form.get('text')
                return make_response(jsonify({'emoji': get_emoji(text)}), 200)

        return make_response(jsonify({'message': 'No function found'}), 404)

    return app
