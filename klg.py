def birds():
    window.destroy()

    def home():
        window1.destroy()
        import os
        os.system("python about_us.py")

    def okProcess():
        frame1.destroy()

        frame2 = Frame(window1, bg="skyblue", cursor="cross")
        frame2.pack(fill=BOTH, expand=YES)

        frame3 = Frame(window1, bg="#46f0f0", cursor="plus")
        frame3.pack(fill=BOTH)

        from tkinter import messagebox

        def printing():
            messagebox.showinfo("Number of Birds", str(counting()) + " Birds are correctly recognize" + "\n\n" + str(incorrect_counting()) + " Birds are selectled wrongly")
            L = Label(frame2, bg="skyblue", fg="black", font="gabriola 30 italic underline")
            L.grid(row=5, column=2, columnspan=15)

            if counting() > incorrect_counting():
                L.config(text="Percentage of Accuracy is " + str("%.2f" % (((counting() - incorrect_counting()) * 100) / 12)) + "%")
            else:
                L.config(text="Percentage of Accuracy is 0.00%")

            Label(frame3, image=smile).grid(row=1, column=1, padx=100, pady=50)
            Label(frame3, text="Thank You !!!", bg="#46f0f0", fg="blue", font="chaurcer 25 italic").grid(row=1, column=2, sticky=N, pady=180)
            Label(frame3, text="Press EXIT to end Playing...", bg="#46f0f0", fg="blue", font="garamond 30 italic").grid(row=2, column=1, sticky=W, padx=10, pady=10)
            Button(frame3, text="EXIT", bg="darksalmon", fg="yellow", bd=3, cursor="arrow", command=exit).grid(row=2, column=2, sticky=W, padx=10, pady=10, ipadx=30)

        def counting():
            count = v1.get() + v2.get() + v3.get() + v4.get() + v5.get() + v6.get() + v7.get() + v8.get() + v9.get() + v10.get() + v11.get() + v12.get()
            return count

        def incorrect_counting():
            incorrect_count = v13.get() + v14.get() + v15.get() + v16.get() + v17.get() + v18.get() + v19.get() + v20.get()
            return incorrect_count

        v1 = IntVar()
        v2 = IntVar()
        v3 = IntVar()
        v4 = IntVar()
        v5 = IntVar()
        v6 = IntVar()
        v7 = IntVar()
        v8 = IntVar()
        v9 = IntVar()
        v10 = IntVar()
        v11 = IntVar()
        v12 = IntVar()
        v13 = IntVar()
        v14 = IntVar()
        v15 = IntVar()
        v16 = IntVar()
        v17 = IntVar()
        v18 = IntVar()
        v19 = IntVar()
        v20 = IntVar()

        Label(frame2, text="Select maximum 12 Birds name", bg="skyblue", fg="black", font="garamond 20 italic").grid(row=0, column=0, sticky=W, padx=100)
        Label(frame2, text="that appeared previously...", bg="skyblue", fg="black", font="garamond 20 italic").grid(row=1, column=0, sticky=W, padx=100)
        Button(frame2, text="HOME", bg="darksalmon", fg="yellow", bd=3, cursor="arrow", command=home).grid(row=1,
                                                                                                                 column=6,
                                                                                                                 padx=200,
                                                                                                                 pady=10,
                                                                                                                 ipadx=20)

        Checkbutton(frame2, text="Crane", fg="red", bg="skyblue", variable=v1, onvalue=1, offvalue=0, command=counting).grid(row=4, column=5, padx=10, pady=10)
        Checkbutton(frame2, text="Cuckoo", fg="red", bg="skyblue", variable=v2, onvalue=1, offvalue=0, command=counting).grid(row=1, column=2, padx=10, pady=10)
        Checkbutton(frame2, text="Dove", fg="red", bg="skyblue", variable=v3, onvalue=1, offvalue=0, command=counting).grid(row=4, column=2, padx=10, pady=10)
        Checkbutton(frame2, text="Eagle", fg="red", bg="skyblue", variable=v4, onvalue=1, offvalue=0, command=counting).grid(row=1, column=4, padx=10, pady=10)
        Checkbutton(frame2, text="Kingfisher", fg="red", bg="skyblue", variable=v5, onvalue=1, offvalue=0, command=counting).grid(row=1, column=5, padx=10, pady=10)
        Checkbutton(frame2, text="Mynah", fg="red", bg="skyblue", variable=v6, onvalue=1, offvalue=0, command=counting).grid(row=2, column=1, padx=10, pady=10)
        Checkbutton(frame2, text="Nightingale", fg="red", bg="skyblue", variable=v7, onvalue=1, offvalue=0, command=counting).grid(row=3, column=5, padx=10, pady=10)
        Checkbutton(frame2, text="Owl", fg="red", bg="skyblue", variable=v8, onvalue=1, offvalue=0, command=counting).grid(row=2, column=3, padx=10, pady=10)
        Checkbutton(frame2, text="Parrot", fg="red", bg="skyblue", variable=v9, onvalue=1, offvalue=0, command=counting).grid(row=2, column=4, padx=10, pady=10)
        Checkbutton(frame2, text="Peacock", fg="red", bg="skyblue", variable=v10, onvalue=1, offvalue=0, command=counting).grid(row=3, column=3, padx=10, pady=10)
        Checkbutton(frame2, text="Quil", fg="red", bg="skyblue", variable=v11, onvalue=1, offvalue=0, command=counting).grid(row=3, column=2, padx=10, pady=10)
        Checkbutton(frame2, text="Sparrow", fg="red", bg="skyblue", variable=v12, onvalue=1, offvalue=0, command=counting).grid(row=3, column=1, padx=10, pady=10)
        Checkbutton(frame2, text="Penguin", fg="red", bg="skyblue", variable=v13, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=2, column=5, padx=10, pady=10)
        Checkbutton(frame2, text="Swallow", fg="red", bg="skyblue", variable=v14, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=3, column=4, padx=10, pady=10)
        Checkbutton(frame2, text="Albatross", fg="red", bg="skyblue", variable=v15, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=2, column=2, padx=10, pady=10)
        Checkbutton(frame2, text="Ibis", fg="red", bg="skyblue", variable=v16, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=4, column=1, padx=10, pady=10)
        Checkbutton(frame2, text="Tocan", fg="red", bg="skyblue", variable=v17, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=1, column=3, padx=10, pady=10)
        Checkbutton(frame2, text="Finches", fg="red", bg="skyblue", variable=v18, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=4, column=3, padx=10, pady=10)
        Checkbutton(frame2, text="Heron", fg="red", bg="skyblue", variable=v19, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=4, column=4, padx=10, pady=10)
        Checkbutton(frame2, text="Pelicans", fg="red", bg="skyblue", variable=v20, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=1, column=1, padx=10, pady=10)

        Button(frame2, text="SUBMIT", bg="darksalmon", fg="yellow", bd=3, cursor="arrow", command=printing).grid(row=5, column=1, padx=10, pady=10, ipadx=20)

    window1 = Tk()
    window1.title("BIRDS")
    window1.iconbitmap("lpu_logo.ico")
    window1.wm_attributes('-fullscreen', 'true')

    smile = PhotoImage(file="smile.gif")
    good_luck = PhotoImage(file="good_luck.gif")

    image1 = PhotoImage(file="crane.gif")
    image2 = PhotoImage(file="cuckoo.gif")
    image3 = PhotoImage(file="dove.gif")
    image4 = PhotoImage(file="eagle.gif")
    image5 = PhotoImage(file="kingfisher.gif")
    image6 = PhotoImage(file="mynah.gif")
    image7 = PhotoImage(file="nightingale.gif")
    image8 = PhotoImage(file="owl.gif")
    image9 = PhotoImage(file="parrot.gif")
    image10 = PhotoImage(file="peacock.gif")
    image11 = PhotoImage(file="quail.gif")
    image12 = PhotoImage(file="sparrow.gif")

    frame1 = Frame(window1, bg="darkseagreen1", cursor="circle")
    frame1.pack(fill=BOTH)

    Label(frame1, image=image1).grid(row=1, column=1, padx=10, pady=10)
    Label(frame1, image=image2).grid(row=1, column=2, padx=10, pady=10)
    Label(frame1, image=image3).grid(row=1, column=3, padx=10, pady=10)
    Label(frame1, image=image4).grid(row=1, column=4, padx=10, pady=10)
    Label(frame1, image=image5).grid(row=1, column=5, padx=10, pady=10)
    Label(frame1, image=image6).grid(row=1, column=6, padx=10, pady=10)
    Label(frame1, image=image7).grid(row=2, column=1, padx=10, pady=10)
    Label(frame1, image=image8).grid(row=2, column=2, padx=10, pady=10)
    Label(frame1, image=image9).grid(row=2, column=3, padx=10, pady=10)
    Label(frame1, image=image10).grid(row=2, column=4, padx=10, pady=10)
    Label(frame1, image=image11).grid(row=2, column=5, padx=10, pady=10)
    Label(frame1, image=image12).grid(row=2, column=6, padx=10, pady=10)

    Label(frame1, text="Press EXIT to end Playing...", bg="darkseagreen1", fg="blue", font="garamond 15 italic").grid(row=3, column=1, sticky=W, padx=10, pady=10)
    Button(frame1, text="EXIT", bg="darksalmon", fg="yellow", bd=3, cursor="arrow", command=exit).grid(row=3, column=2, sticky=W, padx=10, pady=10,ipadx=30)
    Label(frame1, text="Press OK to continue Playing...", bg="darkseagreen1", fg="blue", font="garamond 15 italic").grid(row=3, column=3, sticky=W, padx=10, pady=10)
    Button(frame1, text="OK", bg="darksalmon", fg="yellow", bd=3, cursor="arrow", command=okProcess).grid(row=3, column=4, sticky=W, padx=10, pady=10, ipadx=30)
    Label(frame1, text="Note: Remember the images...", bg="darkseagreen1", fg="blue",
          font="garamond 15 italic").grid(row=3, column=5, sticky=W, padx=10, pady=10)

    Label(frame1, image=good_luck).grid(row=4, column=1, columnspan=6, pady=40)

    window1.mainloop()

