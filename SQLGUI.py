from tkinter import *
import psycopg2

window = Tk()
window.geometry("500x500")

#submitting function
def submit():

    connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="organization")
    cursor = connection.cursor()
    cursor.execute(""" INSERT INTO customer (ssn, name, address, PostalCode) values (%s, %s, %s,%s);
    """,
                   [ssn.get(), name.get(), address.get(), PostalCode.get()
                    ])
    connection.commit()
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

    #ssn.delete(0,END)
    #name.delete(0,END)
    #address.delete(0,END)
   # PostalCode.delete(0,END)

def query():
    connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="organization")
    cursor = connection.cursor()
    cursor.execute("Select * from customer")
    records = cursor.fetchall()
    print(records)

    print_records = ''
    for record in records[0]:
        print_records += str(record) + "\n"

    query_label = Label(window, text=print_records)
    query_label.grid(row=6,column=0, columnspan=2)

#insert new customer : ssn, name, address, PostalCode
#text boxes
ssn= Entry(window, width=30)
ssn.grid(row=0,column=1, padx=20)
name=Entry(window, width=30)
name.grid(row=1,column=1, padx=20)
address=Entry(window, width=30)
address.grid(row=2,column=1, padx=20)
PostalCode=Entry(window, width=30)
PostalCode.grid(row=3,column=1, padx=20)

#labels
ssn_label = Label(window, text="Social security number (SSN)")
ssn_label.grid(row=0, column=0)
name_label = Label(window, text="Name of the customer")
name_label.grid(row=1, column=0)
address_label = Label(window, text="Address of the customer")
address_label.grid(row=2, column=0)
PostalCode_label = Label(window, text="PostalCode of the customer")
PostalCode_label.grid(row=3, column=0)

#button
submit_button = Button(window, text = "Add records to database", command = submit)
submit_button.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#show data button
query_button = Button(window, text="Show Data", command=query)
query_button.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=137 )


#except (Exception, psycopg2.Error) as error:
#   print("Error while connecting to PostgreSQL", error)
#finally:
   # if (connection):
#cursor.close()
#connection.close()
#print("PostgreSQL connection is closed")

window.mainloop()