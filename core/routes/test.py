from core import mes_core
from flask import request, jsonify, send_file


@mes_core.route('/', methods=["GET"])
def get_rec():
    return jsonify({})