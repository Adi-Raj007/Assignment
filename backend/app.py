from flask import Flask, request, jsonify
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
DATABASE = 'database.db'

def create_connection():
    """Create a database connection to the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
    except Error as e:
        print(e)
    return conn

def init_db():
    conn = create_connection()
    cursor = conn.cursor()
    with open('schema.sql', 'r') as f:
        cursor.executescript(f.read())
    with open('sample_data.sql', 'r') as f:
        cursor.executescript(f.read())
    conn.commit()
    conn.close()

@app.route('/add-app', methods=['POST'])
def add_app():
    data = request.get_json()
    app_name = data.get('app_name')
    version = data.get('version')
    description = data.get('description')

    if not all([app_name, version, description]):
        return jsonify({'error': 'Missing fields'}), 400

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO apps (app_name, version, description) VALUES (?, ?, ?)",
        (app_name, version, description)
    )
    conn.commit()
    app_id = cursor.lastrowid
    conn.close()
    return jsonify({'id': app_id, 'app_name': app_name, 'version': version, 'description': description}), 201

@app.route('/get-app/<int:app_id>', methods=['GET'])
def get_app(app_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM apps WHERE id=?", (app_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        app_details = {
            'id': row[0],
            'app_name': row[1],
            'version': row[2],
            'description': row[3]
        }
        return jsonify(app_details), 200
    else:
        return jsonify({'error': 'App not found'}), 404

@app.route('/delete-app/<int:app_id>', methods=['DELETE'])
def delete_app(app_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM apps WHERE id=?", (app_id,))
    conn.commit()
    changes = cursor.rowcount
    conn.close()
    if changes:
        return jsonify({'message': f'App with id {app_id} deleted successfully.'}), 200
    else:
        return jsonify({'error': 'App not found'}), 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
