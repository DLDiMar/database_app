from flask import Flask, request, jsonify
import sqlite3
import csv

app = Flask(__name__)
DATABASE = "database.db"

@app.route("/export_to_csv", methods=["GET"])
def export_to_csv():
    try:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()

        c.execute("SELECT * FROM my_table")
        rows = c.fetchall()

        csv_file = "data.csv"
        with open(csv_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([i[0] for i in c.description])
            writer.writerows(rows)

        conn.close()

        return jsonify({"message": "Database exported to CSV successfully", "file": csv_file}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
