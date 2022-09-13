from tkinter import *
import sqlite3
from tkinter import messagebox
from tkcalendar import *
from tkinter import ttk
import time

new_admin = ''
new_student = ''
new_book = ''
reset = ''
book_issue = ''
edit_window = ''
delete_book_window = ''
search = ''
return_window = ''
charge_window = ''
user_entry_reset = ''
password_entry_reset = ''
usn_entry = ''
password_entry_student = ''
phone_entry = ''
id_entry_new = ''
password_entry_new = ''
contact_entry = ''
id_entry_book = ''
edition_entry = ''
price_entry = ''
usn_entry_issue = ''
book_id_entry = ''
book_id_edit = ''
edition_entry_edit = ''
price_entry_edit = ''
book_id_ent = ''
book_id_entry_one = ''
usn_entry_return = ''

login = Tk()
login.title("Admin Login")
frame = Frame(login ,width=350, height=50, bg='black')
frame.grid(row=0, column=0, columnspan=2)

#function to view the issue record
def view_issue_record():
    view_issue_window = Tk()
    view_issue_window.geometry("800x300")
    view_issue_window.title("All the issue record (pending the return the books)")

    tree_frame = Frame(view_issue_window)
    tree_frame.pack(pady=10)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)
    #define th columns
    my_tree['columns'] = ["USN", "name", "course", "phone", "college", "fromDate", "toDate", "noBook"]

    #formate the columns
    my_tree.column("#0", stretch=NO, width=0)
    my_tree.column("USN", width=75, anchor=CENTER, minwidth=50)
    my_tree.column("name", width=100, anchor=CENTER, minwidth=75)
    my_tree.column("course", width=75, anchor=CENTER, minwidth=50)
    my_tree.column("phone", width=125, anchor=CENTER, minwidth=100)
    my_tree.column("college", width=100, anchor=CENTER, minwidth=75)
    my_tree.column("fromDate", width=75, anchor=CENTER, minwidth=50)
    my_tree.column("toDate", width=75, anchor=CENTER, minwidth=50)
    my_tree.column("noBook", width=50, anchor=CENTER, minwidth=50)

    #formate the heading
    my_tree.heading("USN", text="USN")
    my_tree.heading("name", text="name")
    my_tree.heading("course", text="course")
    my_tree.heading("phone", text="phone")
    my_tree.heading("college", text="college")
    my_tree.heading("fromDate", text="fromDate")
    my_tree.heading("toDate", text="toDate")
    my_tree.heading("noBook", text="noBook")

    connection = sqlite3.connect("student_book.db")
    c = connection.cursor()
    c.execute("SELECT USN, name, course, phone, college, fromDate, toDate, noBook FROM student_issue_record")
    record = c.fetchall()
    connection.commit()
    connection.close()

    count = 0
    for item in record:
        my_tree.insert(parent="", index="end", iid=str(count), values=item)
        count += 1

    my_tree.pack()
    view_issue_window.mainloop()

#function to view all students
def view_student():
    view_student_window = Tk()
    view_student_window.geometry("500x200")
    view_student_window.title("All Students Information")

    tree_frame = Frame(view_student_window)
    tree_frame.pack(pady=10)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)
    tree_scroll.config(command=my_tree.yview)
    #define the columns
    my_tree['columns'] = ["USN", "Name", "Course", "Phone", "College"]

    #formate the columns
    my_tree.column("#0", stretch=NO, width=0)
    my_tree.column("USN", anchor=CENTER, width=75, minwidth=50)
    my_tree.column("Name", anchor=CENTER, width=100, minwidth=75)
    my_tree.column("Course", anchor=CENTER, width=75, minwidth=75)
    my_tree.column("Phone", anchor=CENTER, width=75, minwidth=75)
    my_tree.column("College", anchor=CENTER, width=100, minwidth=85)

    #formate the headings
    my_tree.heading("USN", text="USN")
    my_tree.heading("Name", text="Name")
    my_tree.heading("Course", text="Course")
    my_tree.heading("Phone", text="Phone")
    my_tree.heading("College", text="College")

    #add data to the tree view
    connection = sqlite3.connect("student_database.db")
    c = connection.cursor()
    c.execute("SELECT USN, name, course, phone, college FROM student_info")
    record = c.fetchall()
    connection.commit()
    connection.close()
    count=0
    for item in record:
        my_tree.insert(parent="", index='end', iid=str(count), values=item)
        count += 1
    my_tree.pack()
    view_student_window.mainloop()

#function to view all the admin details
def view_admin():
    view_admin_window = Tk()
    view_admin_window.geometry("600x200")
    view_admin_window.title("All Admin Information")

    tree_frame = Frame(view_admin_window)
    tree_frame.pack(pady=10)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)
    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)
    tree_scroll.config(command=my_tree.yview)
    #define Columns
    my_tree['columns'] = ["AdminID", "FirstName", "LastName", "Contact", "Email"]

    #formate our columns
    my_tree.column("#0", stretch=NO, width=0)
    my_tree.column("AdminID", anchor=CENTER, width=75, minwidth=50)
    my_tree.column("FirstName", anchor=CENTER, width=85, minwidth=75)
    my_tree.column("LastName", anchor=CENTER, width=85, minwidth=75)
    my_tree.column("Contact", anchor=CENTER, width=100, minwidth=75)
    my_tree.column("Email", anchor=CENTER, width=200, minwidth=85)

    #formate the headings
    my_tree.heading("AdminID", text="Admin ID")
    my_tree.heading("FirstName", text="First Name")
    my_tree.heading("LastName", text="Last Name")
    my_tree.heading("Contact", text="Contact")
    my_tree.heading("Email", text="Email")

    connection = sqlite3.connect("admin.db")
    c = connection.cursor()
    c.execute("SELECT ID, first_name, last_name, contact, email FROM admin_info")
    record = c.fetchall()
    connection.commit()
    connection.close()

    count=0
    for item in record:
        my_tree.insert(parent="", index='end', iid=str(count), values=item)
        count +=1
    my_tree.pack()
    view_admin_window.mainloop()

