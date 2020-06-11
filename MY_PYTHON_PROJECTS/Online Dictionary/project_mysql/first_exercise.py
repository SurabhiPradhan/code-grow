import mysql.connector

                            #establish connection & store connection object to a variable
con = mysql.connector.connect(
user ="ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database",
)   

                            # once the connection is established, we want to query data
# create cursor object to navigate through database table
cursor = con.cursor()
word = input("Enter a word: ")

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " %word)
#getting actual data from dictionary in variable results
results = cursor.fetchall()

if results:
    for result in results:
        print (result[1])
else:
    print("No word found!!")        
 