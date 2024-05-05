from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = "database.db"

@app.route("/create_database", methods=["POST"])
def create_database():
    data = request.json
    num_columns = data.get("num_columns")
    if not num_columns or num_columns <= 0:
        return jsonify({"error": "Please provide a valid number of columns"}), 400

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS my_table (id INTEGER PRIMARY KEY)")

    for i in range(num_columns):
        column_name = data.get(f"column_{i+1}")
        if column_name:
            c.execute(f"ALTER TABLE my_table ADD COLUMN {column_name} TEXT")

    conn.commit()
    conn.close()
    return jsonify({"message": "Database created successfully"}), 201

@app.route("/add_entry", methods=["POST"])
def add_entry():
    data = request.json
    values = [data.get(f"value_{i+1}") for i in range(len(data))]
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("INSERT INTO my_table VALUES (NULL" + ", ?" * len(values) + ")", values)
    conn.commit()
    conn.close()
    return jsonify({"message": "Entry added successfully"}), 201

if __name__ == "__main__":
    app.run(debug=True)
