from flask import Response, json


def _resp(res: any, status_code):
    """
    Customized response function

    :param res: response data
    :param status_code: Http Status Code
    :return: instance of the class Response (flask)
    """

    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
