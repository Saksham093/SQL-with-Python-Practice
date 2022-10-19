# Upload Dataset (.csv File) to SQL server using python and fatch the same...
# ---------------------------------------------------------------------------------------

# Import requied libraries...
import pandas as pd
import numpy as np
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="CheckUps"
)

my_cr = mydb.cursor()
# ---------------------------------------------------------------------------------------

# Create Database...
my_cr.execute("Create database CheckUps")
my_cr.execute("use CheckUps")
# ---------------------------------------------------------------------------------------


# Create table "Diabetes"...
my_cr.execute("create table Diabetes(Pregnancies int, Glucose int, BloodPressure int, SkinThickness int, "
              "Insulin int, BMI float, DiabetesPedigreeFunction float, Age int, Outcome float)")
# ---------------------------------------------------------------------------------------


# To Drop Table...
my_cr.execute("Drop table Diabetes")
# ---------------------------------------------------------------------------------------


# Read csv file using pandas...
dataset = pd.read_csv("diabetes-data.csv", index_col=False, delimiter=',')
# ---------------------------------------------------------------------------------------


# Creating a alines to use again and again...
bulk_insert = "Insert into Diabetes(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, " \
              "DiabetesPedigreeFunction, Age, Outcome) Values (%s, %s, %s, %s,%s, %s, %s, %s, %s) "
# ---------------------------------------------------------------------------------------


# Read line by line and push to server and commit ongo...
for i, row in dataset.iterrows():
    value_tuple = tuple(row)
    my_cr.execute(bulk_insert, value_tuple)
    mydb.commit()


# Fatch data & show...
my_cr.execute("Select * from Diabetes limit 5")

for i in my_cr:
    print(i)
# ---------------------------------------------------------------------------------------