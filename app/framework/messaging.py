import json
from flask import jsonify



def create_success_fail_payload(data, success=True, status_code=200):
    """
    Create a JSend compliant success/failure payload and jsonify it with return code.

    See https://github.com/omniti-labs/jsend for details.
    A success means all went well, and (usually) some data was returned.
    A failure means there was a problem with the data submitted, or some precondition
    of the API call wasn't satisfied (a malformed request, missing parameters, etc.)
    :param data: A dict representing any data to be returned.
    :param success: Whether this was a success or failure.
    :return: (jsonified payload, return code)
    """
    payload = {
        'status': 'success' if success else 'fail',
        'data': data,
    }
    resp = jsonify(payload)
    resp.status_code = status_code
    return resp

def create_error_payload(message, status_code=500, data=None):
    """
    Create a JSend compliant error payload and jsonify it with return code.

    See https://github.com/omniti-labs/jsend
    An error represents an error in processing the request, i.e. an exception
    was thrown.
    :param message: A useful message to return about the error.
    :param status_code: HTTP status code.
    :param data: Any data to be returned; optional.
    :return: (jsonified payload, return code)
    """
    resp = jsonify({
        'status': 'error',
        'data': data,
        'message': message,
        'code': status_code
    })
    resp.status_code = status_code
    return resp