def flowers():
    window.destroy()

    def home():
        window1.destroy()
        import os
        os.system("python about_us.py")

    def okProcess():
        frame1.destroy()

        frame2 = Frame(window1, bg="skyblue", cursor="cross")
        frame2.pack(fill=BOTH, expand=YES)

        frame3 = Frame(window1, bg="#46f0f0", cursor="plus")
        frame3.pack(fill=BOTH)

        from tkinter import messagebox

        def printing():
            messagebox.showinfo("Number of Flowers", str(counting()) + " Flowers are correctly recognize" + "\n" + str(incorrect_counting()) + " Flowers are selectled wrongly")
            L = Label(frame2, bg="skyblue", fg="black", font="gabriola 30 italic underline")
            L.grid(row=5, column=2, columnspan=15)
            if counting() > incorrect_counting():
                L.config(text="Percentage of Accuracy is " + str("%.2f" % (((counting() - incorrect_counting()) * 100) / 12)) + "%")
            else:
                L.config(text="Percentage of Accuracy is 0.00%")

            Label(frame3, image=smile).grid(row=1, column=1, padx=100, pady=50)
            Label(frame3, text="Thank You !!!", bg="#46f0f0", fg="blue", font="chaurcer 25 italic").grid(row=1,
                                                                                                         column=2,
                                                                                                         sticky=N,
                                                                                                         pady=180)
            Label(frame3, text="Press EXIT to end Playing...", bg="#46f0f0", fg="blue", font="garamond 30 italic").grid(
                row=2, column=1, sticky=W, padx=10, pady=10)
            Button(frame3, text="EXIT", bg="darksalmon", fg="yellow", bd=3, cursor="arrow", command=exit).grid(row=2,
                                                                                                               column=2,
                                                                                                               sticky=W,
                                                                                                               padx=10,
                                                                                                               pady=10,
                                                                                                               ipadx=30)

        def counting():
            count = v1.get() + v2.get() + v3.get() + v4.get() + v5.get() + v6.get() + v7.get() + v8.get() + v9.get() + v10.get() + v11.get() + v12.get()
            return count

        def incorrect_counting():
            incorrect_count = v13.get() + v14.get() + v15.get() + v16.get() + v17.get() + v18.get() + v19.get() + v20.get()
            return incorrect_count

        v1 = IntVar()
        v2 = IntVar()
        v3 = IntVar()
        v4 = IntVar()
        v5 = IntVar()
        v6 = IntVar()
        v7 = IntVar()
        v8 = IntVar()
        v9 = IntVar()
        v10 = IntVar()
        v11 = IntVar()
        v12 = IntVar()
        v13 = IntVar()
        v14 = IntVar()
        v15 = IntVar()
        v16 = IntVar()
        v17 = IntVar()
        v18 = IntVar()
        v19 = IntVar()
        v20 = IntVar()

        Label(frame2, text="Select maximum 12 Flowers name", bg="skyblue", fg="black", font="garamond 20 italic").grid(row=0,
                                                                                                              column=0,
                                                                                                              sticky=W, padx=100)
        Label(frame2, text="that appeared previously...", bg="skyblue", fg="black", font="garamond 20 italic").grid(
            row=1, column=0, sticky=W, padx=100)
        Button(frame2, text="HOME", bg="darksalmon", fg="yellow", bd=3, cursor="arrow", command=home).grid(row=1,
                                                                                                           column=6,
                                                                                                           padx=100,
                                                                                                           pady=10,
                                                                                                           ipadx=20)

        Checkbutton(frame2, text="Ageratum", fg="red", bg="skyblue", variable=v1, onvalue=1, offvalue=0,
                    command=counting).grid(row=4, column=5, padx=10, pady=10)
        Checkbutton(frame2, text="Allium", fg="red", bg="skyblue", variable=v2, onvalue=1, offvalue=0,
                    command=counting).grid(row=1, column=2, padx=10, pady=10)
        Checkbutton(frame2, text="Alstromeria", fg="red", bg="skyblue", variable=v3, onvalue=1, offvalue=0,
                    command=counting).grid(row=4, column=2, padx=10, pady=10)
        Checkbutton(frame2, text="Alyssum", fg="red", bg="skyblue", variable=v4, onvalue=1, offvalue=0,
                    command=counting).grid(row=1, column=4, padx=10, pady=10)
        Checkbutton(frame2, text="Amarylis", fg="red", bg="skyblue", variable=v5, onvalue=1, offvalue=0,
                    command=counting).grid(row=1, column=5, padx=10, pady=10)
        Checkbutton(frame2, text="Anemone", fg="red", bg="skyblue", variable=v6, onvalue=1, offvalue=0,
                    command=counting).grid(row=2, column=1, padx=10, pady=10)
        Checkbutton(frame2, text="Angelica", fg="red", bg="skyblue", variable=v7, onvalue=1, offvalue=0,
                    command=counting).grid(row=3, column=5, padx=10, pady=10)
        Checkbutton(frame2, text="Balloon flower", fg="red", bg="skyblue", variable=v8, onvalue=1, offvalue=0,
                    command=counting).grid(row=2, column=3, padx=10, pady=10)
        Checkbutton(frame2, text="Baneberry", fg="red", bg="skyblue", variable=v9, onvalue=1, offvalue=0,
                    command=counting).grid(row=2, column=4, padx=10, pady=10)
        Checkbutton(frame2, text="Basket of gold", fg="red", bg="skyblue", variable=v10, onvalue=1, offvalue=0,
                    command=counting).grid(row=3, column=3, padx=10, pady=10)
        Checkbutton(frame2, text="Bloodroot", fg="red", bg="skyblue", variable=v11, onvalue=1, offvalue=0,
                    command=counting).grid(row=3, column=2, padx=10, pady=10)
        Checkbutton(frame2, text="Rose", fg="red", bg="skyblue", variable=v12, onvalue=1, offvalue=0,
                    command=counting).grid(row=3, column=1, padx=10, pady=10)
        Checkbutton(frame2, text="Lily", fg="red", bg="skyblue", variable=v13, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=2, column=5, padx=10, pady=10)
        Checkbutton(frame2, text="Baby's breath", fg="red", bg="skyblue", variable=v14, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=3, column=4, padx=10, pady=10)
        Checkbutton(frame2, text="Crocus", fg="red", bg="skyblue", variable=v15, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=2, column=2, padx=10, pady=10)
        Checkbutton(frame2, text="Orchid", fg="red", bg="skyblue", variable=v16, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=4, column=1, padx=10, pady=10)
        Checkbutton(frame2, text="Lotus", fg="red", bg="skyblue", variable=v17, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=1, column=3, padx=10, pady=10)
        Checkbutton(frame2, text="Daffodil", fg="red", bg="skyblue", variable=v18, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=4, column=3, padx=10, pady=10)
        Checkbutton(frame2, text="Dahlia", fg="red", bg="skyblue", variable=v19, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=4, column=4, padx=10, pady=10)
        Checkbutton(frame2, text="Larkspur", fg="red", bg="skyblue", variable=v20, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=1, column=1, padx=10, pady=10)

        Button(frame2, text="SUBMIT", bg="darksalmon", fg="yellow", bd=3, cursor="arrow", command=printing).grid(row=5,
                                                                                                                 column=1,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 ipadx=20)

    window1 = Tk()
    window1.title("FLOWERS")
    window1.iconbitmap("lpu_logo.ico")
    window1.wm_attributes('-fullscreen', 'true')

    smile = PhotoImage(file="smile.gif")
    good_luck = PhotoImage(file="good_luck.gif")

    image1 = PhotoImage(file="ageratum.gif")
    image2 = PhotoImage(file="allium.gif")
    image3 = PhotoImage(file="alstromeria.gif")
    image4 = PhotoImage(file="alyssum.gif")
    image5 = PhotoImage(file="amarylis.gif")
    image6 = PhotoImage(file="anemone.gif")
    image7 = PhotoImage(file="angelica.gif")
    image8 = PhotoImage(file="balloon-flower.gif")
    image9 = PhotoImage(file="baneberry.gif")
    image10 = PhotoImage(file="basket-of-gold.gif")
    image11 = PhotoImage(file="bloodroot.gif")
    image12 = PhotoImage(file="rose.gif")

    frame1 = Frame(window1, bg="darkseagreen1", cursor="circle")
    frame1.pack(fill=BOTH)

    Label(frame1, image=image1).grid(row=1, column=1, padx=10, pady=10)
    Label(frame1, image=image2).grid(row=1, column=2, padx=10, pady=10)
    Label(frame1, image=image3).grid(row=1, column=3, padx=10, pady=10)
    Label(frame1, image=image4).grid(row=1, column=4, padx=10, pady=10)
    Label(frame1, image=image5).grid(row=1, column=5, padx=10, pady=10)
    Label(frame1, image=image6).grid(row=1, column=6, padx=10, pady=10)
    Label(frame1, image=image7).grid(row=2, column=1, padx=10, pady=10)
    Label(frame1, image=image8).grid(row=2, column=2, padx=10, pady=10)
    Label(frame1, image=image9).grid(row=2, column=3, padx=10, pady=10)
    Label(frame1, image=image10).grid(row=2, column=4, padx=10, pady=10)
    Label(frame1, image=image11).grid(row=2, column=5, padx=10, pady=10)
    Label(frame1, image=image12).grid(row=2, column=6, padx=10, pady=10)

    Label(frame1, text="Press EXIT to end Playing...", bg="darkseagreen1", fg="blue", font="garamond 15 italic").grid(
        row=3, column=1, sticky=W, padx=10, pady=10)
    Button(frame1, text="EXIT", bg="darksalmon", fg="yellow", bd=3, cursor="arrow", command=exit).grid(row=3, column=2,
                                                                                                       sticky=W,
                                                                                                       padx=10, pady=10,
                                                                                                       ipadx=30)
    Label(frame1, text="Press OK to continue Playing...", bg="darkseagreen1", fg="blue",
          font="garamond 15 italic").grid(row=3, column=3, sticky=W, padx=10, pady=10)
    Button(frame1, text="OK", bg="darksalmon", fg="yellow", bd=3, cursor="arrow", command=okProcess).grid(row=3,
                                                                                                          column=4,
                                                                                                          sticky=W,
                                                                                                          padx=10,
                                                                                                          pady=10,
                                                                                                          ipadx=30)
    Label(frame1, text="Note: Remember the images...", bg="darkseagreen1", fg="blue",
          font="garamond 15 italic").grid(row=3, column=5, sticky=W, padx=10, pady=10)

    Label(frame1, image=good_luck).grid(row=4, column=1, columnspan=6, pady=40)

    window1.mainloop()

