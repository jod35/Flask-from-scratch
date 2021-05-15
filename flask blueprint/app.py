from flask import Flask,render_template
from users import user_blueprint
from products import product_blueprint

app=Flask(__name__)
app.register_blueprint(user_blueprint,url_prefix='/users')

app.register_blueprint(product_blueprint,url_prefix='/products')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)