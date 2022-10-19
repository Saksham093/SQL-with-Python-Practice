# To practice SQL using Python ...
# ---------------------------------------------------------------------------------------


# Note : Choose a block to excute and keep rest as commented...
# ---------------------------------------------------------------------------------------


# Import the library used for connecting to localhost MySQL Server with help of Python...
import mysql.connector
# ---------------------------------------------------------------------------------------


# Create instance...
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testdb"
)
# ---------------------------------------------------------------------------------------


# Check Connectivity...
print(mydb)
# ---------------------------------------------------------------------------------------


# Create Cursor to communicate with mysql server...
my_cursor = mydb.cursor()
# ---------------------------------------------------------------------------------------


# Create Database...
my_cursor.execute("CREATE DATABASE testdb") # Not a Case-Sensitive...
# ---------------------------------------------------------------------------------------


# Show all Databases...
my_cursor.execute("Show Databases")

for db in my_cursor:
    print(db)
# ---------------------------------------------------------------------------------------


# Create table in testdb database...
# But first let the cursor togo in working database...
# for this use both ways, if you use this then you have to execute for every statement...
my_cursor.execute("use testdb")
# Or Write in mydb instance as database = "testdb"...
# ---------------------------------------------------------------------------------------


# Create table "Classmates" with column name snd it's type...
my_cursor.execute("create table Classmates(Name varchar(50), Age int, Present bool)")
my_cursor.execute("show tables")

for tb in my_cursor:
    print(tb)
# ---------------------------------------------------------------------------------------


# Now insert rows/values in table...
# To simplify the code...
insert_query = "Insert into Classmates (Name, Age, Present) values (%s, %s, %s)"

person_1 = ("Ab", 10, 1)
# ---------------------------------------------------------------------------------------


# For Single value input...
my_cursor.execute(insert_query, person_1)
# ---------------------------------------------------------------------------------------


# For Multi values input in table, use list...
person_list = [("Aa", 10, 1),
               ("Bb", 20, 0),
               ("Cc", 30, 1),
               ("Dd", 40, 0),
               ("Ee", 50, 1),
               ("Ff", 60, 0)]
# ---------------------------------------------------------------------------------------


# For Multi values input in table, use Executemany...
my_cursor.executemany(insert_query, person_list)
# ---------------------------------------------------------------------------------------


# To Save changes to the Servers we use commit...
mydb.commit()
# ---------------------------------------------------------------------------------------


# Fetch all data from table...
my_cursor.execute("Select * from Classmates")

for person in my_cursor:
    print(person)
# ---------------------------------------------------------------------------------------


# Fetch only selected colum...
my_cursor.execute("Select Age from Classmates")

my_result = my_cursor.fetchall()

for row in my_result:
    print(row)
# ---------------------------------------------------------------------------------------


# Limit your output row to save memory...
# And Offset Means to leave the values...
my_cursor.execute("Select * from Classmates limit 3 Offset 3")

for person in my_cursor:
    print(person)
# ---------------------------------------------------------------------------------------


# use of While Clause in Python for SQL...
where_query = "Select * from classmates where present = 1"
# ---------------------------------------------------------------------------------------


# Here we used Like A%, % is wildcard character to replace after A...
where_query = "Select * from classmates where name like 'A%'"
my_cursor.execute(where_query)

for w in my_cursor:
    print(w)
# ---------------------------------------------------------------------------------------


# Update Values in tables...
update_query = "Update Classmates set age = 90 where name = 'Bb'"
my_cursor.execute(update_query)

mydb.commit()
# ---------------------------------------------------------------------------------------


# Delete row in tables...
delete_query = "Delete from Classmates where name = 'Bb'"
my_cursor.execute(delete_query)

mydb.commit()
# ---------------------------------------------------------------------------------------


# Drop Table from Database...
drop_query = "Drop table if Exists Classmates"
my_cursor.execute(drop_query)

mydb.commit()
# ---------------------------------------------------------------------------------------