def animals():
    window.destroy()

    def home():
        window1.destroy()
        import os
        os.system("python about_us.py")

    def okProcess():
        frame1.destroy()

        frame2 = Frame(window1, bg="skyblue", cursor="cross")
        frame2.pack(fill=BOTH, expand=YES)

        frame3 = Frame(window1, bg="#46f0f0", cursor="plus")
        frame3.pack(fill=BOTH)

        from tkinter import messagebox

        def printing():
            messagebox.showinfo("Number of Animals", str(counting()) + " Animals are correctly recognize" + "\n" + str(incorrect_counting()) + " Animals are selectled wrongly")
            L = Label(frame2, bg="skyblue", fg="black", font="gabriola 30 italic underline")
            L.grid(row=5, column=2, columnspan=15)
            if counting() > incorrect_counting():
                L.config(text="Percentage of Accuracy is " + str("%.2f" % (((counting() - incorrect_counting()) * 100) / 12)) + "%")
            else:
                L.config(text="Percentage of Accuracy is 0.00%")

            Label(frame3, image=smile).grid(row=1, column=1, padx=100, pady=50)
            Label(frame3, text="Thank You !!!", bg="#46f0f0", fg="blue", font="chaurcer 25 italic").grid(row=1,
                                                                                                         column=2,
                                                                                                         sticky=N,
                                                                                                         pady=180)
            Label(frame3, text="Press EXIT to end Playing...", bg="#46f0f0", fg="blue", font="garamond 30 italic").grid(
                row=2, column=1, sticky=W, padx=10, pady=10)
            Button(frame3, text="EXIT", bg="darksalmon", fg="yellow", bd=3, cursor="arrow", command=exit).grid(row=2,
                                                                                                               column=2,
                                                                                                               sticky=W,
                                                                                                               padx=10,
                                                                                                               pady=10,
                                                                                                               ipadx=30)

        def counting():
            count = v1.get() + v2.get() + v3.get() + v4.get() + v5.get() + v6.get() + v7.get() + v8.get() + v9.get() + v10.get() + v11.get() + v12.get()
            return count

        def incorrect_counting():
            incorrect_count = v13.get() + v14.get() + v15.get() + v16.get() + v17.get() + v18.get() + v19.get() + v20.get()
            return incorrect_count

        v1 = IntVar()
        v2 = IntVar()
        v3 = IntVar()
        v4 = IntVar()
        v5 = IntVar()
        v6 = IntVar()
        v7 = IntVar()
        v8 = IntVar()
        v9 = IntVar()
        v10 = IntVar()
        v11 = IntVar()
        v12 = IntVar()
        v13 = IntVar()
        v14 = IntVar()
        v15 = IntVar()
        v16 = IntVar()
        v17 = IntVar()
        v18 = IntVar()
        v19 = IntVar()
        v20 = IntVar()

        Label(frame2, text="Select maximun 12 Animals name", bg="skyblue", fg="black", font="garamond 20 italic").grid(row=0,
                                                                                                              column=0,
                                                                                                              sticky=W, padx=100)
        Label(frame2, text="that appeared previously...", bg="skyblue", fg="black", font="garamond 20 italic").grid(
            row=1, column=0, sticky=W, padx=100)
        Button(frame2, text="HOME", bg="darksalmon", fg="yellow", bd=3, cursor="arrow", command=home).grid(row=1,
                                                                                                           column=6,
                                                                                                           padx=200,
                                                                                                           pady=10,
                                                                                                           ipadx=20)

        Checkbutton(frame2, text="Buffalo", fg="red", bg="skyblue", variable=v1, onvalue=1, offvalue=0,
                    command=counting).grid(row=4, column=5, padx=10, pady=10)
        Checkbutton(frame2, text="Cat", fg="red", bg="skyblue", variable=v2, onvalue=1, offvalue=0,
                    command=counting).grid(row=1, column=2, padx=10, pady=10)
        Checkbutton(frame2, text="Lion", fg="red", bg="skyblue", variable=v3, onvalue=1, offvalue=0,
                    command=counting).grid(row=4, column=2, padx=10, pady=10)
        Checkbutton(frame2, text="Bison", fg="red", bg="skyblue", variable=v4, onvalue=1, offvalue=0,
                    command=counting).grid(row=1, column=4, padx=10, pady=10)
        Checkbutton(frame2, text="Cow", fg="red", bg="skyblue", variable=v5, onvalue=1, offvalue=0,
                    command=counting).grid(row=1, column=5, padx=10, pady=10)
        Checkbutton(frame2, text="Monkey", fg="red", bg="skyblue", variable=v6, onvalue=1, offvalue=0,
                    command=counting).grid(row=2, column=1, padx=10, pady=10)
        Checkbutton(frame2, text="Fox", fg="red", bg="skyblue", variable=v7, onvalue=1, offvalue=0,
                    command=counting).grid(row=3, column=5, padx=10, pady=10)
        Checkbutton(frame2, text="Horse", fg="red", bg="skyblue", variable=v8, onvalue=1, offvalue=0,
                    command=counting).grid(row=2, column=3, padx=10, pady=10)
        Checkbutton(frame2, text="Rabbit", fg="red", bg="skyblue", variable=v9, onvalue=1, offvalue=0,
                    command=counting).grid(row=2, column=4, padx=10, pady=10)
        Checkbutton(frame2, text="Deer", fg="red", bg="skyblue", variable=v10, onvalue=1, offvalue=0,
                    command=counting).grid(row=3, column=3, padx=10, pady=10)
        Checkbutton(frame2, text="Zebra", fg="red", bg="skyblue", variable=v11, onvalue=1, offvalue=0,
                    command=counting).grid(row=3, column=2, padx=10, pady=10)
        Checkbutton(frame2, text="Tiger", fg="red", bg="skyblue", variable=v12, onvalue=1, offvalue=0,
                    command=counting).grid(row=3, column=1, padx=10, pady=10)
        Checkbutton(frame2, text="Cattle", fg="red", bg="skyblue", variable=v13, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=2, column=5, padx=10, pady=10)
        Checkbutton(frame2, text="Pig", fg="red", bg="skyblue", variable=v14, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=3, column=4, padx=10, pady=10)
        Checkbutton(frame2, text="Anteater", fg="red", bg="skyblue", variable=v15, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=2, column=2, padx=10, pady=10)
        Checkbutton(frame2, text="Donkey", fg="red", bg="skyblue", variable=v16, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=4, column=1, padx=10, pady=10)
        Checkbutton(frame2, text="Caracal", fg="red", bg="skyblue", variable=v17, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=1, column=3, padx=10, pady=10)
        Checkbutton(frame2, text="Agouti", fg="red", bg="skyblue", variable=v18, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=4, column=3, padx=10, pady=10)
        Checkbutton(frame2, text="Armadillo", fg="red", bg="skyblue", variable=v19, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=4, column=4, padx=10, pady=10)
        Checkbutton(frame2, text="Bear", fg="red", bg="skyblue", variable=v20, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=1, column=1, padx=10, pady=10)

        Button(frame2, text="SUBMIT", bg="darksalmon", fg="yellow", bd=3, cursor="arrow", command=printing).grid(row=5,
                                                                                                                 column=1,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 ipadx=20)

    window1 = Tk()
    window1.title("ANIMALS")
    window1.iconbitmap("lpu_logo.ico")
    window1.wm_attributes('-fullscreen', 'true')

    smile = PhotoImage(file="smile.gif")
    good_luck = PhotoImage(file="good_luck.gif")

    image1 = PhotoImage(file="bison.gif")
    image2 = PhotoImage(file="buffalo.gif")
    image3 = PhotoImage(file="cat.gif")
    image4 = PhotoImage(file="cow.gif")
    image5 = PhotoImage(file="lion.gif")
    image6 = PhotoImage(file="monkey.gif")
    image7 = PhotoImage(file="tiger.gif")
    image8 = PhotoImage(file="zebra.gif")
    image9 = PhotoImage(file="deer.gif")
    image10 = PhotoImage(file="fox.gif")
    image11 = PhotoImage(file="rabbit.gif")
    image12 = PhotoImage(file="horse.gif")

    frame1 = Frame(window1, bg="darkseagreen1", cursor="circle")
    frame1.pack(fill=BOTH)

    Label(frame1, image=image1).grid(row=1, column=1, padx=10, pady=10)
    Label(frame1, image=image2).grid(row=1, column=2, padx=10, pady=10)
    Label(frame1, image=image3).grid(row=1, column=3, padx=10, pady=10)
    Label(frame1, image=image4).grid(row=1, column=4, padx=10, pady=10)
    Label(frame1, image=image5).grid(row=1, column=5, padx=10, pady=10)
    Label(frame1, image=image6).grid(row=1, column=6, padx=10, pady=10)
    Label(frame1, image=image7).grid(row=2, column=1, padx=10, pady=10)
    Label(frame1, image=image8).grid(row=2, column=2, padx=10, pady=10)
    Label(frame1, image=image9).grid(row=2, column=3, padx=10, pady=10)
    Label(frame1, image=image10).grid(row=2, column=4, padx=10, pady=10)
    Label(frame1, image=image11).grid(row=2, column=5, padx=10, pady=10)
    Label(frame1, image=image12).grid(row=2, column=6, padx=10, pady=10)

    Label(frame1, text="Press EXIT to end Playing...", bg="darkseagreen1", fg="blue", font="garamond 15 italic").grid(
        row=3, column=1, sticky=W, padx=10, pady=10)
    Button(frame1, text="EXIT", bg="darksalmon", fg="yellow", bd=3, cursor="arrow", command=exit).grid(row=3, column=2,
                                                                                                       sticky=W,
                                                                                                       padx=10, pady=10,
                                                                                                       ipadx=30)
    Label(frame1, text="Press OK to continue Playing...", bg="darkseagreen1", fg="blue",
          font="garamond 15 italic").grid(row=3, column=3, sticky=W, padx=10, pady=10)
    Button(frame1, text="OK", bg="darksalmon", fg="yellow", bd=3, cursor="arrow", command=okProcess).grid(row=3,
                                                                                                          column=4,
                                                                                                          sticky=W,
                                                                                                          padx=10,
                                                                                                          pady=10,
                                                                                                          ipadx=30)
    Label(frame1, text="Note: Remember the images...", bg="darkseagreen1", fg="blue",
          font="garamond 15 italic").grid(row=3, column=5, sticky=W, padx=10, pady=10)

    Label(frame1, image=good_luck).grid(row=4, column=1, columnspan=6, pady=40)

    window1.mainloop()


