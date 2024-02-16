from flask import jsonify


def RETURN_FORMATTED_JSON_RESPONSE(data):
    return jsonify(data), 200