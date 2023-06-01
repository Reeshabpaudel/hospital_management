import tkinter
from tkinter import messagebox
class Login:
    def __init__(self):
        self.login_win=tkinter.Tk()
        self.login_win.title("Login")
        self.login_win.geometry("700x500")
        self.login_win.maxsize(700,500)
        self.login_win.config(bg="#EEF8FF")

        self.container1=tkinter.Frame(self.login_win, bg="#EEF8FF", pady=30)
        self.container2=tkinter.Frame(self.login_win, bg="#EEF8FF")
        self.container3=tkinter.Frame(self.login_win, bg="#EEF8FF", padx=10)

        self.heading=tkinter.Label(self.login_win, text="LOGIN", bg="#EEF8FF", font=("Inter",30), pady=50)

        self.name=tkinter.Label(self.container1, text="Username:",bg='#EEF8FF', font=("Inter", 24))
        self.u_name=tkinter.Entry(self.container1, font=("Inter",18), width=20)
        self.u_name.config(bg="#E9E9E9")
        self.u_name.insert(0, "enter your name")
        self.u_name.bind('<FocusIn>',lambda event: self.u_name.delete(0, "end") if self.u_name.get()=='enter your name' else None)
        self.u_name.bind('<FocusOut>', lambda event: self.u_name.insert(0, "enter your name") if self.u_name.get()=="" else None)


        # self.password=tkinter.Label(self.login_win, text="Password:", bg="lightblue" font=("Inter", 24))
        self.password=tkinter.Label(self.container2, text="Password:", bg="#EEF8FF", font=("Inter",24))
        self.t_pass=tkinter.Entry(self.container2, font=("Inter",18), width=20)
        self.t_pass.config(bg="#E9E9E9")
        self.t_pass.insert(0,"enter your password")
        self.t_pass.bind("<FocusIn>", lambda event: self.t_pass.delete(0, "end") if self.t_pass.get()=="enter your password" else None )
        self.t_pass.bind("<FocusOut>", lambda event: self.t_pass.insert(0, "enter your password") if self.t_pass.get()=="" else None)

        self.sign_up=tkinter.Button(self.container3, text="Sign Up", command=self.create_new_user, height=1, width=10, padx=4, font=("Inter", 14))
        self.login=tkinter.Button(self.container3, text="LogIn", command=self.validate_user, height=1, width=10, padx=4, font=("Inter", 14))
    
        self.heading.pack(side="top")
        self.container1.pack()
        self.container2.pack()
        self.container3.pack(side="right")

        self.name.pack(side="left")
        self.u_name.pack(side="left")
        self.password.pack(side="left")
        self.t_pass.pack(side='left')

        self.sign_up.grid(row=0, column=0)
        self.login.grid(row=0, column=1)

        self.login_win.mainloop()

    def validate_user(self):
        print("helo")
        username=self.u_name.get()
        password=self.t_pass.get()
        with open("admin_file.txt","r") as file:
            data=file.read().split()
            if username in data:
                if data[data.index(username)+1]==password:
                    self.admin_window()
                else:
                    messagebox.showerror("Error","Password Error!")
            else:
                messagebox.showerror("Error","Username not found!")
            file.close()

    def create_new_user(self):
        pass

    def admin_window(self):
        self.admin_win=tkinter.Tk()
        self.admin_win.title("admin")
        tkinter.mainloop()

lg=Login()