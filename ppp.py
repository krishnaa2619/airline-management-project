import matplotlib.pyplot as plt
import mysql.connector as conn
from prettytable import PrettyTable as pt
import random as rd
import pandas as pd
import numpy as np
db=conn.connect(host="localhost",
                user="root",
                password="1603", 
                database="airway")


 #LOGIN
def Register():
    cur=db.cursor()
    Cust_Name=input("Enter your Name:")
    Cust_Email=input("Enter you Email:")
    Cust_PhoneNo=int(input("Enter your Phone Number:"))
    Cust_Password=input("Enter your Password:")
    print('='*50)
    query="insert into customer(Cust_Name,Cust_Email,Cust_PhoneNo,Cust_Password)values('{}','{}',{},'{}')".format(Cust_Name,
                                                                                                                  Cust_Email,
                                                                                                                  Cust_PhoneNo,
                                                                                                                  Cust_Password)
    cur.execute(query) 
    db.commit()
    print('='*50)
    print('\n')
    print('*'*30)
    print("Registration completed successfully")
    print('*'*30)
def login():
    cur=db.cursor()
    Cust_Name=input("Enter your Name:")
    Cust_Password=input("Enter your Password:")
    print('='*50)
    query="select * from customer where Cust_Name='{}' and Cust_Password='{}'".format(Cust_Name, Cust_Password)
    cur.execute(query)
    user_record = cur.fetchone() 
    if user_record:
        print('\n')
        print('*'*30)
        print("Login Successful!")
        print('*'*30)
        count=1
        return count
    else:
        print('\n')
        print('*'*30)
        print("Invalid username or password")
        print('*'*30)
        print('\n')
def admin():
    cur=db.cursor()
    Admin_Name=input("Enter your Name:")
    Admin_Password=input("Enter your Password:")
    print('='*50)
    query="select * from admin where Admin_Name='{}' and Admin_Password='{}'".format(Admin_Name,
                                                                                     Admin_Password)
    cur.execute(query)
    user_record = cur.fetchone() 
    if user_record:
        print('\n')
        print('*'*30)
        print("Login Successful!")
        print('*'*30)
        count=1
        return count
    else:
        print('\n')
        print('*'*30)
        print("Invalid username or password.")
        print('*'*30)
        print('\n')
        
#CUSTOMER
def View_available_flights():
    while True:
        print('\n')
        print('1.View flight according to Name')
        print('2.View flight according to Departure city')
        print('3.View flight according to Arrival city')
        print('4.View flight according to your price range')
        print('5.Back')
        print('='*50)
        ch=int(input('Enter your Choice:'))
        print('='*50)
        if ch==1:
            cur=db.cursor()
            fn=input('Enter Flight Name to display=')
            print('='*50)
            print('\n')
            query="select * from flight where Flight_Name='{}'".format(fn)
            cur.execute(query)
            column=[i[0] for i in cur.description]
            table=pt(column)
            for row in cur:
                table.add_row(row)
            print(table)
        elif ch==2:
            cur=db.cursor()
            fn=input('Enter Departure city to display=')
            print('='*50)
            print('\n')
            query="select * from flight where Departure='{}'".format(fn)
            cur.execute(query)
            column=[i[0] for i in cur.description]
            table=pt(column)
            for row in cur:
                table.add_row(row)
            print(table)
        elif ch==3:
            cur=db.cursor()
            fn=input('Enter Arrival city to display=')
            print('='*50)
            print('\n')
            query="select * from flight where Arrival='{}'".format(fn)
            cur.execute(query)
            column=[i[0] for i in cur.description]
            table=pt(column)
            for row in cur:
                table.add_row(row)
            print(table)
        elif ch==4:
            cur=db.cursor()
            mi=int(input('Enter Minimum price='))
            mi=mi-1
            ma=int(input('Enter Maximum price='))
            ma=ma+1
            print('='*50)
            print('\n')
            query="select * from flight where Price > {} and Price < {}".format(mi,ma)
            cur.execute(query)
            column=[i[0] for i in cur.description]
            table=pt(column)
            for row in cur:
                table.add_row(row)
            print(table)
        elif ch==5:
            break
        else:
            print('\n')
            print('*'*30)
            print('invalid choice')
            print('*'*30)
            print('\n')

