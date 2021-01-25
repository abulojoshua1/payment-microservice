from cerberus import Validator
from flask import jsonify, request


def validate_json(validation_schema):
    validator = Validator()

    def wrap(func):
        def wrapped_view(*args, **kwargs):
            if validator.validate(request.json, validation_schema):
                return func(validator.document, *args, **kwargs)
            return jsonify(validator.errors), 400
        return wrapped_view
    return wrap
