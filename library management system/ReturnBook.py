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


def returnn():
    global Submit_btn, label_frame, delete_book_label, delete_book_info, quit_btn, root, canvas1, status
    book_id = delete_book_info.get()
    get_book_id = f"select bookid from {issued_table}"

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
                if check == 'issued':
                    status = True
                else:
                    status = False
        else:
            messagebox.showinfo("Error", "Book ID not present")

    except:
        messagebox.showinfo("Error", "Can't fetch Book IDs")

    issue_sql = f"delete from {issued_table} where bookid = '{book_id}'"
    update_status = f"update {books_table} set status = 'available' where bookid = '{book_id}'"
    try:
        if book_id in all_books_id and status == True:
            cur.execute(issue_sql)
            con.commit()
            cur.execute(update_status)
            con.commit()
            messagebox.showinfo('Success', "Book Returned Successfully")
        else:
            all_books_id.clear()
            messagebox.showinfo('Message', "Please check the book ID")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again")

    all_books_id.clear()
    root.destroy()


def return_book():
    global delete_book_info, submit_btn, quit_btn, canvas1, con, cur, root, label_frame, delete_book_label
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")
    canvas1 = Canvas(root)

    canvas1.config(bg="#006B38")
    canvas1.pack(expand=True, fill=BOTH)

    heading_frame1 = Frame(root, bg="#FFBB00", bd=5)
    heading_frame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    heading_label = Label(heading_frame1, text="Return Book", bg='black', fg='white', font=('Courier', 15))
    heading_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    label_frame = Frame(root, bg='black')
    label_frame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID to Delete
    delete_book_label = Label(label_frame, text="Book ID : ", bg='black', fg='white')
    delete_book_label.place(relx=0.05, rely=0.5)

    delete_book_info = Entry(label_frame)
    delete_book_info.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Submit Button
    submit_btn = Button(root, text="Return", bg='#d1ccc0', fg='black', command=returnn)
    submit_btn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quit_btn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quit_btn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