def Book_seats():
    cur=db.cursor()
    fn=int(input('Enter flight no='))
    print('='*50)
    print('\n')
    query='select Flight_Number from flight where Flight_Number={}'.format(fn)
    cur.execute(query)
    result=cur.fetchone()
    if result:
        query="select * from flight where Flight_Number={}".format(fn)
        cur.execute(query)
        column=[i[0] for i in cur.description]
        table=pt(column)
        for row in cur:
            table.add_row(row)
        print(table)
        print('\n')
        print('ALL THE AVAILABLE CLASS IN THIS FLIGHT')
        print('1.First class')
        print('2.Business class')
        print('3.Premium Economy class')
        print('4.Economy class')
        print('='*50)
        c=int(input('Enter class='))
        print('='*50)
        print('\n')
        if c==1:
            cl='First class'
            df = pd.read_csv("First Class Seats.csv")
            table = pt()
            header = list(df.columns)
            data = list(map(list, np.array(df)))
            table.field_names = header
            for row in data:
                table.add_row(row)
            print(table)
        elif c==2:
            cl='Business class'
            df = pd.read_csv("Bussiness Class Seats.csv")
            table = pt()
            header = list(df.columns)
            data = list(map(list, np.array(df)))
            table.field_names = header
            for row in data:
                table.add_row(row)
            print(table)
        elif c==3:
            cl='Premium Economy class'
            df = pd.read_csv("Premium Economy Class Seats.csv")
            table = pt()
            header = list(df.columns)
            data = list(map(list, np.array(df)))
            table.field_names = header
            for row in data:
                table.add_row(row)
            print(table)
        elif c==4:
            cl='Economy class'
            df = pd.read_csv("Economy Class Seats.csv")
            table = pt()
            header = list(df.columns)
            data = list(map(list, np.array(df)))
            table.field_names = header
            for row in data:
                table.add_row(row)
            print(table)
        print('\n')
        print('='*50)
        cul=input('Enter cloumn_l=')
        ro=int(input('Enter row_no='))
        tic=rd.randint(10000000,99999999)
        print('='*50)
        pn=input('ENTER your phone no=')
        print('='*50)
        query='select Cust_id from customer where Cust_PhoneNo={}'.format(pn)
        cur.execute(query)
        result=cur.fetchone()
        if result:
            Cid=result[0]
            query="insert into booking values({},{},'{}',{},'{}',{})".format(Cid,tic,cl,ro,cul,fn)
            cur.execute(query)
            db.commit()
            print('\n')
            print('*'*30)
            print("Booking Completed!")
            print('='*30)
            print('Your Ticket Number is:',tic)
            print('*'*30)
            print('\n')
        else:
            print('\n')
            print('Invalid Phone Number!')
            print('Please check the number or register as a new customer')
            print('\n')
    else:
        print('\n')
        print('Invalid Flight Number!')
        print('Please check the Flight Number')
        print('\n')
        
def View_booking_detail():
     while True:
         print('\n')
         print("1.View booking according to Ticket Number")
         print("2.View all booking")
         print("3.Back")
         print('='*50)
         ch=int(input('Enter your Choice:'))
         print('='*50)
         if ch==1:
             cur=db.cursor()
             tic=input('Enter Your to Ticket Number=')
             print('='*50)
             print('\n')
             query="select * from booking where Ticket_No='{}'".format(tic)
             cur.execute(query)
             column=[i[0] for i in cur.description]
             table=pt(column)
             for row in cur:
                 table.add_row(row)
             print(table)
         elif ch==2:
             cur=db.cursor()
             pn=input('ENTER your phone no=')
             print('='*50)
             print('\n')
             query='select Cust_id from customer where Cust_PhoneNo={}'.format(pn)
             cur.execute(query)
             result=cur.fetchone()
             if result:
                 Cid=result[0]
                 cur=db.cursor()
                 query="select * from booking where Cust_id={}".format(Cid)
                 cur.execute(query)
                 column=[i[0] for i in cur.description]
                 table=pt(column)
                 for row in cur:
                     table.add_row(row)
                 print(table)
             else:
                 print('*'*30)
                 print('Invalid Phone Number!')
                 print('Please check the number or register as a new customer')
                 print('*'*30)
        
         elif ch==3:
             break
         else:
             print('\n')
             print('*'*30)
             print('invalid choice')
             print('*'*30)
             print('\n')
    
#ADMIN--Flights
def Add_Flights():
    cur=db.cursor()
    fn=rd.randint(10000,99999)
    fl=input("Enter FLight Name:")
    dp=input("Enter Departure City:")
    ar=input("Enter Arrival City:")
    pr=int(input("Enter Price:"))
    print('='*50)
    query="insert into flight values({},'{}','{}','{}',{})".format(fn,fl,dp,ar,pr)
    cur.execute(query)
    db.commit()
    print('\n')
    print('*'*30)
    print("New Flight Added Successfully")
    print('='*50)
    print('Flight Number=',fn)
    print('*'*30)
    print('\n')

