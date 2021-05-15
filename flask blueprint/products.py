from flask import Blueprint,jsonify


product_blueprint=Blueprint('products',__name__)

products=['milk','bread','soap','honey']


@product_blueprint.route('/list')
def product_list():
    return jsonify({"products":products})