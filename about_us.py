def home_page():
    about_us_window.destroy()
    import os
    os.system("python klg.py")

from tkinter import *
import sys
about_us_window = Tk()
about_us_window.title("ABOUT US")
about_us_window.wm_attributes("-fullscreen", "true")
about_us_window.config(bg="aquamarine")
about_us_window.iconbitmap("lpu_logo.ico")


about_us_window1 = Frame(about_us_window, bg="aquamarine")
about_us_window1.pack(side=LEFT)

about_us_window2 = Frame(about_us_window, bg="aquamarine")
about_us_window2.pack(side=LEFT, pady=50)

about_us_window3 = Frame(about_us_window, bg="aquamarine")
about_us_window3.pack(side=LEFT, pady=50)

image1 = PhotoImage(file="subhadip.gif")
image2 = PhotoImage(file="afroz.gif")
image3 = PhotoImage(file="kushgra.gif")

Label(about_us_window1, image=image1).pack(padx=50, pady=10)
Label(about_us_window1, image=image2).pack(padx=50, pady=10)
Label(about_us_window1, image=image3).pack(padx=50, pady=10)


Label(about_us_window2, text="Name: Subhadip Mondal", font="halston 25 italic", bg="aquamarine", fg="orange").pack(anchor=NW)
Label(about_us_window2, text="Reg. No. 11701711", font="halston 25 italic", bg="aquamarine", fg="orange").pack(anchor=NW)
Label(about_us_window2, text="Roll No. B36", font="halston 25 italic", bg="aquamarine", fg="orange").pack(anchor=NW)

Label(about_us_window2, bg="aquamarine").pack(anchor=NW, pady=30)

Label(about_us_window2, text="Name: Afroz Ahmad Bhat", font="halston 25 italic", bg="aquamarine", fg="orange").pack(anchor=NW)
Label(about_us_window2, text="Reg. No. 11701622", font="halston 25 italic", bg="aquamarine", fg="orange").pack(anchor=NW)
Label(about_us_window2, text="Roll No. B35", font="halston 25 italic", bg="aquamarine", fg="orange").pack(anchor=NW)

Label(about_us_window2, bg="aquamarine").pack(anchor=NW, pady=30)

Label(about_us_window2, text="Name: Kushagra Setia", font="halston 25 italic", bg="aquamarine", fg="orange").pack(anchor=NW)
Label(about_us_window2, text="Reg. No. 11701636", font="halston 25 italic", bg="aquamarine", fg="orange").pack(anchor=NW)
Label(about_us_window2, text="Roll No. B34", font="halston 25 italic", bg="aquamarine", fg="orange").pack(anchor=NW)

python = PhotoImage(file="python.gif")
start = PhotoImage(file="start.gif")

Label(about_us_window3, text="Current Version", font="halston 20 italic", bg="aquamarine", fg="blue").pack(anchor=NW, padx=100, pady=20)
Label(about_us_window3, text=sys.version, bg="aquamarine").pack(anchor=NW, padx=100)
Label(about_us_window3, image=python).pack(anchor=NW, padx=100, pady=20)
Label(about_us_window3, text="Click on the START button to continue...", font="halston 25 italic", bg="aquamarine", fg="maroon").pack(anchor=NW)
Button(about_us_window3, image=start, command=home_page).pack(anchor=NW, padx=200, pady=30)

about_us_window.mainloop()