def Cancel_Flights():
    while True:
        print('\n')
        print("1.Cancel by Flights_Number")
        print("2.Cancel by Flight_Name")
        print("3.Cancel by Departure City")
        print("4.Cancel by Arrival City")
        print("5.Back")
        print('='*50)
        ch=int(input('Enter your Choice:'))
        print('='*50)
        if ch==1:
            cur=db.cursor()
            fn=input("Enter Flight_Number for cancel :")
            query="delete from flight where Flight_Number='{}'".format(fn)
            cur.execute(query)
            db.commit()
            r=input("Reason For Flight Cancalation=")
            print('='*50)
            print('\n')
            print('*'*30)
            print("The Flight Has Been Canceld Due To",r)
            print('*'*30)
            print('\n')
        elif ch==2:
            cur=db.cursor()
            fn=input("Enter Flight Name for cancel=")
            query="delete from flight where Flight_Name='{}'".format(fn)
            cur.execute(query)
            db.commit()
            r=input("Reason For Flight Cancalation=")
            print('='*50)
            print('\n')
            print('*'*30)
            print('All Flight of',fn,'has been Cancal due to',r)
            print('*'*30)
            print('\n')
        elif ch==3:
            cur=db.cursor()
            fn=input("Enter Departure for cancel=")
            query="delete from flight where Departure='{}'".format(fn)
            cur.execute(query)
            db.commit()
            r=input("Reason For Flight Cancalation=")
            print('='*50)
            print('\n')
            print('*'*30)
            print('All Flight from',fn,'has been Cancal due to',r)
            print('*'*30)
            print('\n')
        elif ch==4:
            cur=db.cursor()
            fn=input("Enter Arrival for cancel :")
            query="delete from flight where Arrival='{}'".format(fn)
            cur.execute(query)
            db.commit()
            r=input("Reason For Flight Cancalation=")
            print('='*50)
            print('\n')
            print('*'*30)
            print('All Flights to',fn,'has been Cancal due to',r)
            print('*'*30)
            print('\n')
        elif ch==5:
            break
        else:
            print('\n')
            print('*'*30)
            print('invalid choice')
            print('*'*30)
            print('\n')
def Display_Flights():
    while True:
        print('\n')
        print("1.Display by Flight_Number")
        print("2.Display by Flight_Name")
        print("3.Display by Departure")
        print("4.Display by Arrival")
        print("5.Display by price range")
        print("6.Display all flights")
        print("7.Back")
        print('='*50)
        ch=int(input('Enter your Choice:'))
        print('='*50)
        if ch==1:
            cur=db.cursor()
            fn=int(input('Enter Flight Number to display='))
            print('='*50)
            print('\n')
            query="select * from flight where Flight_Number='{}'".format(fn)
            cur.execute(query)
            column=[i[0] for i in cur.description]
            table=pt(column)
            for row in cur:
                table.add_row(row)
            print(table)
        elif ch==2:
            cur=db.cursor()
            fn=input('Enter Flight Name to display=')
            print('='*50)
            print('\n')
            query="select * from flight where Flight_Name='{}'".format(fn)
            cur.execute(query)
            column=[i[0] for i in cur.description]
            table=pt(column)
            for row in cur:
                table.add_row(row)
            print(table)
        elif ch==3:
            cur=db.cursor()
            fn=input('Enter Departure city to display=')
            print('='*50)
            print('\n')
            query="select * from flight where Departure='{}'".format(fn)
            cur.execute(query)
            column=[i[0] for i in cur.description]
            table=pt(column)
            for row in cur:
                table.add_row(row)
            print(table)
        elif ch==4:
            cur=db.cursor()
            fn=input('Enter Arrival city to display=')
            print('='*50)
            print('\n')
            query="select * from flight where Arrival='{}'".format(fn)
            cur.execute(query)
            column=[i[0] for i in cur.description]
            table=pt(column)
            for row in cur:
                table.add_row(row)
            print(table)
        elif ch==5:
            cur=db.cursor()
            mi=int(input('Enter Minimum price='))
            mi=mi-1
            ma=int(input('Enter Maximum price='))
            ma=ma+1
            print('='*50)
            print('\n')
            query="select * from flight where Price > {} and Price < {}".format(mi,ma)
            cur.execute(query)
            column=[i[0] for i in cur.description]
            table=pt(column)
            for row in cur:
                table.add_row(row)
            print(table)  
        elif ch==6:
            cur=db.cursor()
            print('\n')
            query="select * from flight"
            cur.execute(query)
            column=[i[0] for i in cur.description]
            table=pt(column)
            for row in cur:
                table.add_row(row)
            print(table)
            print('\n')
        elif ch==7:
            break
        else:
            print('\n')
            print('*'*30)
            print('invalid choice')
            print('*'*30)
            print('\n')
            
