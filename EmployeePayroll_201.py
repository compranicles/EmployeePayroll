import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector
import tkinter as tk
import tkinter.messagebox as mb
from tkinter.font import nametofont
import time
from tkinter.ttk import Style

def main():
    root = Tk()
    root.title("Employee Payroll Management System")
    root.geometry("1295x650+25+25")
    root.iconbitmap('employee.ico')
    root.resizable(width=False, height=False)

    def admin_modules(admin_user, adminname):
        admin = tk.Toplevel(root)
        admin.title("Employee Payroll Management System - Admin")
        positionR = int(admin.winfo_screenwidth() / 2 - 1200 / 2)
        admin.geometry("1200x600+{}+30".format(positionR))
        admin.iconbitmap('employee.ico')
        admin.resizable(width=False, height=False)
        admin.focus_set()
        root.withdraw()
        admin.configure(bg ='RoyalBlue1')
        

        def addEmp():
            addWin = tk.Toplevel(admin)
            addWin.title("EPMS - Admin - Add Employee")
            positionR = int(addWin.winfo_screenwidth() / 2 - 400 / 2)
            positionD = int(addWin.winfo_screenheight() / 2 - 300 / 2)
            addWin.geometry("400x300+{}+{}".format(positionR, positionD))
            addWin.resizable(width=False, height=False)
            addWin.focus_set()

            lNameLabel = Label(addWin, text="Last Name:", font=("Helvetica 12 bold"))
            lNameEntry = Entry(addWin, font=("Helvetica 14"))
            fNameLabel = Label(addWin, text="First Name:", font=("Helvetica 12 bold"))
            fNameEntry = Entry(addWin, font=("Helvetica 14"))
            deptLabel = Label(addWin, text="Department:", font=("Helvetica 12 bold"))
            deptEntry = Entry(addWin, font=("Helvetica 14"))
            desLabel = Label(addWin, text="Designation:", font=("Helvetica 12 bold"))
            desEntry = Entry(addWin, font=("Helvetica 14"))
            salLabel = Label(addWin, text="Salary:", font=("Helvetica 12 bold"))
            salEntry = Entry(addWin, font=("Helvetica 14"))
            lNameEntry.focus()

            def addClicked():
                lname = lNameEntry.get()
                fname = fNameEntry.get()
                dept = deptEntry.get()
                des = desEntry.get()
                sal = salEntry.get()
                username = lname.lower()+"123"
                username.replace(" ", "_")
                pwd = "password"

                if lname == '' or fname == '' or dept == '' or des == '' or  sal == '':
                    mb.showinfo('Add Status', 'All fields are required', parent=addWin)
                    addWin.focus_set()
                else:
                    cursor = connEmp.cursor()
                    sql = "INSERT INTO employees (last_name, first_name, department, designation, salary, username, pwd) "
                    sql += "VALUES('"+lname+"','"+fname+"','"+dept+"','"+des+"','"+sal+"','"+username+"', '"+pwd+"')"
                    cursor.execute(sql)
                    cursor.execute("commit")

                    info = 'Added Successfully \n\nUsername: '+username+'\nPassword: '+pwd
                    mb.showinfo('Add Status', info)

                    showEmp()

                    addWin.focus_set()
                    lNameEntry.delete(0, 'end')
                    fNameEntry.delete(0, 'end')
                    deptEntry.delete(0, 'end')
                    desEntry.delete(0,'end')
                    salEntry.delete(0,'end')

            def exitAdd():
                addWin.destroy()

            addNewButton = Button(addWin, text="Save", font=("helvetica 12 bold"), bg="royalblue2", height=1, width=10, command=(addClicked))
            addExitButton = Button(addWin, text="Exit", font=("helvetica 12 bold"), bg="red", fg="white", height=1, width=10, command=(exitAdd))
            lNameLabel.place(x=20, y=20)
            lNameEntry.place(x=150, y=20)
            fNameLabel.place(x=20, y=60)
            fNameEntry.place(x=150, y=60)
            deptLabel.place(x=20, y=100)
            deptEntry.place(x=150, y=100)
            desLabel.place(x=20, y=140)
            desEntry.place(x=150, y=140)
            salLabel.place(x=20, y=180)
            salEntry.place(x=150, y=180)
            addNewButton.place(x=40, y=250)
            addExitButton.place(x=250, y=250)

            addWin.mainloop()


        def editEmp():
            editWin = tk.Toplevel(admin)
            editWin.title("EPMS - Admin - Edit Employee")
            positionR = int(editWin.winfo_screenwidth() / 2 - 400 / 2)
            positionD = int(editWin.winfo_screenheight() / 2 - 300 / 2)
            editWin.geometry("400x300+{}+{}".format(positionR, positionD))
            editWin.resizable(width=False, height=False)
            editWin.focus_set()

            lNameLabel = Label(editWin, text="Last Name:", font=("Helvetica 12 bold"))
            lNameEntry = Entry(editWin, font=("Helvetica 14"))
            fNameLabel = Label(editWin, text="First Name:", font=("Helvetica 12 bold"))
            fNameEntry = Entry(editWin, font=("Helvetica 14"))
            deptLabel = Label(editWin, text="Department:", font=("Helvetica 12 bold"))
            deptEntry = Entry(editWin, font=("Helvetica 14"))
            desLabel = Label(editWin, text="Designation:", font=("Helvetica 12 bold"))
            desEntry = Entry(editWin, font=("Helvetica 14"))
            salLabel = Label(editWin, text="Salary:", font=("Helvetica 12 bold"))
            salEntry = Entry(editWin, font=("Helvetica 14"))

            def editClicked():
                id = editId
                lname = lNameEntry.get()
                fname = fNameEntry.get()
                dept = deptEntry.get()
                des = desEntry.get()
                sal = salEntry.get().replace('₱','').strip()

                if lname == '' or fname == '' or dept == '' or des == '' or  sal == '':
                    mb.showinfo('Edit Status', 'All fields are required', parent=editWin)
                    addWin.focus_set()
                else:
                    sql = "UPDATE employees SET last_name = '"+lname+"', first_name = '"+fname
                    sql += "', department = '"+dept+"', designation ='"+des+"', salary = '"+sal+"' WHERE id = '"+id+"' "
                    cursor.execute(sql)
                    cursor.execute("commit")

                    info = 'Modified Successfully'
                    mb.showinfo('Edit Status', info)

                    showEmp()
                    editWin.destroy()

            editNewButton = Button(editWin, text="Save", font=("helvetica 12 bold"), bg="royalblue2", height=1, width=10, command=editClicked)
            editExitButton = Button(editWin, text="Exit", font=("helvetica 12 bold"), bg="red", fg="white", height=1, width=10, command=editWin.destroy)
            lNameLabel.place(x=20, y=20)
            lNameEntry.place(x=150, y=20)
            fNameLabel.place(x=20, y=60)
            fNameEntry.place(x=150, y=60)
            deptLabel.place(x=20, y=100)
            deptEntry.place(x=150, y=100)
            desLabel.place(x=20, y=140)
            desEntry.place(x=150, y=140)
            salLabel.place(x=20, y=180)
            salEntry.place(x=150, y=180)
            editNewButton.place(x=40, y=250)
            editExitButton.place(x=250, y=250)

            editSelect = employeeTable.selection()
            itemValue = ()
            editId = ""
            for item in editSelect:
                itemValue = employeeTable.item(item, "values")

            if len(itemValue) == 0:
                mb.showerror('Edit Status', 'No Selected Employee', parent=editWin)
                editWin.destroy()
            else:
                editId = itemValue[0]
                print(editId)
                cursor = connEmp.cursor()
                sql = "SELECT * FROM employees WHERE id = '" + editId + "' "
                cursor.execute(sql)
                result = cursor.fetchall()
                print(result)
                lNameEntry.insert(0, result[0][1])
                fNameEntry.insert(0, result[0][2])
                deptEntry.insert(0, result[0][3])
                desEntry.insert(0, result[0][4])
                salEntry.insert(0, "₱ {:,.2f}".format(float(result[0][5])))

            editWin.mainloop()

        def delEmp():
            delWin = tk.Toplevel(admin)
            delWin.title("EPMS - Admin - Delete Employee")
            positionR = int(delWin.winfo_screenwidth() / 2 - 400 / 2)
            positionD = int(delWin.winfo_screenheight() / 2 - 400 / 2)
            delWin.geometry("400x400+{}+{}".format(positionR, positionD))
            delWin.resizable(width=False, height=False)
            delWin.focus_set()
            delLabel = Label(delWin, text="Do you really want to delete this Employee?", font=("Helvetica 12 bold"), fg="red")
            lNameLabel = Label(delWin, text="Last Name:", font=("Helvetica 12 bold"))
            lNameEntry = Entry(delWin, font=("Helvetica 14"))
            fNameLabel = Label(delWin, text="First Name:", font=("Helvetica 12 bold"))
            fNameEntry = Entry(delWin, font=("Helvetica 14"))
            deptLabel = Label(delWin, text="Department:", font=("Helvetica 12 bold"))
            deptEntry = Entry(delWin, font=("Helvetica 14"))
            desLabel = Label(delWin, text="Designation:", font=("Helvetica 12 bold"))
            desEntry = Entry(delWin, font=("Helvetica 14"))
            salLabel = Label(delWin, text="Salary:", font=("Helvetica 12 bold"))
            salEntry = Entry(delWin, font=("Helvetica 14"))

            def delClicked():
                id = delId
                sql = "DELETE FROM records WHERe id_e = '"+ delId+"' "
                cursor.execute(sql)
                cursor.execute("commit")

                sql = "DELETE FROM employees WHERE id = '"+ delId +"' "
                cursor.execute(sql)
                cursor.execute("commit")

                info = 'Deleted Successfully'
                mb.showinfo('Delete Status', info)

                showEmp()
                delWin.destroy()

            delNewButton = Button(delWin, text="Delete", font=("helvetica 12 bold"), bg="red", fg="white", height=1, width=10, command=delClicked)
            delExitButton = Button(delWin, text="Cancel", font=("helvetica 12 bold"), bg="royalblue2", height=1, width=10, command=delWin.destroy)
            delLabel.place(x=30, y=40)
            lNameLabel.place(x=20, y=100)
            lNameEntry.place(x=150, y=100)
            fNameLabel.place(x=20, y=140)
            fNameEntry.place(x=150, y=140)
            deptLabel.place(x=20, y=180)
            deptEntry.place(x=150, y=180)
            desLabel.place(x=20, y=220)
            desEntry.place(x=150, y=220)
            salLabel.place(x=20, y=260)
            salEntry.place(x=150, y=260)
            delNewButton.place(x=40, y=350)
            delExitButton.place(x=250, y=350)

            delSelect = employeeTable.selection()
            itemValue = ()
            delId = ""
            for item in delSelect:
                itemValue = employeeTable.item(item, "values")

            if len(itemValue) == 0:
                mb.showerror('Delete Status', 'No Selected Employee', parent=delWin)
                delWin.destroy()
            else:
                delId = itemValue[0]
                print(delId)
                cursor = connEmp.cursor()
                sql = "SELECT * FROM employees WHERE id = '" + delId + "' "
                cursor.execute(sql)
                result = cursor.fetchall()
                print(result)
                lNameEntry.insert(0, result[0][1])
                fNameEntry.insert(0, result[0][2])
                deptEntry.insert(0, result[0][3])
                desEntry.insert(0, result[0][4])
                salEntry.insert(0, "₱ {:,.2f}".format(float(result[0][5])))
                lNameEntry['state'] = "readonly"
                fNameEntry['state'] = "readonly"
                deptEntry['state'] = "readonly"
                desEntry['state'] = "readonly"
                salEntry['state'] = "readonly"

            delWin.mainloop()

        def payEmp():
            payWin = tk.Toplevel(admin)
            payWin.title("EPMS - Admin - Employee Payroll")
            positionR = int(payWin.winfo_screenwidth() / 2 - 1120 / 2)
            positionD = int(payWin.winfo_screenheight() / 2 - 600 / 2)
            payWin.geometry("1120x600+{}+{}".format(positionR, positionD))
            payWin.resizable(width=False, height=False)
            payWin.focus_set()

            payLabel = Label(payWin, text="Monthly Payroll", font=("Helvetica 16 bold"))
            eNumLabel = Label(payWin, text="Employee Number:", font=("Helvetica 12"))
            eNumEntry = Entry(payWin, font=("Helvetica 12"))
            lNameLabel = Label(payWin, text="Last Name:", font=("Helvetica 12"))
            lNameEntry = Entry(payWin, font=("Helvetica 12"))
            fNameLabel = Label(payWin, text="First Name:", font=("Helvetica 12"))
            fNameEntry = Entry(payWin, font=("Helvetica 12"))
            deptLabel = Label(payWin, text="Department:", font=("Helvetica 12"))
            deptEntry = Entry(payWin, font=("Helvetica 12"))
            desLabel = Label(payWin, text="Designation:", font=("Helvetica 12"))
            desEntry = Entry(payWin, font=("Helvetica 12"))
            salLabel = Label(payWin, text="Salary:", font=("Helvetica 12"))
            salEntry = Entry(payWin, font=("Helvetica 12"))
            dateLabel = Label(payWin, text="For the month of: ", font=("Helvetica 12 bold"))
            incomeLabel = Label(payWin, text="Earnings:", font=("Helvetica 14 bold"))
            rateLabel = Label(payWin, text="Rate per Day:", font=("Helvetica 12 bold"))
            rateEntry = Entry(payWin, font=("Helvetica 12"))
            daysLabel = Label(payWin, text="Days:", font=("Helvetica 12 bold"))
            daysEntry = Entry(payWin, font=("Helvetica 12"))
            alloLabel = Label(payWin, text="Allowances:", font=("Helvetica 12 bold"))
            alloEntry = Entry(payWin, font=("Helvetica 12"))
            gSalLabel = Label(payWin, text="Total Earnings:", font=("Helvetica 12 bold"))
            gSalEntry = Entry(payWin, font=("Helvetica 12"),state="readonly")
            deductLabel = Label(payWin, text="Deductions:", font=("Helvetica 14 bold"))
            sssLabel = Label(payWin, text="SSS:", font=("Helvetica 12 bold"))
            sssEntry = Entry(payWin, font=("Helvetica 12"))
            philLabel = Label(payWin, text="PhilHealth:", font=("Helvetica 12 bold"))
            philEntry = Entry(payWin, font=("Helvetica 12"))
            otLabel = Label(payWin, text="Others:", font=("Helvetica 12 bold"))
            otEntry = Entry(payWin, font=("Helvetica 12"))
            tDedLabel = Label(payWin, text="Total Deductions:", font=("Helvetica 12 bold"))
            tDedEntry = Entry(payWin, font=("Helvetica 12"),state="readonly")
            nPayLabel = Label(payWin, text="Net Salary:", font=("Helvetica 12 bold"))
            nPayEntry = Entry(payWin, font=("Helvetica 12"), state="readonly")

            monthCombo = ttk.Combobox(payWin, values=["MONTH", "January", "February", "March", "April", "May", "June",
                        "July", "August", "September", "October", "November", "December"], state="readonly", width= 11,font=("Helvetica", "11"))
            yearCombo = ttk.Combobox(payWin, values=["YEAR", "2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027",
                                                    "2028", "2029", "2030"], state="readonly", width= 7, font=("Helvetica", "11"))

            def calculate():
                ratePerDay = rateEntry.get()
                dayVal = daysEntry.get()
                allowance = alloEntry.get()
                sss = sssEntry.get()
                pH = philEntry.get()
                others = otEntry.get()

                if ratePerDay == '' or dayVal == '' or sss == '' or pH == '' or others == '':
                    mb.showinfo('Calculate Status', 'Fill all Blanks', parent=payWin)
                    payWin.focus_set()

                else:
                    dayVal = float(dayVal)
                    allowance = float(allowance.replace('₱', ''))
                    sss = float(sss.replace('₱', ''))
                    pH = float(pH.replace('₱', ''))
                    others = float(others.replace('₱', ''))
                    grossSal = rate * dayVal + allowance
                    deduct = sss + pH + others
                    netSal = float(grossSal - deduct)

                    gSalEntry['state'] = NORMAL
                    tDedEntry['state'] = NORMAL
                    nPayEntry['state'] = NORMAL

                    gSalEntry.delete(0, 'end')
                    tDedEntry.delete(0, 'end')
                    nPayEntry.delete(0, 'end')

                    gSalEntry.insert(0, "₱ {:,.2f}".format(grossSal))
                    tDedEntry.insert(0, "₱ {:,.2f}".format(deduct))
                    nPayEntry.insert(0, "₱ {:,.2f}".format(netSal))

                    gSalEntry['state'] = "readonly"
                    tDedEntry['state'] = "readonly"
                    nPayEntry['state'] = "readonly"

                    saveButton['state'] = NORMAL

            def save():
                cursor = connEmp.cursor()
                sql = "SELECT * FROM records WHERE id_e = '"+str(eNumEntry.get())+"' "
                cursor.execute(sql)
                result = cursor.fetchall()

                checkDate = monthCombo.get() +' '+yearCombo.get()
                
                flag = 0
                for i in result:
                    if i[3] == checkDate:
                        flag = 1

                if (monthCombo.get()=="MONTH" or yearCombo.get()=="YEAR"):
                    mb.showinfo('Save Status', 'Specify the Pay Period', parent=payWin)
                    payWin.focus_set()
                elif flag == 1:
                    mb.showinfo('Save Status', 'Employee has been paid on that month', parent=payWin)
                    payWin.focus_set()
                else:
                    emId = str(eNumEntry.get())
                    ratePerDay = rateEntry.get().replace(',','').replace('₱', '')
                    dayVal = daysEntry.get()
                    allowance = alloEntry.get().replace(',','').replace('₱', '')
                    sss = sssEntry.get().replace('₱', '')
                    pH = philEntry.get().replace('₱', '')
                    others = otEntry.get().replace('₱', '').replace(',', '')
                    grossSal = gSalEntry.get().replace(',', '').replace('₱', '')
                    deduct = tDedEntry.get().replace(',', '').replace('₱', '')
                    netSal = nPayEntry.get().replace(',', '').replace('₱', '')
                    payDate = monthCombo.get() + " " + yearCombo.get()
                    dateSaved = str(time.strftime("%B %d, %Y"))

                    cursor = connEmp.cursor()
                    sql = "INSERT INTO records (id_e, date_save, date_payroll, rate_per_day, days_worked, allowance, gross_salary, "
                    sql += "sss, philhealth, other_deduct, total_deduct, net_salary) "
                    sql += "VALUES ('"+emId+"','"+dateSaved+"','"+payDate+"','"+ratePerDay+"', '"+allowance+"', "
                    sql += "'"+dayVal+"','"+grossSal+"','"+sss+"','"+pH+"','"+others+"','"+deduct+"','"+netSal+"') "
                    cursor.execute(sql)
                    cursor.execute("commit")

                    mb.showinfo('Save Status', 'Payroll Saved', parent=payWin)
                    showEmp()
                    payWin.destroy()

            calButton = Button(payWin, text="Calculate", font=("Helvetica 14 bold"), bg="royalBlue2", height=2, width=10,
                            command=calculate)

            saveButton = Button(payWin, text="Save", font=("Helvetica 14 bold"), bg="green", height=2, width=10, state = DISABLED, command = save)

            exitPay = Button(payWin, text="Exit", font=("Helvetica 12 bold"), fg="red", height=1, width=12, command=payWin.destroy)

            payLabel.place(x=440, y=20)
            eNumLabel.place(x=20, y=80)
            eNumEntry.place(x=200, y=80)
            lNameLabel.place(x=430, y=80)
            lNameEntry.place(x=550, y=80)
            fNameLabel.place(x=780, y=80)
            fNameEntry.place(x=900, y=80)
            deptLabel.place(x=20, y=110)
            deptEntry.place(x=200, y=110)
            desLabel.place(x=430, y=110)
            desEntry.place(x=550, y=110)
            salLabel.place(x=780, y=110)
            salEntry.place(x=900, y=110)
            dateLabel.place(x=360, y=165)
            monthCombo.place(x=510, y=167)
            yearCombo.place(x=630, y=167)
            incomeLabel.place(x=20, y=220)
            rateLabel.place(x=20, y=280)
            rateEntry.place(x=160, y=280)
            daysLabel.place(x=20, y=320)
            daysEntry.place(x=160, y=320)
            alloLabel.place(x=20, y=360)
            alloEntry.place(x=160, y=360)
            gSalLabel.place(x=20, y=420)
            gSalEntry.place(x=160, y=420)
            

            deductLabel.place(x=420, y=220)
            sssLabel.place(x=420, y=280)
            sssEntry.place(x=580, y=280)
            philLabel.place(x=420, y=320)
            philEntry.place(x=580, y=320)
            otLabel.place(x=420, y=360)
            otEntry.place(x=580, y=360)
            tDedLabel.place(x=420, y=420)
            tDedEntry.place(x=580, y=420)

            nPayLabel.place(x=180,y=520)
            nPayEntry.place(x=300,y=520)

            calButton.place(x=900, y=360)
            saveButton.place(x=900, y=440)
            exitPay.place(x=900, y=550)

            monthCombo.current(0)
            yearCombo.current(0)

            paySelect = employeeTable.selection()
            itemValue = ()
            payId = ""
            for item in paySelect:
                itemValue = employeeTable.item(item, "values")

            if len(itemValue) == 0:
                mb.showerror('Status', 'No Selected Employee', parent=payWin)
                payWin.destroy()
            else:
                payId = itemValue[0]
                print(payId)
                cursor = connEmp.cursor()
                sql = "SELECT * FROM employees WHERE id = '" + payId + "' "
                cursor.execute(sql)
                result = cursor.fetchall()
                print(result)
                eNumEntry.insert(0, payId)
                lNameEntry.insert(0, result[0][1])
                fNameEntry.insert(0, result[0][2])
                deptEntry.insert(0, result[0][3])
                desEntry.insert(0, result[0][4])
                salEntry.insert(0, "₱ {:,.2f}".format(float(result[0][5])))
                eNumEntry['state'] = "readonly"
                lNameEntry['state'] = "readonly"
                fNameEntry['state'] = "readonly"
                deptEntry['state'] = "readonly"
                desEntry['state'] = "readonly"
                salEntry['state'] = "readonly"

                salary = float(result[0][5])
                rate = float(salary/30)
                rateEntry.insert(0, "₱ {:,.2f}".format(rate))
                sssEntry.insert(0, "₱ {:,.2f}".format(sssCompute(salary)))
                philEntry.insert(0, "₱ {:,.2f}".format(philhealthCompute(salary)))
                daysEntry.insert(0, '0')
                otEntry.insert(0, '₱ 0.00')
                alloEntry.insert(0, '₱ 0.00')
                rateEntry['state'] = "readonly"
                sssEntry['state'] = "readonly"
                philEntry['state'] = "readonly"

            payWin.mainloop()

        def disRecord():
            disWin = tk.Toplevel(admin)
            disWin.title("EPMS - Admin - View Records")
            positionR = int(disWin.winfo_screenwidth()/2 - 720/ 2)
            positionD = int(disWin.winfo_screenheight()/2 - 550/ 2)
            disWin.geometry("720x550+{}+{}".format(positionR, positionD))
            disWin.resizable(width=False, height=False)
            disWin.focus_set()

            def showPayroll():
                sql = "SELECT CONCAT(first_name,' ',last_name), date_save, date_payroll, net_salary " 
                sql += " FROM records INNER JOIN employees ON records.id_e = employees.id ORDER BY records.id DESC"
                cursor = connEmp.cursor()
                cursor.execute(sql)
                rows = cursor.fetchall()
                print(rows)
                total = cursor.rowcount
                print(str(total))
                
                for i in rows:
                    payrollTable.insert('', 'end', values=(i[0], i[1], i[2], "₱ {:,.2f}".format(float(i[3]))))

            exitDis = Button(disWin, text="Exit", font=("helvetica 12 bold"), bg="red", fg="white", height=1, width=10, command=disWin.destroy)

            payrollTable = ttk.Treeview(disWin, selectmode='browse', columns=(1,2,3,4), show="headings", height="20")
            payrollTable.place(x= 20, y= 20)
            payrollTable.heading(1, text="Employee Name")
            payrollTable.heading(2, text="Date Issued")
            payrollTable.heading(3, text="Month Paid")
            payrollTable.heading(4, text="Net Salary")
            payrollTable.column(1, width=200, anchor="center")
            payrollTable.column(2, width=150, anchor="center")
            payrollTable.column(3, width=150, anchor="center")
            payrollTable.column(4, width=175, anchor="center")

            exitDis.place(x=540, y=490)
            
            showPayroll()

            disWin.mainloop()

        def addNew():
            addNewWin = tk.Toplevel(admin)
            addNewWin.title("EPMS - Admin - Add New Admin")
            positionR = int(addNewWin.winfo_screenwidth() / 2 - 400 / 2)
            positionD = int(addNewWin.winfo_screenheight() / 2 - 200 / 2)
            addNewWin.geometry("400x200+{}+{}".format(positionR, positionD))
            addNewWin.resizable(width=False, height=False)
            addNewWin.focus_set()

            adNameLabel = Label(addNewWin, text="Name:", font=("Helvetica 12 bold"))
            adNameEntry = Entry(addNewWin, font=("Helvetica 14"))
            userLabel = Label(addNewWin, text="Username:", font=("Helvetica 12 bold"))
            userEntry = Entry(addNewWin, font=("Helvetica 14"))
            passLabel = Label(addNewWin, text="Password:", font=("Helvetica 12 bold"))
            passEntry = Entry(addNewWin, font=("Helvetica 14"), show="*")
            userEntry.focus()

            def adminClicked():
                user = userEntry.get()
                pwd = passEntry.get()
                adname = adNameEntry.get()

                if user == '' or pwd == '' or adname == '':
                    mb.showinfo('Add Status', 'All fields are required', parent=addNewWin)
                    addWin.focus_set()

                else:
                    cursor = connEmp.cursor()
                    sql = "SELECT username, password FROM admin"
                    cursor.execute(sql) 
                    result = cursor.fetchall()
                    print(result)

                    flag = 0
                    for row in result:
                        if row[0] == user:
                            flag = 1

                    if flag == 1:
                        mb.showinfo('Add Status', 'Username already taken', parent=addNewWin)
                        addWin.focus_set()
                    else:
                        cursor = connEmp.cursor()
                        sql = "INSERT INTO admin (username, password, admin_name) VALUES ('"+user+"', '"+pwd+"', '"+adname+"' )"
                        cursor.execute(sql)
                        cursor.execute("commit")

                        mb.showinfo('Add Admin Status', 'Admin Added Successfully')
                        addNewWin.focus_set()

                        adNameEntry.delete(0, 'end')
                        userEntry.delete(0, 'end')
                        passEntry.delete(0, 'end')

                    

            addNewButton = Button(addNewWin, text="Save", font=("helvetica 12 bold"), bg="royalblue2", height=1, width=10, command=(adminClicked))
            addExitButton = Button(addNewWin, text="Exit", font=("helvetica 12 bold"), bg="red", fg="white", height=1, width=10, command=addNewWin.destroy)

            adNameLabel.place(x=20,y=20)
            adNameEntry.place(x=150,y=20)
            userLabel.place(x=20, y=60)
            userEntry.place(x=150, y=60)
            passLabel.place(x=20, y=100)
            passEntry.place(x=150, y=100)

            addNewButton.place(x=40, y=150)
            addExitButton.place(x=250, y=150)

            addNewWin.mainloop()
        
        def changeUser():
            chUserWin = tk.Toplevel(admin)
            chUserWin.title("EPMS - Admin - Change Username")
            positionR = int(chUserWin.winfo_screenwidth() / 2 - 500 / 2)
            positionD = int(chUserWin.winfo_screenheight() / 2 - 200 / 2)
            chUserWin.geometry("500x200+{}+{}".format(positionR, positionD))
            chUserWin.resizable(width=False, height=False)
            chUserWin.focus_set()

            userLabel = Label(chUserWin, text="Enter Username:", font=("Helvetica 12 bold"))
            userEntry = Entry(chUserWin, font=("Helvetica 14"))
            userNewLabel = Label(chUserWin, text="Enter New Username:", font=("Helvetica 12 bold"))
            userNewEntry = Entry(chUserWin, font=("Helvetica 14"))
            userConfirmLabel = Label(chUserWin, text="Confirm New Username:", font=("Helvetica 12 bold"))
            userConfirmEntry = Entry(chUserWin, font=("Helvetica 14"))
            userEntry.focus()

            def userClicked():
                username = userEntry.get()
                newUsername = userNewEntry.get()
                newUsername2 = userConfirmEntry.get()

                if username == '' or newUsername == '' or newUsername2 == '':
                    mb.showinfo('Change Username Status', 'All fields are required.', parent=chUserWin)
                    chUserWin.focus_set()
                elif username != admin_user:
                    mb.showinfo('Change Username Status', 'Incorrect Username.', parent=chUserWin)
                elif username == newUsername:
                    mb.showinfo('Change Username Status', 'Current Username and New Username must be different.', parent=chUserWin)
                elif newUsername != newUsername2:
                    mb.showinfo('Change Username Status', 'Usernames do not match.', parent=chUserWin)
                else:
                    cursor=connEmp.cursor()
                    sql = "UPDATE admin SET username = '"+newUsername+"' WHERE username = '"+username+"' "
                    cursor.execute(sql)
                    cursor.execute("commit")

                    mb.showinfo('Change Username Status', 'Username Changed Successfully')
                    chUserWindow.destroy()

            addNewButton = Button(chUserWin, text="Save", font=("helvetica 12 bold"), bg="royalblue2", height=1, width=10, command=(userClicked))
            addExitButton = Button(chUserWin, text="Exit", font=("helvetica 12 bold"), bg="red", fg="white", height=1, width=10, command=chUserWin.destroy)

            userLabel.place(x=20, y=20)
            userEntry.place(x=240, y=20)
            userNewLabel.place(x=20, y=60)
            userNewEntry.place(x=240, y=60)
            userConfirmLabel.place(x=20, y=100)
            userConfirmEntry.place(x=240, y=100)

            addNewButton.place(x=40, y=150)
            addExitButton.place(x=350, y=150)

            chUserWin.mainloop() 

        def changepass():
            chpassWin = tk.Toplevel(admin)
            chpassWin.title("EPMS - Admin - Change Password")
            positionR = int(chpassWin.winfo_screenwidth() / 2 - 500 / 2)
            positionD = int(chpassWin.winfo_screenheight() / 2 - 200 / 2)
            chpassWin.geometry("500x200+{}+{}".format(positionR, positionD))
            chpassWin.resizable(width=False, height=False)
            chpassWin.focus_set()

            passLabel = Label(chpassWin, text="Enter password:", font=("Helvetica 12 bold"))
            passEntry = Entry(chpassWin, font=("Helvetica 14"), show="*")
            passNewLabel = Label(chpassWin, text="Enter New password:", font=("Helvetica 12 bold"))
            passNewEntry = Entry(chpassWin, font=("Helvetica 14"), show="*")
            passConfirmLabel = Label(chpassWin, text="Confirm New password:", font=("Helvetica 12 bold"))
            passConfirmEntry = Entry(chpassWin, font=("Helvetica 14"), show="*")
            passEntry.focus()

            def passClicked():
                password = passEntry.get()
                newpassword = passNewEntry.get()
                newpassword2 = passConfirmEntry.get()

                cursor = connEmp.cursor()
                sql = "SELECT username, password FROM admin"
                cursor.execute(sql) 
                result = cursor.fetchall()
                print(result)

                flag = 0
                for row in result:
                    if row[1] == password:
                        flag = 1

                if password == '' or newpassword == '' or newpassword2 == '':
                    mb.showinfo('Change Password Status', 'All fields are required.', parent=chpassWin)
                    chpassWin.focus_set()
                elif flag == 0:
                    mb.showinfo('Change Password Status', 'Incorrect Password.', parent=chpassWin)
                elif password == newpassword:
                    mb.showinfo('Change Password Status', 'Current Password and New Password must be different.', parent=chpassWin)
                elif newpassword != newpassword2:
                    mb.showinfo('Change Password Status', 'Passwords do not match.', parent=chpassWin)
                else:
                    sql = "UPDATE admin SET password = '"+newpassword+"' WHERE username = '"+admin_user+"' "
                    cursor.execute(sql)
                    cursor.execute("commit")

                    mb.showinfo('Change Password Status', 'Password Changed Successfully')
                    chpassWindow.destroy()

            addNewButton = Button(chpassWin, text="Save", font=("helvetica 12 bold"), bg="royalblue2", height=1, width=10, command=(passClicked))
            addExitButton = Button(chpassWin, text="Exit", font=("helvetica 12 bold"), bg="red", fg="white", height=1, width=10, command=chpassWin.destroy)

            passLabel.place(x=20, y=20)
            passEntry.place(x=240, y=20)
            passNewLabel.place(x=20, y=60)
            passNewEntry.place(x=240, y=60)
            passConfirmLabel.place(x=20, y=100)
            passConfirmEntry.place(x=240, y=100)

            addNewButton.place(x=40, y=150)
            addExitButton.place(x=350, y=150)

            chpassWin.mainloop() 

        def comma(n):
            r = []
            for i, c in enumerate(reversed(str(n))):
                if i and (not (i % 3)) :
                    r.insert(0, ',')
                r.insert(0, c)

            return ''.join(r)

        def philhealthCompute(salary):
            if salary <= 10000:
                pH = (10000 * 0.0275)/ 2
            elif salary > 10000 and salary < 40000:
                pH = round(salary * 0.0275, 2)/ 2
            else:
                pH = (40000 * 0.0275)/ 2
            return pH

        def sssCompute(salary):
            if(salary < 2250):
                sss = 80.00
            elif(salary >= 2250 and salary <= 2749.99):
                sss = 100.00
            elif(salary >= 2750 and salary <= 3249.99):
                sss = 120.00
            elif(salary >= 3250 and salary <= 3749.99):
                sss = 140.00
            elif(salary >= 3750 and salary <= 4249.99):
                sss = 160.00
            elif(salary >= 4250 and salary <= 4749.99):
                sss = 180.00
            elif(salary >= 4750 and salary <= 5249.99):
                sss = 200.00
            elif(salary >= 5250 and salary <= 5749.99):
                sss = 220.00
            elif(salary >= 5750 and salary <= 6249.99):
                sss = 240.00
            elif(salary >= 6250 and salary <= 6749.99):
                sss = 260.00
            elif(salary >= 6750 and salary <= 7249.99):
                sss = 280.00
            elif(salary >= 7250 and salary <= 7749.99):
                sss = 300.00
            elif(salary >= 7750 and salary <= 8249.99):
                sss = 320.00
            elif(salary >= 8250 and salary <= 8749.99):
                sss = 340.00
            elif(salary >= 8750 and salary <= 9249.99):
                sss = 360.00
            elif(salary >= 9250 and salary <= 9749.99):
                sss = 380.00
            elif(salary >= 9750 and salary <= 10249.99):
                sss = 400.00
            elif(salary >= 10250 and salary <= 10749.99):
                sss = 420.00
            elif(salary >= 10750 and salary <= 11249.99):
                sss = 440.00
            elif(salary >= 11250 and salary <= 11749.99):
                sss = 460.00
            elif(salary >= 11750 and salary <= 12249.99):
                sss = 480.00
            elif(salary >= 12250 and salary <= 12749.99):
                sss = 500.00
            elif(salary >= 12750 and salary <= 13249.99):
                sss = 520.00
            elif(salary >= 13250 and salary <= 13749.99):
                sss = 540.00
            elif(salary >= 13750 and salary <= 14249.99):
                sss = 560.00
            elif(salary >= 14250 and salary <= 14749.99):
                sss = 580.00
            elif(salary >= 14750 and salary <= 15249.99):
                sss = 600.00
            elif(salary >= 15250 and salary <= 15749.99):
                sss = 620.00
            elif(salary >= 15750 and salary <= 16249.99):
                sss = 640.00
            elif(salary >= 16250 and salary <= 16749.99):
                sss = 660.00
            elif(salary >= 16750 and salary <= 17249.99):
                sss = 680.00
            elif(salary >= 17250 and salary <= 17749.99):
                sss = 700.00
            elif(salary >= 17750 and salary <= 18249.99):
                sss = 720.00
            elif(salary >= 18250 and salary <= 18749.99):
                sss = 740.00
            elif(salary >= 18750 and salary <= 19249.99):
                sss = 760.00
            elif(salary >= 19250 and salary <= 19749.99):
                sss = 780.00
            elif(salary >= 19750):
                sss = 800.00
            return sss

        def showEmp():
            sql = "SELECT * FROM employees ORDER BY id DESC"
            cursor = connEmp.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            total = cursor.rowcount
            print(str(total))
            countEmployees['text'] = 'Total Number of Employees: '+str(total)

            for i in employeeTable.get_children():
                employeeTable.delete(i)

            for i in rows:
                employeeTable.insert('', 'end', values=(i[0], i[1], i[2], i[3], i[4], "₱ {:,.2f}".format(float(i[5]))))

        def search():
            value = searchEntry.get().lower()
            category = catCombo.get().strip().lower().replace(' ', '_')

            if value == '' and category == '-Category-': 
                pass
            elif category == '-Category-':
                mb.showinfo('Search', 'Specify Search Category', parent=admin)
                admin.focus_set()
            elif value == '':
                pass
            else:
                if category == 'employee_number':
                    category = 'id'

                cursor = connEmp.cursor()
                sql = "SELECT * FROM employees WHERE "+category+" = '"+value+"' "
                cursor.execute(sql)
                result = cursor.fetchall()

                if len(result) != 0:
                    for i in employeeTable.get_children():
                        employeeTable.delete(i)

                    for i in result:
                        employeeTable.insert('', 'end', values=(i[0], i[1], i[2], i[3], i[4], "₱ {:,.2f}".format(float(i[5]))))

                    
        
        def clear():
            searchEntry.delete(0, 'end')
            searchEntry.focus
            showEmp()
                
        
        def exitPressed():
            if mb.askokcancel("Log Out", "Do you really want to log out?"):
                admin.destroy()
                root.deiconify()


        admin.protocol("WM_DELETE_WINDOW", exitPressed)
        
        addicon = PhotoImage(file="icons/add.png")
        addButton = Button(admin, image=addicon, text=" Add", compound="left", font=("Helvetica 14 bold"), bg = "snow2", fg="black", height = 60, width = 120, command=addEmp)
        addButton.place(x=30, y=30 )

        editicon = PhotoImage(file="icons/edit.png")
        editButton = Button(admin, image=editicon, text=" Edit", compound="left", font=("Helvetica 14 bold"), bg = "snow2",  fg="black", height = 60, width = 120, command=editEmp)
        editButton.place(x=30, y=130)
        
        delicon = PhotoImage(file="icons/delete.png")
        deleteButton = Button(admin,  image=delicon, text=" Delete", compound="left", font=("Helvetica 14 bold"), bg = "snow2",  fg="black", height = 60, width = 120, command=delEmp)
        deleteButton.place(x=30, y=230 )

        payicon = PhotoImage(file="icons/payroll.png")
        payrollButton = Button(admin, image=payicon, text=" Payroll", compound="left", font=("Helvetica 14 bold"), bg = "snow2",fg ="black", height = 60, width = 120, command=payEmp)
        payrollButton.place(x=30, y=330 )

        recicon = PhotoImage(file="icons/record.png")
        recordsButton = Button(admin, image=recicon, text=" Records", compound="left", font=("Helvetica 14 bold"), bg = "snow", fg ="black", height = 60, width = 120, command=disRecord)
        recordsButton.place(x=30, y=430)

        exiticon = PhotoImage(file="icons/exit.png")
        exitButton = Button(admin, image=exiticon, text=" Log Out", compound="left", font=("Helvetica 12 bold"), bg = "snow2", fg = "black",height = 30, width = 120, command=exitPressed)
        exitButton.place(x=30, y=530)

        addAdmin = Button(admin, text="Add New Admin", font=("Helvetica 12 bold"), fg="blue", height=1, width=15, command= addNew)
        addAdmin.place(x=230, y=530)

        updateUser = Button(admin, text="Change Username", font=("Helvetica 12 bold"), fg="blue", height=1, width=15, command=changeUser)
        updateUser.place(x=430, y=530)

        updatePass = Button(admin, text="Change Password", font=("Helvetica 12 bold"), fg="blue", height=1, width=15,command=changepass)
        updatePass.place(x=630, y=530)

        adminLabel = Label(admin, text="Hello "+adminname+"!", font="Helvetica 18 bold", bg= 'royalblue1')
        adminLabel.place(x=860, y=530)
        
        countEmployees = Label(admin, font="Helvetica 12 bold", bg= 'royalblue1')
        countEmployees.place(x=900, y=30)

        searchLabel = Label(admin, font=("Helvetica 14 bold"), text="Search: ", bg='royalblue1')
        searchLabel.place(x=210, y=30)
        searchEntry = Entry(admin, font=("Helvetica 14"))
        searchEntry.place(x=460, y=30)
        searchicon = PhotoImage(file="icons/search-icon.png")
        searchButton = Button(admin, image=searchicon, width=25, height=25, bg="white", command=search)
        searchButton.place(x=690, y=30)
        clearicon = PhotoImage(file="icons/clear.png")
        clearButton = Button(admin, image=clearicon, relief="flat",width=18, height=18, bg="white", command=clear)
        clearButton.place(x=657, y=32)

        catCombo = ttk.Combobox(admin, values=["-Category-","Employee Number", "Last Name", "First Name", "Department", "Designation",
                                "Salary"], state="readonly", width= 16, font=("Helvetica", "11"))
        admin.option_add('*TCombobox*Listbox.font', ("Helvetica", "11"))
        catCombo.place(x=300, y=34)
        catCombo.current(0)

        employeeTable = ttk.Treeview(admin, selectmode='browse', columns=(1,2,3,4,5,6), show="headings", height="20")
        employeeTable.place(x= 200, y= 65)
        employeeTable.heading(1, text="Employee Number")
        employeeTable.heading(2, text="Last Name")
        employeeTable.heading(3, text="First Name")
        employeeTable.heading(4, text="Department")
        employeeTable.heading(5, text="Designation")
        employeeTable.heading(6, text="Salary")
        employeeTable.column(1, width=200, anchor="center")
        employeeTable.column(2, width=150, anchor="center")
        employeeTable.column(3, width=150, anchor="center")
        employeeTable.column(4, width=150, anchor="center")
        employeeTable.column(5, width=150, anchor="center")
        employeeTable.column(6, width=150, anchor="center")

        showEmp()

        admin.mainloop()
    

    def user_modules(userId, userEntered):
        user = tk.Toplevel(root)
        user.title("Employee Payroll Management System - Employee Profile")
        positionR = int(user.winfo_screenwidth() / 2 - 960 / 2)
        user.geometry("960x650+{}+30".format(positionR))
        root.withdraw()
        user.resizable(width=False, height=False)
        user.focus_set()

        userFrame = Frame(user, borderwidth = 10, relief ="flat", width=960, height=650, bg="gray72")
        frame1 = Frame(userFrame, borderwidth=1, relief="flat", width=400, height= 625, background="RoyalBlue1")
        frame2 = Frame(userFrame, borderwidth=1, relief="flat", width=535, height= 625,background="RoyalBlue1")
            
        EmpID_Label = Label(frame1,text="Employee ID:",font=("Helvetica 12 bold "), background="RoyalBlue1")
        EmpID_Entry = Entry(frame1, font=("Helvetica 12"), width=28, disabledbackground='RoyalBlue1', disabledforeground='black')
        NLabel = Label(frame1,text="Name:",font=("Helvetica 12 bold "),background="RoyalBlue1")
        NEntry = Entry(frame1, font=("Helvetica 12"), width=28, disabledbackground='RoyalBlue1', disabledforeground='black')
        DepLabel =  Label(frame1,text="Department:",font=("Helvetica 12 bold "),background="RoyalBlue1")
        DepEntry = Entry(frame1, font=("Helvetica 12"), width=28, disabledbackground='RoyalBlue1', disabledforeground='black')
        DesLabel =  Label(frame1,text="Designation:",font=("Helvetica 12 bold "),background="RoyalBlue1")
        DesEntry = Entry(frame1, font=("Helvetica 12"), width=28, disabledbackground='RoyalBlue1', disabledforeground='black')

        def changeUser():
            chUserWin = tk.Toplevel(user)
            chUserWin.title("EPMS - Employee - Change Username")
            positionR = int(chUserWin.winfo_screenwidth() / 2 - 500 / 2)
            positionD = int(chUserWin.winfo_screenheight() / 2 - 200 / 2)
            chUserWin.geometry("500x200+{}+{}".format(positionR, positionD))
            chUserWin.resizable(width=False, height=False)
            chUserWin.focus_set()

            userLabel = Label(chUserWin, text="Enter Username:", font=("Helvetica 12 bold"))
            userEntry = Entry(chUserWin, font=("Helvetica 14"))
            userNewLabel = Label(chUserWin, text="Enter New Username:", font=("Helvetica 12 bold"))
            userNewEntry = Entry(chUserWin, font=("Helvetica 14"))
            userConfirmLabel = Label(chUserWin, text="Confirm New Username:", font=("Helvetica 12 bold"))
            userConfirmEntry = Entry(chUserWin, font=("Helvetica 14"))

            def userClicked():
                username = userEntry.get()
                newUsername = userNewEntry.get()
                newUsername2 = userConfirmEntry.get()

                if username == '' or newUsername == '' or newUsername2 == '':
                    mb.showinfo('Change Username Status', 'All fields are required.', parent=chUserWin)
                    chUserWin.focus_set()
                elif username != userEntered:
                    mb.showinfo('Change Username Status', 'Incorrect Username.', parent=chUserWin)
                elif username == newUsername:
                    mb.showinfo('Change Username Status', 'Current Username and New Username must be different.', parent=chUserWin)
                elif newUsername != newUsername2:
                    mb.showinfo('Change Username Status', 'Usernames do not match.', parent=chUserWin)
                else:
                    cursor=connEmp.cursor()
                    sql = "UPDATE employees SET username = '"+newUsername+"' WHERE id = '"+str(userId)+"' "
                    cursor.execute(sql)
                    cursor.execute("commit")

                    mb.showinfo('Change Username Status', 'Username Changed Successfully')
                    chUserWindow.destroy()

            addNewButton = Button(chUserWin, text="Save", font=("helvetica 12 bold"), bg="royalblue2", height=1, width=10, command=(userClicked))
            addExitButton = Button(chUserWin, text="Exit", font=("helvetica 12 bold"), bg="red", fg="white", height=1, width=10, command=chUserWin.destroy)

            userLabel.place(x=20, y=20)
            userEntry.place(x=240, y=20)
            userNewLabel.place(x=20, y=60)
            userNewEntry.place(x=240, y=60)
            userConfirmLabel.place(x=20, y=100)
            userConfirmEntry.place(x=240, y=100)

            addNewButton.place(x=40, y=150)
            addExitButton.place(x=350, y=150)

            chUserWin.mainloop() 
        
        def changepass():
            chpassWin = tk.Toplevel(user)
            chpassWin.title("EPMS - Employee - Change Password")
            positionR = int(chpassWin.winfo_screenwidth() / 2 - 500 / 2)
            positionD = int(chpassWin.winfo_screenheight() / 2 - 200 / 2)
            chpassWin.geometry("500x200+{}+{}".format(positionR, positionD))
            chpassWin.resizable(width=False, height=False)
            chpassWin.focus_set()

            passLabel = Label(chpassWin, text="Enter password:", font=("Helvetica 12 bold"))
            passEntry = Entry(chpassWin, font=("Helvetica 14"), show="*")
            passNewLabel = Label(chpassWin, text="Enter New password:", font=("Helvetica 12 bold"))
            passNewEntry = Entry(chpassWin, font=("Helvetica 14"), show="*")
            passConfirmLabel = Label(chpassWin, text="Confirm New password:", font=("Helvetica 12 bold"))
            passConfirmEntry = Entry(chpassWin, font=("Helvetica 14"), show="*")

            def passClicked():
                password = passEntry.get()
                newpassword = passNewEntry.get()
                newpassword2 = passConfirmEntry.get()

                cursor = connEmp.cursor()
                sql = "SELECT username, pwd FROM employees WHERE id = '"+str(userId)+"' "
                cursor.execute(sql) 
                result = cursor.fetchall()
                print(result)

                flag = 0
                for row in result:
                    if row[1] == password:
                        flag = 1

                if password == '' or newpassword == '' or newpassword2 == '':
                    mb.showinfo('Change Password Status', 'All fields are required.', parent=chpassWin)
                    chpassWin.focus_set()
                elif flag == 0:
                    mb.showinfo('Change Password Status', 'Incorrect Password.', parent=chpassWin)
                elif password == newpassword:
                    mb.showinfo('Change Password Status', 'Current Password and New Password must be different.', parent=chpassWin)
                elif newpassword != newpassword2:
                    mb.showinfo('Change Password Status', 'Passwords do not match.', parent=chpassWin)
                else:
                    sql = "UPDATE employees SET pwd = '"+newpassword+"' WHERE id = '"+str(userId)+"' "
                    cursor.execute(sql)
                    cursor.execute("commit")

                    mb.showinfo('Change Password Status', 'Password Changed Successfully')
                    chpassWin.destroy()

            addNewButton = Button(chpassWin, text="Save", font=("helvetica 12 bold"), bg="royalblue2", height=1, width=10, command=(passClicked))
            addExitButton = Button(chpassWin, text="Exit", font=("helvetica 12 bold"), bg="red", fg="white", height=1, width=10, command=chpassWin.destroy)

            passLabel.place(x=20, y=20)
            passEntry.place(x=240, y=20)
            passNewLabel.place(x=20, y=60)
            passNewEntry.place(x=240, y=60)
            passConfirmLabel.place(x=20, y=100)
            passConfirmEntry.place(x=240, y=100)

            addNewButton.place(x=40, y=150)
            addExitButton.place(x=350, y=150)

            chpassWin.mainloop() 

        def userShow():
            cursor = connEmp.cursor()
            sql = "SELECT id, CONCAT(first_name,' ',last_name), department, designation FROM employees WHERE id = '"+str(userId)+"' "
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)

            EmpID_Entry.insert(0, result[0][0])
            NEntry.insert(0, result[0][1])
            DepEntry.insert(0, result[0][2])
            DesEntry.insert(0, result[0][3])
            EmpID_Entry['state']=DISABLED
            NEntry['state']=DISABLED
            DepEntry['state']=DISABLED
            DesEntry['state']=DISABLED

        def viewPayslip():
            viewPsWin = tk.Toplevel(user)
            viewPsWin.title("EPMS - Employee - View Payslip")
            positionR = int(viewPsWin.winfo_screenwidth() / 2 - 800 / 2)
            positionD = int(viewPsWin.winfo_screenheight() / 2 - 600 / 2)
            viewPsWin.geometry("800x600+{}+{}".format(positionR, positionD))
            viewPsWin.resizable(width=False, height=False)
            viewPsWin.focus_set()
            viewPsWin.configure(bg="royalblue1")

            pSLabel = Label(viewPsWin, font=("Helvetica 14 bold"), bg="royalblue1")
            emIdLabel = Label(viewPsWin, text="Employee Number:", font=("Helvetica 11"), bg="royalblue1")
            emIdEntry = Entry(viewPsWin, font=("Helvetica 12"), disabledbackground='RoyalBlue1', disabledforeground='black')
            emNameLabel = Label(viewPsWin, text="Employee Name:", font=("Helvetica 11"), bg="royalblue1")
            emNameEntry = Entry(viewPsWin, font=("Helvetica 12"), disabledbackground='RoyalBlue1', disabledforeground='black')
            emDeptLabel = Label(viewPsWin, text="Department:", font=("Helvetica 11"), bg="royalblue1")
            emDeptEntry = Entry(viewPsWin, font=("Helvetica 12"), disabledbackground='RoyalBlue1', disabledforeground='black')
            emDesLabel = Label(viewPsWin, text="Designation:", font=("Helvetica 11"), bg="royalblue1")
            emDesEntry = Entry(viewPsWin, font=("Helvetica 12"), disabledbackground='RoyalBlue1', disabledforeground='black')
            
            linetxt = "________________________________________"

            incFrame = Frame(viewPsWin, bg="DarkOliveGreen2", height=300, width=400, bd= 5, relief="ridge")
            incLabel = Label(incFrame, bg="DarkOliveGreen2", text= "Earnings:", font="Helvetica 13 bold")
            rateLabel = Label(incFrame, text="Rate per Day:", font=("Helvetica 12 bold"), bg="DarkOliveGreen2")
            rateEntry = Entry(incFrame, font=("Helvetica 12 bold"), disabledbackground="DarkOliveGreen2", disabledforeground='black')
            daysLabel = Label(incFrame, text="Days:", font=("Helvetica 12 bold"), bg="DarkOliveGreen2")
            daysEntry = Entry(incFrame, font=("Helvetica 12 bold"), disabledbackground="DarkOliveGreen2", disabledforeground='black')
            alloLabel = Label(incFrame, text="Allowances:", font=("Helvetica 12 bold"), bg="DarkOliveGreen2")
            alloEntry = Entry(incFrame, font=("Helvetica 12 bold"), disabledbackground="DarkOliveGreen2", disabledforeground='black')
            gSalLabel = Label(incFrame, text="Total Earnings:", font=("Helvetica 12 bold"), bg="DarkOliveGreen2")
            gSalEntry = Entry(incFrame, font=("Helvetica 12 bold"), disabledbackground="DarkOliveGreen2", disabledforeground='black')
            line1Label = Label(incFrame, text=linetxt, font=("Helvetica 12 bold"), background="DarkOliveGreen2" )

            dedFrame = Frame(viewPsWin, bg="Coral2", height=300, width=400, bd= 5, relief="ridge")
            dedLabel = Label(dedFrame, bg="Coral2", text= "Deductions:", font="Helvetica 13 bold")
            sssLabel = Label(dedFrame, text="SSS:", font=("Helvetica 12 bold"), bg="Coral2",)
            sssEntry = Entry(dedFrame, font=("Helvetica 12 bold"), disabledbackground="Coral2", disabledforeground='black')
            philLabel = Label(dedFrame, text="PhilHealth:", font=("Helvetica 12 bold"), bg="Coral2",)
            philEntry = Entry(dedFrame, font=("Helvetica 12 bold"), disabledbackground="Coral2", disabledforeground='black')
            otLabel = Label(dedFrame, text="Others:", font=("Helvetica 12 bold"), bg="Coral2",)
            otEntry = Entry(dedFrame, font=("Helvetica 12 bold"), disabledbackground="Coral2", disabledforeground='black')
            tDedLabel = Label(dedFrame, text="Total Deductions:", font=("Helvetica 12 bold"), bg="Coral2",)
            tDedEntry = Entry(dedFrame, font=("Helvetica 12 bold"), disabledbackground="Coral2", disabledforeground='black')
            line2Label = Label(dedFrame, text=linetxt, font=("Helvetica 12 bold"), background="Coral2" )

            nPayFrame = Frame(viewPsWin, bg="mediumseagreen", height=40, width=400, relief="ridge", bd=5)
            nPayLabel = Label(nPayFrame, text="Net Salary:", font=("Helvetica 12 bold"), bg="mediumseagreen")
            nPayEntry = Entry(nPayFrame, font=("Helvetica 12 bold"), disabledbackground="mediumseagreen", disabledforeground='black')
            
            exitbut = Button(viewPsWin,text="Exit",width=10, background="red", foreground="Snow2", font=("Helvetica 12 bold"),command=viewPsWin.destroy)
            
            pSLabel.place(x=230, y=20)
            emIdLabel.place(x=40, y=70)
            emIdEntry.place(x=180, y=70)
            emNameLabel.place(x=420, y=70)
            emNameEntry.place(x=560, y=70)
            emDeptLabel.place(x=40, y=100)
            emDeptEntry.place(x=180, y=100)
            emDesLabel.place(x=420, y=100)
            emDesEntry.place(x=560, y=100)

            incFrame.place(x=1, y=180)
            incLabel.place(x=5,y=5)
            rateLabel.place(x=5,y=65)
            rateEntry.place(x=180, y=65)
            daysLabel.place(x=5, y=115)
            daysEntry.place(x=180, y=115)
            alloLabel.place(x=5, y=165)
            alloEntry.place(x=180, y=165)
            gSalLabel.place(x=5, y=250)
            gSalEntry.place(x=180, y=250)
            line1Label.place(x=5, y=220)

            dedFrame.place(x=401, y=180)
            dedLabel.place(x=5,y=5)
            sssLabel.place(x=5,y=65)  
            sssEntry.place(x=180, y=65)
            philLabel.place(x=5, y=115)
            philEntry.place(x=180, y=115)
            otLabel.place(x=5, y=165)
            otEntry.place(x=180, y=165)
            tDedLabel.place(x=5, y=250)
            tDedEntry.place(x=180, y=250)
            line2Label.place(x=5, y=220)
            
            nPayFrame.place(x=401, y=481)
            nPayLabel.place(x=5, y=3)
            nPayEntry.place(x=180, y=3)

            exitbut.place(x=650, y=550)
            
            emIdEntry.insert(0, EmpID_Entry.get())
            emNameEntry.insert(0, NEntry.get())
            emDeptEntry.insert(0, DepEntry.get())
            emDesEntry.insert(0, DesEntry.get())
            emIdEntry['state'] = DISABLED
            emNameEntry['state'] = DISABLED
            emDeptEntry['state'] = DISABLED
            emDesEntry['state'] = DISABLED

            viewSelect = salaryTable.selection()
            itemValue = ()
            editId = ""
            for item in viewSelect:
                itemValue = salaryTable.item(item, "values")

            if len(itemValue) == 0:
                mb.showerror('View Status', 'No Selected Payslip', parent=viewPsWin)
                viewPsWin.destroy()
            
            else:
                index = salaryTable.index(salaryTable.selection())
                print(index)
                pSId = payIdHolder[index]

                cursor = connEmp.cursor()
                sql = "SELECT * FROM RECORDS WHERE id = '"+str(pSId)+"' "
                cursor.execute(sql)
                result = cursor.fetchall()

                pSLabel['text'] = "Payslip for the Period of "+result[0][3]
                rateEntry.insert(0, "₱ {:,.2f}".format(float(result[0][4])))
                daysEntry.insert(0, result[0][5])
                alloEntry.insert(0, "₱ {:,.2f}".format(float(result[0][6])))
                gSalEntry.insert(0, "₱ {:,.2f}".format(float(result[0][7])))
                sssEntry.insert(0, "₱ {:,.2f}".format(float(result[0][8]))) 
                philEntry.insert(0, "₱ {:,.2f}".format(float(result[0][9])))
                otEntry.insert(0, "₱ {:,.2f}".format(float(result[0][10])))
                tDedEntry.insert(0, "₱ {:,.2f}".format(float(result[0][11])))
                nPayEntry.insert(0, "₱ {:,.2f}".format(float(result[0][12])))

                rateEntry['state'] = DISABLED
                daysEntry['state'] = DISABLED
                alloEntry['state'] = DISABLED
                gSalEntry['state'] = DISABLED
                sssEntry['state'] = DISABLED 
                philEntry['state'] = DISABLED
                otEntry['state'] = DISABLED
                tDedEntry['state'] = DISABLED
                nPayEntry['state'] = DISABLED



            viewPsWin.mainloop()

            
        def exitPressed():
            if mb.askokcancel("Log Out", "Do you really want to log out?"):
                user.destroy()
                root.deiconify()


        user.protocol("WM_DELETE_WINDOW", exitPressed)
             
        payIdHolder = []

        salaryTable = ttk.Treeview(frame2, selectmode='browse', columns=(1,2,3), show="headings", height="22")
        salaryTable.place(x= 40, y= 30)
        salaryTable.heading(1, text="Date Issued")
        salaryTable.heading(2, text="Month Paid")
        salaryTable.heading(3, text="Net Salary")
        salaryTable.column(1, width=150, anchor="center")
        salaryTable.column(2, width=150, anchor="center")
        salaryTable.column(3, width=150, anchor="center")

        Userbutton = Button(frame1,text="Change Username", width=20,background="midnight blue", foreground="Snow2", font=("Helvetica 12 bold"), command=changeUser)
        Passbutton = Button(frame1,text="Change Password",width=20, background="midnight blue", foreground="Snow2", font=("Helvetica 12 bold"), command=changepass)
        Logoutbutton = Button(frame1,text="Log Out",width=10, background="red", foreground="Snow2", font=("Helvetica 12 bold"),command=exitPressed)
        Detailbutton = Button(frame2,text="View Payslip",width=15,background="green", foreground="Snow2", font=("Helvetica 12 bold"), command=viewPayslip)

        EmpID_Label.place(x=10,y=80)
        EmpID_Entry.place(x=120,y=80)
        NLabel.place(x=10,y=120)
        NEntry.place(x=120,y=120)
        DepLabel.place(x=10,y=160)
        DepEntry.place(x=120,y=160)
        DesLabel.place(x=10,y=200)
        DesEntry.place(x=120,y=200)
        Userbutton.place(x=100,y=300)
        Passbutton.place(x=100,y=340)
        Logoutbutton.place(x=150,y=550)
        Detailbutton.place(x=200,y=550)

        userFrame.place(x=0, y=0)
        frame1.place(x=1,y=1)
        frame2.place(x=403, y=1)

        userShow()

        cursor = connEmp.cursor()
        sql = "SELECT date_save, date_payroll, net_salary, id FROM records WHERE id_e = '"+str(userId)+"' ORDER BY id DESC "
        cursor.execute(sql)
        rows = cursor.fetchall()

        for i in rows:
            salaryTable.insert('', 'end', values=(i[0], i[1], "₱ {:,.2f}".format(float(i[2]))))
        
        for item in rows:
            payIdHolder.append(item[3])
        print(payIdHolder)


        user.mainloop()

    def main_grids():
        headlabel1 = Label(main,text="Employee Payroll", font=('Helvetica 29 bold'), background ="midnight blue",foreground='snow2')
        headlabel2 = Label(main,text = "Management System", font=('Helvetica 25 italic'), background="midnight blue",foreground='gold')
        headlabel1.grid(column = 0, row =0, rowspan = 2, sticky=(W,S), padx = 7)
        headlabel2.grid(column = 0, row =2, sticky=(W,N), padx = 10)
        main.grid(column=0, row=0, sticky= (N,W,E,S))
        frame1.grid(column=0, row=0, columnspan = 1, rowspan=3, sticky= (N,W,E,S))
        frame2.grid(column=1, row=0, columnspan = 5, rowspan=3, sticky= (N,W,E,S))
        frame3.grid(column=0, row=3, columnspan= 10,rowspan= 7, sticky= (N,W,E,S))
    
        employEntry.delete(0,'end')
        employPassEntry.delete(0,'end')
        var.set(1)
        userbutton()    


    def admin_login():
        # gets username and pass from the entry
        admin_user = adminEntry.get()
        admin_pass = adminPassEntry.get()

        cursor = connEmp.cursor()
        sql = "SELECT username, password, admin_name FROM admin"
        cursor.execute(sql) 
        result = cursor.fetchall()
        print(result)

        admin_name = ''

        flag = 0
        for row in result:
            if row[0] == admin_user and row[1] == admin_pass:
                flag =1
                admin_name = row[2]

        if flag == 1:
            wrongPassLabel2.grid_forget()
            adminEntry.delete(0, len(admin_user))
            adminPassEntry.delete(0, len(admin_pass))
            admin_modules(admin_user, admin_name)
            
        else:
            wrongPassLabel2.grid(column = 3, row = 2, sticky=(W,N))
            adminEntry.delete(0, len(admin_user))
            adminPassEntry.delete(0, len(admin_pass))
            adminEntry.focus()

    def user_login():
        # GETS username and pass from the enty
        user_user = employEntry.get()
        user_pass = employPassEntry.get()

        cursor = connEmp.cursor()
        sql = "SELECT id, username, pwd FROM employees"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

        userId = ""
        flag = 0
        for row in result:
            if row[1] == user_user and row[2] == user_pass:
                flag = 1
                userId = row[0]

        if flag == 1:
            wrongPassLabel.grid_forget()
            employEntry.delete(0, 'end')
            employPassEntry.delete(0, 'end')
            user_modules(userId, user_user)
            
        else:
            wrongPassLabel.grid(column = 3, row = 2, sticky=(W,N))
            wrongpassbutton1.grid(column= 4, row = 2, sticky=(W,N))
            employEntry.delete(0, 'end')
            employPassEntry.delete(0, 'end')
            employEntry.focus()



    def adminbutton():
        wrongPassLabel.grid_forget()
        wrongpassbutton1.grid_forget()
        employPassEntry.grid_forget()
        employEntry.grid_forget()
        employPassLabel.grid_forget()
        employUser.grid_forget()
        employButton.grid_forget()
        adminUser.grid(column=3, row=0, sticky = (W,S), pady = 5)
        adminEntry.grid(column=3, row=1, sticky = (W,N), pady = 5)
        adminPassLabel.grid(column=4, row=0,sticky = (W,S), pady = 5)
        adminPassEntry.grid(column=4, row = 1, sticky = (W,N), pady = 5)
        adminButton.grid(column=5, row=1, sticky=(W,N))
        wrongpassbutton2.grid(column= 4, row = 2, sticky=(W,N))
        adminEntry.bind('<Return>', (lambda e: admin_login()))
        adminPassEntry.bind('<Return>', (lambda e: admin_login()))
        adminEntry.focus()
    
    
    def userbutton():
        adminUser.grid_forget()
        adminEntry.grid_forget()
        adminPassLabel.grid_forget()
        adminPassEntry.grid_forget()
        adminButton.grid_forget()
        wrongPassLabel2.grid_forget()
        wrongpassbutton2.grid_forget()
        employUser.grid(column=3, row=0, sticky = (W,S), pady = 5)
        employEntry.grid(column=3, row=1, sticky = (W,N), pady = 5)
        employPassLabel.grid(column=4, row=0,sticky = (W,S), pady = 5)
        employPassEntry.grid(column=4, row =1, sticky = (W,N), pady = 5)
        employButton.grid(column=5, row=1, sticky=(W,N))
        wrongpassbutton1.grid(column= 4, row = 2, sticky=(W,N))
        employEntry.bind('<Return>', (lambda e: user_login()))
        employPassEntry.bind('<Return>', (lambda e: user_login()))
        employEntry.focus()
    
    def adminforgot():
        adforWin = tk.Toplevel(root)
        adforWin.title("EPMS - Forgot Password")
        positionR = int(adforWin.winfo_screenwidth() / 2 - 400 / 2)
        positionD = int(adforWin.winfo_screenheight() / 2 - 200 / 2)
        adforWin.geometry("400x200+{}+{}".format(positionR, positionD))
        adforWin.resizable(width=False, height=False)
        adforWin.focus_set()

        forgotLabel = Label(adforWin, text="Provide the following details to reset password:", font=("Helvetica 12 bold"))
        nameLabel = Label(adforWin, text="Name:", font=("Helvetica 12 bold"))
        nameEntry = Entry(adforWin, font=("Helvetica 14"))
        userLabel = Label(adforWin, text="Username:", font=("Helvetica 12 bold"))
        userEntry = Entry(adforWin, font=("Helvetica 14"))
        nameEntry.focus()

        def adminCheck():
            username = userEntry.get().lower().strip()
            adminname = nameEntry.get().lower().strip()

            if username == '' or adminname == '':
                mb.showinfo('Status', 'All fields are required', parent=adforWin)
                adforWin.focus_set()
            else:
                cursor = connEmp.cursor()
                sql = "SELECT * FROM admin"
                cursor.execute(sql)
                rows = cursor.fetchall()
                
                adminId = ''

                flag = 0
                for i in rows:
                    if i[1] == username and i[3].lower() == adminname:
                        flag = 1
                        adminId = i[0]
                
                if flag == 0:
                    mb.showinfo('Status', 'Incorrect Info')
                    adforWin.destroy()
                
                else:
                    resetpass(adminId)
            
        def resetpass(adId):
            resetWin = tk.Toplevel(adforWin)
            resetWin.title("EPMS - Forgot Password")
            positionR = int(resetWin.winfo_screenwidth() / 2 - 500 / 2)
            positionD = int(resetWin.winfo_screenheight() / 2 - 200 / 2)
            resetWin.geometry("500x200+{}+{}".format(positionR, positionD))
            resetWin.resizable(width=False, height=False)
            adforWin.withdraw()
            resetWin.focus_set()

            resetLabel = Label(resetWin, text="Resetting Password", font=("Helvetica 12 bold"))
            passLabel = Label(resetWin, text="New Password:", font=("Helvetica 12 bold"))
            passEntry = Entry(resetWin, font=("Helvetica 14"), show="*")
            conPassLabel = Label(resetWin, text="Confirm New Password:", font=("Helvetica 12 bold"))
            conPassEntry = Entry(resetWin, font=("Helvetica 14"), show="*")
            passEntry.focus()

            def chaPas():
                pwd = passEntry.get()
                conpwd = conPassEntry.get()

                if pwd == '' or conpwd == '':
                    mb.showinfo('Reset Status', 'All fields required.', parent=resetWin)
                    resetWin.focus_set()
                elif pwd != conpwd:
                    mb.showinfo('Reset Status', 'Passwords do not match.', parent=resetWin)
                    resetWin.focus_set()
                else:
                    cursor = connEmp.cursor()
                    sql = "UPDATE admin SET password = '"+pwd+"' WHERE id = '"+str(adId)+"' "
                    cursor.execute(sql)
                    cursor.execute("commit")

                    mb.showinfo('Reset Password', 'Password Changed Successfully', parent=resetWin)
                    resetWin.destroy()
                    adforWin.destroy()
                    adminEntry.focus()

            conButton = Button(resetWin, text="Confirm", font=("helvetica 12 bold"), bg="royalblue2", height=1, width=10, command=chaPas)
            canButton = Button(resetWin, text="Cancel", font=("helvetica 12 bold"), bg="red", fg="white", height=1, width=10, command=resetWin.destroy)

            resetLabel.place(x=15, y=20)
            passLabel.place(x=20, y=60)
            passEntry.place(x=240, y=60)
            conPassLabel.place(x=20, y=100)
            conPassEntry.place(x=240, y=100)

            conButton.place(x=40, y=150)
            canButton.place(x=340, y=150)
            
            resetWin.mainloop()

        enterButton = Button(adforWin, text="Enter", font=("helvetica 12 bold"), bg="royalblue2", height=1, width=10, command=adminCheck)
        cancelButton = Button(adforWin, text="Cancel", font=("helvetica 12 bold"), bg="red", fg="white", height=1, width=10, command=adforWin.destroy)

        forgotLabel.place(x=15, y=20)
        nameLabel.place(x=20, y=60)
        nameEntry.place(x=150, y=60)
        userLabel.place(x=20, y=100)
        userEntry.place(x=150, y=100)

        enterButton.place(x=40, y=150)
        cancelButton.place(x=250, y=150)

        adforWin.mainloop()   
    
    def employforgot():
        empforWin = tk.Toplevel(root)
        empforWin.title("EPMS - Forgot Password")
        positionR = int(empforWin.winfo_screenwidth() / 2 - 500 / 2)
        positionD = int(empforWin.winfo_screenheight() / 2 - 350 / 2)
        empforWin.geometry("500x350+{}+{}".format(positionR, positionD))
        empforWin.resizable(width=False, height=False)
        empforWin.focus_set()

        forgotLabel = Label(empforWin, text="Provide the following details to reset password:", font=("Helvetica 12 bold"))
        eNumLabel = Label(empforWin, text="Employee Number:", font=("Helvetica 12 bold"))
        eNumEntry = Entry(empforWin, font=("Helvetica 14"))
        nameLabel = Label(empforWin, text="Name:", font=("Helvetica 12 bold"))
        nameEntry = Entry(empforWin, font=("Helvetica 14"))
        userLabel = Label(empforWin, text="Username:", font=("Helvetica 12 bold"))
        userEntry = Entry(empforWin, font=("Helvetica 14"))
        deptLabel = Label(empforWin, text="Department:", font=("Helvetica 12 bold"))
        deptEntry = Entry(empforWin, font=("Helvetica 14"))
        desLabel = Label(empforWin, text="Designation:", font=("Helvetica 12 bold"))
        desEntry = Entry(empforWin, font=("Helvetica 14"))
        eNumEntry.focus()

        def employCheck():
            empId = eNumEntry.get().strip()
            employname = nameEntry.get().lower().strip()
            username = userEntry.get().lower().strip()
            department = deptEntry.get().lower().strip()
            designation = desEntry.get().lower().strip()

            if username == '' or employname == '' or empId == '' or department == '' or designation == '' :
                mb.showinfo('Status', 'All fields are required', parent=empforWin)
                empforWin.focus_set()
            else:
                cursor = connEmp.cursor()
                sql = "SELECT * FROM employees"
                cursor.execute(sql)
                rows = cursor.fetchall()
                
                employId = ''

                flag = 0
                for i in rows:
                    if i[0] == int(empId) and (i[2]+' '+i[1]).lower() == employname and i[3].lower() == department and i[4].lower() == designation and i[6] == username:
                        flag = 1
                        employId = i[0]
                
                if flag == 0:
                    mb.showinfo('Status', 'Incorrect Info')
                    empforWin.destroy()
                
                else:
                    resetpass(employId)
            
        def resetpass(empId):
            resetWin = tk.Toplevel(empforWin)
            resetWin.title("EPMS - Forgot Password")
            positionR = int(resetWin.winfo_screenwidth() / 2 - 500 / 2)
            positionD = int(resetWin.winfo_screenheight() / 2 - 200 / 2)
            resetWin.geometry("500x200+{}+{}".format(positionR, positionD))
            resetWin.resizable(width=False, height=False)
            empforWin.withdraw()
            resetWin.focus_set()

            resetLabel = Label(resetWin, text="Resetting Password", font=("Helvetica 12 bold"))
            passLabel = Label(resetWin, text="New Password:", font=("Helvetica 12 bold"))
            passEntry = Entry(resetWin, font=("Helvetica 14"), show="*")
            conPassLabel = Label(resetWin, text="Confirm New Password:", font=("Helvetica 12 bold"))
            conPassEntry = Entry(resetWin, font=("Helvetica 14"), show="*")
            passEntry.focus()

            def chaPas():
                pwd = passEntry.get()
                conpwd = conPassEntry.get()

                if pwd == '' or conpwd == '':
                    mb.showinfo('Reset Status', 'All fields required.', parent=resetWin)
                    resetWin.focus_set()
                elif pwd != conpwd:
                    mb.showinfo('Reset Status', 'Passwords do not match.', parent=resetWin)
                    resetWin.focus_set()
                else:
                    cursor = connEmp.cursor()
                    sql = "UPDATE employees SET pwd = '"+pwd+"' WHERE id = '"+str(empId)+"' "
                    cursor.execute(sql)
                    cursor.execute("commit")

                    mb.showinfo('Reset Password', 'Password Changed Successfully', parent=resetWin)
                    resetWin.destroy()
                    empforWin.destroy()
                    employEntry.focus()

            conButton = Button(resetWin, text="Confirm", font=("helvetica 12 bold"), bg="royalblue2", height=1, width=10, command=chaPas)
            canButton = Button(resetWin, text="Cancel", font=("helvetica 12 bold"), bg="red", fg="white", height=1, width=10, command=resetWin.destroy)

            resetLabel.place(x=15, y=20)
            passLabel.place(x=20, y=60)
            passEntry.place(x=240, y=60)
            conPassLabel.place(x=20, y=100)
            conPassEntry.place(x=240, y=100)

            conButton.place(x=40, y=150)
            canButton.place(x=340, y=150)
            
            resetWin.mainloop()

        enterButton = Button(empforWin, text="Enter", font=("helvetica 12 bold"), bg="royalblue2", height=1, width=10, command=employCheck)
        cancelButton = Button(empforWin, text="Cancel", font=("helvetica 12 bold"), bg="red", fg="white", height=1, width=10, command=empforWin.destroy)

        forgotLabel.place(x=15, y=20)
        eNumLabel.place(x=20, y=60)
        eNumEntry.place(x=240, y=60)
        nameLabel.place(x=20, y=100)
        nameEntry.place(x=240, y=100)
        userLabel.place(x=20, y=140)
        userEntry.place(x=240, y=140)
        deptLabel.place(x=20, y=180)
        deptEntry.place(x=240, y=180)
        desLabel.place(x=20, y=220)
        desEntry.place(x=240, y=220)

        enterButton.place(x=40, y=300)
        cancelButton.place(x=340, y=300)

        empforWin.mainloop()  

    connEmp = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "db_payroll"
        )

    img = ImageTk.PhotoImage(Image.open("bg.jpg"))
    main = Frame(root, borderwidth = 10, relief ="flat", width=1295, height=650)
    frame1 = Frame(main, borderwidth=10, relief="flat", width=300, height= 200, bg = "midnightBlue")
    frame2 = Frame(main, borderwidth=10, relief="flat", width=927, height= 200, bg = "royalblue1")
    frame3 = Frame(main, borderwidth=10, relief="flat", width=1240, height= 430)

    var = IntVar()
    typeUser = Label(main, text="Type of User: ", font=('Helvetica', 13), background = "RoyalBlue1").grid(column = 1, row= 0, sticky=(W,S), padx = 10, pady = 10)
    empRadio = tkinter.Radiobutton(main, indicatoron = 0, text= "Employee",background="midnightblue",foreground='snow2',selectcolor="dodgerblue",disabledforeground = "midnightblue",activebackground="snow2",activeforeground="midnightblue", variable= var, value= 1, command = userbutton, font=('Helvetica 13 bold')).grid(column = 1, row = 1, sticky=(N,E), ipadx=10,)
    admRadio = tkinter.Radiobutton(main, indicatoron = 0, text= "Admin",background="midnightblue",foreground='snow2',selectcolor="dodgerblue",disabledforeground = "midnightblue", activebackground="snow2",activeforeground="midnightblue", variable= var, value= 2, command = adminbutton, font=('Helvetica 13 bold')).grid(column = 2, row = 1, sticky=(N,W),  ipadx= 10)
                                                                                                                                                                                                                                                                                                        
    #wrongpass and pasword widgets
    wrongPassLabel = Label(main, text= "Wrong Username or Password",  font=('helvetica', 10), background="RoyalBlue1", foreground="red")
    wrongPassLabel2=  Label(main, text= "Wrong Username or Password",  font=('helvetica', 10), background="RoyalBlue1", foreground="red")
    wrongpassbutton1= Button(main, text="Forgot Password?", font=('Helvetica 10'), relief='flat', background='royalblue1', command=employforgot)
    wrongpassbutton2= Button(main, text="Forgot Password?", font=('Helvetica 10'), relief='flat', background='royalblue1', command=adminforgot )

    # creation of widgets for employee entries
    employUser = Label(main, text= "Username: ", bg = "royalblue1", font=("helvetica 12"))
    employEntry = Entry(main, font=('Helvetica', 12))
    employPassLabel = Label(main, text= "Password: ",bg = "royalblue1", font=("helvetica 12"))
    employPassEntry = Entry(main, show="*",font=('Helvetica', 12))
    employButton = Button(main, text="Log In", command = user_login, font=('Helvetica', 11, "bold"), bg="midnightblue", fg="white", width = 7)

    # creation of widgets for admin entries
    adminUser = Label(main, text = "Username: ", bg = "royalblue1", font=("helvetica 12"))
    adminEntry = Entry(main, font=('Helvetica', 12))
    adminPassLabel = Label(main, text = "Password: ", bg = "royalblue1", font=("helvetica 12"))
    adminPassEntry = Entry(main, show= "*", font=('Helvetica', 12))
    adminButton = Button(main, text="Log In", command= admin_login ,font=('Helvetica', 11, "bold"), bg="midnightblue", fg="white", width = 7)

    #showing widgets to the frame
    main_grids()
    userbutton()

    picture = Label(main, image = img)
    picture.grid(column=0, row=3, columnspan= 10,rowspan= 8, sticky= (N,W,E,S))

    Style().configure("Treeview", font=("Helvetica 12"))
    Style().configure("Treeview.Heading", font=("Helvetica 14"), fieldbackground="midnightblue")

    root.mainloop()

if __name__ == '__main__':
    
    main()
    