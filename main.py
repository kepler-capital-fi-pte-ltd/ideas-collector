from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
import create_idea

app = FlaskAPI(__name__)

@app.route("/find_reuters_code", methods=['POST'])
def notes_list():
    """
    Get back the reuters code for a string search.
    """
    if request.method == 'POST':
        req = request.data.get_json()
        return create_idea.get_reuters_code(req['search_key'])