def Update_Flights():
    while True:
        print('\n')
        print("1.Update the Flights_Name")
        print("2.Update the Departure City")
        print("3.Update the Arrival City")
        print("4.Update the Price")
        print("5.Back")
        print('='*50)
        ch=int(input('Enter your Choice:'))
        print('='*50)
        if ch==1:
            cur=db.cursor()
            fn=int(input("Enter Flight_Number to Update="))
            fl=input("Enter the New Flight_Name=")
            print('='*50)
            query="update flight set Flight_Name='{}' where Flight_Number={}".format(fl,fn)
            cur.execute(query)
            db.commit()
            print('\n')
            print('*'*30)
            print("Data Updated Successfully")
            print('*'*30)
        elif ch==2:
            cur=db.cursor()
            fn=int(input("Enter Flight_Number to Update="))
            dp=input("Enter the New Departure City=")
            print('='*50)
            query="update flight set Departure='{}' where Flight_Number={}".format(dp,fn)
            cur.execute(query)
            db.commit()
            print('\n')
            print('*'*30)
            print("Data Updated Successfully")
            print('*'*30)
        elif ch==3:
            cur=db.cursor()
            fn=int(input("Enter Flight_Number to Update="))
            ar=input("Enter the New Arrival City=")
            print('='*50)
            query="update flight set Arrival='{}' where Flight_Number={}".format(ar,fn)
            cur.execute(query)
            db.commit()
            print('\n')
            print('*'*30)
            print("Data Updated Successfully")
            print('*'*30)
        elif ch==4:
            cur=db.cursor()
            fn=int(input("Enter Flight_Number to Update="))
            pr=input("Enter the New Price to Update=")
            print('='*50)
            query="update flight set Price='{}' where Flight_Number={}".format(pr,fn)
            cur.execute(query)
            db.commit()
            print('\n')
            print('*'*30)
            print("Data Updated Successfully")
            print('*'*30)
        elif ch==5:
            break
        else:
            print('\n')
            print('*'*30)
            print('invalid choice')
            print('*'*30)
            print('\n')
#ADMIN--customer_management--Customer_Records
def display_all_Customer_Records():
    cur=db.cursor()
    query="select * from customer"
    cur.execute(query)
    column=[i[0] for i in cur.description]
    table=pt(column)
    for row in cur:
        table.add_row(row)
    print(table)
 
def Search_Customer_Records():
    while True:
        cur=db.cursor()
        print('\n')
        print('1.Search by Cust_Id')
        print('2.Search by Cust_Name')
        print('3.Search by Cust_Email')
        print('4.Search by Cust_PhoneNo')
        print('5.Back')
        print('='*50)
        ch=int(input('Enter your Choice:'))
        print('='*50)
        if ch==1:
            cur=db.cursor()
            Id=int(input('Enter Cust_Id='))
            print('='*50)
            print('\n')
            query="select * from customer where Cust_Id={}".format(Id)
            cur.execute(query)
            column=[i[0] for i in cur.description]
            table=pt(column)
            for row in cur:
                table.add_row(row)
            print(table)
        elif ch==2:
            cur=db.cursor()
            Name=input('Enter Cust_Name=')
            print('='*50)
            print('\n')
            query="select * from customer where Cust_Name='{}'".format(Name)
            cur.execute(query)
            column=[i[0] for i in cur.description]
            table=pt(column)
            for row in cur:
                table.add_row(row)
            print(table)
        elif ch==3:
            cur=db.cursor()
            Email=input('Enter Cust_Email=')
            print('='*50)
            print('\n')
            query="select * from customer where Cust_Email='{}'".format(Email)
            cur.execute(query)
            column=[i[0] for i in cur.description]
            table=pt(column)
            for row in cur:
                table.add_row(row)
            print(table)
        elif ch==4:
            cur=db.cursor()
            PhoneNo=input('Enter Cust_PhoneNo=')
            print('='*50)
            print('\n')
            query="select * from customer where Cust_PhoneNo='{}'".format(PhoneNo)
            cur.execute(query)
            column=[i[0] for i in cur.description]
            table=pt(column)
            for row in cur:
                table.add_row(row)
            print(table)
        elif ch==5:
            break
        else:
            print('\n')
            print('*'*30)
            print('invalid choice')
            print('*'*30)
