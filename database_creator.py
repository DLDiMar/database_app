import tkinter as tk
from tkinter import simpledialog, messagebox
import sqlite3

class DatabaseCreatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("SQLite Database Creator")

        self.column_labels = []
        self.column_entries = []
        self.num_columns = tk.IntVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Number of Columns:").grid(row=0, column=0)
        tk.Entry(self.master, textvariable=self.num_columns).grid(row=0, column=1)
        tk.Button(self.master, text="Create Database", command=self.create_database).grid(row=0, column=2)

    def create_database(self):
        num_columns = self.num_columns.get()
        if num_columns <= 0:
            messagebox.showerror("Error", "Please enter a valid number of columns")
            return

        self.column_labels.clear()
        self.column_entries.clear()

        for i in range(num_columns):
            label = tk.Label(self.master, text=f"Column {i+1}:")
            label.grid(row=i+1, column=0)
            entry = tk.Entry(self.master)
            entry.grid(row=i+1, column=1)
            self.column_labels.append(label)
            self.column_entries.append(entry)

        tk.Button(self.master, text="Save Database", command=self.save_database).grid(row=num_columns+1, columnspan=3)
        tk.Button(self.master, text="Add Records", command=self.add_records).grid(row=num_columns+2, columnspan=3)

    def save_database(self):
        db_name = "database.db"
        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        c.execute("CREATE TABLE IF NOT EXISTS my_table (id INTEGER PRIMARY KEY)")

        for i, entry in enumerate(self.column_entries):
            column_name = entry.get()
            if column_name.strip() != "":
                c.execute(f"ALTER TABLE my_table ADD COLUMN {column_name} TEXT")

        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Database created successfully")

    def add_records(self):
        num_columns = len(self.column_entries)
        if num_columns == 0:
            messagebox.showerror("Error", "Please create a database first")
            return

        record_values = []
        for i in range(num_columns):
            value = simpledialog.askstring("Input", f"Enter value for {self.column_entries[i].get()}")
            if value is None:
                return
            record_values.append(value)

        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("INSERT INTO my_table VALUES (NULL" + ", ?" * (len(record_values)) + ")", record_values)
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Record added successfully")

def main():
    root = tk.Tk()
    app = DatabaseCreatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
