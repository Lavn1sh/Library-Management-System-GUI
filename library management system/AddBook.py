from tkinter import *
from tkinter import messagebox
import pymysql


def new_book():
    book_id = book_info_label_1.get()
    title = book_info_label_2.get()
    author = book_info_label_3.get()
    status = book_info_label_4.get()
    status = status.lower()

    add_new_book = f"insert into {books_table} values('{book_id}', '{title}', '{author}', '{status}')"

    try:
        cur.execute(add_new_book)
        con.commit()
        messagebox.showinfo('Success', "Book added successfully")
        if book_id == "":
            raise ValueError("")
    except ValueError:
        messagebox.showinfo("Error", "Can't add data into Database")
    root.destroy()


def add_book():
    global root, canvas1, heading_frame1, heading_label, book_info_label_1, book_info_label_2, book_info_label_3, \
        book_info_label_4, books_table, cur, con

    sql_pass = "mysqlstar111"
    sql_database = "library"
    con = pymysql.connect(host="localhost", user="root", password=sql_pass, database=sql_database)
    cur = con.cursor()

    books_table = "books"
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    canvas1 = Canvas(root)
    canvas1.config(bg="#ff6e40")
    canvas1.pack(expand=True, fill=BOTH)

    heading_frame1 = Frame(root, bg="#FFBB00", bd=5)
    heading_frame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    heading_label = Label(heading_frame1, text="Add Books", bg='black', fg='white', font=('Courier', 15))
    heading_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    label_frame = Frame(root, bg='black')
    label_frame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)
    # book_id
    book_id_label = Label(label_frame, text="Book ID : ", bg='black', fg='white')
    book_id_label.place(relx=0.05, rely=0.2, relheight=0.08)

    book_info_label_1 = Entry(label_frame)
    book_info_label_1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)
    # book_title
    book_title_label = Label(label_frame, text="Title : ", bg='black', fg='white')
    book_title_label.place(relx=0.05, rely=0.35, relheight=0.08)

    book_info_label_2 = Entry(label_frame)
    book_info_label_2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)
    # book_author
    book_author_label = Label(label_frame, text="Author : ", bg='black', fg='white')
    book_author_label.place(relx=0.05, rely=0.50, relheight=0.08)

    book_info_label_3 = Entry(label_frame)
    book_info_label_3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)
    # book_status
    book_status_label = Label(label_frame, text="Status(Avail/issued) : ", bg='black', fg='white')
    book_status_label.place(relx=0.05, rely=0.65, relheight=0.08)

    book_info_label_4 = Entry(label_frame)
    book_info_label_4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

    submit_btn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=new_book)
    submit_btn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quit_btn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quit_btn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
