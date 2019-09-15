from flask import Blueprint, jsonify, request, Response, json

from ..models.PerfomanceModel import PerformanceModel, PerformanceSchema
from . import _resp

perf_api = Blueprint('perf_api', __name__)
perf_schema = PerformanceSchema()
perf_not_found_error = {'error': 'performance not found'}


@perf_api.route('/', methods=['POST'])
def create():
    """
    Create Performance endpoint
    Example of input POST data:
    {
        "reuters_id":"1",
        "L1M":"1",
        "L1Y":"2",
        "YTD":"3",
        "since_inception":"4",
    }
    :return: created performance
    """
    json_data = request.get_json()
    data = perf_schema.load(json_data, partial=True)
    performance = PerformanceModel(data)
    performance.save()
    return perf_schema.dumps(performance)


@perf_api.route('/<int:iden>', methods=['GET'])
def get(iden: int):
    """
    Get performance by ID endpoint
    :param iden: id of the performance
    :return: performance
    """
    performance = PerformanceModel.get(iden)
    if not performance:
        return _resp(perf_not_found_error, 404)
    return perf_schema.dumps(performance)


@perf_api.route('/<int:iden>', methods=['PUT'])
def update(iden: int):
    """
    Update performance by ID endpoint
    :param iden: id of the performance
    :return: updated performance
    """
    req_data = request.get_json()

    performance = PerformanceModel.get(iden)
    if not performance:
        return _resp(perf_not_found_error, 404)
    data = perf_schema.load(req_data, partial=True)
    performance.update(data)

    return perf_schema.dumps(performance)


@perf_api.route('/<int:iden>', methods=['DELETE'])
def delete(iden: int):
    """
    Delete performance by ID endpoint
    :param iden: id of the performance
    :return: 204 HTTP Status Code
    """
    performance = PerformanceModel.get(iden)
    if not performance:
        return _resp(perf_not_found_error, 404)
    performance.delete()
    return _resp({}, 204)


@perf_api.route('/', methods=['GET'])
def get_all():
    """
    Get performances
    query: limit - limit the number of requested performances
    :return: [Performance]
    """

    limit = request.args.get('limit', default=100, type=int)
    if limit > 1000:
        limit = 1000

    performances = PerformanceModel.get_all(limit)
    return perf_schema.dumps(performances, many=True)