def Delete_Customer_Records():
    while True:
        cur=db.cursor()
        print('\n')
        print('1.Delete by Cust_Id')
        print('2.Delete by Cust_Name')
        print('3.Delete by Cust_Email')
        print('4.Delete by Cust_PhoneNo')
        print('5.Back')
        print('='*50)
        ch=int(input('Enter your Choice:'))
        print('='*50)
        if ch==1:
            cur=db.cursor()
            Id=int(input('Enter The Cust_Id='))
            query="delete from customer where Cust_id={}".format(Id)
            print('='*50)
            cur.execute(query)
            db.commit()
            print('\n')
            print('*'*30)
            print("Data Deleted Successfully")
            print('*'*30)
        elif ch==2:
            cur=db.cursor()
            Name=input('Enter Cust_Name=')
            query="delete from customer where Cust_Name='{}'".format(Name)
            print('='*50)
            cur.execute(query)
            db.commit()
            print('\n')
            print('*'*30)
            print("Data Deleted Successfully")
            print('*'*30)
            print('\n')
        elif ch==3:
            cur=db.cursor()
            Email=input('Enter Cust_Email=')
            query="delete from customer where Cust_Email='{}'".format(Email)
            print('='*50)
            cur.execute(query)
            db.commit()
            print('\n')
            print('*'*30)
            print("Data Deleted Successfully")
            print('*'*30)
            print('\n')
        elif ch==4:
            cur=db.cursor()
            PhoneNo=input('Enter Cust_PhoneNo=')
            query="delete from customer where Cust_PhoneNo='{}'".format(PhoneNo)
            print('='*50)
            cur.execute(query)
            db.commit()
            print('\n')
            print('*'*30)
            print("Data Deleted Successfully")
            print('*'*30)
            print('\n')
        elif ch==5:
            break
        else:
            print('\n')
            print('*'*30)
            print('invalid choice')
            print('*'*30)
def Update_Customer_Records():
    while True:
        cur=db.cursor()
        print('\n')
        print('1.Update Cust_Name')
        print('2.Update Cust_Email')
        print('3.Update Cust_PhoneNo')
        print('4.Back')
        print('='*50)
        ch=int(input('Enter your Choice:'))
        print('='*50)
        if ch==1:
            cur=db.cursor()
            Id=int(input('Enter Cust_Id='))
            Name=input('Enter the New Cust_Name=')
            print('='*50)
            query="update customer set Cust_Name='{}' where Cust_Id={}".format(Name,Id)
            cur.execute(query)
            db.commit()
            print('\n')
            print('*'*30)
            print("Data Updated Successfully")
            print('*'*30)
        elif ch==2:
            cur=db.cursor()
            Id=int(input('Enter Cust_Id='))
            Email=input('Enter New Cust_Email=')
            print('='*50)
            query="update customer set Cust_Email='{}' where Cust_Id={}".format(Email,Id)
            cur.execute(query)
            db.commit()
            print('\n')
            print('*'*30)
            print("Data Updated Successfully")
            print('*'*30)
        elif ch==3:
            cur=db.cursor()
            Id=int(input('Enter Cust_Id='))
            PhoneNo=input('Enter New Cust_PhoneNo=')
            print('='*50)
            query="update customer set Cust_PhoneNo={} where Cust_Id={}".format(PhoneNo,Id)
            cur.execute(query)
            db.commit()
            print('\n')
            print('*'*30)
            print("Data Updated Successfully")
            print('*'*30)
        elif ch==4:
            break
        else:
            print('\n')
            print('*'*30)
            print('invalid choice')
            print('*'*30)    
def Add_Customer_Records():
    cur=db.cursor()
    Cust_Name=input("Enter your Name:")
    Cust_Email=input("Enter you Email:")
    Cust_PhoneNo=int(input("Enter your Phone Number:"))
    Cust_Password=input("Enter your Password:")
    print('='*50)
    query="insert into customer (Cust_Name,Cust_Email,Cust_PhoneNo,Cust_Password) values('{}','{}',{},'{}')".format(Cust_Name,
                                                                                                                    Cust_Email,
                                                                                                                    Cust_PhoneNo,
                                                                                                                    Cust_Password)
    cur.execute(query)
    db.commit()
    print('\n')
    print('*'*30)
    print("Data Inserted Successfully")
    print('*'*30)
