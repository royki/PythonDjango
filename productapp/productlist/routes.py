from productlist import app
from flask import render_template
from productlist.models import Item
# from productlist.models import Instances

@app.route('/')
def get_product_list():
    # items = [
    #     {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    #     {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    #     {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    # ]

    items = Item.query.all()
    return render_template('product.html', items=items)

# @app.route('/')
# def get_ec2_list():
#     instances = Instances.query.all()
#     return render_template('instancelist.html', instances=instances)
