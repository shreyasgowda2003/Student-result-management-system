from tkinter import *
from tkinter import messagebox, ttk
import sqlite3 
import os

class studentSystem:
    def __init__(self, home):
        self.home = home
        self.home.title("Student Page")
        self.home.geometry("1600x800+0+0")
        self.home.config(bg="white")

        # Title of Student Page
        title = Label(self.home, text="Student Result", font=("times new roman", 20, "bold"), bg="purple", fg="white")
        title.pack(fill=X)

        # Create a main frame
        main_frame = Frame(self.home)
        main_frame.pack(fill=BOTH, expand=1)

        # Create a canvas
        canvas = Canvas(main_frame, bg="white")
        canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add a vertical scrollbar to the canvas
        scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Configure the canvas and link it with the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Create an inner frame inside the canvas
        inner_frame = Frame(canvas, bg="white")
        canvas.create_window((0, 0), window=inner_frame, anchor=NW)

        # Your existing code for UI elements goes here

        # Searching Button
        self.var_search = StringVar()
        lbl_rollno = Label(inner_frame, text="Enter Roll No. ", font=("times new roman", 30, "bold"), bg="white", pady=20)
        lbl_rollno.grid(row=0, column=0, padx=10, pady=25)
        txt_rollno1 = Entry(inner_frame, textvariable=self.var_search, font=("times new roman", 15, "bold"), bg="lightyellow")
        txt_rollno1.grid(row=0, column=1, padx=10, pady=25)
        btn_search = Button(inner_frame, text="Search", font=("times new roman", 15, "bold"), bg="blue", fg="white", cursor="hand2", command=self.search)
        btn_search.grid(row=0, column=2, padx=10, pady=25)
        btn_clear = Button(inner_frame, text="Clear", font=("times new roman", 15, "bold"), bg="orange", fg="white", cursor="hand2", command=self.clear)
        btn_clear.grid(row=0, column=3, padx=10, pady=25)

        button_Logout = Button(inner_frame, text="Logout", font=("times new roman", 15, "bold"), bg="red", fg="white", cursor="hand2", command=self.logout)
        button_Logout.grid(row=0, column=4, padx=10, pady=25)

        # Result Of Student and content to show
        lbl_roll = Label(inner_frame, text="Roll No.", font=("times new roman", 18, "bold"), bg="white", bd=2, pady=25)
        lbl_roll.grid(row=1, column=0, padx=10, pady=25, sticky=W)
        lbl_name = Label(inner_frame, text="Name", font=("times new roman", 18, "bold"), bg="white", bd=2, pady=25)
        lbl_name.grid(row=2, column=0, padx=10, pady=25, sticky=W)
        lbl_course = Label(inner_frame, text="Course", font=("times new roman", 18, "bold"), bg="white", bd=2, pady=25)
        lbl_course.grid(row=3, column=0, padx=10, pady=25, sticky=W)
        lbl_marks = Label(inner_frame, text="Marks Obtained", font=("times new roman", 18, "bold"), bg="white", bd=2, pady=25)
        lbl_marks.grid(row=4, column=0, padx=10, pady=25, sticky=W)
        lbl_full = Label(inner_frame, text="Total Marks", font=("times new roman", 18, "bold"), bg="white", bd=2, pady=25)
        lbl_full.grid(row=5, column=0, padx=10, pady=25, sticky=W)
        lbl_percentage = Label(inner_frame, text="Percentage", font=("times new roman", 18, "bold"), bg="white", bd=2, pady=25)
        lbl_percentage.grid(row=6, column=0, padx=10, pady=25, sticky=W)

        self.roll = Label(inner_frame, font=("times new roman", 18, "bold"), bg="white", bd=2)
        self.roll.grid(row=1, column=1, padx=10, pady=25,sticky=W)
        self.name = Label(inner_frame, font=("times new roman", 18, "bold"), bg="white", bd=2)
        self.name.grid(row=2, column=1, padx=10, pady=25,sticky=W)
        self.course = Label(inner_frame, font=("times new roman", 18, "bold"), bg="white", bd=2)
        self.course.grid(row=3, column=1, padx=10, pady=25,sticky=W)
        self.marks = Label(inner_frame, font=("times new roman", 18, "bold"), bg="white", bd=2)
        self.marks.grid(row=4, column=1, padx=10, pady=25,sticky=W)
        self.full = Label(inner_frame, font=("times new roman", 18, "bold"), bg="white", bd=2)
        self.full.grid(row=5, column=1, padx=10, pady=25,sticky=W)
        self.percentage = Label(inner_frame, font=("times new roman", 18, "bold"), bg="white", bd=2)
        self.percentage.grid(row=6, column=1, padx=10, pady=25,sticky=W)

        # Add a scrollbar to the canvas
        canvas.config(scrollregion=canvas.bbox("all"))

        # Functionality to scroll with touchpad
        canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    # Functions
    def search(self):
        conn=sqlite3.connect(database="ResultManagementSystem.db")
        cur=conn.cursor()     
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Roll No. should be required",parent=self.home)
            else:
                cur.execute("Select * from result where roll=?",(self.var_search.get(),))
                row=cur.fetchone()
                if row !=None:
                    self.var_id=row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks.config(text=row[4])
                    self.full.config(text=row[5])
                    self.percentage.config(text=row[6])
                else:
                    messagebox.showerror("Error","No record Found",parent=self.home) 
               
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def clear(self):
        self.var_id=""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.full.config(text="")
        self.percentage.config(text="")
        self.var_search.set("")
    
    def logout(self):
        op=messagebox.askyesno("Confirm Again","Do You really Want to Logout ?",parent=self.home)
        if op==True:
            self.home.destroy()
            os.system("Python Login.py")

if __name__=="__main__":
    home=Tk()
    obj=studentSystem(home)
    home.mainloop()
