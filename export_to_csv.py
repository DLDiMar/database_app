import sqlite3
import csv

def export_to_csv(database_name, csv_file):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()

    c.execute("SELECT * FROM my_table")
    rows = c.fetchall()

    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([i[0] for i in c.description])
        writer.writerows(rows)

    conn.close()

def main():
    database_name = "database.db"
    csv_file = "data.csv"
    export_to_csv(database_name, csv_file)
    print("Database exported to CSV successfully")

if __name__ == "__main__":
    main()
