# app.py
from flask import Flask, redirect, url_for
from join import join_blueprint

app = Flask(__name__)

# 註冊 join.py 中的 Blueprint
app.register_blueprint(join_blueprint, url_prefix='/books')

# 添加根路由
@app.route('/')
def home():
    return redirect(url_for('join_blueprint.book_sales_query'))  # 重定向到 book_sales_query 路由

if __name__ == "__main__":
    app.run(debug=True)
