import mysql.connector as a
con=a.connect(user="root",password="root",host="localhost",database="hoteldb")
c=con.cursor()

sql1="USE hoteldb"
c.execute(sql1)

sql2="DROP TABLE IF EXISTS checkin"
c.execute(sql2)

sql3="DROP TABLE IF EXISTS checkout"
c.execute(sql3)

sql4="CREATE TABLE checkin (s_no int NOT NULL AUTO_INCREMENT PRIMARY KEY,numberofguests int NOT NULL,guests_names varchar(100) NOT NULL,id_number int NOT NULL,date DATE)"
c.execute(sql4)

sql5="CREATE TABLE checkout (serial int NOT NULL AUTO_INCREMENT PRIMARY KEY,numberofguests int NOT NULL,date DATE,days_stayed int NOT NULL, fare int NOT NULL,totalbill int NOT NULL)"
c.execute(sql5)

con.commit()