# definition to view all the books
def view_book():
    view = Tk()
    view.geometry("500x300")
    view.title("All the Books.")

    tree_frame = Frame(view)
    tree_frame.pack(pady=10)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)
    tree_scroll.config(command=my_tree.yview)

    #define the columns
    my_tree['columns'] = ["BookID", "Title", "Author", "Edition", "Price"]

    #formate the columns
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("BookID", anchor=CENTER, width=75, minwidth=50)
    my_tree.column("Title", anchor=CENTER, width=125, minwidth=50)
    my_tree.column("Author", anchor=CENTER, width=125, minwidth=50)
    my_tree.column("Edition", anchor=CENTER, width=75, minwidth=50)
    my_tree.column("Price", anchor=CENTER, width=75, minwidth=50)

    #create headings
    my_tree.heading("BookID", text="Book ID",anchor=CENTER)
    my_tree.heading("Title", text="Title",anchor=CENTER)
    my_tree.heading("Author", text="Author" ,anchor=CENTER)
    my_tree.heading("Edition", text="Edition",anchor=CENTER)
    my_tree.heading("Price", text="Price",anchor=CENTER)

    #adding data to the
    connection = sqlite3.connect("all_books.db")
    c = connection.cursor()
    c.execute("SELECT bookID, title, author, edition, price FROM book_info")
    record = c.fetchall()
    connection.commit()
    connection.close()
    count_index = 0
    for item in record:
        my_tree.insert(parent="", index='end',iid=str(count_index), values=item)
        count_index += 1

    my_tree.pack(pady=10)
    view.mainloop()

#to return the book
def return_book_checking(usn):
    try:
        usn = int(usn)
        found = False
        connection = sqlite3.connect('student_book.db')
        c = connection.cursor()
        c.execute("SELECT USN FROM student_issue_record")
        record = c.fetchall()
        connection.commit()
        connection.close()

        for item in record:
            if (usn,) == item:
                found = True
        global charge_window
        if found:
            return_window.destroy()
            charge_window = Tk()
            charge_window.geometry("250x250")

            connection = sqlite3.connect("student_book.db")
            c = connection.cursor()
            #updating the database with to submit date
            c.execute(f"UPDATE student_issue_record SET submitDate = ? WHERE USN = {usn}", (cal.get_date(), ))
            c.execute(f"SELECT fromDate, toDate, submitDate, noBook FROM student_issue_record WHERE USN = {usn}")
            record = c.fetchall()
            connection.commit()
            connection.close()

            from_date = record[0][0]
            to_date = record[0][1]
            submit_date = record[0][2]
            no_book = record[0][3]

            #retrieving the date number, month number and year number from, the from_date
            from_date_list = []
            for item in from_date:
                from_date_list.append(item)

            backslash_index_from = []
            for i in range(len(from_date_list)):
                if from_date_list[i] == '/':
                    backslash_index_from.append(i)
            from_month = from_date[0:backslash_index_from[0]]
            from_date_number = from_date[backslash_index_from[0] + 1: backslash_index_from[1]]
            from_year = from_date[backslash_index_from[1] + 1: len(from_date_list)]

            #retrieving the date number, month number and year number from, the to_date
            to_date_list = []
            for item in to_date:
                to_date_list.append(item)
            backslash_index_to = []
            for i in range(len(to_date_list)):
                if to_date_list[i] == '/':
                    backslash_index_to.append(i)
            to_month = to_date[0:backslash_index_to[0]]
            to_date_number = to_date[backslash_index_to[0] + 1:backslash_index_to[1]]
            to_year = to_date[backslash_index_to[1] + 1:len(to_date_list)]

            # retrieving the date number, month number and year number from, the submit_date
            submit_date_list = []
            for item in submit_date:
                submit_date_list.append(item)
            backslash_index_submit = []
            for i in range(len(submit_date_list)):
                if submit_date_list[i] == '/':
                    backslash_index_submit.append(i)
            submit_month = submit_date[0:backslash_index_submit[0]]
            submit_date_number = submit_date[backslash_index_submit[0] + 1:backslash_index_submit[1]]
            submit_year = submit_date[backslash_index_submit[1] + 1:len(to_date_list)]

            #calculating The charge
            charge = 0
            if from_year <= submit_year <= to_year:
                if from_month <= submit_month <= to_month:
                    if from_date_number == submit_date_number or submit_date_number == to_date_number:
                        charge += 25
                    elif from_date_number <= submit_date_number <= to_date_number:
                        charge += 25
                    else:
                        charge += 50
                else:
                    charge += 100
            else:
                charge += 200

            connection = sqlite3.connect("student_book.db")
            c = connection.cursor()
            c.execute(f"SELECT charge FROM student_issue_record WHERE USN ={usn}")
            record = c.fetchall()
            final_charge = charge + record[0][0]
            c.execute(f"DELETE FROM student_issue_record WHERE USN = {usn}")
            connection.commit()
            connection.close()

            connection = sqlite3.connect("all_books.db")
            c = connection.cursor()
            c.execute(f"SELECT issue, stdID FROM book_info WHERE stdID = {usn}")
            c.execute(f"UPDATE book_info SET issue = 'no' WHERE stdID = {usn}")
            c.execute(f"UPDATE book_info SET stdID = ? WHERE stdID = {usn}", (0, ))
            connection.commit()
            connection.close()
            charge_window.configure(bg='black')

            charge_text = Label(charge_window, text='Fine is: ', font=("bold", 25), fg='white', bg='black', justify=CENTER)
            charge_text.grid(row=0, column=0, padx=30, pady=50)

            charge_label = Label(charge_window, text=final_charge, font=("bold", 25), fg='yellow', bg='black', justify=CENTER)
            charge_label.grid(row=1, column = 0, padx=30, pady=10)

            connection = sqlite3.connect("issue_record.db")
            c = connection.cursor()
            c.execute("INSERT INTO issue_table VALUES (?, ?, ?, ?, ?, ?);", (usn, from_date, to_date, submit_date,
                                                                             final_charge, no_book))
            connection.commit()
            connection.close()

            charge_window.mainloop()
        else:
            messagebox.showerror("Information", f"Student with USN {usn} has returned all books.")
    except ValueError:
        usn_entry_return.delete(0, END)
        messagebox.showerror("Information", "Enter the correct datatype credentials.")

#definition for returning the book
def return_book():
    global return_window
    return_window = Tk()
    return_window.geometry("300x250")

    frame_return = Frame(return_window, width=300, height=50, bg='black')
    frame_return.grid(row=0, column=0, columnspan=2)

    return_label = Label(return_window, text="Returning Book", fg='white', bg='black', font='bold', justify=CENTER)
    return_label.grid(row=0, column=0, columnspan=2, pady=10)

    usn_return = Label(return_window, text="Enter USN", font=6)
    usn_return.grid(row=1, column=0, padx=10, pady=10)

    global usn_entry_return
    usn_entry_return = Entry(return_window, width=25)
    usn_entry_return.grid(row=1, column=1, pady=10)

    return_button = Button(return_window, text="Return", command=lambda :return_book_checking((usn_entry_return.get())))
    return_button.grid(row=2, column=0, columnspan=2, ipadx=20, pady=10)
    return_window.mainloop()

