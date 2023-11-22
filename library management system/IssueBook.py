from tkinter import *
import pymysql
from tkinter import messagebox

sql_pass = "mysqlstar111"
sql_database = "library"
con = pymysql.connect(host="localhost", user="root", password=sql_pass, database=sql_database)
cur = con.cursor()
books_table = "books"
issued_table = "books_issued"
all_books_id = []


def issue():
    global issue_btn, label_frame, book_id_label, book_id_info, issued_to_info, quit_btn, root, canvas1, status
    book_id = book_id_info.get()
    issued_to = issued_to_info.get()
    issue_btn.destroy()
    label_frame.destroy()
    book_id_label.destroy()
    book_id_info.destroy()
    issued_to_info.destroy()

    get_book_id = f"select bookid from {books_table}"
    try:
        cur.execute(get_book_id)
        con.commit()
        for i in cur:
            all_books_id.append(i[0])
        if book_id in all_books_id:
            check_avail = f"select status from {books_table} where bookid = '{book_id}'"
            cur.execute(check_avail)
            con.commit()
            for i in cur:
                check = i[0]
                if check == 'available':
                    status = True
                else:
                    status = False
        else:
            messagebox.showinfo("Error", "Book ID not present")
    except:
        messagebox.showinfo("Error", "Can't fetch Book IDs")

    issue_sql = f"insert into {issued_table} values('{book_id}', '{issued_to}')"
    show_issued = f"select * from {issued_table}"
    update_status = f"update {books_table} set status = 'issued' where bookid = '{book_id}'"

    try:
        if book_id in all_books_id and status == True:
            cur.execute(issue_sql)
            con.commit()
            cur.execute(update_status)
            con.commit()
            messagebox.showinfo('Success', "Book Issued Successfully")
            root.destroy()
        else:
            all_books_id.clear()
            messagebox.showinfo('Message', "Book Already Issued")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again")

    all_books_id.clear()


def issue_book():
    global issue_btn, label_frame, book_id_label, book_id_info, issued_to_info, quit_btn, root, canvas1, status
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    canvas1 = Canvas(root)
    canvas1.config(bg="#D6ED17")
    canvas1.pack(expand=True, fill=BOTH)
    heading_frame1 = Frame(root, bg="#FFBB00", bd=5)
    heading_frame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    heading_label = Label(heading_frame1, text="Issue Book", bg='black', fg='white', font=('Courier', 15))
    heading_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    label_frame = Frame(root, bg='black')
    label_frame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID
    book_id_label = Label(label_frame, text="Book ID : ", bg='black', fg='white')
    book_id_label.place(relx=0.05, rely=0.2)

    book_id_info = Entry(label_frame)
    book_id_info.place(relx=0.3, rely=0.2, relwidth=0.62)

    # Issued To Student name
    issued_to_label = Label(label_frame, text="Issued To : ", bg='black', fg='white')
    issued_to_label.place(relx=0.05, rely=0.4)

    issued_to_info = Entry(label_frame)
    issued_to_info.place(relx=0.3, rely=0.4, relwidth=0.62)

    # Issue Button
    issue_btn = Button(root, text="Issue", bg='#d1ccc0', fg='black', command=issue)
    issue_btn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quit_btn = Button(root, text="Quit", bg='#aaa69d', fg='black', command=root.destroy)
    quit_btn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
