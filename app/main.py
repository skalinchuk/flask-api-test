from flask import Flask, request, jsonify
from .services import get_books, get_authors

app = Flask(__name__)

ORDERABLE_FIELDS = ['published', 'title']
ORDER_DIRECTIONS = ['asc', 'desc']


@app.route("/books")
def books():
    order_by = request.args.get('order_by', '').lower()
    order_dir = request.args.get('order_dir', 'asc').lower()
    if order_by not in ORDERABLE_FIELDS:
        order_by = ''
    if order_dir not in ORDER_DIRECTIONS:
        order_dir = ''

    return jsonify(get_books(order_by, order_dir))


@app.route("/authors")
def authors():
    return jsonify(get_authors())
