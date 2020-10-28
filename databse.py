import sqlite3

knj = sqlite3.connect("Kiranja.db")

k = knj.cursor()


#k.execute('''CREATE TABLE Lessons
#             ( TeacherName text, 
#             PhoneNumebr number )''')

# Insert a row of data
k.execute("INSERT INTO Subjectt VALUES (?,?)", subject)

# Save (commit) the changes
knj.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
knj.close() 