#ADMIN--customer_management--Customer_Bookings
def Display_Customer_Booking():
    while True:
        print('\n')
        print('1.Display all Customer Booking')
        print('2.Display Customer Booking by Ticket Number')
        print('3.Display Customer Booking by Customer ID')
        print('4.Back')
        print('='*50)
        ch=int(input("Enter your Choice:"))
        print('='*50)
        if ch==1:
            cur=db.cursor()
            print('\n')
            query="select * from booking"
            cur.execute(query)
            column=[i[0] for i in cur.description]
            table=pt(column)
            for row in cur:
                table.add_row(row)
            print(table)
        elif ch==2:
            cur=db.cursor()
            tic=int(input('Enter Ticket Number='))
            print('='*50)
            print('\n')
            query="select * from booking where Ticket_No={}".format(tic)
            cur.execute(query)
            column=[i[0] for i in cur.description]
            table=pt(column)
            for row in cur:
                table.add_row(row)
            print(table)
        elif ch==3:
            cur=db.cursor()
            Id=int(input('Enter Customer ID='))
            print('='*50)
            print('\n')
            query="select * from booking where Cust_id={}".format(Id)
            cur.execute(query)
            column=[i[0] for i in cur.description]
            table=pt(column)
            for row in cur:
                table.add_row(row)
            print(table)
        elif ch==4:
            break
        else:
            print('\n')
            print('*'*30)
            print('invalid choice')
            print('*'*30)
def Cancal_Customer_Booking():
    while True:
        print('\n')
        print("1.Cancel Customer Booking by Ticket Number")
        print("2.Cancel Customer Booking by Customer ID")
        print("3.Back")
        print('='*50)
        ch=int(input('Enter your Choice:'))
        print('='*50)
        if ch==1:
            cur=db.cursor()
            tic=input("Enter Ticket Number for Cancelation=")
            print('='*50)
            query="delete from booking where Ticket_No={}".format(tic)
            cur.execute(query)
            db.commit()
            print('\n')
            print('*'*30)
            print("The Booking Has Been Canceld")
            print('*'*30)
        elif ch==2:
            cur=db.cursor()
            tic=input("Enter Customer ID for Cancelation=")
            print('='*50)
            query="delete from booking where Cust_id={}".format(tic)
            cur.execute(query)
            db.commit()
            print('\n')
            print('*'*30)
            print("The Booking Has Been Canceld")
            print('*'*30)
        elif ch==3:
            break
        else:
            print('\n')
            print('*'*30)
            print('invalid choice')
            print('*'*30)