#to display the information of the book
def display_book_information(bookID):
    try:
        book_id = int(bookID)
        found = False
        connection = sqlite3.connect("all_books.db")
        c = connection.cursor()
        c.execute("SELECT bookID FROM book_info")
        record = c.fetchall()
        connection.commit()
        connection.close()

        for item in record:
            if (book_id,) == item:
                found = True
        if found:
            display = Tk()
            display.title(f"Information of Book ID: {book_id}")
            display.geometry("350x300")
            display.configure(bg='black')
            search.destroy()

            connection = sqlite3.connect("all_books.db")
            c = connection.cursor()
            c.execute(f"SELECT * FROM book_info WHERE bookID = {book_id}")
            record = c.fetchall()
            connection.commit()
            connection.close()

            book_name = Label(display, text=f"Book Name:    {record[0][1]}", fg='white', bg='black', font=8, justify=CENTER)
            book_name.grid(row=0, column=0, padx=10, pady=10)

            book_author = Label(display, text=f"Book Author:    {record[0][2]}", fg='white', bg='black', font=8, justify=CENTER)
            book_author.grid(row=1, column=0, pady=10)

            book_edition = Label(display, text=f"Book Edition:  {record[0][3]}", fg='white', bg='black', font=8, justify=CENTER)
            book_edition.grid(row=2, column=0, padx=10, pady=10)

            book_price = Label(display, text=f"Book Price:  {record[0][4]}", fg='white', bg='black', font=8, justify=CENTER)
            book_price.grid(row=3, column=0,padx=10, pady=10)

            connection = sqlite3.connect('all_books.db')
            c = connection.cursor()
            c.execute(f"SELECT issue FROM book_info WHERE bookId = {book_id}")
            record = c.fetchall()
            connection.commit()
            connection.close()

            if record[0][0] == 'issue':
                available = 'Availability: issue'
            else:
                available = 'Availability: not issued'
            available_label = Label(display, text=available, fg='white', bg='black', font=8, justify=CENTER)
            available_label.grid(row=4, column=0, padx=10, pady=10)
            display.mainloop()
        else:
            messagebox.showerror("Information", "Book not in database.")
    except ValueError:
        book_id_entry_one.delete(0, END)
        messagebox.showerror("Information", "Enter the correct datatype credentials.")

#defintion search book
def search_book():
    global search
    search = Tk()
    search.geometry("300x250")

    frame_search = Frame(search, width=300, height=50, bg='black')
    frame_search.grid(row=0, column=0, columnspan=2)

    search_label = Label(search, text="Search Book", font="bold", justify="center", bg='black', fg='red')
    search_label.grid(row=0, column=0, columnspan=2, pady=5)

    book_id_label = Label(search, text="Book ID", font=6)
    book_id_label.grid(row=1, column=0, padx=5, pady=10)

    global book_id_entry_one
    book_id_entry_one = Entry(search, width=25)
    book_id_entry_one.grid(row=1, column=1, pady=10, padx=5)

    search_button = Button(search, text="Search", command=lambda :display_book_information((book_id_entry_one.get())))
    search_button.grid(row=2, column=0, columnspan=2, ipadx=20, pady=10)
    search.mainloop()

#delete book checking
def delete_book_checking(bookID):
    try:
        book_id = int(bookID)
        found = False
        connection = sqlite3.connect('all_books.db')
        c = connection.cursor()
        c.execute("SELECT bookID FROM book_info")
        record = c.fetchall()
        connection.commit()
        connection.close()

        for item in record:
            if (book_id,) == item:
                found = True

        if found:
            connection = sqlite3.connect('all_books.db')
            c = connection.cursor()
            c.execute(f"SELECT issue FROM book_info WHERE bookId = {book_id}")
            record = c.fetchall()
            connection.commit()
            connection.close()

            if record[0][0] == 'issue':
                messagebox.showerror("Information", "Cannot Delete the Borrowed Book.")
            else:
                connection = sqlite3.connect('all_books.db')
                c = connection.cursor()
                c.execute(f"DELETE FROM book_info WHERE bookId = {book_id}")
                connection.commit()
                connection.close()
                messagebox.showinfo("Information", "Book Deleted from database.")
                delete_book_window.destroy()
        else:
            messagebox.showerror("Information", "Book Not in the Database.")
    except ValueError:
        book_id_ent.delete(0, END)
        messagebox.showerror("Information", "Enter the correct datatype credentials.")

#delete book function after delete button
def delete_book():
    global delete_book_window
    delete_book_window = Tk()
    delete_book_window.geometry("300x200")

    frame_d = Frame(delete_book_window, width=300, height=50, bg='black')
    frame_d.grid(row=0, column=0, columnspan=2)

    delete_label = Label(delete_book_window, text="Delete Book", font="bold", justify="center", bg='black', fg='white')
    delete_label.grid(row=0, column=0, columnspan=2, pady=20)

    book_id = Label(delete_book_window, text="Book Id", font=6)
    book_id.grid(row=1, column=0, pady=10)

    global book_id_ent
    book_id_ent = Entry(delete_book_window, width=25)
    book_id_ent.grid(row=1, column=1, pady=10)

    delete_button = Button(delete_book_window, text="Delete",
                               command=lambda :delete_book_checking((book_id_ent.get())))
    delete_button.grid(row=2, column=0, columnspan=2, ipadx=20, pady=10)
    delete_book_window.mainloop()

#commitiing the changes
def commit(bookID, title, author, edition, price):
    try:
        edition_new = int(edition)
        price_new = int(price)
        connection = sqlite3.connect('all_books.db')
        c = connection.cursor()
        c.execute("SELECT * FROM book_info")
        c.execute(f"""UPDATE book_info SET title = ? WHERE bookID = {bookID};""", (title,))
        c.execute(f"UPDATE book_info SET author = ? WHERE bookID = {bookID};", (author,))
        c.execute(f"UPDATE book_info SET edition = ? WHERE bookID = {bookID};", (edition_new,))
        c.execute(f"UPDATE book_info SET price = ? WHERE bookID = {bookID};", (price_new,))
        connection.commit()
        connection.close()
        messagebox.showinfo("Information", "Changes are done.")
        edit_window.destroy()
    except ValueError:
        edition_entry_edit.delete(0, END)
        price_entry_edit.delete(0, END)
        messagebox.showerror("Information", "Enter the correct datatype credentials.")

