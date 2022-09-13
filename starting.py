from tkinter import *
main_window = Tk()
main_window.geometry("300x250")
main_window.title("Admin or Student")

def login_as_admin():
    main_window.destroy()
    import main

def login_as_student():
    main_window.destroy()
    import main_student

frame = Frame(main_window ,width=300, height=50, bg='black')
frame.grid(row=0, column=0, columnspan=2)

text_label = Label(main_window, text="Select Admin or Student", font="bold", fg='white', bg='black', justify=CENTER)
text_label.grid(row=0, columnspan=2, column=0)

admin_button = Button(main_window, text="Login As Admin", font=("Arial", 12), padx=3, pady=3, command=login_as_admin)
admin_button.grid(row=1, column=0, pady=15, padx=85)

student_button = Button(main_window, text="Login As Student", font=("Arial",12), padx=3, pady=3,command=login_as_student)
student_button.grid(row=2, column=0, pady=15, padx=75)
main_window.mainloop()