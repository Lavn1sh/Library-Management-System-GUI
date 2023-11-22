from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *


sql_pass = "mysqlstar111"
sql_database = "library"
con = pymysql.connect(host="localhost", user="root", password=sql_pass, database=sql_database)
cur = con.cursor()

root = Tk()
root.title("Library")
root.minsize(height=400, width=400)
root.geometry("600x500")

canvas1 = Canvas(root)
canvas1.config(bg="#d0a2f7")
canvas1.pack(expand=True, fill=BOTH)

heading_frame1 = Frame(root, bg="#FFBB00", bd=5)
heading_frame1.place(relx=0.23, rely=0.1, relwidth=0.55, relheight=0.13)
heading_label = Label(heading_frame1, text="WELCOME TO\nASCENDANCE LIBRARY", bg='black', fg='white', font=('Courier', 15))
heading_label.place(relx=0, rely=0, relwidth=1, relheight=1)

btn_add = Button(root, text="Add Book", bg='black', fg='white', command=add_book)
btn_add.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn_delete = Button(root, text="Delete Book", bg='black', fg='white', command=delete_book)
btn_delete.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn_view = Button(root, text="View Book List", bg='black', fg='white', command=view_books)
btn_view.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn_issue = Button(root, text="Issue Book To Student", bg='black', fg='white', command=issue_book)
btn_issue.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

btn_return = Button(root, text="Return Book", bg='black', fg='white', command=return_book)
btn_return.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

root.mainloop()
