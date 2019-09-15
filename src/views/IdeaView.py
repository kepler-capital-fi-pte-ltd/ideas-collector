from flask import Blueprint, request

from ..models.IdeaModel import IdeaModel, IdeaSchema
from . import _resp

idea_api = Blueprint('idea_api', __name__)
idea_schema = IdeaSchema()
idea_not_found_error = {'error': 'idea not found'}


@idea_api.route('/', methods=['POST'])
def create():
    """
    Create idea endpoint
    Example of input POST data:
    {
        "reuters_id":"1",
        "company":"Company Name",
        "author":"5cf049669faa622b7486dbe2",
        "market":"US",
        "thesis":"thesis",
        "position":"buy" | "sell" | "hold"
        "metadata_":"metadata"
    }
    :return: created idea
    """
    req_data = request.get_json()
    data = idea_schema.load(req_data, partial=True)
    idea = IdeaModel(data)
    idea.save()
    return idea_schema.dumps(idea)


@idea_api.route('/<int:iden>', methods=['GET'])
def get(iden: int):
    """
    Get idea endpoint

    :param iden: id of the idea
    :return: idea
    """
    idea = IdeaModel.get(iden)
    if not idea:
        return _resp(idea_not_found_error, 404)
    return idea_schema.dumps(idea)


@idea_api.route('/<int:iden>', methods=['PUT'])
def update(iden: int):
    """
    Update idea endpoint

    :param iden: ID of the idea
    :return: updated idea
    """
    req_data = request.get_json()

    idea = IdeaModel.get(iden)
    if not idea:
        return _resp(idea_not_found_error, 404)

    data = idea_schema.load(req_data, partial=True)
    idea.update(data)

    return idea_schema.dumps(idea)


@idea_api.route('/<int:iden>', methods=['DELETE'])
def delete(iden: int):
    """
    Delete idea by ID endpoint
    :param iden: id of the Idea
    :return: 204 HTTP Status Code
    """

    idea = IdeaModel.get(iden)

    if not idea:
        return _resp(idea_not_found_error, 404)

    idea.delete()
    return _resp({}, 204)


@idea_api.route('/', methods=['GET'])
def get_all():
    """
    Get all ideas endpoint
    query: limit - limit the number of requested ideas
    :return: [Idea]
    """
    limit = request.args.get('limit', default=100, type=int)
    print(limit)
    if limit > 1000:
        limit = 1000
    ideas = IdeaModel.get_all(limit)
    return idea_schema.dumps(ideas, many=True)
