from flask import Flask 

app = Flask(__name__)

import sqlite3
connection = sqlite3.connect('data.db', check_same_thread=False)
crsr = connection.cursor()

'''# Create the table, read the article below if you
# are unsure of what they mean
# https://www.w3schools.com/sql/sql_datatypes.asp
SQL_STATEMENT = """CREATE TABLE emp (
    staff_number INTEGER PRIMARY KEY,
    fname VARCHAR(20),
    lname VARCHAR(30),
    gender CHAR(1),
    joining DATE
);"""
crsr.execute(SQL_STATEMENT)
# Insert some users into our database
crsr.execute("""INSERT INTO emp VALUES (26, "Zakaria", "Khabbab", "M", "2022-07-01");""")
crsr.execute("""INSERT INTO emp VALUES (1, "Bill", "Gates", "M", "1980-10-28");""")'''




@app.route('/')
def index():
    return "Hello"


@app.route('/data')
def get_drinks():
    crsr.execute("SELECT * FROM  emp")
    # Store + print the fetched data
    result = crsr.fetchall()
    output = []
    for i in result:
        data = {'first_name': i[1], 'surname': i[2], 'Sex': i[3], 'Joining': i[-1]}
        output.append(data)

    #return "running"
    return {'Data': output}


