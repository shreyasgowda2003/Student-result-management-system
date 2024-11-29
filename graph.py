import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from data import s_data, i_data, gen_data, adm_data

class GraphClass:
    def __init__(self, home):
        self.home = home
        self.home.title("Dashboard")
        self.home.state('zoomed')
        self.home.config(bg="white")
        
        side_frame = tk.Frame(self.home, bg="#69C5FF")
        side_frame.pack(side="left", fill="y")

        label = tk.Label(side_frame, text="Dashboard", bg="#4C2A85", fg="#FFF", font=("Arial", 25))
        label.pack(pady=25, padx=20)

        charts_frame = tk.Frame(self.home)
        charts_frame.pack()

        upper_frame = tk.Frame(charts_frame)
        upper_frame.pack(fill="both", expand=True)

        # Define rainbow colors
        rainbow_colors = ['#FF0000', '#FF7F00', '#FFFF00', '#00FF00', '#0000FF', '#4B0082', '#8B00FF']

        # Plot first bar chart with rainbow colors
        fig1, ax1 = plt.subplots()
        ax1.bar(s_data.keys(), s_data.values(), color=rainbow_colors)
        ax1.set_title("Students Took Course from Different States")
        ax1.set_xlabel("States")
        ax1.set_ylabel("No of Students")
        canvas1 = FigureCanvasTkAgg(fig1, upper_frame)
        canvas1.draw()
        canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)

        # Plot second bar chart with rainbow colors
        fig2, ax2 = plt.subplots()
        ax2.barh(list(i_data.keys()), i_data.values(), color=rainbow_colors)
        ax2.set_title("Course choosed by Student")
        ax2.set_xlabel("No of Students")
        ax2.set_ylabel("Courses")
        canvas2 = FigureCanvasTkAgg(fig2, upper_frame)
        canvas2.draw()
        canvas2.get_tk_widget().pack(side="left", fill="both", expand=True)

        lower_frame = tk.Frame(charts_frame)
        lower_frame.pack(fill="both", expand=True)

        # Plot pie chart with rainbow colors
        fig3, ax3 = plt.subplots()
        ax3.pie(gen_data.values(), labels=gen_data.keys(), autopct='%1.1f%%', colors=rainbow_colors)
        ax3.set_title("Student Gender")
        canvas3 = FigureCanvasTkAgg(fig3, lower_frame)
        canvas3.draw()
        canvas3.get_tk_widget().pack(side="left", fill="both", expand=True)

        # Plot line chart with rainbow colors
        fig4, ax4 = plt.subplots()
        ax4.plot(list(adm_data.keys()), list(adm_data.values()), color=rainbow_colors[0])  # Using the first color
        ax4.set_title("Admission of Student")
        ax4.set_xlabel("Year")
        ax4.set_ylabel("Course")
        canvas4 = FigureCanvasTkAgg(fig4, lower_frame)
        canvas4.draw()
        canvas4.get_tk_widget().pack(side="left", fill="both", expand=True)

if __name__ == "__main__":
    home = tk.Tk()
    obj = GraphClass(home)
    home.mainloop()
