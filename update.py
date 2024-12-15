from flask import Blueprint, request, redirect, url_for
import mysql.connector

update_bp = Blueprint('update_bp', __name__)

db_config = {
    'user': 'root',
    'password': 'Jessicashiu13_forDateBase',
    'host': 'localhost',
    'database': 'homework'
}

@update_bp.route('/update/<int:book_id>', methods=['POST'])
def update_book(book_id):
    # 從表單中取得書籍的新資訊
    new_name = request.form.get(f'Book_Name_{book_id}')  # 書名
    new_price = request.form.get(f'Book_Price_{book_id}')  # 價格
    new_author = request.form.get(f'Book_Author_{book_id}')  # 作者
    new_publisher = request.form.get(f'Book_Publisher_{book_id}')  # 出版社

    # 確認至少有一個欄位有新值
    if not any([new_name, new_price, new_author, new_publisher]):
        return "No data to update", 400

    # 連接到資料庫並更新內容
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # 更新語句和動態參數
    update_query = """
    UPDATE book 
    SET 
        Book_Name = %s, 
        Book_Price = %s, 
        Book_Author = %s, 
        Book_Publisher = %s 
    WHERE Book_ID = %s
    """
    
    # 執行更新語句
    cursor.execute(update_query, (new_name, new_price, new_author, new_publisher, book_id))
    conn.commit()  # 提交更改
    
    cursor.close()
    conn.close()
    
    # 更新完成後，重定向到主頁面
    return redirect(url_for('read_bp.index'))
