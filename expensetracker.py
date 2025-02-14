import sqlite3
#the first is to connect to db
conn=sqlite3.connect('monthexpense.db')
cursor=conn.cursor()
#first fn is the one to add expense
cursor.execute('CREATE TABLE IF NOT EXISTS expense (id INTEGER PRIMARY KEY,name TEXT, amount REAL)')
conn.commit()
def add_expense(name,amount):
    cursor.execute('INSERT INTO expense (name,amount) VALUES(?,?)', (name,amount))
    conn.commit()
#the second one id the one to view exprense
def view_expense():
    cursor.execute('SELECT * FROM  expense')
    for row in cursor.fetchall():
        print(row)

while True:
    action=input('input either (a) to add or (v) to view expense:')
    if action =='a':
        name=input('Enter the name of the expense:')
        amount=float(input('Enter the amount:'))
        add_expense(name,amount)
    elif action =='v':
        view_expense()
    else:
        print("You have entered the wrong choice")
        break