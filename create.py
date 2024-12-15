from flask import Blueprint, request, redirect, url_for
import mysql.connector

create_bp = Blueprint('create_bp', __name__)

db_config = {
    'user': 'root',
    'password': 'Jessicashiu13_forDateBase',
    'host': 'localhost',
    'database': 'homework'
}

@create_bp.route('/add', methods=['POST'])
def add_book():
    Book_ID = request.form['Book_ID']
    Book_Name = request.form['Book_Name']
    Book_Price = request.form['Book_Price']
    Book_Author = request.form['Book_Author']
    Book_Publisher = request.form['Book_Publisher']
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    query = """INSERT INTO book (Book_ID, Book_Name, Book_Price, Book_Author, Book_Publisher) 
               VALUES (%s, %s, %s, %s, %s)"""
    cursor.execute(query, (Book_ID, Book_Name, Book_Price, Book_Author, Book_Publisher))
    conn.commit()
    
    cursor.close()
    conn.close()
    
    return redirect(url_for('read_bp.index'))