def fruits():
    window.destroy()

    def home():
        window1.destroy()
        import os
        os.system("python about_us.py")

    def okProcess():
        frame1.destroy()

        frame2 = Frame(window1, bg="skyblue", cursor="cross")
        frame2.pack(fill=BOTH, expand=YES)

        frame3 = Frame(window1, bg="#46f0f0", cursor="plus")
        frame3.pack(fill=BOTH)

        from tkinter import messagebox

        def printing():
            messagebox.showinfo("Number of Fruits", str(counting()) + " Fruits are correctly recognize" + "\n" + str(incorrect_counting()) + " Fruits are selectled wrongly")
            L = Label(frame2, bg="skyblue", fg="black", font="gabriola 30 italic underline")
            L.grid(row=5, column=2, columnspan=15)
            if counting() > incorrect_counting():
                L.config(text="Percentage of Accuracy is " + str("%.2f" % (((counting() - incorrect_counting()) * 100) / 12)) + "%")
            else:
                L.config(text="Percentage of Accuracy is 0.00%")

            Label(frame3, image=smile).grid(row=1, column=1, padx=100, pady=50)
            Label(frame3, text="Thank You !!!", bg="#46f0f0", fg="blue", font="chaurcer 25 italic").grid(row=1,
                                                                                                         column=2,
                                                                                                         sticky=N,
                                                                                                         pady=180)
            Label(frame3, text="Press EXIT to end Playing...", bg="#46f0f0", fg="blue", font="garamond 30 italic").grid(
                row=2, column=1, sticky=W, padx=10, pady=10)
            Button(frame3, text="EXIT", bg="darksalmon", fg="yellow", bd=3, cursor="arrow", command=exit).grid(row=2,
                                                                                                               column=2,
                                                                                                               sticky=W,
                                                                                                               padx=10,
                                                                                                               pady=10,
                                                                                                               ipadx=30)

        def counting():
            count = v1.get() + v2.get() + v3.get() + v4.get() + v5.get() + v6.get() + v7.get() + v8.get() + v9.get() + v10.get() + v11.get() + v12.get()
            return count

        def incorrect_counting():
            incorrect_count = v13.get() + v14.get() + v15.get() + v16.get() + v17.get() + v18.get() + v19.get() + v20.get()
            return incorrect_count

        v1 = IntVar()
        v2 = IntVar()
        v3 = IntVar()
        v4 = IntVar()
        v5 = IntVar()
        v6 = IntVar()
        v7 = IntVar()
        v8 = IntVar()
        v9 = IntVar()
        v10 = IntVar()
        v11 = IntVar()
        v12 = IntVar()
        v13 = IntVar()
        v14 = IntVar()
        v15 = IntVar()
        v16 = IntVar()
        v17 = IntVar()
        v18 = IntVar()
        v19 = IntVar()
        v20 = IntVar()

        Label(frame2, text="Select maximum 12 Fruits name", bg="skyblue", fg="black", font="garamond 20 italic").grid(row=0,
                                                                                                              column=0,
                                                                                                              sticky=W, padx=100)
        Label(frame2, text="that appeared previously...", bg="skyblue", fg="black", font="garamond 20 italic").grid(
            row=1, column=0, sticky=W, padx=100)
        Button(frame2, text="HOME", bg="darksalmon", fg="yellow", bd=3, cursor="arrow", command=home).grid(row=1,
                                                                                                           column=6,
                                                                                                           padx=200,
                                                                                                           pady=10,
                                                                                                           ipadx=20)

        Checkbutton(frame2, text="Orange", fg="red", bg="skyblue", variable=v1, onvalue=1, offvalue=0,
                    command=counting).grid(row=4, column=5, padx=10, pady=10)
        Checkbutton(frame2, text="Mango", fg="red", bg="skyblue", variable=v2, onvalue=1, offvalue=0,
                    command=counting).grid(row=1, column=2, padx=10, pady=10)
        Checkbutton(frame2, text="Lemon", fg="red", bg="skyblue", variable=v3, onvalue=1, offvalue=0,
                    command=counting).grid(row=4, column=2, padx=10, pady=10)
        Checkbutton(frame2, text="Jujube", fg="red", bg="skyblue", variable=v4, onvalue=1, offvalue=0,
                    command=counting).grid(row=1, column=4, padx=10, pady=10)
        Checkbutton(frame2, text="Guava", fg="red", bg="skyblue", variable=v5, onvalue=1, offvalue=0,
                    command=counting).grid(row=1, column=5, padx=10, pady=10)
        Checkbutton(frame2, text="Grape", fg="red", bg="skyblue", variable=v6, onvalue=1, offvalue=0,
                    command=counting).grid(row=2, column=1, padx=10, pady=10)
        Checkbutton(frame2, text="Goji berry", fg="red", bg="skyblue", variable=v7, onvalue=1, offvalue=0,
                    command=counting).grid(row=3, column=5, padx=10, pady=10)
        Checkbutton(frame2, text="Durian", fg="red", bg="skyblue", variable=v8, onvalue=1, offvalue=0,
                    command=counting).grid(row=2, column=3, padx=10, pady=10)
        Checkbutton(frame2, text="Cranberry", fg="red", bg="skyblue", variable=v9, onvalue=1, offvalue=0,
                    command=counting).grid(row=2, column=4, padx=10, pady=10)
        Checkbutton(frame2, text="Cherry", fg="red", bg="skyblue", variable=v10, onvalue=1, offvalue=0,
                    command=counting).grid(row=3, column=3, padx=10, pady=10)
        Checkbutton(frame2, text="Blackberry", fg="red", bg="skyblue", variable=v11, onvalue=1, offvalue=0,
                    command=counting).grid(row=3, column=2, padx=10, pady=10)
        Checkbutton(frame2, text="Apple", fg="red", bg="skyblue", variable=v12, onvalue=1, offvalue=0,
                    command=counting).grid(row=3, column=1, padx=10, pady=10)
        Checkbutton(frame2, text="Banana", fg="red", bg="skyblue", variable=v13, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=2, column=5, padx=10, pady=10)
        Checkbutton(frame2, text="Pears", fg="red", bg="skyblue", variable=v14, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=3, column=4, padx=10, pady=10)
        Checkbutton(frame2, text="Limes", fg="red", bg="skyblue", variable=v15, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=2, column=2, padx=10, pady=10)
        Checkbutton(frame2, text="Apricot", fg="red", bg="skyblue", variable=v16, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=4, column=1, padx=10, pady=10)
        Checkbutton(frame2, text="Peach", fg="red", bg="skyblue", variable=v17, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=1, column=3, padx=10, pady=10)
        Checkbutton(frame2, text="Nectarine", fg="red", bg="skyblue", variable=v18, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=4, column=3, padx=10, pady=10)
        Checkbutton(frame2, text="Cucumber", fg="red", bg="skyblue", variable=v19, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=4, column=4, padx=10, pady=10)
        Checkbutton(frame2, text="Watermelon", fg="red", bg="skyblue", variable=v20, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=1, column=1, padx=10, pady=10)

        Button(frame2, text="SUBMIT", bg="darksalmon", fg="yellow", bd=3, cursor="arrow", command=printing).grid(row=5,
                                                                                                                 column=1,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 ipadx=20)

    window1 = Tk()
    window1.title("FRUITS")
    window1.iconbitmap("lpu_logo.ico")
    window1.wm_attributes('-fullscreen', 'true')

    smile = PhotoImage(file="smile.gif")
    good_luck = PhotoImage(file="good_luck.gif")

    image1 = PhotoImage(file="orange.gif")
    image2 = PhotoImage(file="mango.gif")
    image3 = PhotoImage(file="lemon.gif")
    image4 = PhotoImage(file="jujube.gif")
    image5 = PhotoImage(file="guava.gif")
    image6 = PhotoImage(file="grape.gif")
    image7 = PhotoImage(file="goji-berry.gif")
    image8 = PhotoImage(file="durian.gif")
    image9 = PhotoImage(file="cranberry.gif")
    image10 = PhotoImage(file="cherry.gif")
    image11 = PhotoImage(file="blackberry.gif")
    image12 = PhotoImage(file="apple.gif")

    frame1 = Frame(window1, bg="darkseagreen1", cursor="circle")
    frame1.pack(fill=BOTH)

    Label(frame1, image=image1).grid(row=1, column=1, padx=10, pady=10)
    Label(frame1, image=image2).grid(row=1, column=2, padx=10, pady=10)
    Label(frame1, image=image3).grid(row=1, column=3, padx=10, pady=10)
    Label(frame1, image=image4).grid(row=1, column=4, padx=10, pady=10)
    Label(frame1, image=image5).grid(row=1, column=5, padx=10, pady=10)
    Label(frame1, image=image6).grid(row=1, column=6, padx=10, pady=10)
    Label(frame1, image=image7).grid(row=2, column=1, padx=10, pady=10)
    Label(frame1, image=image8).grid(row=2, column=2, padx=10, pady=10)
    Label(frame1, image=image9).grid(row=2, column=3, padx=10, pady=10)
    Label(frame1, image=image10).grid(row=2, column=4, padx=10, pady=10)
    Label(frame1, image=image11).grid(row=2, column=5, padx=10, pady=10)
    Label(frame1, image=image12).grid(row=2, column=6, padx=10, pady=10)

    Label(frame1, text="Press EXIT to end Playing...", bg="darkseagreen1", fg="blue", font="garamond 15 italic").grid(
        row=3, column=1, sticky=W, padx=10, pady=10)
    Button(frame1, text="EXIT", bg="darksalmon", fg="yellow", bd=3, cursor="arrow", command=exit).grid(row=3, column=2,
                                                                                                       sticky=W,
                                                                                                       padx=10, pady=10,
                                                                                                       ipadx=30)
    Label(frame1, text="Press OK to continue Playing...", bg="darkseagreen1", fg="blue",
          font="garamond 15 italic").grid(row=3, column=3, sticky=W, padx=10, pady=10)
    Button(frame1, text="OK", bg="darksalmon", fg="yellow", bd=3, cursor="arrow", command=okProcess).grid(row=3,
                                                                                                          column=4,
                                                                                                          sticky=W,
                                                                                                          padx=10,
                                                                                                          pady=10,
                                                                                                          ipadx=30)
    Label(frame1, text="Note: Remember the images...", bg="darkseagreen1", fg="blue",
          font="garamond 15 italic").grid(row=3, column=5, sticky=W, padx=10, pady=10)

    Label(frame1, image=good_luck).grid(row=4, column=1, columnspan=6, pady=40)

    window1.mainloop()