#display the other entry widgets if the book id exists in the database.
def edit_book_database(bookID, window):
    try:
        book_id = int(bookID)
        connection = sqlite3.connect('all_books.db')
        c = connection.cursor()
        c.execute("SELECT bookID FROM book_info")
        record = c.fetchall()
        connection.commit()
        connection.close()

        found_book = False
        for item in record:
            if book_id == item[0]:
                found_book = True
                break

        if found_book:
            connection = sqlite3.connect('all_books.db')
            c = connection.cursor()
            c.execute(f"SELECT bookID, title, author, edition, price FROM book_info WHERE bookId = {book_id}")
            record = c.fetchall()

            title_book = Label(window, text="Title", font=8)
            title_book.grid(row=3, column=0, padx=20, pady=5)

            title_entry = Entry(window, width=30)
            title_entry.insert(0, record[0][1])
            title_entry.grid(row=3, column=1, padx=10, pady=5)

            author_book = Label(window, text="Author", font=8)
            author_book.grid(row=4, column=0, padx=20, pady=5)

            author_entry = Entry(window, width=30)
            author_entry.insert(0, record[0][2])
            author_entry.grid(row=4, column=1, padx=10, pady=5)

            edition_book = Label(window, text="Edition", font=8)
            edition_book.grid(row=5, column=0, padx=20, pady=5)

            global edition_entry_edit
            edition_entry_edit = Entry(window, width=30)
            edition_entry_edit.insert(0, record[0][3])
            edition_entry_edit.grid(row=5, column=1, padx=10, pady=5)

            price_book = Label(window, text="Price", font=8)
            price_book.grid(row=6, column=0, padx=20, pady=5)

            global price_entry_edit
            price_entry_edit = Entry(window, width=30)
            price_entry_edit.insert(0, record[0][4])
            price_entry_edit.grid(row=6, column=1, padx=10, pady=5)

            commit_button = Button(window, text = "Commit the Changes",
            command=lambda: commit(book_id, title_entry.get(), author_entry.get(), (edition_entry_edit.get()),
                                   (price_entry_edit.get())))
            commit_button.grid(row=7, column=0, columnspan=2, padx=20, pady=10)
            connection.commit()
            connection.close()
            window.mainloop()
        else:
            messagebox.showerror("Information", f"The book with ID {book_id} is not in the records.")
            window.mainloop()
    except ValueError:
        book_id_edit.delete(0, END)
        messagebox.showerror("Information", "Enter the correct datatype credentials.")

#for editing the book of the input bookID
def edit_book_function():
    global edit_window
    edit_window = Tk()
    edit_window.geometry("370x400")

    frame_edit = Frame(edit_window, width=370, height=50, bg='black')
    frame_edit.grid(row=0, column=0, columnspan=2)

    edit_label = Label(edit_window, text="Edit Book Information", font="bold", justify="center", bg='black', fg='white')
    edit_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    book_id_label = Label(edit_window, text="Book ID", font=("bold", 14))
    book_id_label.grid(row=1, column=0, padx=10 ,pady=10)

    global book_id_edit
    book_id_edit = Entry(edit_window, width=35)
    book_id_edit.grid(row=1, column=1, padx=10, pady=10)

    submit_button_edit = Button(edit_window, text="Submit", borderwidth=2,
                                command=lambda: edit_book_database((book_id_edit.get()), edit_window))
    submit_button_edit.grid(row=2, column=0, columnspan=2, ipadx=20, pady=5)
    edit_window.mainloop()

def issue_book_command(bookID, usn, date):
    # retrieving all the information of the student from the database
    connection = sqlite3.connect('student_database.db')
    c = connection.cursor()
    c.execute(f"SELECT USN, name, course, phone, college FROM student_info WHERE USN = {usn}")
    # the below record has the information of the student
    record = c.fetchall()
    connection.commit()
    connection.close()

    # adding a new record in the student_issue_record table if it does not exist
    connection = sqlite3.connect('student_book.db')
    c = connection.cursor()
    c.execute("SELECT USN FROM student_issue_record")
    # the bellow record has all the USN number
    record_one = c.fetchall()
    connection.commit()
    connection.close()

    connection_check = sqlite3.connect('all_books.db')
    c_check = connection_check.cursor()
    c_check.execute(f"SELECT reserved FROM book_info WHERE bookId = {bookID}")
    record_two = c_check.fetchall()
    connection_check.commit()
    connection_check.close()

    if ("reserved",) not in record_two:
        if (usn,) not in record_one:
            connection = sqlite3.connect("student_book.db")
            c = connection.cursor()
            c.execute(
                "INSERT INTO student_issue_record (USN, name, course, phone, college, noBook) VALUES (?, ?, ?, ?, ?, ?);",
                (record[0][0], record[0][1], record[0][2], record[0][3], record[0][4], 0))
            connection.commit()
            connection.close()

        # checking if the student is borrowing more than the maximum number of books
        borrow_condition = False

        connection = sqlite3.connect('student_book.db')
        c = connection.cursor()
        c.execute(f"SELECT noBook FROM student_issue_record WHERE USN = {usn}")
        # the below record has the information of books borrowed
        record_for_checking = c.fetchall()
        final_record = record_for_checking[0][0]
        if final_record >= 3:
            messagebox.showerror("Information", "Cannot Borrow more than 3 books.")
        else:
            borrow_condition = True
            c.execute(f"UPDATE student_issue_record SET noBook = {final_record + 1} WHERE USN = {usn}")
            c.execute(f"UPDATE student_issue_record SET charge = {100} WHERE USN = {usn}")
            c.execute(f"UPDATE student_issue_record SET fromDate = (?) WHERE USN = {usn}", (cal.get_date(),))
            c.execute(f"UPDATE student_issue_record SET toDate = (?) WHERE USN = {usn}", (date,))
        connection.commit()
        connection.close()

        if borrow_condition:
            connection = sqlite3.connect('all_books.db')
            c = connection.cursor()
            c.execute(f"UPDATE book_info SET issue = 'issue' WHERE bookID = {bookID}")
            c.execute(f"UPDATE book_info SET stdID = {usn} WHERE bookID = {bookID}")
            connection.commit()
            connection.close()
            ####To Do:  display the borrowed book in the issue Tk() window.
            messagebox.showinfo("Information", "Book Borrowed.")
    else:
        #check if the reservedID is same as the usn number
        connection = sqlite3.connect("all_books.db")
        c = connection.cursor()
        c.execute(f"SELECT reservedID FROM book_info WHERE bookID = {bookID}")
        record_id = c.fetchall()
        connection.commit()
        connection.close()

        found_issue = False
        connection = sqlite3.connect("all_books.db")
        c = connection.cursor()
        c.execute(f"SELECT issue FROM book_info WHERE bookID = {bookID}")
        record_issue = c.fetchall()
        connection.commit()
        connection.close()

        if ("issue", ) in record_issue:
            found_issue = True

        if found_issue:
            messagebox.showerror("Information", "Can borrow the book once the book is returned.")
        else:
            if (usn, ) in record_id:
                if (usn,) not in record_one:
                    connection = sqlite3.connect("student_book.db")
                    c = connection.cursor()
                    c.execute("INSERT INTO student_issue_record (USN, name, course, phone, college, noBook) VALUES (?, ?, ?, ?, ?, ?);",
                        (record[0][0], record[0][1], record[0][2], record[0][3], record[0][4], 0))
                    connection.commit()
                    connection.close()

                # checking if the student is borrowing more than the maximum number of books
                borrow_condition = False
                connection = sqlite3.connect('student_book.db')
                c = connection.cursor()
                c.execute(f"SELECT noBook FROM student_issue_record WHERE USN = {usn}")
                # the below record has the information of books borrowed
                record_for_checking = c.fetchall()
                final_record = record_for_checking[0][0]
                if final_record >= 3:
                    messagebox.showerror("Information", "Cannot Borrow more than 3 books.")
                else:
                    borrow_condition = True
                    c.execute(f"UPDATE student_issue_record SET noBook = {final_record + 1} WHERE USN = {usn}")
                    c.execute(f"UPDATE student_issue_record SET charge = {100} WHERE USN = {usn}")
                    c.execute(f"UPDATE student_issue_record SET fromDate = (?) WHERE USN = {usn}", (cal.get_date(),))
                    c.execute(f"UPDATE student_issue_record SET toDate = (?) WHERE USN = {usn}", (date,))
                connection.commit()
                connection.close()

                if borrow_condition:
                    connection = sqlite3.connect('all_books.db')
                    c = connection.cursor()
                    c.execute(f"UPDATE book_info SET issue = 'issue' WHERE bookID = {bookID}")
                    c.execute(f"UPDATE book_info SET stdID = {usn} WHERE bookID = {bookID}")
                    c.execute(f"UPDATE book_info SET reserved = (?) WHERE bookID = {bookID}", ("no",))
                    c.execute(f"UPDATE book_info SET reservedID = (?) WHERE bookID = {bookID}", (0,))
                    connection.commit()
                    connection.close()
                    ####To Do:  display the borrowed book in the issue Tk() window.
                    messagebox.showinfo("Information", "Book Borrowed.")
            else:
                messagebox.showerror("Information", "Book is reserved.")

