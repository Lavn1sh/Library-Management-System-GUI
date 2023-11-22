from tkinter import *
import pymysql
from tkinter import messagebox


sql_pass = "mysqlstar111"
sql_database = "library"
con = pymysql.connect(host="localhost", user="root", password=sql_pass, database=sql_database)
cur = con.cursor()
books_table = "books"


def view_books():
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    canvas1 = Canvas(root)
    canvas1.config(bg="#12a4d9")
    canvas1.pack(expand=True, fill=BOTH)

    heading_frame1 = Frame(root, bg="#FFBB00", bd=5)
    heading_frame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    heading_label = Label(heading_frame1, text="View Books", bg='black', fg='white', font=('Courier', 15))
    heading_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    label_frame = Frame(root, bg='black')
    label_frame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25
    Label(label_frame, text="%-10s%-40s%-30s%-20s" % ('Book_ID', 'Title', 'Author', 'Status'),
          bg='black', fg='white').place(relx=0.07, rely=0.1)
    Label(label_frame, text="----------------------------------------------------------------------------", bg='black',
          fg='white').place(relx=0.05, rely=0.2)

    get_books = f"select * from {books_table}"
    try:
        cur.execute(get_books)
        con.commit()
        for i in cur:
            Label(label_frame, text="%-10s%-30s%-30s%-20s" % (i[0], i[1], i[2], i[3]), bg='black', fg='white').place(
                relx=0.07, rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")

    quit_btn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quit_btn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
