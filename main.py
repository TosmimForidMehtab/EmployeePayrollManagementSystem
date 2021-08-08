from tkinter import *
from tkinter import messagebox, ttk
import pymysql
import time
import os
import tempfile


class EmployeeSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("EmployeePayrollManagementSystem | Dev--Tosmim")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        title = Label(
            self.root, text="EmployeePayrollManagementSystem", font=("times new roman", 30, "bold"),
            bg="#262626", fg="white", anchor="w", padx=10).place(x=0, y=0, relwidth=1)
        lbl_show_emp = Button(self.root, text="All Employees", command=self.employee_frame,
                              font=("times new roman", 13,), bg="green",
                              fg="white").place(
            x=1000,
            y=12,
            height=27)
        # Frame1
        # Variables
        self.var_emp_id = StringVar()
        self.var_emp_des = StringVar()
        self.var_emp_doj = StringVar()
        self.var_emp_name = StringVar()
        self.var_emp_dob = StringVar()
        self.var_emp_age = StringVar()
        self.var_emp_exp = StringVar()
        self.var_emp_gen = StringVar()
        self.var_emp_pid = StringVar()
        self.var_emp_email = StringVar()
        self.var_emp_cont = StringVar()
        # self.var_emp_add = StringVar()
        Frame1 = Frame(self.root, bd=5, relief=RIDGE, bg="#EFEBE2")
        Frame1.place(x=10, y=70, width=750, height=600)
        title2 = Label(
            Frame1, text="Employee Details", font=("times new roman", 20,), bg="#800000", fg="white",
            anchor="w", padx=10).place(x=0, y=0, relwidth=1)
        # Row1
        lbl_id = Label(Frame1, text="Employee ID", font=("times new roman", 15,),
                       bg="#A52A2A", fg="white").place(
            x=10,
            y=70)
        self.txt_id = Entry(Frame1, font=("times new roman", 15,), textvariable=self.var_emp_id, bg="#5C5C5C",
                            fg="white")
        self.txt_id.place(x=138, y=70.88, width=200)
        lbl_search = Button(Frame1, text="Search", command=self.search, font=("times new roman", 15,), bg="#808000",
                            fg="white").place(
            x=350,
            y=70,
            relheight=0.045)
        # Row2
        lbl_des = Label(
            Frame1, text="Employee Designation", font=("times new roman", 15,), bg="#A52A2A",
            fg="white").place(x=10, y=120 + 30)
        txt_des = Entry(Frame1, font=("times new roman", 15,), textvariable=self.var_emp_des, bg="#5C5C5C",
                        fg="white").place(
            x=210, y=122 + 30,
            width=200)

        lbl_doj = Label(Frame1, text="D.O.J", font=("times new roman", 15,), bg="#A52A2A", fg="white").place(
            x=450,
            y=120 + 30)
        txt_doj = Entry(Frame1, font=("times new roman", 15,), textvariable=self.var_emp_doj, bg="#5C5C5C",
                        fg="white").place(
            x=523, y=122 + 30,
            width=170)

        # Row3
        lbl_name = Label(Frame1, text="Name", font=("times new roman", 15,), bg="#A52A2A", fg="white").place(
            x=10,
            y=170 + 30)
        txt_name = Entry(Frame1, font=("times new roman", 15,), textvariable=self.var_emp_name, bg="#5C5C5C",
                         fg="white").place(
            x=80, y=171.5 + 30,
            width=330)

        lbl_dob = Label(Frame1, text="D.O.B", font=("times new roman", 15,), bg="#A52A2A", fg="white").place(
            x=450,
            y=170 + 30)
        txt_dob = Entry(Frame1, font=("times new roman", 15,), textvariable=self.var_emp_dob, bg="#5C5C5C",
                        fg="white").place(
            x=523.5, y=171.5 + 30,
            width=170)

        # Row4
        lbl_age = Label(Frame1, text="Age", font=("times new roman", 15,), bg="#A52A2A", fg="white").place(
            x=10,
            y=220 + 60)
        txt_age = Entry(Frame1, font=("times new roman", 15,), textvariable=self.var_emp_age, bg="#5C5C5C",
                        fg="white").place(
            x=65, y=220.5 + 60,
            width=345)

        lbl_exp = Label(
            Frame1, text="Experience(in Yrs)", font=("times new roman", 15,), bg="#A52A2A",
            fg="white").place(x=450, y=220 + 60)
        txt_exp = Entry(Frame1, font=("times new roman", 15,), textvariable=self.var_emp_exp, bg="#5C5C5C",
                        fg="white").place(
            x=627, y=220.5 + 60,
            width=90)

        # Row5
        lbl_gen = Label(Frame1, text="Gender", font=("times new roman", 15,), bg="#A52A2A", fg="white").place(
            x=10,
            y=270 +
              60)
        txt_gen = Entry(Frame1, font=("times new roman", 15,), textvariable=self.var_emp_gen, bg="#5C5C5C",
                        fg="white").place(
            x=90, y=271.5 + 60,
            width=200)

        lbl_pr_id = Label(Frame1, text="Proof ID", font=("times new roman", 15,), bg="#A52A2A", fg="white").place(
            x=330,
            y=270 + 60)
        txt_pr_id = Entry(Frame1, font=("times new roman", 15,), bg="#5C5C5C", textvariable=self.var_emp_pid,
                          fg="white").place(
            x=430, y=271.5 + 60,
            width=300)

        # Row6
        lbl_mail = Label(Frame1, text="Email", font=("times new roman", 15,), bg="#A52A2A", fg="white").place(
            x=10,
            y=320 +
              100)
        txt_mail = Entry(Frame1, font=("times new roman", 15,), textvariable=self.var_emp_email, bg="#5C5C5C",
                         fg="white").place(
            x=80, y=321.5 + 100,
            width=200)

        lbl_no = Label(Frame1, text="Contact Number", font=("times new roman", 15,), bg="#A52A2A", fg="white").place(
            x=330, y=320 + 100)
        txt_no = Entry(Frame1, font=("times new roman", 15,), textvariable=self.var_emp_cont, bg="#5C5C5C",
                       fg="white").place(
            x=485, y=321.5 + 100,
            width=250)

        # Row7
        lbl_add = Label(Frame1, text="Address", font=("times new roman", 15,), bg="#A52A2A", fg="white").place(
            x=10,
            y=370
              + 102)

        self.var_emp_add = Text(Frame1, font=("times new roman", 15,), bg="#5C5C5C",
                                fg="black")
        self.var_emp_add.place(x=100, y=371.5 + 100,
                               width=600, height=100)

        # Frame2
        # Variables
        self.var_sal_mon = StringVar()
        self.var_sal_yr = StringVar()
        self.var_sal_bsal = StringVar()
        self.var_sal_conv = StringVar()
        self.var_sal_tdays = StringVar()
        self.var_sal_abs = StringVar()
        self.var_sal_med = StringVar()
        self.var_sal_pfund = StringVar()
        self.var_sal_netsal = StringVar()

        Frame2 = Frame(self.root, bd=5, relief=RIDGE, bg="#EFEBE2")
        Frame2.place(x=770, y=70, width=500, height=300)
        title3 = Label(
            Frame2, text="Employee Salary Details", font=("times new roman", 20,), bg="#800000", fg="white",
            anchor="w", padx=10).place(x=0, y=0, relwidth=1)
        # Row1
        lbl_month = Label(Frame2, text="Month", font=("times new roman", 13,), bg="#A52A2A", fg="white").place(
            x=10,
            y=60 - 5)
        txt_month = Entry(Frame2, font=("times new roman", 15,), textvariable=self.var_sal_mon, bg="#5C5C5C",
                          fg="white").place(x=80, y=60 - 5, width=100)
        lbl_year = Label(Frame2, text="Year", font=("times new roman", 13,), bg="#A52A2A", fg="white").place(
            x=270,
            y=60 - 5)
        txt_year = Entry(Frame2, font=("times new roman", 15,), textvariable=self.var_sal_yr, bg="#5C5C5C",
                         fg="white").place(x=330, y=60 - 5, width=90)

        # Row2
        lbl_bsal = Label(Frame2, text="Basic Salary", font=("times new roman", 13,), bg="#A52A2A", fg="white").place(
            x=10, y=110 - 10)
        txt_bsal = Entry(Frame2, font=("times new roman", 15,), textvariable=self.var_sal_bsal, bg="#5C5C5C",
                         fg="white").place(x=120, y=110 - 10, width=90)

        lbl_con = Label(Frame2, text="Convenience", font=("times new roman", 13,), bg="#A52A2A", fg="white").place(
            x=270, y=110 - 10)
        txt_con = Entry(Frame2, font=("times new roman", 15,), textvariable=self.var_sal_conv, bg="#5C5C5C",
                        fg="white").place(x=385, y=110 - 10, width=100)

        # Row3
        lbl_tday = Label(Frame2, text="Total Days", font=("times new roman", 13,), bg="#A52A2A", fg="white").place(
            x=10,
            y=160 - 15)
        txt_tday = Entry(Frame2, font=("times new roman", 15,), textvariable=self.var_sal_tdays, bg="#5C5C5C",
                         fg="white").place(x=110, y=160 - 15, width=100)

        lbl_abs = Label(Frame2, text="Absents", font=("times new roman", 13,), bg="#A52A2A", fg="white").place(
            x=270,
            y=160 - 15)
        txt_abs = Entry(Frame2, font=("times new roman", 15,), textvariable=self.var_sal_abs, bg="#5C5C5C",
                        fg="white").place(x=347, y=160 - 15, width=100)

        # Row4
        lbl_med = Label(Frame2, text="Medical", font=("times new roman", 13,), bg="#A52A2A", fg="white").place(
            x=10,
            y=210 - 20)
        txt_med = Entry(Frame2, font=("times new roman", 15,), textvariable=self.var_sal_med, bg="#5C5C5C",
                        fg="white").place(x=95, y=210 - 20, width=90)

        lbl_pfund = Label(Frame2, text="Provident Fund", font=("times new roman", 13,), bg="#A52A2A", fg="white").place(
            x=230, y=210 - 20)
        txt_pfund = Entry(Frame2, font=("times new roman", 15,), textvariable=self.var_sal_pfund, bg="#5C5C5C",
                          fg="white").place(
            x=360, y=210 - 20,
            width=120)

        # Row5
        lbl_nsal = Label(Frame2, text="Net Salary", font=("times new roman", 13,), bg="#A52A2A", fg="white").place(
            x=10,
            y=260 - 25)
        txt_nsal = Entry(Frame2, font=("times new roman", 15,), textvariable=self.var_sal_netsal, bg="#5C5C5C",
                         fg="white").place(x=110, y=260 - 25, width=90)

        lbl_calc = Button(Frame2, text="Calculate", font=("times new roman", 15,), command=self.calculate, bg="orange",
                          fg="white").place(
            x=230,
            y=255 - 25,
            height=27)
        self.lbl_save = Button(Frame2, text="Save", command=self.add, font=("times new roman", 15), bg="green",
                               fg="white")
        self.lbl_save.place(
            x=350,
            y=255 - 25,
            height=27)
        lbl_clr = Button(Frame2, text="Clear", command=self.clear, font=("times new roman", 15), bg="violet",
                         fg="white").place(
            x=430, y=255 - 25,
            height=27)

        self.lbl_upd = Button(Frame2, text="Update", state=DISABLED, font=("times new roman", 15), command=self.update,
                              bg="blue",
                              fg="white")
        self.lbl_upd.place(
            x=230,
            y=260,
            height=27, width=92)
        self.lbl_del = Button(Frame2, text="Delete", state=DISABLED, command=self.delete, font=("times new roman", 15),
                              bg="red",
                              fg="white")
        self.lbl_del.place(
            x=350,
            y=260,
            height=27, width=141)
        # Frame3
        Frame3 = Frame(self.root, bd=5, relief=RIDGE, bg="#EFEBE2")
        Frame3.place(x=770, y=380, width=500, height=290)

        # Calculator Frame
        self.var_txt = StringVar()
        self.var_op = ''

        def btn_clc(num):
            self.var_op = self.var_op + str(num)
            self.var_txt.set(self.var_op)

        def result():
            res = str(eval(self.var_op))
            self.var_txt.set(res)
            self.var_op = ''

        def clr_cal():
            self.var_txt.set('')
            self.var_op = ''

        Cal_frame = Frame(Frame3, bg="#ffa64d", relief=RIDGE)
        Cal_frame.place(x=5, y=5, width=219, height=268.5)
        txt_result = Entry(Cal_frame, bg="lightblue", textvariable=self.var_txt, font=("times new roman", 25, "bold"),
                           justify=RIGHT)
        txt_result.place(x=0, y=0, relwidth=1, height=50)
        # Row1
        btn_9 = Button(Cal_frame, text="9", command=lambda: btn_clc(9), bg="black", fg="white",
                       font=("times new roman", 12, "bold")).place(
            x=0,
            y=30 + 30,
            w=53,
            h=40)
        btn_8 = Button(Cal_frame, text="8", command=lambda: btn_clc(8), bg="black", fg="white",
                       font=("times new roman", 12, "bold")).place(
            x=55,
            y=30 + 30,
            w=53,
            h=30 + 10)
        btn_7 = Button(Cal_frame, text="7", command=lambda: btn_clc(7), bg="black", fg="white",
                       font=("times new roman", 12, "bold")).place(
            x=110,
            y=30 + 30,
            w=53,
            h=30 + 10)
        btn_pl = Button(Cal_frame, text="+", command=lambda: btn_clc('+'), bg="black", fg="white",
                        font=("times new roman", 12, "bold")).place(
            x=165,
            y=30 + 30,
            w=53,
            h=30 + 10)
        # Row 2
        btn_4 = Button(Cal_frame, text="4", command=lambda: btn_clc(4), bg="black", fg="white",
                       font=("times new roman", 12, "bold")).place(
            x=0,
            y=62 + 40,
            w=53,
            h=30 + 10)
        btn_5 = Button(Cal_frame, text="5", command=lambda: btn_clc(5), bg="black", fg="white",
                       font=("times new roman", 12, "bold")).place(
            x=0 + 55, y=62 + 40, w=53, h=30 + 10)
        btn_6 = Button(Cal_frame, text="6", bg="black", command=lambda: btn_clc(6), fg="white",
                       font=("times new roman", 12, "bold")).place(
            x=55 + 55, y=62 + 40, w=53, h=30 + 10)
        btn_min = Button(Cal_frame, text="-", bg="black", command=lambda: btn_clc('-'), fg="white",
                         font=("times new roman", 12, "bold")).place(
            x=55 + 55 + 55, y=62 + 40, w=53, h=30 + 10)

        # Row3
        btn_3 = Button(Cal_frame, text="3", bg="black", command=lambda: btn_clc(3), fg="white",
                       font=("times new roman", 12, "bold")).place(
            x=0,
            y=94 + 50,
            w=53,
            h=30 + 10)
        btn_2 = Button(Cal_frame, text="2", bg="black", command=lambda: btn_clc(2), fg="white",
                       font=("times new roman", 12, "bold")).place(
            x=0 + 55, y=94 + 50, w=53, h=30 + 10)
        btn_1 = Button(Cal_frame, text="1", bg="black", fg="white", command=lambda: btn_clc(1),
                       font=("times new roman", 12, "bold")).place(
            x=55 + 55, y=94 + 50, w=53, h=30 + 10)
        btn_mul = Button(Cal_frame, text="*", command=lambda: btn_clc('*'), bg="black", fg="white",
                         font=("times new roman", 12, "bold")).place(
            x=55 + 55 + 55, y=94 + 50, w=53, h=30 + 10)

        # Row4
        btn_pnt = Button(Cal_frame, text=".", command=lambda: btn_clc('.'), bg="black", fg="white",
                         font=("times new roman", 12, "bold")).place(
            x=0,
            y=126 + 60,
            w=53,
            h=30 + 10)
        btn_zero = Button(Cal_frame, text="0", bg="black", command=lambda: btn_clc(0), fg="white",
                          font=("times new roman", 12, "bold")).place(
            x=0 + 55, y=126 + 60, w=53, h=30 + 10)
        btn_eq = Button(Cal_frame, text="=", bg="black", command=lambda: result(), fg="white",
                        font=("times new roman", 12, "bold")).place(
            x=55 + 55, y=126 + 60, w=53, h=30 + 10)
        btn_div = Button(Cal_frame, text="/", command=lambda: btn_clc('/'), bg="black", fg="white",
                         font=("times new roman", 12, "bold")).place(
            x=55 + 55 + 55, y=126 + 60, w=53, h=30 + 10)
        # Row5
        btn_zero = Button(Cal_frame, text="Clear", bg="black", command=lambda: clr_cal(), fg="white",
                          font=("times new roman", 12, "bold")).place(x=0, y=126 + 60 + 45, w=220, h=30)

        # ======Salary Frame======
        sal_frame = Frame(Frame3, Frame3, bg="lightyellow", relief=RIDGE)
        sal_frame.place(x=230, y=5, width=257, height=268.5)
        title_sal = Label(
            sal_frame, text="Salary Receipt", font=("times new roman", 20,), bg="#800000", fg="white",
            anchor="w", padx=10).place(x=0, y=0, relwidth=1)

        sal_frame2 = Frame(sal_frame, bg="white", bd=2, relief=RIDGE)
        sal_frame2.place(x=0, y=30, relwidth=1, height=200)

        self.sample = f"""          Company Name:XYZ\n          Address:Xyz, Floor 4
-------------------------------------
Employee ID\t: 
Salary of\t: MM-YYYY
Generated On\t: DD-MM-YYYY
-------------------------------------
Total Days\t: DD
Total Present\t: DD
Total Absent\t: DD
Convence\t: Rs.______
Medical\t: Rs.______
PF\t": Rs.______
Basic Salary\t: Rs.______
Net Salary\t: Rs._________

***************************
This is a computer 
generated slip
No signature required
"""
        scroll_y = Scrollbar(sal_frame2, orient=VERTICAL)
        scroll_y.pack(fill=Y, side=RIGHT)

        self.txt_salary_receipt = Text(sal_frame2, font=("times new roman", 12), bg="lightgreen",
                                       yscrollcommand=scroll_y.set)
        self.txt_salary_receipt.pack(fill=BOTH, expand=1)

        scroll_y.config(command=self.txt_salary_receipt.yview)
        self.txt_salary_receipt.insert(END, self.sample)

        self.btn_print = Button(sal_frame, text="Print", state=DISABLED, command=self.Print, font=("times new roman", 15,), bg="black",
                                fg="white")
        self.btn_print.place(
            x=120.5,
            y=230,
            height=30, width=100)

        self.check_connection()

    # ------------Functions Start----------
    def search(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", db="ems")
            cur = con.cursor()
            cur.execute("select * from emp_salary where e_id=%s", (self.var_emp_id.get()))
            row = cur.fetchone()
            # print(rows)
            if row == None:
                messagebox.showerror("ERROR", "Invalid Employee ID", parent=self.root)
            else:
                print(row)
                self.var_emp_id.set(row[0])
                self.var_emp_des.set(row[1])
                self.var_emp_name.set(row[2])
                self.var_emp_age.set(row[3])
                self.var_emp_gen.set(row[4])
                self.var_emp_email.set(row[5])
                self.var_emp_add.delete('1.0', END)
                self.var_emp_add.insert(END, row[6])
                self.var_emp_doj.set(row[7])
                self.var_emp_dob.set(row[8])
                self.var_emp_exp.set(row[9])
                self.var_emp_pid.set(row[10])
                self.var_emp_cont.set(row[11])
                self.var_sal_mon.set(row[12])
                self.var_sal_bsal.set(row[13])
                self.var_sal_tdays.set(row[14])
                self.var_sal_med.set(row[15])
                self.var_sal_netsal.set(row[16])
                self.var_sal_yr.set(row[17])
                self.var_sal_conv.set(row[18])
                self.var_sal_abs.set(row[19])
                self.var_sal_pfund.set(row[20])
                file = open("SalaryReceipt/" + str(row[21]), "r")
                self.txt_salary_receipt.delete("1.0", END)
                for i in file:
                    self.txt_salary_receipt.insert(END, i)
                file.close()
                self.lbl_save.config(state=DISABLED)
                self.lbl_upd.config(state=NORMAL)
                self.lbl_del.config(state=NORMAL)
                self.txt_id.config(state="readonly")
                self.btn_print.config(state=NORMAL)

        except Exception as e:
            messagebox.showerror("ERROR", f"Error due to {str(e)}")

    def clear(self):
        self.lbl_save.config(state=NORMAL)
        self.lbl_upd.config(state=DISABLED)
        self.lbl_del.config(state=DISABLED)
        self.btn_print.config(state=DISABLED)
        self.txt_id.config(state=NORMAL)
        self.var_emp_id.set("")
        self.var_emp_des.set("")
        self.var_emp_name.set("")
        self.var_emp_age.set("")
        self.var_emp_gen.set("")
        self.var_emp_email.set("")
        self.var_emp_add.delete('1.0', END)
        self.var_emp_doj.set("")
        self.var_emp_dob.set("")
        self.var_emp_exp.set("")
        self.var_emp_pid.set("")
        self.var_emp_cont.set("")
        self.var_sal_mon.set("")
        self.var_sal_bsal.set("")
        self.var_sal_tdays.set("")
        self.var_sal_med.set("")
        self.var_sal_netsal.set("")
        self.var_sal_yr.set("")
        self.var_sal_conv.set("")
        self.var_sal_abs.set("")
        self.var_sal_pfund.set("")
        self.txt_salary_receipt.delete("1.0", END)
        self.txt_salary_receipt.insert(END, self.sample)

    def delete(self):
        if self.var_emp_id.get() == "":
            messagebox.showerror("ERROR", "Employee ID required")
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", db="ems")
                cur = con.cursor()
                cur.execute("select * from emp_salary where e_id=%s", (self.var_emp_id.get()))
                row = cur.fetchone()
                # print(rows)
                if row == None:
                    messagebox.showerror("ERROR", "Invalid Employee ID", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?")
                    if op:
                        cur.execute("delete from emp_salary where e_id=%s", (self.var_emp_id.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("SUCCESS", "Employee Record deleted", parent=self.root)
                        self.clear()
            except Exception as e:
                messagebox.showerror("ERROR", f"Error due to {str(e)}")

    def add(self):
        if self.var_emp_id.get() == "" or self.var_emp_name == "":
            messagebox.showerror("ERROR", "Details are not sufficient")
        else:

            try:
                con = pymysql.connect(host="localhost", user="root", password="", db="ems")
                cur = con.cursor()
                cur.execute("select * from emp_salary where e_id=%s", (self.var_emp_id.get()))
                row = cur.fetchone()
                # print(rows)
                if row != None:
                    messagebox.showerror("ERROR", "Employee ID already exists", parent=self.root)
                else:
                    cur.execute(
                        "insert into emp_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            self.var_emp_id.get(),
                            self.var_emp_des.get(),
                            self.var_emp_name.get(),
                            self.var_emp_age.get(),
                            self.var_emp_gen.get(),
                            self.var_emp_email.get(),
                            self.var_emp_add.get('1.0', END),
                            self.var_emp_doj.get(),
                            self.var_emp_dob.get(),
                            self.var_emp_exp.get(),
                            self.var_emp_pid.get(),
                            self.var_emp_cont.get(),
                            self.var_sal_mon.get(),
                            self.var_sal_bsal.get(),
                            self.var_sal_tdays.get(),
                            self.var_sal_med.get(),
                            self.var_sal_netsal.get(),
                            self.var_sal_yr.get(),
                            self.var_sal_conv.get(),
                            self.var_sal_abs.get(),
                            self.var_sal_pfund.get(),
                            self.var_emp_id.get() + ".txt"
                        )
                    )
                    con.commit()
                    con.close()
                    file = open("SalaryReceipt/" + str(self.var_emp_id.get()) + ".txt", "w")
                    file.write(self.txt_salary_receipt.get("1.0", END))
                    file.close()
                    messagebox.showinfo("SUCCESS", "Record added successfully")
                    self.btn_print.config(state=NORMAL)
            except Exception as e:
                messagebox.showerror("ERROR", f"Error due to {str(e)}")

    def update(self):
        if self.var_emp_id.get() == "" or self.var_emp_name == "":
            messagebox.showerror("ERROR", "Details are not sufficient")
        else:

            try:
                con = pymysql.connect(host="localhost", user="root", password="", db="ems")
                cur = con.cursor()
                cur.execute("select * from emp_salary where e_id=%s", (self.var_emp_id.get()))
                row = cur.fetchone()
                # print(rows)
                if row == None:
                    messagebox.showerror("ERROR", "Invalid ID... Try Again", parent=self.root)
                else:
                    cur.execute(
                        "UPDATE `emp_salary` SET `e_designation`=%s,`e_name`=%s,`e_age`=%s,`e_gen`=%s,`e_email`=%s,`e_address`=%s,`edoj`=%s,`edob`=%s,`e_experience`=%s,`e_proofid`=%s,`e_contact`=%s,`sal_month`=%s,`sal_bsal`=%s,`sal_tdays`=%s,`sal_med`=%s,`sal_netsal`=%s,`sal_year`=%s,`sal_conv`=%s,`sal_abs`=%s,`sal_pfund`=%s,`sal_receipt`=%s WHERE `e_id`=%s",
                        (

                            self.var_emp_des.get(),
                            self.var_emp_name.get(),
                            self.var_emp_age.get(),
                            self.var_emp_gen.get(),
                            self.var_emp_email.get(),
                            self.var_emp_add.get('1.0', END),
                            self.var_emp_doj.get(),
                            self.var_emp_dob.get(),
                            self.var_emp_exp.get(),
                            self.var_emp_pid.get(),
                            self.var_emp_cont.get(),
                            self.var_sal_mon.get(),
                            self.var_sal_bsal.get(),
                            self.var_sal_tdays.get(),
                            self.var_sal_med.get(),
                            self.var_sal_netsal.get(),
                            self.var_sal_yr.get(),
                            self.var_sal_conv.get(),
                            self.var_sal_abs.get(),
                            self.var_sal_pfund.get(),
                            self.var_emp_id.get() + ".txt",
                            self.var_emp_id.get()
                        )
                    )
                    con.commit()
                    con.close()
                    file = open("SalaryReceipt/" + str(self.var_emp_id.get()) + ".txt", "w")
                    file.write(self.txt_salary_receipt.get("1.0", END))
                    file.close()
                    messagebox.showinfo("SUCCESS", "Record Updated successfully")
            except Exception as e:
                messagebox.showerror("ERROR", f"Error due to {str(e)}")

    def calculate(self):
        if self.var_sal_mon.get() == "" or self.var_sal_yr.get() == "" or self.var_sal_bsal == "" or self.var_sal_med == "":
            messagebox.showerror("ERROR", "All fields are required")
        else:
            per_day = int(self.var_sal_bsal.get()) / int(self.var_sal_tdays.get())
            work_day = int(self.var_sal_tdays.get()) - int(self.var_sal_abs.get())
            sal = per_day * work_day
            deduct = int(self.var_sal_med.get()) + int(self.var_sal_pfund.get())
            addition = int(self.var_sal_conv.get())
            net_sal = sal - deduct + addition
            self.var_sal_netsal.set(str(round(net_sal, 2)))
            # =========Receipt Update=========
            new_sample = f"""          Company Name:XYZ\n          Address:Xyz, Floor 4
-------------------------------------
Employee ID\t: {self.var_emp_id.get()}
Salary of\t: {self.var_sal_mon.get()}-{self.var_sal_yr.get()}
Generated On\t: {str(time.strftime("%D-%m-%Y"))}
-------------------------------------
Total Days\t: {self.var_sal_tdays.get()}
Total Absent\t: {self.var_sal_abs.get()}
Total Present\t: {str(int(self.var_sal_tdays.get()) - int(self.var_sal_abs.get()))}
Convence\t: Rs.{self.var_sal_conv.get()}
Medical\t: Rs.{self.var_sal_med.get()}
PF\t: Rs.{self.var_sal_med.get()}
Basic Salary\t: Rs.{self.var_sal_bsal.get()}
Net Salary\t: Rs.{self.var_sal_netsal.get()}

***************************
This is a computer 
generated slip
No signature required
"""
            self.txt_salary_receipt.delete("1.0", END)
            self.txt_salary_receipt.insert(END, new_sample)

    def check_connection(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", db="ems")
            cur = con.cursor()
            cur.execute("select * from emp_salary")
            rows = cur.fetchall()
            print(rows)
        except Exception as e:
            messagebox.showerror("ERROR", f"Error due to {str(e)}")

    def show(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", db="ems")
            cur = con.cursor()
            cur.execute("select * from emp_salary")
            rows = cur.fetchall()
            self.employee_tree.delete(*self.employee_tree.get_children())
            for row in rows:
                self.employee_tree.insert("", END, values=row)
            con.close()
        except Exception as e:
            messagebox.showerror("ERROR", f"Error due to {str(e)}")

    def employee_frame(self):
        self.root2 = Toplevel(self.root)
        self.root2.title("All Employees | Dev--Tosmim")
        self.root2.geometry("1200x500+50+60")
        self.root2.config(bg="white")
        title = Label(
            self.root2, text="All Employee Details", font=("times new roman", 30, "bold"),
            bg="#262626", fg="white", anchor="w", padx=10).pack(side=TOP, fill=X)
        self.root2.focus_force()

        scrolly = Scrollbar(self.root2, orient=VERTICAL)
        scrollx = Scrollbar(self.root2, orient=HORIZONTAL)

        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        self.employee_tree = ttk.Treeview(self.root2, columns=(
            'e_id', 'e_designation', 'e_name', 'e_age', 'e_gen', 'e_email', 'e_address', 'edoj', 'edob', 'e_experience',
            'e_proofid', 'e_contact', 'sal_month', 'sal_bsal', 'sal_tdays', 'sal_med', 'sal_netsal', 'sal_year',
            'sal_conv',
            'sal_abs', 'sal_pfund', 'sal_receipt'), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        self.employee_tree.heading('e_id', text="E_ID")
        self.employee_tree.heading('e_designation', text="Designation")
        self.employee_tree.heading('e_name', text="Name")
        self.employee_tree.heading('e_age', text="Age")
        self.employee_tree.heading('e_gen', text="Gender")
        self.employee_tree.heading('e_email', text="Email")
        self.employee_tree.heading('e_address', text="Address")
        self.employee_tree.heading('edoj', text="DateofJoining")
        self.employee_tree.heading('edob', text="DateofBirth")
        self.employee_tree.heading('e_experience', text="Experience")
        self.employee_tree.heading('e_proofid', text="ProofID")
        self.employee_tree.heading('e_contact', text="ContactInfo")
        self.employee_tree.heading('sal_month', text="CurrentMonth")
        self.employee_tree.heading('sal_bsal', text="BasicSalary")
        self.employee_tree.heading('sal_tdays', text="TotalWorkingDays")
        self.employee_tree.heading('sal_med', text="Medical")
        self.employee_tree.heading('sal_netsal', text="NetSalary")
        self.employee_tree.heading('sal_year', text="CurrentMonth")
        self.employee_tree.heading('sal_conv', text="Convence")
        self.employee_tree.heading('sal_abs', text="Absent days")
        self.employee_tree.heading('sal_pfund', text="ProvidentFund")
        self.employee_tree.heading('sal_receipt', text="SalaryReceipt")
        self.employee_tree['show'] = 'headings'

        self.employee_tree.column('e_id', width=100)
        self.employee_tree.column('e_designation', width=100)
        self.employee_tree.column('e_name', width=100)
        self.employee_tree.column('e_age', width=100)
        self.employee_tree.column('e_gen', width=100)
        self.employee_tree.column('e_email', width=100)
        self.employee_tree.column('e_address', width=300)
        self.employee_tree.column('edoj', width=100)
        self.employee_tree.column('edob', width=100)
        self.employee_tree.column('e_experience', width=100)
        self.employee_tree.column('e_proofid', width=100)
        self.employee_tree.column('e_contact', width=100)
        self.employee_tree.column('sal_month', width=100)
        self.employee_tree.column('sal_bsal', width=100)
        self.employee_tree.column('sal_tdays', width=100)
        self.employee_tree.column('sal_med', width=100)
        self.employee_tree.column('sal_netsal', width=100)
        self.employee_tree.column('sal_year', width=100)
        self.employee_tree.column('sal_conv', width=100)
        self.employee_tree.column('sal_abs', width=100)
        self.employee_tree.column('sal_pfund', width=100)
        self.employee_tree.column('sal_receipt', width=100)
        scrollx.config(command=self.employee_tree.xview)
        scrolly.config(command=self.employee_tree.yview)
        self.employee_tree.pack(fill=BOTH, expand=1)
        self.show()
        self.root2.mainloop()

    def Print(self):
        file = tempfile.mktemp(".txt")
        open(file, 'w').write(self.txt_salary_receipt.get('1.0', END))
        os.startfile(file, 'print')


root = Tk()
obj = EmployeeSystem(root)
root.mainloop()