#issue book submit
def issue_book(bookID, title, usn, window):
    try:
        book_id = int(bookID)
        found_book = False

        connection = sqlite3.connect('all_books.db')
        c = connection.cursor()
        c.execute("SELECT bookID, title FROM book_info")
        record = c.fetchall()

        if (book_id, str(title),) in record:
            ##Just to check in case of errors while issuing books because of unwanted space.##
            found_book = True
        connection.commit()
        connection.close()

        if found_book:
            connection = sqlite3.connect("all_books.db")
            c = connection.cursor()
            c.execute(f"SELECT issue FROM book_info WHERE bookId = {book_id}")
            record_issue = c.fetchall()
            connection.commit()
            connection.close()

            if ("issue",) in record_issue:
                messagebox.showerror("Information", "Book already borrowed.")
            else:
                frame_issue = Frame(window, width=400, height=50, bg='black')
                frame_issue.grid(row=8, column=0, columnspan=2)

                issue_book_label = Label(window, text="Issue Book", font="bold", fg='magenta', bg='black')
                issue_book_label.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

                issue_cal = Calendar(window, selectmode="day", year=2022, month=7, day=3)
                issue_cal.grid(row=9, column=0, columnspan=2, padx=80, pady=5)

                issue_button = Button(window, text="Issue",
                                      command=lambda: issue_book_command(book_id, usn, issue_cal.get_date()))
                issue_button.grid(row=10, columnspan=2, column=0, padx=20, pady=5, ipadx=35)
        else:
            messagebox.showerror("Information", f"The book with ID {book_id} in not in the records.")
    except ValueError:
        book_id_entry.delete(0, END)
        messagebox.showerror("Information", "Enter the correct datatype credentials.")

#checking if the student is in the database
def student_checking(usn, window):
    try:
        usn_student_checking = int(usn)
        connection = sqlite3.connect('student_database.db')
        c = connection.cursor()
        c.execute("SELECT USN FROM student_info")
        record = c.fetchall()

        found = False
        for item in record:
            if usn_student_checking == item[0]:
                found = True
                break
        connection.commit()
        connection.close()

        if found:
            connection = sqlite3.connect('student_database.db')
            c = connection.cursor()
            c.execute(f"SELECT name, USN, course, phone, college FROM student_info WHERE USN = {usn_student_checking}")
            record = c.fetchall()
            display = f"Name: \t {record[0][0]} \n" \
                      f"USN Number:\t {record[0][1]} \n" \
                      f"Course: \t {record[0][2]} \n" \
                      f"Phone: \t {record[0][3]} \n" \
                      f"College: \t {record[0][4]}"
            std_information = Label(window, text=display, font=("bold", 12))
            std_information.grid(row=3, column=0, columnspan=2, pady=25, padx=5)
            connection.commit()
            connection.close()

            frame_issue = Frame(window, width=400, height=50, bg='black')
            frame_issue.grid(row=4, column=0, columnspan=2)

            issue_book_text = Label(window, text="Issue Book", font="bold", bg='black', fg='yellow')
            issue_book_text.grid(row=4, column=0, padx=5, pady=10, columnspan=2)

            book_id = Label(window, text="Book ID", font="bold")
            book_id.grid(row=5, column=0, padx=40, pady=5)

            global book_id_entry
            book_id_entry = Entry(window, width=30)
            book_id_entry.grid(row=5, column=1, padx=10, pady=5)

            title = Label(window, text="Title", font="bold")
            title.grid(row=6, column=0, padx=40, pady=5)

            title_entry = Entry(window, width=30)
            title_entry.grid(row=6, column=1, padx=10, pady=5)

            submit_issue = Button(window, text="Submit", font="bold", borderwidth=3,
                                  command=lambda: issue_book((book_id_entry.get()), title_entry.get()
                                                             , usn_student_checking, window))
            submit_issue.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=30)
            window.mainloop()
        else:
            messagebox.showerror("Information", "Invalid USN Number")
    except ValueError:
        usn_entry_issue.delete(0, END)
        messagebox.showerror("Information", "Enter the correct datatype credentials.")

