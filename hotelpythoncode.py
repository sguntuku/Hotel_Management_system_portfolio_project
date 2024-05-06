import mysql.connector as a
con = a.connect(host="localhost", user="root", password="root", database="hoteldb")

def checkin():
    x=int(input("enter the serial number: "))
    y=int(input("enter number of guests: "))
    z=input("enter guests name: ")
    m=int(input("enter the id"))
    n=input("date: ")
    data = (x,y,z,m,n)
    sql='insert into checkin values(%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("data entered successfully")
    main()
def checkout():
    x=int(input("enter the serial number: "))
    y=int(input("number of guests: "))
    z=input("enter date of exit: ")
    m=int(input("enter days stayed: "))
    n=int(input("fare: "))
    totalbill=int(n*y*m)
    data = (x,y,z,m,n,totalbill)
    sql='insert into checkout values(%s,%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("total fare: ",totalbill)
    print("data entered successfully")
    main()
def main():
    print("1.checkin 2.checkout")
    i= int(input("enter the number:1.checkin 2.checkout "))
    if i==1:
           checkin()
    elif i==2:
           checkout()
    main()
main()
