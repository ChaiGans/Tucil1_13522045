from tkinter import *

window = Tk()

width = 800
height = 600

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

center_x_position = int((screen_width/2) - (width/2))
center_y_position = int((screen_height/2) - (height/2))

window.geometry(f"{width}x{height}+{center_x_position}+{center_y_position}")
window.title("CYBERPUNK77 BREACH GUI")
window.configure(bg="#121212")
border_color = Frame(window, background="#D0ED57")

# Creating widgets
heading_1 = Label(window, text="Cyberpunk 2077 Hacking Minigame Solver", font=("Rajdhani", 24), fg="#D0ED57", bg="#121212")
heading_2 = Label(window, text="INSTANT BREACH PROTOCOL SOLVER - START CRACKING SAMURAI", font=("Rajdhani", 12), fg="#D0ED57", bg="#121212")
buffer_label = Label(window, text="SPECIFY BUFFER SIZE", bg="#121212", fg="#D0ED57")
buffer_size = Entry(window)
enter_code_matrix_label = Label(window, text="ENTER CODE MATRIX", bg="#121212", fg="#D0ED57")
matrix = Entry(window)
enter_sequences_label = Label(window, text="ENTER SEQUENCES", bg="#121212", fg="#D0ED57")
enter_sequences = Entry(window)
solve_button = Button(window, text="SOLVE")

# Placing widgets on the screen
heading_1.grid(row=0, column=0, sticky=W)
heading_2.grid(row=1, column=0, sticky=W)
buffer_label.grid(row=2, column=0, sticky=W)
buffer_size.grid(row=3, column=0, sticky=EW)
enter_code_matrix_label.grid(row=4, column=0, sticky=W)
matrix.grid(row=5, column=0, sticky=EW)
enter_sequences_label.grid(row=6, column=0, sticky=W)
enter_sequences.grid(row=7, column=0, sticky=EW)
solve_button.grid(row=8, column=0, sticky=W)

window.mainloop()