#issue book function
def issuing_book():
    global book_issue
    book_issue = Tk()
    book_issue.geometry("400x755")

    frame_issue = Frame(book_issue, width=400, height=50, bg='black')
    frame_issue.grid(row=0, column=0, columnspan=2)

    text_issue = Label(book_issue, text="Student Information", font="bold", bg='black', fg='magenta', justify="center")
    text_issue.grid(row=0, column=0, padx=10,pady=10, columnspan=2)

    usn_text = Label(book_issue, text="USN", font="bold")
    usn_text.grid(row=1, column=0, padx=40,pady=10)

    global usn_entry_issue
    usn_entry_issue = Entry(book_issue, width=35)
    usn_entry_issue.grid(row=1, column=1, padx=10, pady=10)

    submit = Button(book_issue, text="Submit", borderwidth=2, font="bold",
                    command= lambda: student_checking((usn_entry_issue.get()), book_issue))
    submit.grid(row=2, column=0, columnspan=2, ipadx=30)
    book_issue.mainloop()

#adding the book to the all_book database
def add_book(book_id, title, author, edition, price):
    try:
        book_id = int(book_id)
        edition = int(edition)
        price = int(price)
        connection = sqlite3.connect('all_books.db')
        c = connection.cursor()
        c.execute("INSERT INTO book_info (bookID, title, author, edition, price) VALUES (?, ?, ?, ?, ?);",
                  (book_id, title, author, edition, price))
        messagebox.showinfo("Information", "Book Added, Close.")
        connection.commit()
        connection.close()
        new_book.destroy()
    except ValueError:
        id_entry_book.delete(0, END)
        edition_entry.delete(0, END)
        price_entry.delete(0, END)
        messagebox.showerror("Information", "Enter the correct datatype credentials.")

#function to new window to add book
def book_new():
    global new_book
    new_book = Tk()
    new_book.geometry("300x350")

    frame_book = Frame(new_book, width=300, height=50, bg='black')
    frame_book.grid(row=0, column=0, columnspan=2)

    text_book = Label(new_book, text="New Book", font="bold", justify="center", bg='black', fg='white')
    text_book.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

    id_book = Label(new_book, text="Book ID", font=8)
    id_book.grid(row=1, column=0, padx=10, pady=10)

    global id_entry_book
    id_entry_book = Entry(new_book, width=30)
    id_entry_book.grid(row=1, column=1, padx=10, pady=10)

    title_book = Label(new_book, text="Title", font=8)
    title_book.grid(row=2, column=0, padx=10, pady=5)

    title_entry = Entry(new_book, width=30)
    title_entry.grid(row=2, column=1, padx=10, pady=5)

    author_book = Label(new_book, text="Author", font=8)
    author_book.grid(row=3, column=0, padx=10, pady=5)

    author_entry = Entry(new_book, width=30)
    author_entry.grid(row=3, column=1, padx=10, pady=5)

    edition_book = Label(new_book, text="Edition", font=8)
    edition_book.grid(row=4, column=0, padx=10, pady=5)

    global edition_entry
    edition_entry = Entry(new_book, width=30)
    edition_entry.grid(row=4, column=1, padx=10, pady=5)

    price_book = Label(new_book, text="Price", font=8)
    price_book.grid(row=5, column=0, padx=10, pady=5)

    global price_entry
    price_entry = Entry(new_book, width=30)
    price_entry.grid(row=5, column=1, padx=10, pady=5)

    submit_book_button = Button(new_book, text="Submit", padx=5, pady=5, font=4
    , command=lambda: add_book((id_entry_book.get()), title_entry.get(), author_entry.get(),
                               (edition_entry.get()), (price_entry.get())))
    submit_book_button.grid(row=6, column=0, columnspan=2, pady=20, ipadx=40)
    new_book.mainloop()

#adding in the database, new admin (admin)
def addition_admin_new(id_, password, first, last, contact, email):
    try:
        id_new = int(id_)
        password_new = int(password)
        contact_new = int(contact)
        connection = sqlite3.connect('admin.db')
        c = connection.cursor()
        c.execute("INSERT INTO admin_info VALUES (?, ?, ?, ?, ?, ?);",(id_new, password_new, first, last, contact_new, email))
        messagebox.showinfo("Information", "New Admin added. Close")
        connection.commit()
        connection.close()
        new_admin.destroy()
    except ValueError:
        id_entry_new.delete(0, END)
        password_entry_new.delete(0, END)
        contact_entry.delete(0, END)
        messagebox.showerror("Information", "Enter the correct datatype credentials.")

#adding in the database, new student (student_database)
def addition_student_new(usn, password, name, course, phone, college):
    try:
        usn_new = int(usn)
        password_new = int(password)
        phone_new = int(phone)

        connection = sqlite3.connect('student_database.db')
        c = connection.cursor()
        c.execute("INSERT INTO student_info VALUES (?, ?, ?, ?, ?, ?);", (usn_new, password_new, name, course,
                                                                          phone_new, college))
        messagebox.showinfo("Information", "New Student added. Close")
        connection.commit()
        connection.close()
        new_student.destroy()
    except ValueError:
        usn_entry.delete(0, END)
        password_entry_student.delete(0, END)
        phone_entry.delete(0, END)
        messagebox.showerror("Information", "Enter the correct datatype credentials.")

#function for adding a new admin to the database
def admin_new():
    global new_admin
    new_admin = Tk()

    new_admin.geometry("300x350")

    frame_admin = Frame(new_admin, width=300, height=50, bg='black')
    frame_admin.grid(row=0, column=0, columnspan=2)

    text_new = Label(new_admin, text="New Admin", font="bold", justify="center", bg='black', fg='white')
    text_new.grid(row=0, columnspan=2, column=0, padx = 10, pady=10)

    id_text = Label(new_admin, text="ID", font=8)
    id_text.grid(row=1, column=0, padx = 10, pady=10)

    global id_entry_new
    id_entry_new = Entry(new_admin, width=26)
    id_entry_new.grid(row=1, column=1, padx = 10, pady=10)

    password_text_new = Label(new_admin, text="Password", font=8)
    password_text_new.grid(row=2, column=0, padx=5, pady=5)

    global password_entry_new
    password_entry_new = Entry(new_admin, width=26, show="*")
    password_entry_new.grid(row=2, column=1, padx=5, pady=5)

    first_text = Label(new_admin, text="First Name", font=8)
    first_text.grid(row=3, column=0, padx=5, pady=5)

    first_entry = Entry(new_admin, width=26)
    first_entry.grid(row=3, column=1, padx=5, pady=5)

    last_text = Label(new_admin, text="Last Name", font=8)
    last_text.grid(row=4, column=0, padx=5, pady=5)

    last_entry = Entry(new_admin, width=26)
    last_entry.grid(row=4, column=1, padx=5, pady=5)

    contact_text = Label(new_admin, text="Contact", font=8)
    contact_text.grid(row=5, column=0, padx=5, pady=5)

    global contact_entry
    contact_entry = Entry(new_admin, width=26)
    contact_entry.grid(row=5, column=1, padx=5, pady=5)

    email_text = Label(new_admin, text="Email", font=8)
    email_text.grid(row=6, column=0, padx=5, pady=5)

    email_entry = Entry(new_admin, width=26)
    email_entry.grid(row=6, column=1, padx=5, pady=5)

    submit_button_new = Button(new_admin, text="Submit", font=("Arial", 10), borderwidth=5,
                               command=lambda:
    addition_admin_new((id_entry_new.get()), (password_entry_new.get()), first_entry.get(), last_entry.get(),
                       (contact_entry.get()), email_entry.get()))
    submit_button_new.grid(row=7, column=0, columnspan=2, padx=(15, 0), pady=5, ipadx=60, ipady=6)
    new_admin.mainloop()

