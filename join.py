# join.py
from flask import Blueprint, render_template
import mysql.connector

# 建立 Blueprint
join_blueprint = Blueprint('join_blueprint', __name__)

# 建立資料庫連接
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jessicashiu13_forDateBase",  # 替換成我的 MySQL 密碼
        database="homework"    # 替換成我的資料庫名稱
    )

# 路由：查詢並顯示 JOIN 查詢結果
@join_blueprint.route('/query')
def book_sales_query():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # JOIN 查詢
    query = """
    SELECT Book.Book_ID, Book.Book_Name, Book.Book_Price, Book.Book_Author, Book.Book_Publisher,
           Booksale.Book_SalesVolume, Booksale.Book_MonthSalesVolume
    FROM Book
    LEFT JOIN Booksale ON Book.Book_ID = Booksale.Book_ID
    """
    cursor.execute(query)
    results = cursor.fetchall()

    # 關閉連接
    cursor.close()
    connection.close()

    # 將查詢結果傳送至模板
    return render_template('index.html', results=results)