# view graph
def view_graph():
    while True:
        print('\n')
        print('1.bookings vs customer')
        print('2.bookings vs flights')
        print('3.back')
        print('='*50)
        ch=int(input('Enter your Choice:'))
        print('='*50)
        if ch==1:
            while True:
                print('\n')
                print('1.Bar Chart')
                print('2.Line Chart')
                print('3.Pie Chart')
                print('4.back')
                print('='*50)
                ch=int(input('Enter your Choice:'))
                print('='*50)
                if ch==1:
                    cur=db.cursor()
                    query='select Cust_id,count(Ticket_No) from booking group by Cust_id order by Cust_id'
                    cur.execute(query)
                    result=cur.fetchall()
                    plt.figure(figsize=(10, 6))
                    if result:
                        Cid=[row[0]for row in result]
                        bc=[row[1]for row in result]
                        x_position=np.arange(len(Cid))
                        plt.bar(x_position,bc,
                                color='c')
                    plt.xticks(x_position,[str(cid) for cid in Cid],rotation=45)
                    plt.yticks(bc)
                    plt.xlabel(" Customer Id ")
                    plt.ylabel("No. of Bookings")
                    plt.title('Booking Frequency by Customer (Bar Chart)',
                              fontsize=16,
                              color='darkblue',
                              weight='bold')
                    plt.show()
                    print('\n')
                    print('*'*30)
                    print('Chart Displayed Successfully')
                    print('*'*30)
                elif ch==2:
                    cur=db.cursor()
                    query='select Cust_id,count(Ticket_No) from booking group by Cust_id order by Cust_id'
                    cur.execute(query)
                    result=cur.fetchall()
                    plt.figure(figsize=(10, 6))
                    if result:
                        Cid=[row[0]for row in result]
                        bc=[row[1]for row in result]
                        x_position=np.arange(len(Cid))
                        plt.plot(x_position,bc,
                                 marker='*',
                                 markersize=10,
                                 color='c',
                                 linewidth=2,
                                 linestyle='dashdot')
                    plt.xticks(x_position,[str(cid) for cid in Cid],rotation=45)
                    plt.yticks(bc)
                    plt.xlabel(" Customer Id ") #add the Label on x-axis
                    plt.ylabel("No. of Bookings") #add the Label on y-axis
                    plt.title('Booking Frequency by Customer (Line Chart)',
                              fontsize=16,
                              color='darkblue',
                              weight='bold')
                    plt.show()
                    print('\n')
                    print('*'*30)
                    print('Chart Displayed Successfully')
                    print('*'*30)
                elif ch==3:
                    cur=db.cursor()
                    query='select Cust_id,count(Ticket_No) from booking group by Cust_id order by Cust_id'
                    cur.execute(query)
                    result=cur.fetchall()
                    if result:
                        Cid=[row[0]for row in result]
                        bc=[row[1]for row in result]
                        df=pd.DataFrame({'No. of Bookings':bc},index=Cid)
                    df.plot(kind='pie',
                            y='No. of Bookings',
                            legend=False,
                            autopct='%1.1f%%',       
                            startangle=90)
                    plt.title('Booking Frequency by Customer (Pie Chart)',
                              fontsize=16,
                              color='darkblue',
                              weight='bold')
                    plt.show()
                    print('\n')
                    print('*'*30)
                    print('Chart Displayed Successfully')
                    print('*'*30)
                elif ch==4:
                    break
                else:
                    print('\n')
                    print('*'*30)
                    print('invalid choice')
                    print('*'*30)   
        elif ch==2:
            while True:
                print('\n')
                print('1.Bar Chart')
                print('2.Line Chart')
                print('3.Pie Chart')
                print('4.back')
                print('='*50)
                ch=int(input('Enter your Choice:'))
                print('='*50)
                if ch==1:
                    cur=db.cursor()
                    query='select Flight_No,count(*) from booking group by Flight_No'
                    cur.execute(query)
                    result=cur.fetchall()
                    plt.figure(figsize=(10, 6))
                    if result:
                        Fno=[row[0]for row in result]
                        bc=[row[1]for row in result]
                        x_position=np.arange(len(Fno))
                        plt.bar(x_position, bc,
                                color='y')
                    plt.xticks(x_position,[str(fno) for fno in Fno],rotation=45)
                    plt.yticks(bc)
                    plt.xlabel(" Flight Number ") #add the Label on x-axis
                    plt.ylabel("No. of Bookings") #add the Label on y-axis
                    plt.title('Booking Frequency by Customer (Bar Chart)',
                              fontsize=16,
                              color='darkblue',
                              weight='bold')
                    plt.show()
                    print('\n')
                    print('*'*30)
                    print('Chart Displayed Successfully')
                    print('*'*30)
                elif ch==2:
                    cur=db.cursor()
                    query='select Flight_No,count(*) from booking group by Flight_No'
                    cur.execute(query)
                    result=cur.fetchall()
                    plt.figure(figsize=(10, 6))
                    if result:
                        Fno=[row[0]for row in result]
                        bc=[row[1]for row in result]
                        x_position=np.arange(len(Fno))
                        plt.plot(x_position, bc,
                                 marker='*',
                                 markersize=10,
                                 color='y',
                                 linewidth=2,
                                 linestyle='dashdot')
                    plt.xticks(x_position,[str(fno) for fno in Fno],rotation=45)
                    plt.yticks(bc)
                    plt.xlabel(" Flight Number ")
                    plt.ylabel("No. of Bookings")
                    plt.title('Booking Frequency by Customer (Line Chart)',
                              fontsize=16,
                              color='darkblue',
                              weight='bold')
                    plt.show()
                    print('\n')
                    print('*'*30)
                    print('Chart Displayed Successfully')
                    print('*'*30)
                elif ch==3:
                    cur=db.cursor()
                    query='select Flight_No,count(*) from booking group by Flight_No'
                    cur.execute(query)
                    result=cur.fetchall()
                    if result:
                        Cid=[row[0]for row in result]
                        bc=[row[1]for row in result]
                        df=pd.DataFrame({'No. of Bookings':bc},index=Cid)
                    df.plot(kind='pie',
                            y='No. of Bookings',
                            legend=False,
                            autopct='%1.1f%%',       
                            startangle=90)
                    plt.title('Booking Frequency by Customer (Pie Chart)',
                              fontsize=16,
                              color='darkblue',
                              weight='bold')
                    plt.show()
                    print('\n')
                    print('*'*30)
                    print('Chart Displayed Successfully')
                    print('*'*30)
                elif ch==4:
                    break
                else:
                    print('\n')
                    print('*'*30)
                    print('invalid choice')
                    print('*'*30)
        elif ch==3:
            break
        else:
            print('\n')
            print('*'*30)
            print('invalid choice')
            print('*'*30)