#function for adding a new student into the database
def student_new():
    global new_student
    new_student = Tk()
    new_student.geometry("300x365")

    frame_student = Frame(new_student, width=300, height=50, bg='black')
    frame_student.grid(row=0, column=0, columnspan=2)

    text_start = Label(new_student, text="New Student", font="bold", justify="center", bg='black', fg='white')
    text_start.grid(row=0, column=0, pady=5, columnspan=2)

    usn_text = Label(new_student, text="USN", font=5)
    usn_text.grid(row=1, column=0,padx=10, pady=10)

    global usn_entry
    usn_entry = Entry(new_student, width=30)
    usn_entry.grid(row=1, column=1, padx=5, pady=10)

    password_label = Label(new_student, text="Password", font=5)
    password_label.grid(row=2,column=0, padx=5, pady=10)

    global password_entry_student
    password_entry_student = Entry(new_student, width=25, font=("Arial", 10), show="*")
    password_entry_student.grid(row=2, column=1, pady=10)

    name_text = Label(new_student, text="Name", font=5)
    name_text.grid(row=3, column=0, padx=10, pady=5)

    name_entry = Entry(new_student, width=30)
    name_entry.grid(row=3, column=1, padx=5, pady=5)

    course_text = Label(new_student, text="Course", font=5)
    course_text.grid(row=4, column=0, padx=10, pady=5)

    course_entry = Entry(new_student, width=30)
    course_entry.grid(row=4, column=1, padx=5, pady=5)

    phone_text = Label(new_student, text="Phone", font=5)
    phone_text.grid(row=5, column=0, padx=10, pady=5)

    global phone_entry
    phone_entry = Entry(new_student, width=30)
    phone_entry.grid(row=5, column=1, padx=5, pady=5)

    college_text = Label(new_student, text="College", font=5)
    college_text.grid(row=6, column=0, padx=10, pady=5)

    college_entry = Entry(new_student, width=30)
    college_entry.grid(row=6, column=1, padx=5, pady=5)

    submit_button_std = Button(new_student, text="Submit", borderwidth=2, background='white',
    command=lambda: addition_student_new((usn_entry.get()), (password_entry_student.get()), name_entry.get(), course_entry.get(),
                                         (phone_entry.get()), college_entry.get()))
    submit_button_std.grid(row=7, column=0, columnspan=2, pady=10, ipadx=50)
    new_student.mainloop()

#function to display time
def display_time(time_label):
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    am_pm = time.strftime("%p")

    time_label.config(text=hour+":"+minute+":"+second+" "+am_pm)
    time_label.after(1000, lambda :display_time(time_label))

#main dashboard
def main_page():
    main = Tk()
    main.geometry("600x550")

    frame2 = Frame(main, width=600, height=55, bg='black')
    frame2.grid(row=0, column=0, columnspan=2)

    text_initial = Label(main, text="DashBoard", font=("Arial", 30), fg='white', bg='black', justify='center',
                         background='black')
    text_initial.grid(row=0, column=0, columnspan=2, pady=5)

    #Name from the records
    connection = sqlite3.connect('admin.db')
    c = connection.cursor()
    c.execute(f"SELECT first_name, last_name FROM admin_info WHERE ID = {user_entry.get()}")
    record = c.fetchall()
    name = Label(main, text=f"Name: {record[0][0]} {record[0][1]}", font="bold")
    name.grid(row=1, column=0)
    connection.commit()
    connection.close()
    #Date
    date = Label(main, text=f"Date: {cal.get_date()}", font="bold")
    date.grid(row=1, column=1)
    login.destroy()
    time_label = Label(main, text="", font='bold')
    time_label.grid(row=2, column=0, columnspan=2)
    display_time(time_label)

    admin_new_button = Button(main, text = "Add new Admin", padx=10, pady=10, font=("Bold", 12), fg='blue', borderwidth=5,
                              command=admin_new)
    admin_new_button.grid(row=3, column = 0, ipadx=60, padx=20, pady=10)

    student_new_button = Button(main, text="Add new Student", padx=10, pady=10, font=("Bold", 12), fg='blue', borderwidth=5,
                              command=student_new)
    student_new_button.grid(row=3, column=1, ipadx=60, padx=2, pady=10)

    add_book_button = Button(main, text="Add Book", font=("Arial", 12), fg='white', bg='red', borderwidth=3, padx=10
                             , pady=10, command=book_new)
    add_book_button.grid(row=4, column=0, padx=20, pady=10, ipadx=70)

    issue_book_button = Button(main, text="Issue Book", font=("Arial", 12), fg='white', bg='blue', borderwidth=3, padx=10,
                             pady=10, command=issuing_book)
    issue_book_button.grid(row=4, column=1, padx=20, pady=10, ipadx=70)

    edit_book_button = Button(main, text="Edit Book", font=("Arial", 12), fg='white', bg='green', borderwidth=3,
                               padx=10,
                               pady=10, command=edit_book_function)
    edit_book_button.grid(row=5, column=0, padx=20, pady=10, ipadx=70)

    return_book_button = Button(main, text="Return Book", font=("Arial", 12), fg='white', bg='purple', borderwidth=3,
                               padx=10,
                               pady=10, command=return_book)
    return_book_button.grid(row=5, column=1, padx=20, pady=10, ipadx=70)

    search_book_button = Button(main, text="Search Book", font=("Arial", 12), fg='white', bg='magenta', borderwidth=3,
                                padx=10,
                                pady=10, command=search_book)
    search_book_button.grid(row=6, column=0, padx=20, pady=10, ipadx=60)

    view_book_button = Button(main, text="View All Books", font=("Arial", 12), fg='white', bg='green', borderwidth=3,
                            padx=10, pady=10, command=view_book)
    view_book_button.grid(row=7,column=0, padx=20, pady=10, ipadx=53)


    delete_button = Button(main, text="Delete Book", font=("Arial", 12), fg='white', bg='blue', borderwidth=3,
                           padx=10, pady=10, command=delete_book)
    delete_button.grid(row=6, column=1, padx=20, pady=10, ipadx=60)

    view_admin_button = Button(main, text="View All Admin", font=("Arial", 12), fg='white', bg='red', borderwidth=3,
                               padx=10, pady=10, command=view_admin)
    view_admin_button.grid(row=7, column=1, padx=20, pady=10, ipadx=53)

    view_student_button = Button(main, text="View All Students", font=("Arial",12), fg='white', bg='pink', borderwidth=3,
                                 padx=10, pady=10, command=view_student)
    view_student_button.grid(row=8, column=0, padx=20,pady=10, ipadx=48)

    view_issue_record_button = Button(main, text="View Issue Record", font=("Arial", 12), fg='white', bg='blue', borderwidth=3,
                         padx=10,
                         pady=10, command=view_issue_record)
    view_issue_record_button.grid(row=8, column=1, padx=20, pady=10, ipadx=50)
    main.mainloop()

