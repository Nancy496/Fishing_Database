#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install mysql-connector-python==8.0.17


# In[13]:


import mysql.connector as conn
mydb = conn.connect(
    host="localhost",
    user="root",
    password="nancywachira",
    database="Fishing")
print("Success")


# In[15]:


mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS Fishing")
print("Database created")


# In[16]:


mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)


# In[18]:


import mysql.connector as conn

mydb = conn.connect(
    host="localhost",
    user="root",
    password="nancywachira",
    database="Fishing")

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS Boat_Table (Boat_Id INT PRIMARY KEY,Boat_Name VARCHAR(100),Boat_Size INT,Boat_Lenght INT, Station_Id INT, Boat_Capacity INT, Fishing Boolean)")
print("Boat_Table created")


# In[19]:


import mysql.connector as conn

mydb = conn.connect(
    host="localhost",
    user="root",
    password="nancywachira",
    database="Fishing")

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Fisher_Table (FisherPerson_Id INT PRIMARY KEY,Fisher_Name VARCHAR(100),Boat_Id INT, Phone_Number INT, Email_Address VARCHAR(100), Age INT)")
print("Fisher_table created")


# In[20]:


import mysql.connector as conn

mydb = conn.connect(
    host="localhost",
    user="root",
    password="nancywachira",
    database="Fishing")

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Owner_Table (Owner_Id INT PRIMARY KEY, Owner_Name VARCHAR(100),Boat_Id INT, Phone_Number INT, Email_Address VARCHAR(100))")
print("Owner_Table created")


# In[21]:


import mysql.connector as conn

mydb = conn.connect(
    host="localhost",
    user="root",
    password="nancywachira",
    database="Fishing")

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Station (Station_Id INT PRIMARY KEY, Station_Name VARCHAR(100), Address VARCHAR(100))")
print("Station_Table created")


# In[29]:


import mysql.connector as conn
import csv
mydb = conn.connect(
    host="localhost",
    user="root",
    password="nancywachira",
    database="Fishing")

mycursor = mydb.cursor()

# Read from csv file
Njoki = csv.reader(open(r"C:\Users\User\Downloads\Boat_Table (2).csv",'r'))
next(Njoki) #Skip the first row 
    
    #insert records line by line
for row in Njoki:
    mycursor.execute('INSERT IGNORE INTO Boat_Table(Boat_ID, Boat_Name, Boat_Size, Boat_Lenght, Station_ID, Boat_Capacity, Fishing) VALUES(%s,%s,%s,%s,%s,%s,%s)',row)
mydb.commit() 
print("Records added to Boat_Table")


# In[30]:


import mysql.connector as conn
import csv
mydb = conn.connect(
    host="localhost",
    user="root",
    password="nancywachira",
    database="Fishing")

mycursor = mydb.cursor()

# Read from csv file
Njoki1 = csv.reader(open(r"C:\Users\User\Downloads\Fisher_Table.csv",'r'))
next(Njoki1) #Skip the first row 
    
    #insert records line by line
for row in Njoki1:
    mycursor.execute('INSERT IGNORE INTO Fisher_Table(FisherPerson_ID, Fisher_Name, Boat_Id, Phone_Number, Email_Address, Age) VALUES(%s,%s,%s,%s,%s,%s)',row)
mydb.commit() 
print("Records added to Fisher_Table")


# In[32]:


import mysql.connector as conn
import csv
mydb = conn.connect(
    host="localhost",
    user="root",
    password="nancywachira",
    database="Fishing")

mycursor = mydb.cursor()

# Read from csv file
Njoki2 = csv.reader(open(r"C:\Users\User\Downloads\Owner_Table.csv",'r'))
next(Njoki2) #Skip the first row 
    
    #insert records line by line
for row in Njoki2:
    mycursor.execute('INSERT IGNORE INTO Owner_Table(Owner_ID, Owner_Name, Boat_Id, Phone_Number, Email_Address) VALUES(%s,%s,%s,%s,%s)',row)
mydb.commit() 
print("Records added to Owner_Table")


# In[2]:


import mysql.connector as conn
import csv
mydb = conn.connect(
    host="localhost",
    user="root",
    password="nancywachira",
    database="Fishing")

mycursor = mydb.cursor()

# Read from csv file
Njoki3 = csv.reader(open(r"C:\Users\User\Downloads\Station_2.csv",'r'))
next(Njoki3) #Skip the first row 
    
    #insert records line by line
for row in Njoki3:
    mycursor.execute('INSERT IGNORE INTO Station(Station_ID, Station_Name, Address) VALUES(%s,%s,%s)',row)
mydb.commit() 
print("Records added to Station_Table")


# In[8]:


import mysql.connector as conn
import csv
mydb = conn.connect(
    host="localhost",
    user="root",
    password="nancywachira",
    database="Fishing")

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Boat_Table INNER JOIN Station         ON Boat_Table.Station_Id = Station.Station_Id")

for x in mycursor.fetchall():
    print (x)


# In[10]:



import mysql.connector as conn
import csv
mydb = conn.connect(
    host="localhost",
    user="root",
    password="nancywachira",
    database="Fishing")

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Fisher_Table INNER JOIN Boat_Table          ON Fisher_Table.Boat_Id = Boat_Table.Boat_Id          INNER JOIN Owner_Table ON Owner_Table.Boat_Id = Boat_Table.Boat_Id")
for x in mycursor.fetchall():
    print (x)


# In[ ]:




