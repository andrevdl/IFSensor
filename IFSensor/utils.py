from enum import Flag, auto

from werkzeug.exceptions import BadRequest
from functools import wraps
from flask import request, jsonify

class CRUDMethods(Flag):
    READ = auto()
    CREATE = auto()
    UPDATE = auto()
    DELETE = auto()
    SEARCH_WITHOUT_ID = auto()
    SEARCH_BY_ID = auto()
    SEARCH = SEARCH_WITHOUT_ID | SEARCH_BY_ID
    READ_CREATE = READ | CREATE
    READ_CREATE_UPDATE = READ | CREATE | UPDATE
    ALL = READ | CREATE | UPDATE | DELETE
    POST_EXECUTE = CREATE # For now, may change later
    GET_EXECUTE = READ # For now, may change later

def is_flag_set(set, flag):
    return (set & flag) == flag

def register_api(app, crud, view, endpoint, url, pk='id', pk_type='int'):
    view_func = view.as_view(endpoint)

    if is_flag_set(crud, CRUDMethods.SEARCH_WITHOUT_ID):
        app.add_url_rule(url, view_func=view_func, methods=['GET',])    

    if is_flag_set(crud, CRUDMethods.READ) and not is_flag_set(crud, CRUDMethods.SEARCH_BY_ID):
        app.add_url_rule(url, defaults={pk: None},
                        view_func=view_func, methods=['GET',])
    if is_flag_set(crud, CRUDMethods.CREATE):
        app.add_url_rule(url, view_func=view_func, methods=['POST',])

    if is_flag_set(crud, CRUDMethods.READ) or is_flag_set(crud, CRUDMethods.SEARCH_BY_ID):
        if is_flag_set(crud, CRUDMethods.UPDATE) and is_flag_set(crud, CRUDMethods.DELETE):
            app.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,
                            methods=['GET', 'PUT', 'DELETE'])
        elif is_flag_set(crud, CRUDMethods.UPDATE):
            app.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,
                            methods=['GET', 'PUT'])
        elif is_flag_set(crud, CRUDMethods.DELETE):
            app.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,
                            methods=['GET', 'DELETE'])
        else:
            app.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,
                            methods=['GET'])

def validate_json(f):
    @wraps(f)
    def wrapper(*args, **kw):
        try:
            request.json.get
        except Exception:
            msg = "payload must be a valid json"
            return jsonify({"error": msg}), 400
        return f(*args, **kw)
    return wrapper           