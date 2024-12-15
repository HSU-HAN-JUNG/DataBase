from flask import Blueprint, request, redirect, url_for
import mysql.connector

delete_bp = Blueprint('delete_bp', __name__)

db_config = {
    'user': 'root',
    'password': 'Jessicashiu13_forDateBase',
    'host': 'localhost',
    'database': 'homework'
}

@delete_bp.route('/delete/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    query = "DELETE FROM book WHERE Book_ID = %s"
    cursor.execute(query, (book_id,))
    conn.commit()
    
    cursor.close()
    conn.close()
    
    return redirect(url_for('read_bp.index'))
