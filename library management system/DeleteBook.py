from tkinter import *
import pymysql
from tkinter import messagebox


sql_pass = "mysqlstar111"
sql_database = "library"
con = pymysql.connect(host="localhost", user="root", password=sql_pass, database=sql_database)
cur = con.cursor()
books_table = "books"
issued_table = "books_issued"


def delete():
    book_id = book_info_label_1.get()
    delete_from_books = f"delete from {books_table} where bookid = '{book_id}'"
    delete_from_issued = f"delete from {issued_table} where bookid = '{book_id}'"

    try:
        cur.execute(delete_from_books)
        con.commit()
        cur.execute(delete_from_issued)
        con.commit()
        messagebox.showinfo("Success!",  "Book record deleted successfully.")
    except pymysql.Error as e:
        messagebox.showinfo("Failed!", f"MySQL Error: {e}")
    book_info_label_1.delete(0, END)
    root.destroy()


def delete_book():
    global book_info_label_1, canvas1, root, con, cur, books_table, issued_table
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    canvas1 = Canvas(root)
    canvas1.config(bg="#006B38")
    canvas1.pack(expand=True, fill=BOTH)

    heading_frame1 = Frame(root, bg="#FFBB00", bd=5)
    heading_frame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    heading_label = Label(heading_frame1, text="Delete Book", bg='black', fg='white', font=('Courier', 15))
    heading_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    label_frame = Frame(root, bg='black')
    label_frame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    delete_book_label = Label(label_frame, text="Book ID : ", bg='black', fg='white')
    delete_book_label.place(relx=0.05, rely=0.5)

    book_info_label_1 = Entry(label_frame)
    book_info_label_1.place(relx=0.3, rely=0.5, relwidth=0.62)

    submit_btn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=delete)
    submit_btn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quit_btn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quit_btn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()