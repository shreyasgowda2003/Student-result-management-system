from tkinter import *
from PIL import Image, ImageTk  
from tkinter import ttk, messagebox
import sqlite3

class ViewClass:
    def __init__(self, home):
        self.home = home
        self.home.title("Student Result Management System")
        self.home.geometry("1520x780+0+0")
        self.home.config(bg="white")
        self.home.focus_force()

        # Title label
        title_label = Label(self.home, text="View Student Results", font=("times new roman", 20, "bold"), bg="purple", fg="white")
        title_label.pack(fill=X)  # Pack the title label to fill the horizontal space

        # Create a main frame
        main_frame = Frame(self.home)
        main_frame.pack(fill=BOTH, expand=1)

        # Create a canvas
        self.canvas = Canvas(main_frame, bg="white")
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.canvas.bind("<MouseWheel>", self.on_mouse_wheel)
        self.canvas.bind("<Button-4>", self.on_mouse_wheel)  # Touchpad scroll up
        self.canvas.bind("<Button-5>", self.on_mouse_wheel)  # Touchpad scroll down

        # Add a vertical scrollbar to the canvas
        scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=self.canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Configure the canvas and link it with the scrollbar
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Create an inner frame inside the canvas
        inner_frame = Frame(self.canvas, bg="white")
        self.canvas.create_window((0, 0), window=inner_frame, anchor=NW)

        # Your existing code for UI elements goes here
        self.var_search = StringVar()
        self.var_id = ""

        lbl_select = Label(inner_frame, text="Select By Roll No.", font=("times new roman", 20, "bold"), bg="white")
        lbl_select.grid(row=0, column=0, padx=10, pady=20)  # Adjusted pady for line spacing

        txt_select = Entry(inner_frame, textvariable=self.var_search, font=("times new roman", 20), bg="lightyellow")
        txt_select.grid(row=0, column=1, padx=10, pady=20, ipadx=10)  # Adjusted pady and ipadx for alignment

        btn_search = Button(inner_frame, text="Search", font=("times new roman", 15, "bold"), bg="lightblue",
                            fg="black", cursor="hand2", command=self.search)
        btn_search.grid(row=0, column=2, padx=10, pady=20, ipadx=10)  # Adjusted pady and ipadx for alignment

        btn_clear = Button(inner_frame, text="Clear", font=("times new roman", 15, "bold"), bg="lightgreen",
                           fg="black", cursor="hand2", command=self.clear)
        btn_clear.grid(row=0, column=3, padx=10, pady=20, ipadx=10)  # Adjusted pady and ipadx for alignment

        # Define vertical spacing between widgets
        vertical_spacing = 40  # Adjusted vertical spacing for better alignment

        lbl_roll = Label(inner_frame, text="Roll No:", font=("times new roman", 18, "bold"), bg="white", bd=2)
        lbl_roll.grid(row=1, column=0, padx=10, pady=vertical_spacing, sticky=W)

        lbl_name = Label(inner_frame, text="Name:", font=("times new roman", 18, "bold"), bg="white", bd=2)
        lbl_name.grid(row=2, column=0, padx=10, pady=vertical_spacing, sticky=W)

        lbl_course = Label(inner_frame, text="Course:", font=("times new roman", 18, "bold"), bg="white", bd=2)
        lbl_course.grid(row=3, column=0, padx=10, pady=vertical_spacing, sticky=W)

        lbl_marks = Label(inner_frame, text="Marks Obtained:", font=("times new roman", 18, "bold"), bg="white", bd=2)
        lbl_marks.grid(row=4, column=0, padx=10, pady=vertical_spacing, sticky=W)

        lbl_full = Label(inner_frame, text="Total Marks:", font=("times new roman", 18, "bold"), bg="white", bd=2)
        lbl_full.grid(row=5, column=0, padx=10, pady=vertical_spacing, sticky=W)

        lbl_percentage = Label(inner_frame, text="Percentage:", font=("times new roman", 18, "bold"), bg="white", bd=2)
        lbl_percentage.grid(row=6, column=0, padx=10, pady=vertical_spacing, sticky=W)

        self.roll = Label(inner_frame, font=("times new roman", 18, "bold"), bg="white", bd=2)
        self.roll.grid(row=1, column=1, padx=10, pady=vertical_spacing, sticky=W)

        self.name = Label(inner_frame, font=("times new roman", 18, "bold"), bg="white", bd=2)
        self.name.grid(row=2, column=1, padx=10, pady=vertical_spacing, sticky=W)

        self.course = Label(inner_frame, font=("times new roman", 18, "bold"), bg="white", bd=2)
        self.course.grid(row=3, column=1, padx=10, pady=vertical_spacing, sticky=W)

        self.marks = Label(inner_frame, font=("times new roman", 18, "bold"), bg="white", bd=2)
        self.marks.grid(row=4, column=1, padx=10, pady=vertical_spacing, sticky=W)

        self.full = Label(inner_frame, font=("times new roman", 18, "bold"), bg="white", bd=2)
        self.full.grid(row=5, column=1, padx=10, pady=vertical_spacing, sticky=W)

        self.percentage = Label(inner_frame, font=("times new roman", 18, "bold"), bg="white", bd=2)
        self.percentage.grid(row=6, column=1, padx=10, pady=vertical_spacing, sticky=W)

        btn_delete = Button(inner_frame, text="Delete", font=("times new roman", 15, "bold"), bg="red", fg="white",
                            cursor="hand2", command=self.delete)
        btn_delete.grid(row=7, column=0, columnspan=2, padx=10, pady=20, sticky=W+E)  # Adjusted pady for line spacing

        inner_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def search(self):
        conn = sqlite3.connect(database="ResultManagementSystem.db")
        cur = conn.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Roll No. should be required", parent=self.home)
            else:
                cur.execute("Select * from result where roll=?", (self.var_search.get(),))
                row = cur.fetchone()
                if row != None:
                    self.var_id = row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks.config(text=row[4])
                    self.full.config(text=row[5])
                    self.percentage.config(text=row[6])
                else:
                    messagebox.showerror("Error", "No record Found", parent=self.home)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def clear(self):
        self.var_id = ""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.full.config(text="")
        self.percentage.config(text="")
        self.var_search.set("")

    def delete(self):
        conn = sqlite3.connect(database="ResultManagementSystem.db")
        cur = conn.cursor()
        try:
            if self.var_id == "":
                messagebox.showerror("Error", "search Student Result First", parent=self.home)
            else:
                cur.execute("Select * from result where rid=?", (self.var_id,))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Student Result", parent=self.home)
                else:
                    p = messagebox.askyesno("Confirm", "Do you really want to delete", parent=self.home)
                    if p == True:
                        cur.execute("Delete from result where rid=? ", (self.var_id,))
                        conn.commit()
                        messagebox.showinfo("Delete", "Result deleted Successfully", parent=self.home)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def on_mouse_wheel(self, event):
        if event.num == 5 or event.delta == -120:
            self.canvas.yview_scroll(1, "units")
        if event.num == 4 or event.delta == 120:
            self.canvas.yview_scroll(-1, "units")


if __name__ == "__main__":
    home = Tk()
    obj = ViewClass(home)
    home.mainloop()
