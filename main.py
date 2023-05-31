import tkinter as tk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("students.db")
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                subject TEXT,
                grade INTEGER
            )''')
conn.commit()

def display_students():
    c.execute("SELECT * FROM students")
    students = c.fetchall()
    messagebox.showinfo("Studenci", str(students))

def add_student(name, subject, grade):
    c.execute("INSERT INTO students (name, subject, grade) VALUES (?, ?, ?)", (name, subject, grade))
    conn.commit()
    messagebox.showinfo("Sukces", "Student został dodany")

def delete_student(student_id):
    c.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    messagebox.showinfo("Sukces", "Student został usunięty")

def edit_student(student_id, name, subject, grade):
    c.execute("UPDATE students SET name=?, subject=?, grade=? WHERE id=?", (name, subject, grade, student_id))
    conn.commit()
    messagebox.showinfo("Sukces", "Dane studenta zostały zaktualizowane")

def add_button_clicked():
    name = name_entry.get()
    subject = subject_entry.get()
    grade = grade_entry.get()

    if name and subject and grade:
        add_student(name, subject, grade)
    else:
        messagebox.showerror("Błąd", "Wszystkie pola muszą być wypełnione")

def delete_button_clicked():
    student_id = delete_entry.get()

    if student_id:
        delete_student(student_id)
    else:
        messagebox.showerror("Błąd", "Wprowadź identyfikator studenta")



root = tk.Tk()
root.title("Aplikacja Studenci")

display_button = tk.Button(root, text="Wyświetl studentów", command=display_students)
display_button.pack()

add_label = tk.Label(root, text="Dodaj studenta:")
add_label.pack()

name_label = tk.Label(root, text="Imię:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

subject_label = tk.Label(root, text="Przedmiot:")
subject_label.pack()

subject_entry = tk.Entry(root)
subject_entry.pack()

grade_label = tk.Label(root, text="Ocena:")
grade_label.pack()

grade_entry = tk.Entry(root)
grade_entry.pack()

add_button = tk.Button(root, text="Dodaj", command=add_button_clicked)
add_button.pack()

delete_label = tk.Label(root, text="Usuń studenta:")
delete_label.pack()

delete_entry = tk.Entry(root)
delete_entry.pack()

delete_button = tk.Button(root, text="Usuń", command=delete_button_clicked)
delete_button.pack()

edit_id_label = tk.Label(root, text="Identyfikator:")
edit_id_label.pack()

edit_id_entry = tk.Entry(root)
edit_id_entry.pack()

edit_name_label = tk.Label(root, text="Imię:")
edit_name_label.pack()

edit_name_entry = tk.Entry(root)
edit_name_entry.pack()

edit_subject_label = tk.Label(root, text="Przedmiot:")
edit_subject_label.pack()

edit_subject_entry = tk.Entry(root)
edit_subject_entry.pack()

edit_grade_label = tk.Label(root, text="Ocena:")
edit_grade_label.pack()

edit_grade_entry = tk.Entry(root)
edit_grade_entry.pack()

root.mainloop()

conn.close()
