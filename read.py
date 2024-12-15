from flask import Blueprint, render_template
import mysql.connector

read_bp = Blueprint('read_bp', __name__)

db_config = {
     'user': 'root',
    'password': 'Jessicashiu13_forDateBase',
    'host': 'localhost',
    'database': 'homework'
}

@read_bp.route('/')
def index():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM book")
    book = cursor.fetchall()
    
    cursor.close()
    conn.close()

    # Render the posts with the add/delete functionality
    return render_template('index.html', book=book)