#function for changing the password in the database
def checking(user_id, new_password):
    try:
        user_id_new = int(user_id)
        new_password_new = int(new_password)
        connection = sqlite3.connect('admin.db')
        cursor = connection.cursor()
        cursor.execute("SELECT ID FROM admin_info")
        record = cursor.fetchall()
        found = False
        for item in record:
            if (user_id_new,) == item:
                found = True
        connection.commit()
        connection.close()

        if found:
            connection = sqlite3.connect('admin.db')
            cursor = connection.cursor()
            cursor.execute("SELECT ID, password FROM admin_info")
            cursor.execute(f"UPDATE admin_info SET password = {new_password_new} WHERE ID = {user_id_new}")
            connection.commit()
            connection.close()
            messagebox.showinfo("Change Password", "Password Changed")
            reset.destroy()
        else:
            messagebox.showinfo("Information", "Enter correct User ID")
    except ValueError:
        user_entry_reset.delete(0, END)
        password_entry_reset.delete(0, END)
        messagebox.showerror("Information", "Enter the correct datatype credentials.")

#function to reset the password for th given admin i.e., for the given user id number
def forgot_password():
    global reset
    reset = Tk()
    reset.geometry("300x300")
    reset.title("Change Password")

    frame1 = Frame(reset, width=300, height=50, bg='black')
    frame1.grid(row=0, column=0, columnspan=2)

    text_label = Label(reset, text="NEW PASSWORD", font=("BOLD", 20), fg='red', justify='center',  bg='black')
    text_label.grid(row=0, column=0, padx=(10, 10), pady=10, columnspan=2)

    user_id_text_reset = Label(reset, text="User-ID", font=("Arial", 10), fg='black')
    user_id_text_reset.grid(row=1, column=0, pady=25, padx=15)

    global user_entry_reset
    user_entry_reset = Entry(reset, width=25, font=("Arial", 10))
    user_entry_reset.grid(row=1, column=1, pady=25)

    password_text_reset = Label(reset, text="Password", font=("Arial", 10), fg='black')
    password_text_reset.grid(row=2, column=0, pady=25, padx=15)

    global password_entry_reset
    password_entry_reset = Entry(reset, width=25, font=("Arial", 10), show="*")
    password_entry_reset.grid(row=2, column=1, pady=25)

    submit_button_reset = Button(reset, text="Submit", font=("Arial", 12), command=lambda:
                                 checking((user_entry_reset.get()), (password_entry_reset.get())), borderwidth=5)
    submit_button_reset.grid(row=3, column=0, columnspan=2, padx=(15, 0), pady=25, ipadx=100)
    reset.mainloop()

#to check if the input i.e., user id and password is correct
def login_button_check():
    try:
        user_id = int(user_entry.get())
        password = int(password_entry.get())
        connection = sqlite3.connect('admin.db')
        cursor1 = connection.cursor()
        cursor1.execute("SELECT ID, password FROM admin_info")
        record = cursor1.fetchall()
        found = False
        for item in record:
            if (user_id, password,) == item:
                found = True
        connection.commit()
        connection.close()
        if found:
            submit_button.config(state=DISABLED)
            forgot_button.config(state=DISABLED)
            main_page()
        else:
            messagebox.showerror("Information", "Wrong Credential")
    except ValueError:
        user_entry.delete(0, END)
        password_entry.delete(0, END)
        messagebox.showerror("Information", "Enter the correct datatype credentials.")

#clearing the entry boxes
def clear():
    user_entry.delete(0, END)
    password_entry.delete(0, END)


text = Label(login, text="ADMIN LOGIN", font=("BOLD", 25), fg='white', justify=CENTER, background='black')
text.grid(row=0, column=0, padx=(10,10), pady=10, columnspan=2)

user_id_text = Label(login, text="User-ID", font=("Arial", 15), fg= 'black')
user_id_text.grid(row=1, column=0, pady=10, padx=15)

user_entry = Entry(login, width=25, font=("Arial", 10))
user_entry.grid(row=1, column=1, pady=10)

password_text = Label(login, text="Password", font=("Arial", 15), fg= 'black')
password_text.grid(row=2, column=0, pady=10, padx=15)

password_entry = Entry(login, width=25, font=("Arial", 10), show="*")
password_entry.grid(row=2, column=1, pady=10)

submit_button = Button(login, text="Login", font=("Arial", 12), command=login_button_check, borderwidth=5)
submit_button.grid(row=3, column=0, columnspan=2, padx=(15, 0), pady=15, ipadx=100)

forgot_button = Button(login, text="Forgot Password", font=("Arial", 12), command=forgot_password, borderwidth=5)
forgot_button.grid(row=4, column=0, columnspan=2, padx=(15, 0), pady=15, ipadx=65)

clear_button = Button(login, text="Clear", font=("Arial", 12), command=clear, borderwidth=5)
clear_button.grid(row=5, column=0, columnspan=2, padx=(15, 0), pady=15, ipadx=65)

set_date = Label(login, text="Set Today's Date", font="bold")
set_date.grid(row=6, column=0, columnspan=2)

cal = Calendar(login, selectmode="day", year=2022, month=7, day=3)
cal.grid(row=7, column=0, padx=10, pady=10, columnspan=2)
login.mainloop()