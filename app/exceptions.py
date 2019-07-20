from flask import jsonify


def template(data, code=500):
    return {'message': {'errors': {'details': data}}, 'status_code': code}

UNKNOWERROR = template([], 500)


class ExceptionHandler(Exception):
    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        if status_code is not None:
            self.status_code = 400
        self.payload = payload
    
    def to_json(self):
        rv= self.message
        return jsonify(rv)

    @classmethod
    def unknow_error(cls):
        return cls(**UNKNOWERROR)