while True:
    print('\n')
    print('*'*15+'Welcome to airway reservation system'+'*'*15)
    print('1.Register as a new customer')
    print('2.login as customer')
    print('3.login as admin')
    print('='*50)
    ch=int(input('Enter your Choice:'))
    print('='*50)
    if ch==1:
        Register()
    elif ch==2:
        b=login()
        if b==1:
            while True:
                print('\n')
                print('1.View available flights')
                print('2.Book seats')
                print('3.View booking detail')
                print('4.Exit')
                print('='*50)
                ch=int(input("Enter your Choice:"))
                print('='*50)
                if ch==1:
                    View_available_flights()
                elif ch==2:
                    Book_seats()
                elif ch==3:
                    View_booking_detail()
                elif ch==4:
                    break
                else:
                    print('\n')
                    print('*'*30)
                    print('invalid choice')
                    print('*'*30)
# elif ch==3                    
    elif ch==3:
        q=admin()
        if q==1:
            while True:
                print('\n')
                print('1.Flight')
                print('2.Customer management')
                print('3.View Graph')
                print('4.Exit')
                print('='*50)
                ch=int(input("Enter your Choice:"))
                print('='*50)
                if ch==1:
                    while True:
                        print('\n')
                        print("1.Add Flights")
                        print("2.Update Flights")
                        print("3.Cancel Flights")
                        print("4.Display Flights")
                        print("5.Back")
                        print("="*50)
                        ch=int(input("Enter Your Choice:"))
                        print("="*50)
                        if ch==1:
                            Add_Flights()
                        elif ch==2:
                            Update_Flights()
                        elif ch==3:
                            Cancel_Flights()
                        elif ch==4:
                            Display_Flights()
                        elif ch==5:
                            break
                        else:
                            print('\n')
                            print('*'*30)
                            print('invalid choice')
                            print('*'*30)
                elif ch==2:
                    while True:
                        print('\n')
                        print('1.Customer Records')
                        print('2.Customer Bookings')
                        print('3.Back')
                        print('='*50)
                        ch=int(input("Enter your Choice:"))
                        print('='*50)
                        if ch==1:
                            while True:
                                print('\n')
                                print('1.Display all Customer Records')
                                print('2.Search Customer Records')
                                print('3.Update Customer Records')
                                print('4.Delete Customer Records')
                                print('5.Add Customer Records')
                                print('6.Back')
                                print('='*50)
                                ch=int(input("Enter your Choice:"))
                                print('='*50)
                                if ch==1:
                                    display_all_Customer_Records()
                                elif ch==2:
                                    Search_Customer_Records()
                                elif ch==3:
                                    Update_Customer_Records()
                                elif ch==4:
                                    Delete_Customer_Records()
                                elif ch==5:
                                    Add_Customer_Records()
                                elif ch==6:
                                    break
                                else:
                                    print('\n')
                                    print('*'*30)
                                    print('invalid choice')
                                    print('*'*30)
                        elif ch==2:
                            while True:
                                print('\n')
                                print('1.Display Customer Bookings')
                                print('2.Cancal Customer Booking')
                                print('3.Back')
                                print('='*50)
                                ch=int(input("Enter your Choice:"))
                                print('='*50)
                                if ch==1:
                                    Display_Customer_Booking()
                                elif ch==2:
                                    Cancal_Customer_Booking()
                                elif ch==3:
                                    break
                                else:
                                    print('\n')
                                    print('*'*30)
                                    print('invalid choice')
                                    print('*'*30)
                        elif ch==3:
                            break
                        else:
                            print('\n')
                            print('*'*30)
                            print('invalid choice')
                            print('*'*30)
                elif ch==3:
                    view_graph()
                elif ch==4:
                    break
                else:
                    print('\n')
                    print('*'*30)
                    print('invalid choice')
                    print('*'*30)      
    else:
        print('\n')
        print('*'*30)
        print('invalid choice')
        print('*'*30)