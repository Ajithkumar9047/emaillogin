import os
from tkinter import *
import  random
from tkinter import messagebox
import datetime as dt
date = dt.datetime.now()
d=f'{date:%A, %B %d, %Y}'
root = Tk()
scroll_text = StringVar()
msg2 = "THANK YOU FOR VISITING US..."
text2 = ""
n = 0


class Bill_App:


    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("BILLING")
        bg_color = "#0BB5FF"
        title = Label(self.root, text="SETHURAM TRADERS", bd=10, relief=GROOVE, bg=bg_color, fg="#003151",
                      font=("times new roman", 30, "bold"), pady=2).pack(fill=X)
        self.Date=d
        # ====cakes======
        self.plaincake = DoubleVar()
        self.plumcake = DoubleVar()
        self.birthdaycake = DoubleVar()
        self.blackforest = DoubleVar()
        self.creamcake = DoubleVar()
        self.fruitecake = DoubleVar()

        # =====peace =====
        self.browny_peace = IntVar()
        self.plum_peace = IntVar()
        self.plain_peace = IntVar()
        self.BF_peace = IntVar()
        self.cream_peace = IntVar()
        self.fruitecake_peace = IntVar()

        # =====additional value====
        self.Addition = StringVar()
        self.Addval = DoubleVar()
        self.Addval_price = IntVar()


        # =====Total Price=====
        self.cake_price = StringVar()
        self.peace_cake_price = StringVar()
        self.total_add = StringVar()

        # =======Tax price======
        self.cake_tax = StringVar()
        self.peace_tax = StringVar()
        self.chocolate_tax = StringVar()

        # ====name of customer=====
        self.c_name = StringVar()
        self.c_phon = StringVar()
        self.bill = StringVar()
        a = random.randint(1000, 9999)
        self.bill.set(str(a))
        self.search_bill = StringVar()

        # ===========cust Detail========
        F1 = LabelFrame(self.root, text="Customer Details", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        bg=bg_color, fg="#191970")  #
        F1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F1, text="Name Of Customer", bg=bg_color, fg="#003151",
                          font=("times new roman", 15, "bold")).grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=20, textvariable=self.c_name, font="arial 10", bd=7, relief=SUNKEN).grid(row=0,
                                                                                                             column=1,
                                                                                                             padx=5,
                                                                                                             pady=10)

        cphn_lbl = Label(F1, text="Phone Number", bg=bg_color, fg="#003151", font=("times new roman", 15, "bold")).grid(
            row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=20, textvariable=self.c_phon, font="arial 10", bd=7, relief=SUNKEN).grid(row=0,
                                                                                                            column=3,
                                                                                                            padx=5,
                                                                                                            pady=10)

        c_bill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="#003151",
                           font=("times new roman", 15, "bold")).grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=20, textvariable=self.search_bill, font="arial 10", bd=7, relief=SUNKEN).grid(
            row=0, column=5, padx=5, pady=10)

        bill_btn = Button(F1, text="Search", command=self.find_bill, bg="#03C04A", fg="white", width=10, bd=7,
                          font="arial 12 bold").grid(row=0, column=6, pady=10, padx=40)

        # ======Juices Frame=======
        F2 = LabelFrame(self.root, text="kg_cake", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        fg="#191970", bg=bg_color)
        F2.place(x=5, y=180, width=300, height=380)

        sprite_lbl1 = Label(F2, text="plaincake", font=("times new roman", 16, "bold"), bg=bg_color, fg="#003151").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        sprite_txt = Entry(F2, width=10, textvariable=self.plaincake, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        thumbsup_lbl1 = Label(F2, text="plum_cake", font=("times new roman", 16, "bold"), bg=bg_color,
                              fg="#003151").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        thumbsup_txt = Entry(F2, width=10, textvariable=self.plumcake, font=("times new roman", 16, "bold"), bd=5,
                             relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        coco_cola_lbl1 = Label(F2, text="birthday", font=("times new roman", 16, "bold"), bg=bg_color,
                               fg="#003151").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        coco_cola_txt = Entry(F2, width=10, textvariable=self.birthdaycake, font=("times new roman", 16, "bold"), bd=5,
                              relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        sveen_Up_lbl1 = Label(F2, text="blackforest", font=("times new roman", 16, "bold"), bg=bg_color, fg="#003151").grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        sveen_Up_txt = Entry(F2, width=10, textvariable=self.blackforest, font=("times new roman", 16, "bold"), bd=5,
                             relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        Dukes_lbl1 = Label(F2, text="cream_cake", font=("times new roman", 16, "bold"), bg=bg_color, fg="#003151").grid(
            row=4, column=0, padx=10, pady=10, sticky="w")
        Dukes_txt = Entry(F2, width=10, textvariable=self.creamcake, font=("times new roman", 16, "bold"), bd=5,
                          relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        mirinda_lbl1 = Label(F2, text="fruite_cake", font=("times new roman", 16, "bold"), bg=bg_color, fg="#003151").grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        mirinda_txt = Entry(F2, width=10, textvariable=self.fruitecake, font=("times new roman", 16, "bold"), bd=5,
                            relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        #  =======Chips Frame=======

        F3 = LabelFrame(self.root, text="peace_cake", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        fg="#191970", bg=bg_color)
        F3.place(x=300, y=180, width=325, height=380)

        lays_lbl1 = Label(F3, text="browny_peace", font=("times new roman", 16, "bold"), bg=bg_color, fg="#003151").grid(row=0,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 sticky="w")
        lays_txt = Entry(F3, width=10, textvariable=self.browny_peace, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        doritos_lbl1 = Label(F3, text="plain_cake", font=("times new roman", 16, "bold"), bg=bg_color, fg="#003151").grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        doritos_txt = Entry(F3, width=10, textvariable=self.plain_peace, font=("times new roman", 16, "bold"), bd=5,
                            relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        pringles_lbl1 = Label(F3, text="plum_peace", font=("times new roman", 16, "bold"), bg=bg_color,
                              fg="#003151").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        pringles_txt = Entry(F3, width=10, textvariable=self.plum_peace, font=("times new roman", 16, "bold"), bd=5,
                             relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        peppy_lbl1 = Label(F3, text="BF_peace", font=("times new roman", 16, "bold"), bg=bg_color, fg="#003151").grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        peppy_txt = Entry(F3, width=10, textvariable=self.BF_peace, font=("times new roman", 16, "bold"), bd=5,
                          relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        kurkure_lbl1 = Label(F3, text="cream_peace", font=("times new roman", 16, "bold"), bg=bg_color, fg="#003151").grid(
            row=4, column=0, padx=10, pady=10, sticky="w")
        kurkure_txt = Entry(F3, width=10, textvariable=self.cream_peace, font=("times new roman", 16, "bold"), bd=5,
                            relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        wheels_lbl1 = Label(F3, text="fruite_peace", font=("times new roman", 16, "bold"), bg=bg_color, fg="#003151").grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        wheels_txt = Entry(F3, width=10, textvariable=self.fruitecake_peace, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # ========Chocolate============

        F4 = LabelFrame(self.root, text="Additional", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        fg="#191970", bg=bg_color)
        F4.place(x=630, y=180, width=300, height=380)
        wheels1 = Label(F4, text="newproduct", font=("times new roman", 16, "bold"), bg=bg_color,
                            fg="#003151").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        kurkure_txt1 = Entry(F4, width=10, textvariable=self.Addition, font=("times new roman", 16, "bold"), bd=5,
                            relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)
        wheels2= Label(F4, text="quantity", font=("times new roman", 16, "bold"), bg=bg_color,
                        fg="#003151").grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        kurkure_txt2 = Entry(F4, width=10, textvariable=self.Addval, font=("times new roman", 16, "bold"), bd=5,
                             relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)
        wheels3 = Label(F4, text="price", font=("times new roman", 16, "bold"), bg=bg_color,
                        fg="#003151").grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        kurkure_txt3= Entry(F4, width=10, textvariable=self.Addval_price, font=("times new roman", 16, "bold"), bd=5,
                             relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)


        # Bill

        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=930, y=180, width=430, height=380)
        bill = Label(F5, text="BILL", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # =======Button=======
        F6 = LabelFrame(self.root, text="Bill Menu", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        fg="#191970", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)

        a1_lbl1 = Label(F6, text="Total cake Price", bg=bg_color, fg="#003151",
                        font=("times new roman", 14, "bold")).grid(row=0, column=0, padx=20, pady=1, sticky="w")
        a1_txt = Entry(F6, width=18, textvariable=self.cake_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=1, padx=10, pady=1)

        a2_lbl1 = Label(F6, text="Total peace cake", bg=bg_color, fg="#003151",
                        font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        a2_txt = Entry(F6, width=18, textvariable=self.peace_cake_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=1, column=1, padx=10, pady=1)

        a3_lbl1 = Label(F6, text="Total Addition Price", bg=bg_color, fg="#003151",
                        font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        a3_txt = Entry(F6, width=18, textvariable=self.total_add, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=2, column=1, padx=10, pady=1)

        b1_lbl1 = Label(F6, text="cake Tax", bg=bg_color, fg="#003151", font=("times new roman", 14, "bold")).grid(
            row=0, column=2, padx=20, pady=1, sticky="w")
        b1_txt = Entry(F6, width=18, textvariable=self.cake_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0,
                                                                                                                  column=3,
                                                                                                                  padx=10,
                                                                                                                  pady=1)

        b2_lbl1 = Label(F6, text="peace_Tax", bg=bg_color, fg="#003151", font=("times new roman", 14, "bold")).grid(
            row=1, column=2, padx=20, pady=1, sticky="w")
        b2_txt = Entry(F6, width=18, textvariable=self.peace_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1,
                                                                                                                  column=3,
                                                                                                                  padx=10,
                                                                                                                  pady=1)

        b3_lbl1 = Label(F6, text="Chocolate Tax", bg=bg_color, fg="#003151", font=("times new roman", 14, "bold")).grid(
            row=2, column=2, padx=20, pady=1, sticky="w")
        b3_txt = Entry(F6, width=18, textvariable=self.chocolate_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=2, column=3, padx=10, pady=1)

        btn_A = Frame(F6, bd=7, relief=GROOVE)
        btn_A.place(x=750, width=570, height=105)

        total = Button(btn_A, command=self.total, text="Total", bg="#03C04A", fg="White", bd=5, pady=15, width=6,
                       font="arial 13 bold").grid(row=0, column=0, padx=5, pady=5)
        Generate_bill = Button(btn_A, command=self.bill_area, text="Generate Bill", bg="#03C04A", fg="White", bd=5,
                               pady=15, width=11, font="arial 13 bold").grid(row=0, column=1, padx=5, pady=5)
        clear = Button(btn_A, text="Clear", command=self.clear_data, bg="#03C04A", fg="White", bd=5, pady=15, width=5,
                       font="arial 13 bold").grid(row=0, column=2, padx=5, pady=5)
        Exit = Button(btn_A, text="Exit", command=self.Exit_app, bg="#03C04A", fg="White", bd=5, pady=15, width=6,
                      font="arial 13 bold").grid(row=0, column=3, padx=5, pady=5)
        print=Button(btn_A, text="Print Bill", command=self.print_bill, bg="#03C04A", fg="White", bd=5, pady=15, width=6,
                      font="arial 13 bold").grid(row=0, column=4, padx=5, pady=5)
        self.welcome_bill()

        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, fg="#191970", bg=bg_color)
        F6.place(x=0, y=690, relwidth=1, height=110)

        # ============scroll text=============

        def display():
            global text2, n, msg2
            for t in range(len(msg2)):
                for k in range(t):
                    text2 += ' '
                for g in range(len(msg2) - t):
                    text2 += msg2[g]
                # text2 = text2.strip()
                F6.update()
                F6.after(200)
                text2 = text2.strip()
                scroll_text.set('')
                scroll_text.set(text2)
                text2 = ''
            scroll_text.set('')
            txtscroll.after(200, display)

        txtscroll = Entry(F6, textvariable=scroll_text, font=('arial', 50, 'bold'), fg='#003151', bd=10, bg=bg_color,
                          width=150)
        txtscroll.grid(row=0, column=0, columnspan=4)
        display()

    def total(self):
        self.plumcake_price = 400
        self.plaincake_price = 400
        self.birthdaycake_price = 500
        self.blackforest_price = 600
        self.creamcake_price = 600
        self.fruitecake_price = 700
        self.plum = (self.plumcake.get() * self.plumcake_price)
        self.plain = (self.plaincake.get() * self.plaincake_price )
        self.b_c = (self.birthdaycake.get() * self.birthdaycake_price)
        self.bf_c= (self.blackforest.get() * self.blackforest_price )
        self.c_c = (self.creamcake.get() * self.creamcake_price )
        self.f_c = (self.fruitecake.get() * self.fruitecake_price )
        self.total_cake_price = float(
            self.plum +
            self.plain +
            self.b_c +
            self.bf_c +
            self.c_c +
            self.f_c
        )
        self.cake_price.set("Rs. " + str(self.total_cake_price))
        #self.cs_tax = round((self.total_cake_price * 0.1), 2)
        #self.cake_tax.set("Rs. " + str(self.cs_tax))

        self.browny_peace_price = 60
        self.plain_peace_price = 40
        self.plum_peace_price = 50
        self.cream_peace_price = 60
        self.BF_peace_price = 60
        self.fruitecake_peace_price = 70
        self.j_s_p = (self.browny_peace.get() * self.browny_peace_price)
        self.j_t_p = (self.plain_peace.get() * self.plain_peace_price)
        self.j_c_p = (self.plum_peace.get() * self.plum_peace_price )
        self.j_sv_p = (self.cream_peace.get() * self.cream_peace_price)
        self.j_d_p = (self.BF_peace.get() * self.BF_peace_price)
        self.j_m_p = (self.fruitecake_peace.get() * self.fruitecake_peace_price)
        self.total_peace_price = float(
            self.j_s_p +
            self.j_t_p +
            self.j_c_p +
            self.j_sv_p +
            self.j_d_p +
            self.j_m_p
        )
        self.peace_cake_price.set("Rs. " + str(self.total_peace_price))
        #self.je_tax = round((self.total_peace_price * 0.05), 2)
        #self.peace_tax.set("Rs. " + str(self.je_tax))

        self.Addval_price_total=float(self.Addval.get()*self.Addval_price.get())

        self.total_add.set("Rs. " + str(self.Addval_price_total))

        self.Total_bill = float(self.total_cake_price +
                                self.total_peace_price +
                                self.Addval_price_total
                                )

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWELCOME TO SETHURAM TRADERS\n")
        self.txtarea.insert(END,F"   Railway Station Road,Chinnasalem-606201\n")
        self.txtarea.insert(END, F"\t\tContact-7358531841")
        self.txtarea.insert(END, f"\n BILL NUMBER : {self.bill.get()}")
        self.txtarea.insert(END, f"\n CUSTOMER NAME : {self.c_name.get()}")
        self.txtarea.insert(END, f"\n PHONE NUMBER : {self.c_phon.get()}")
        self.txtarea.insert(END, f"\n================================================")
        self.txtarea.insert(END, f"\nPRODUCTS    QUANTITY     PRICE        TOTALPRICE")
        self.txtarea.insert(END, f"\n================================================")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phon.get() == "":
            messagebox.showerror("Error", "Customer Detais are Required")
        elif self.peace_cake_price.get() == "Rs. 0.0" and self.cake_price.get() == "Rs. 0.0" and self.total_add.get() == "Rs. 0.0":
            messagebox.showerror("Error", "Products Not selected")
        else:
            self.welcome_bill()

            # ====kg cake bill generate======
            if self.plaincake.get() != 0:
                self.txtarea.insert(END, f"\n Plaincake\t\t{self.plaincake.get()}\t{self.plaincake_price}\t\t{self.plain}")
            if self.plumcake.get() != 0:
                self.txtarea.insert(END,f"\n plumcake\t\t{self.plumcake.get()}\t{self.plumcake_price}\t\t{self.plum}")
            if self.birthdaycake.get() != 0:
                self.txtarea.insert(END,f"\n birthday_cake\t\t{self.birthdaycake.get()}\t{self.birthdaycake_price}\t\t{self.b_c}")
            if self.blackforest.get() != 0:
                self.txtarea.insert(END, f"\n blackforst\t\t{self.blackforest.get()}\t{self.blackforest_price}\t\t{self.bf_c}")
            if self.creamcake.get() != 0:
                self.txtarea.insert(END, f"\n cream_cake\t\t{self.creamcake.get()}\t{self.creamcake_price}\t\t{self.c_c}")
            if self.fruitecake.get() != 0:
                self.txtarea.insert(END, f"\n Fruit_cake\t\t{self.fruitecake.get()}\t{self.fruitecake_price}\t\t{self.f_c}")

            # =========chips bill generate======
            if self.browny_peace.get() != 0:
                self.txtarea.insert(END, f"\n browny_peace\t\t{self.browny_peace.get()}\t{self.browny_peace_price}\t\t{self.j_s_p}")
            if self.plain_peace.get() != 0:
                self.txtarea.insert(END, f"\n plain_peace\t\t{self.plain_peace.get()}\t{self.plain_peace_price}\t\t{self.j_t_p}")
            if self.plum_peace.get() != 0:
                self.txtarea.insert(END,f"\n Plum_peace\t\t{self.plum_peace.get()}\t{self.plum_peace_price}\t\t{self.j_c_p}")
            if self.cream_peace.get() != 0:
                self.txtarea.insert(END, f"\n Cream_peace\t\t{self.cream_peace.get()}\t{self.cream_peace_price}\t\t{self.j_sv_p}")
            if self.BF_peace.get() != 0:
                self.txtarea.insert(END, f"\n blackforest_peace\t\t{self.BF_peace.get()}\t{self.BF_peace_price}\t\t{self.j_d_p}")
            if self.fruitecake_peace.get() != 0:
                self.txtarea.insert(END, f"\n fruite_peace\t\t{self.fruitecake_peace.get()}\t{self.fruitecake_peace_price}\t\t{self.j_m_p}")

            # =========chocolate bill generate=====
            if self.Addval.get() != 0:
                self.txtarea.insert(END, f"\n {self.Addition.get()}\t\t{self.Addval.get()}\t{self.Addval_price.get()}\t\t{self.Addval_price_total}")

            self.txtarea.insert(END, f"\n-----------------------------------------------")
            self.txtarea.insert(END, f"\n TOTAL BILL\t\t\tRs. {str(self.Total_bill)}")
            self.txtarea.insert(END, f"\n-----------------------------------------------")
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the Bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open(f"C:\\cakeshop\\{self.Date}"+"-" + str(self.bill.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill No :{self.bill.get()} Saved Succeddfully")
        else:
            return

    def find_bill(self):
        present = "no"
        for i in os.listdir("C:\\cakeshop\\cakeshop/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"C:\\cakeshop\\cakeshop/{i}", "r")
                self.txtarea.delete('1.0', END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill Number")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you want to clear?")
        if op > 0:
            self.plumcake.set(0)
            self.plaincake.set(0)
            self.birthdaycake.set(0)
            self.blackforest.set(0)
            self.creamcake.set(0)
            self.fruitecake.set(0)

            # =====chips=====
            self.browny_peace.set(0)
            self.plain_peace.set(0)
            self.plum_peace.set(0)
            self.cream_peace.set(0)
            self.BF_peace.set(0)
            self.fruitecake_peace.set(0)

            # =====Chocolate====
            self.Addition.set("")
            self.Addval.set(0)
            self.Addval_price.set(0)


            # =====Total Price=====
            self.cake_price.set("")
            self.peace_cake_price.set("")
            self.total_add.set("")

            # =======Tax price======
            self.cake_tax.set("")
            self.peace_tax.set("")
            self.chocolate_tax.set("")

            # ====name of customer=====
            self.c_name.set("")
            self.c_phon.set("")
            self.bill.set("")
            a = random.randint(1, 1000)
            self.bill.set(str(a))
            self.search_bill.set("")
            self.welcome_bill()

    def Exit_app(self):
        op = messagebox.askyesno("Exit", "Do you want to exit?")
        if op > 0:
            self.root.destroy()
    def print_bill(self):
        os.startfile("C:\\cakeshop\\cakeshop" + str(self.bill.get()) + ".txt", "print")

obj = Bill_App(root)
root.configure(bg="#87CEEB")
root.mainloop()