def players():
    window.destroy()

    def home():
        window1.destroy()
        import os
        os.system("python about_us.py")

    def okProcess():
        frame1.destroy()

        frame2 = Frame(window1, bg="skyblue", cursor="cross")
        frame2.pack(fill=BOTH, expand=YES)

        frame3 = Frame(window1, bg="#46f0f0", cursor="plus")
        frame3.pack(fill=BOTH)

        from tkinter import messagebox

        def printing():
            messagebox.showinfo("Number of Players", str(counting()) + " Players are correctly recognize" + "\n" + str(incorrect_counting()) + " Players are selectled wrongly")
            L = Label(frame2, bg="skyblue", fg="black", font="gabriola 30 italic underline")
            L.grid(row=5, column=2, columnspan=15)
            if counting() > incorrect_counting():
                L.config(text="Percentage of Accuracy is " + str("%.2f" % (((counting() - incorrect_counting()) * 100) / 12)) + "%")
            else:
                L.config(text="Percentage of Accuracy is 0.00%")

            Label(frame3, image=smile).grid(row=1, column=1, padx=100, pady=50)
            Label(frame3, text="Thank You !!!", bg="#46f0f0", fg="blue", font="chaurcer 25 italic").grid(row=1,
                                                                                                         column=2,
                                                                                                         sticky=N,
                                                                                                         pady=180)
            Label(frame3, text="Press EXIT to end Playing...", bg="#46f0f0", fg="blue", font="garamond 30 italic").grid(
                row=2, column=1, sticky=W, padx=10, pady=10)
            Button(frame3, text="EXIT", bg="darksalmon", fg="yellow", bd=3, cursor="arrow", command=exit).grid(row=2,
                                                                                                               column=2,
                                                                                                               sticky=W,
                                                                                                               padx=10,
                                                                                                               pady=10,
                                                                                                               ipadx=30)

        def counting():
            count = v1.get() + v2.get() + v3.get() + v4.get() + v5.get() + v6.get() + v7.get() + v8.get() + v9.get() + v10.get() + v11.get() + v12.get()
            return count

        def incorrect_counting():
            incorrect_count = v13.get() + v14.get() + v15.get() + v16.get() + v17.get() + v18.get() + v19.get() + v20.get()
            return incorrect_count

        v1 = IntVar()
        v2 = IntVar()
        v3 = IntVar()
        v4 = IntVar()
        v5 = IntVar()
        v6 = IntVar()
        v7 = IntVar()
        v8 = IntVar()
        v9 = IntVar()
        v10 = IntVar()
        v11 = IntVar()
        v12 = IntVar()
        v13 = IntVar()
        v14 = IntVar()
        v15 = IntVar()
        v16 = IntVar()
        v17 = IntVar()
        v18 = IntVar()
        v19 = IntVar()
        v20 = IntVar()

        Label(frame2, text="Select maximum 12 Players name", bg="skyblue", fg="black", font="garamond 20 italic").grid(row=0,
                                                                                                              column=0,
                                                                                                              sticky=W, padx=100)
        Label(frame2, text="that appeared previously...", bg="skyblue", fg="black", font="garamond 20 italic").grid(
            row=1, column=0, sticky=W, padx=100)
        Button(frame2, text="HOME", bg="darksalmon", fg="yellow", bd=3, cursor="arrow", command=home).grid(row=1,
                                                                                                           column=6,
                                                                                                           padx=50,
                                                                                                           pady=10,
                                                                                                           ipadx=20)

        Checkbutton(frame2, text="M S Dhoni", fg="red", bg="skyblue", variable=v1, onvalue=1, offvalue=0,
                    command=counting).grid(row=4, column=5, padx=10, pady=10)
        Checkbutton(frame2, text="Sachin Tendulkar", fg="red", bg="skyblue", variable=v2, onvalue=1, offvalue=0,
                    command=counting).grid(row=1, column=2, padx=10, pady=10)
        Checkbutton(frame2, text="Suresh Raina", fg="red", bg="skyblue", variable=v3, onvalue=1, offvalue=0,
                    command=counting).grid(row=4, column=2, padx=10, pady=10)
        Checkbutton(frame2, text="Lionel Messi", fg="red", bg="skyblue", variable=v4, onvalue=1, offvalue=0,
                    command=counting).grid(row=1, column=4, padx=10, pady=10)
        Checkbutton(frame2, text="Umesh Yadav", fg="red", bg="skyblue", variable=v5, onvalue=1, offvalue=0,
                    command=counting).grid(row=1, column=5, padx=10, pady=10)
        Checkbutton(frame2, text="Chris Gayle", fg="red", bg="skyblue", variable=v6, onvalue=1, offvalue=0,
                    command=counting).grid(row=2, column=1, padx=10, pady=10)
        Checkbutton(frame2, text="Gautam Gambhir", fg="red", bg="skyblue", variable=v7, onvalue=1, offvalue=0,
                    command=counting).grid(row=3, column=5, padx=10, pady=10)
        Checkbutton(frame2, text="Shikhar Dhawan", fg="red", bg="skyblue", variable=v8, onvalue=1, offvalue=0,
                    command=counting).grid(row=2, column=3, padx=10, pady=10)
        Checkbutton(frame2, text="Cristano Ronaldo", fg="red", bg="skyblue", variable=v9, onvalue=1, offvalue=0,
                    command=counting).grid(row=2, column=4, padx=10, pady=10)
        Checkbutton(frame2, text="Sam Billings", fg="red", bg="skyblue", variable=v10, onvalue=1, offvalue=0,
                    command=counting).grid(row=3, column=3, padx=10, pady=10)
        Checkbutton(frame2, text="Shane Watson", fg="red", bg="skyblue", variable=v11, onvalue=1, offvalue=0,
                    command=counting).grid(row=3, column=2, padx=10, pady=10)
        Checkbutton(frame2, text="Virat Kholi", fg="red", bg="skyblue", variable=v12, onvalue=1, offvalue=0,
                    command=counting).grid(row=3, column=1, padx=10, pady=10)
        Checkbutton(frame2, text="Harry Kane", fg="red", bg="skyblue", variable=v13, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=2, column=5, padx=10, pady=10)
        Checkbutton(frame2, text="Luka Modric", fg="red", bg="skyblue", variable=v14, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=3, column=4, padx=10, pady=10)
        Checkbutton(frame2, text="Rishabh Pant", fg="red", bg="skyblue", variable=v15, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=2, column=2, padx=10, pady=10)
        Checkbutton(frame2, text="Kane Williamson", fg="red", bg="skyblue", variable=v16, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=4, column=1, padx=10, pady=10)
        Checkbutton(frame2, text="Faf Du Plessis", fg="red", bg="skyblue", variable=v17, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=1, column=3, padx=10, pady=10)
        Checkbutton(frame2, text="Harbhajan Singh", fg="red", bg="skyblue", variable=v18, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=4, column=3, padx=10, pady=10)
        Checkbutton(frame2, text="Yuvraj Singh", fg="red", bg="skyblue", variable=v19, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=4, column=4, padx=10, pady=10)
        Checkbutton(frame2, text="David Miller", fg="red", bg="skyblue", variable=v20, onvalue=1, offvalue=0, command=incorrect_counting).grid(row=1, column=1, padx=10, pady=10)

        Button(frame2, text="SUBMIT", bg="darksalmon", fg="yellow", bd=3, cursor="arrow", command=printing).grid(row=5,
                                                                                                                 column=1,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 ipadx=20)

    window1 = Tk()
    window1.title("PLAYERS")
    window1.iconbitmap("lpu_logo.ico")
    window1.wm_attributes('-fullscreen', 'true')

    smile = PhotoImage(file="smile.gif")
    good_luck = PhotoImage(file="good_luck.gif")

    image1 = PhotoImage(file="sachin-tendulkar.gif")
    image2 = PhotoImage(file="mahendra-singh-dhoni.gif")
    image3 = PhotoImage(file="suresh-raina.gif")
    image4 = PhotoImage(file="lionel-messi.gif")
    image5 = PhotoImage(file="gautam-gambhir.gif")
    image6 = PhotoImage(file="shikhar-dhawan.gif")
    image7 = PhotoImage(file="chris-gayle.gif")
    image8 = PhotoImage(file="sam-billings.gif")
    image9 = PhotoImage(file="cristiano-ronaldo.gif")
    image10 = PhotoImage(file="virat-kohli.gif")
    image11 = PhotoImage(file="umesh-yadav.gif")
    image12 = PhotoImage(file="shane-watson.gif")

    frame1 = Frame(window1, bg="darkseagreen1", cursor="circle")
    frame1.pack(fill=BOTH)

    Label(frame1, image=image1).grid(row=1, column=1, padx=10, pady=10)
    Label(frame1, image=image2).grid(row=1, column=2, padx=10, pady=10)
    Label(frame1, image=image3).grid(row=1, column=3, padx=10, pady=10)
    Label(frame1, image=image4).grid(row=1, column=4, padx=10, pady=10)
    Label(frame1, image=image5).grid(row=1, column=5, padx=10, pady=10)
    Label(frame1, image=image6).grid(row=1, column=6, padx=10, pady=10)
    Label(frame1, image=image7).grid(row=2, column=1, padx=10, pady=10)
    Label(frame1, image=image8).grid(row=2, column=2, padx=10, pady=10)
    Label(frame1, image=image9).grid(row=2, column=3, padx=10, pady=10)
    Label(frame1, image=image10).grid(row=2, column=4, padx=10, pady=10)
    Label(frame1, image=image11).grid(row=2, column=5, padx=10, pady=10)
    Label(frame1, image=image12).grid(row=2, column=6, padx=10, pady=10)

    Label(frame1, text="Press EXIT to end Playing...", bg="darkseagreen1", fg="blue", font="garamond 15 italic").grid(
        row=3, column=1, sticky=W, padx=10, pady=10)
    Button(frame1, text="EXIT", bg="darksalmon", fg="yellow", bd=3, cursor="arrow", command=exit).grid(row=3, column=2,
                                                                                                       sticky=W,
                                                                                                       padx=10, pady=10,
                                                                                                       ipadx=30)
    Label(frame1, text="Press OK to continue Playing...", bg="darkseagreen1", fg="blue",
          font="garamond 15 italic").grid(row=3, column=3, sticky=W, padx=10, pady=10)
    Button(frame1, text="OK", bg="darksalmon", fg="yellow", bd=3, cursor="arrow", command=okProcess).grid(row=3,
                                                                                                          column=4,
                                                                                                          sticky=W,
                                                                                                          padx=10,
                                                                                                          pady=10,
                                                                                                          ipadx=30)
    Label(frame1, text="Note: Remember the images...", bg="darkseagreen1", fg="blue",
          font="garamond 15 italic").grid(row=3, column=5, sticky=W, padx=10, pady=10)

    Label(frame1, image=good_luck).grid(row=4, column=1, columnspan=6, pady=40)

    window1.mainloop()

