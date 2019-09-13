from flask import Blueprint, jsonify, request, Response, json, g

from ..models.IdeaModel import IdeaModel, IdeaSchema

idea_api = Blueprint('idea_api', __name__)
idea_schema = IdeaSchema()


@idea_api.route('/', methods=['POST'])
def create():
    """
    Create idea function

    :return: created Idea
    """
    req_data = request.get_json()
    print(req_data)
    data, error = idea_schema.load(req_data, partial=True)

    if error:
        return _resp(error, 400)

    idea = IdeaModel(data)
    idea.save()
    data = idea_schema.dump(idea).data
    return _resp(data, 201)


@idea_api.route('/<iden>', methods=['GET'])
def get(iden: str) -> dict:
    """
    Get idea function

    :param iden: id of the idea
    :return: idea
    """
    idea = IdeaModel.get(iden)
    return jsonify(idea)


@idea_api.route('/<int:iden>', methods=['PUT'])
def update(iden):
    """
    Update idea function
    :param iden: ID of the idea
    :return: updated idea
    """
    req_data = request.get_json()

    idea = IdeaModel.get(iden)
    if not idea:
        return _resp({'error': 'idea not found'}, 404)

    data, error = idea_schema.load(req_data, partial=True)

    if error:
        return _resp(error, 400)

    idea.update(data)

    return jsonify(idea)


@idea_api.route('/<int:iden>', methods=['DELETE'])
def delete(iden):
    idea = IdeaModel.get(iden)

    if not idea:
        return _resp({'error': 'idea not found'}, 404)

    idea.delete()
    return _resp({'message': f"idea {iden} deleted"}, 204)


def _resp(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dump(res),
        status=status_code
    )
