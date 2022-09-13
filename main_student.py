import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

main_student_login = Tk()
main_student_login.geometry("350x200")

reserve = ''
book_entry = ''
book_entry_cancel = ''

# function to cancel the reserving book
def cancel_function(usn, bookID):
    try:
        bookID = int(bookID)
        connection = sqlite3.connect("all_books.db")
        c = connection.cursor()
        c.execute("SELECT bookID FROM book_info")
        record_id = c.fetchall()
        connection.commit()
        connection.close()

        if (bookID, ) in record_id:
            connection = sqlite3.connect("all_books.db")
            c = connection.cursor()
            c.execute(f"SELECT reserved FROM book_info WHERE bookId = {bookID}")
            record_reserved = c.fetchall()
            connection.commit()
            connection.close()

            if ("reserved",) in record_reserved:
                connection = sqlite3.connect("all_books.db")
                c = connection.cursor()
                c.execute(f"SELECT reservedID FROM book_info WHERE bookID = {bookID}")
                record_reserved_id = c.fetchall()
                connection.commit()
                connection.close()
                if record_reserved_id[0][0] != usn:
                    messagebox.showerror("Information", f"Student with USN {usn} did not reserve the book with ID {bookID}.")
                else:
                    connection = sqlite3.connect("all_books.db")
                    c = connection.cursor()
                    c.execute(f"UPDATE book_info SET reserved = 'no' WHERE bookID = {bookID};")
                    c.execute(f"UPDATE book_info SET reservedID = (?) WHERE bookID = {bookID};", (0,))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo("Information", "Reserve Cancelled.")
            else:
                messagebox.showerror("Information", "Did not reserve this book.")
        else:
            messagebox.showerror("Information", f"The book with ID {bookID} not in the database.")
    except ValueError:
        book_entry_cancel.delete(0, END)
        messagebox.showerror("Information", "Enter the correct datatype credentials.")

# function to cancel the reserving window
def cancel_reserve(usn):
    cancel_window = Tk()
    cancel_window.geometry("310x150")
    cancel_window.title("Cancel Reserved Book")
    cancel_window.title("Cancel Reserve")

    frame_cancel = Frame(cancel_window, width=310, height=50, bg='black')
    frame_cancel.grid(row=0, column=0, columnspan=2)

    first_label_cancel = Label(cancel_window, text="CANCEL RESERVE",
                        font=("BOLD", 25), fg='white', justify=CENTER, background='black')
    first_label_cancel.grid(row=0, column=0, columnspan=2)

    book_id_label = Label(cancel_window, text="Book ID")
    book_id_label.grid(row=1, column=0, padx=5, pady=10)

    global book_entry_cancel
    book_entry_cancel = Entry(cancel_window, width=30)
    book_entry_cancel.grid(row=1, column=1, padx=5, pady=10)

    submit_cancel_button = Button(cancel_window, text="Cancel", padx=5, pady=5,
                                  command=lambda :cancel_function(usn, book_entry_cancel.get()))
    submit_cancel_button.grid(row=2, column=0, columnspan=2, pady=10)
    cancel_window.mainloop()

# function to display all the books to the student
def display_book():
    display_window = Tk()
    display_window.geometry("700x350")
    display_window.title("Display All Books")

    tree_frame = Frame(display_window)
    tree_frame.pack()

    tree_scroll_y = Scrollbar(tree_frame)
    tree_scroll_y.pack(side=RIGHT, fill=Y)

    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll_y.set)
    tree_scroll_y.config(command=my_tree.yview)

    #defining the columns for the my_tree
    my_tree['columns'] = ["bookID", "title", "author", "edition", "price", "availability", "reservedId", "issued"]

    #formatting the columns
    my_tree.column("#0", stretch=NO, width=0)
    my_tree.column("bookID", anchor=CENTER, width=75, minwidth=50)
    my_tree.column("title", anchor=CENTER, width=100, minwidth=85)
    my_tree.column("author", anchor=CENTER, width=100, minwidth=85)
    my_tree.column("edition", anchor=CENTER, width=60, minwidth=60)
    my_tree.column("price", anchor=CENTER, width=60, minwidth=60)
    my_tree.column("availability", anchor=CENTER, width=100, minwidth=75)
    my_tree.column("reservedId", anchor = CENTER, width=125, minwidth=125)
    my_tree.column("issued", anchor=CENTER, width=50, minwidth=50)

    #formatting the headings
    my_tree.heading("bookID", text="Book ID")
    my_tree.heading("title", text="Title")
    my_tree.heading("author", text="Author")
    my_tree.heading("edition", text="Edition")
    my_tree.heading("price", text="Price")
    my_tree.heading("availability", text="Availability")
    my_tree.heading("reservedId", text="Reserved student ID")
    my_tree.heading("issued", text="issued")

    connection = sqlite3.connect("all_books.db")
    c = connection.cursor()
    c.execute("SELECT bookID, title, author, edition, price, reserved, reservedID, issue FROM book_info")
    records = c.fetchall()
    connection.commit()
    connection.close()

    count = 0
    for item in records:
        if item[5] != "reserved":
            if item[7] == "issue":
                empty_tuple = (item[0], item[1], item[2], item[3], item[4], "Not Reserved", "None", "issue")
                my_tree.insert(parent="", index='end', iid=str(count), values=empty_tuple)
            else:
                empty_tuple = (item[0], item[1], item[2], item[3], item[4], "Not Reserved", "None", "No")
                my_tree.insert(parent="", index='end', iid=str(count), values=empty_tuple)
        else:
            my_tree.insert(parent="", index="end", iid=str(count), values=item)
        count += 1
    my_tree.pack(pady=10)
    display_window.mainloop()