from tkinter import *

window = Tk()
window.title("HOME PAGE")
window.iconbitmap("lpu_logo.ico")
window.wm_attributes('-fullscreen','true')

frame1 = Frame(window, bg="darkseagreen1")
frame1.pack(fill=BOTH)

Label(frame1, text="WELCOME", fg="red", font="papyrus 25 italic bold", bg="darkseagreen1").pack()
Label(frame1, text="TO", fg="red", font="papyrus 25 italic bold", bg="darkseagreen1").pack()
Label(frame1, text="KIDS LEARNING GAME", fg="red", font="papyrus 25 italic bold", bg="darkseagreen1").pack()

Label(frame1, text="Click On the Image to Continue the Game...", fg="blue", font="garamond 25 italic", bg="darkseagreen1").pack(anchor=NW, padx=10, pady=10)

homebird = PhotoImage(file="homebird.gif")
homeflower = PhotoImage(file="homeflower.gif")
homeanimal = PhotoImage(file="homeanimal.gif")
homefruit = PhotoImage(file="homefruit.gif")
homeplayer = PhotoImage(file="homeplayer.gif")

Button(frame1, image=homebird, command=birds).pack(side=LEFT, padx=10)
Button(frame1, image=homeflower, command=flowers).pack(side=LEFT, padx=10)
Button(frame1, image=homeanimal, command=animals).pack(side=LEFT, padx=10)
Button(frame1, image=homefruit, command=fruits).pack(side=LEFT, padx=10)
Button(frame1, image=homeplayer, command=players).pack(side=LEFT, padx=10)

frame2 = Frame(window, bg="darkseagreen1")
frame2.pack(anchor=NW, fill=BOTH)

Label(frame2, text="BIRDS", bg="darkseagreen1", fg="blue", font="garamond 20 italic").pack(side=LEFT, padx=70, pady=5)
Label(frame2, text="FLOWERS", bg="darkseagreen1", fg="blue", font="garamond 20 italic").pack(side=LEFT, padx=120, pady=5)
Label(frame2, text="ANIMALS", bg="darkseagreen1", fg="blue", font="garamond 20 italic").pack(side=LEFT, padx=30, pady=5)
Label(frame2, text="FRUITS", bg="darkseagreen1", fg="blue", font="garamond 20 italic").pack(side=LEFT, padx=120, pady=5)
Label(frame2, text="PLAYERS", bg="darkseagreen1", fg="blue", font="garamond 20 italic").pack(side=LEFT, padx=50, pady=5)

frame3 = Frame(window, bg="darkseagreen1")
frame3.pack(anchor=NW, fill=BOTH)

Label(frame3, text="Press EXIT to End Playing...", fg="blue", font="garamond 15 italic", bg="darkseagreen1").pack(side=LEFT, padx=10, pady=25)
Button(frame3, text="EXIT", bg="darksalmon", fg="yellow", bd=3, cursor="arrow", command=exit).pack(side=LEFT, padx=10, pady=25, ipadx=30)

window.mainloop()