#function to reserve
def reserve_function(usn, bookID):
    try:
        bookID = int(bookID)
        connection = sqlite3.connect('all_books.db')
        c = connection.cursor()
        c.execute("SELECT bookID FROM book_info")
        record = c.fetchall()
        connection.commit()
        connection.close()

        found = False
        if (bookID, ) in record:
            found = True

        if found:
            connection = sqlite3.connect('all_books.db')
            c = connection.cursor()
            c.execute("SELECT reserved FROM book_info WHERE bookID = (?);", (bookID,))
            reserved_record = c.fetchall()
            connection.commit()
            connection.close()

            if ('reserved', ) in reserved_record:
                messagebox.showerror("Information", "Book is already reserved.")
            else:
                reserve.destroy()
                connection = sqlite3.connect('all_books.db')
                c = connection.cursor()
                c.execute("UPDATE book_info SET reserved = 'reserved' WHERE bookId = (?);", (bookID,))
                c.execute("UPDATE book_info SET reservedId = (?) WHERE bookID = (?);", (usn, bookID,))
                connection.commit()
                connection.close()
                messagebox.showinfo("Information", "Book Reserved.")
        else:
            messagebox.showerror("Information", "Book not in Library.")
    except ValueError:
        book_entry.delete(0, END)
        messagebox.showerror("Information", "Enter the correct datatype credentials.")

# function to reserve a book
def reserve_window(usn):
        global reserve
        reserve = Tk()
        reserve.geometry("250x150")
        reserve.title("Reserve Book")
        frame_window = Frame(reserve, width=250, height=50, bg='black')
        frame_window.grid(row=0, column=0, columnspan=2)
        initial_label = Label(reserve, text="Book Reserving", font=("BOLD", 25), fg='white', justify=CENTER,
                              background='black')
        initial_label.grid(row=0, column=0, columnspan=2)
        book_id_label = Label(reserve, text="Book ID")
        book_id_label.grid(row=1, column=0, padx=5, pady=10)

        global book_entry
        book_entry = Entry(reserve, width=30)
        book_entry.grid(row=1, column=1, padx=5, pady=10)

        submit_button_reserve = Button(reserve, text="Submit", padx=5, pady=5,
                                       command=lambda :reserve_function(usn, (book_entry.get())))
        submit_button_reserve.grid(row=2, columnspan=2, column=0)
        reserve.mainloop()

# function to open the new window
def new_window(usn):
    main_student_login.destroy()
    window = Tk()
    window.geometry("250x285")
    window.title("Student's Dashboard")

    frame_window = Frame(window, width=250, height=50, bg='black')
    frame_window.grid(row=0, column=0, columnspan=2)

    first_label_window = Label(window, text="DASHBOARD",font=("BOLD", 25), fg='white', justify=CENTER,
                               background='black')
    first_label_window.grid(row=0,column=0)

    reserve_book_button = Button(window, text="Reserve Book", justify=CENTER, padx=5, pady=5, font=4,
                                 command=lambda :reserve_window(usn))
    reserve_book_button.grid(row=1, column=0, pady=10)

    cancel_reserve_book_button = Button(window, text="Cancel Reserve", justify=CENTER, padx=5, pady=5, font=4,
                                        command=lambda :cancel_reserve(usn))
    cancel_reserve_book_button.grid(row=2,column=0,pady=5)

    display_book_button = Button(window, text="Display All Books", justify=CENTER, padx=5, pady=5, font=4,
                                 command=display_book)
    display_book_button.grid(row=3, column=0, pady=10)
    window.mainloop()

# function to check is the student is in the database.
def checking(usn, password):
    try:
        usn = int(usn)
        password = int(password)
        connection = sqlite3.connect('student_database.db')
        c = connection.cursor()
        c.execute("SELECT USN, password FROM student_info")
        record = c.fetchall()
        connection.commit()
        connection.close()

        found = False
        if (usn, password, ) in record:
            found = True

        if found:
            new_window(usn)
        else:
            messagebox.showerror("Information", f"Student with USN {usn} does not exists.")
    except ValueError:
        usn_entry.delete(0, END)
        password_entry.delete(0, END)
        messagebox.showerror("Information", "Enter the correct datatype credentials.")
main_student_login.title("Student Login Window")

frame = Frame(main_student_login ,width=350, height=50, bg='black')
frame.grid(row=0, column=0, columnspan=2)

first_label = Label(main_student_login, text="STUDENT LOGIN",
                    font=("BOLD", 25), fg='white', justify=CENTER, background='black')
first_label.grid(row=0, column=0, columnspan=2)

usn_label = Label(main_student_login, text="USN", font=5)
usn_label.grid(row=1, column=0, padx=10, pady=10)

usn_entry = Entry(main_student_login, width=35)
usn_entry.grid(row=1, column=1, padx=5, pady=10)

password_label = Label(main_student_login, text="Password", font=5)
password_label.grid(row=2, column=0, padx=10, pady=5)

password_entry = Entry(main_student_login, width=35, show="*")
password_entry.grid(row=2 ,column=1, padx=5, pady=5)

submit_button = Button(main_student_login, text="Submit", font=5, padx=5, pady=5, borderwidth=3,
                       command=lambda :checking((usn_entry.get()), (password_entry.get())))
submit_button.grid(row=3, column=0, columnspan=2)
main_student_login.mainloop()