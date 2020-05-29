from tkinter import *
import psycopg2
import tkinter as tk
from PIL import ImageTk, Image



#Database login
user="postgres"
password="postgres"
host="127.0.0.1"
database="pg4"

#Main design
root = Tk()
root.title("Webshop GUI")

canvas1 = tk.Canvas(root, width=1080, height=500, relief='raised', bg='white')
canvas1.pack()

img  = Image.open('C:/pg4.png')
img = img.resize((90, 110), Image.ANTIALIAS)
photo=ImageTk.PhotoImage(img)
lab=Label(image=photo, borderwidth=0).place(x = 530, y = 80 , anchor = CENTER)

def center_window(w=1080, h=500):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

center_window()
label_GUI = tk.Label(root, text='Welcome to the PG4 Webshop\n Managament Application ',bg='#ffffff', font=('Sans Serif', 20))
canvas1.create_window(530, 230, window=label_GUI)

#main design after deliting the widgets in the functions
def beauty():
    canvas1.create_line(0, 150, 1280, 150, fill='#ab6aa5', width=2) #long line
    canvas1.create_line(0, 400, 1280, 400, fill='#ab6aa5', width=2) #long line
    label_GUI = tk.Label(root, text='© PG4, 2020',bg='#ffffff', font=('Sans Serif', 9, 'italic'))
    canvas1.create_window(1000, 480, window=label_GUI)
beauty()

#------------------------------------------------------------SECTION ONE OF THE MENU-----------------------------------------------------------------------------------------

def Manage_Orders():
    #delete all widgets
    canvas1.delete("all")
    #call the main design
    beauty()

    #entry for finalizing the product
    entry_id = tk.Entry(root)
    entry_id.insert(0,'Enter order ID')
    entry_id.config(bd=2)
    canvas1.create_window(945, 250, window=entry_id)

    #entry for selecting specific order
    entry_specific_order = tk.Entry(root)
    entry_specific_order.insert(0,'Enter order ID')
    entry_specific_order.config(bd=2)
    canvas1.create_window(405, 250, window=entry_specific_order)

    def select_all_orders():
        #define screen size
        w=600
        h=400
        screen=Tk()
        screen.title("Webshop GUI: orders list")
        # get screen width and height
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        # calculate position x, y
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        screen.geometry('%dx%d+%d+%d' % (w, h, x, y))
        scroll_bar = Scrollbar(screen, orient=VERTICAL)
        scroll_bar.pack(side = RIGHT,fill=Y)
        mylist = Listbox(screen,  yscrollcommand = scroll_bar.set)

        #connecting to the database and executing SQL line
        try:
            connection = psycopg2.connect(user=user, password=password,
                                          host=host, database=database)

            PostgreSQL_select_Query = ("SELECT * from orders")
            cursor = connection.cursor()
            cursor.execute(PostgreSQL_select_Query)
            connection.commit()

            #output in the main window
            Orders = cursor.rowcount
            label_all_orders = tk.Label(root, text='Overall number of orders: ' + str(Orders), bg='#ffffff', font=('Sans Serif', 10))
            canvas1.create_window(135, 350, window=label_all_orders)

            #output in the new window
            for row in cursor.fetchall():
                mylist.insert(END, "Order ID: " + str(row[0]) + "    Time: " + str(row[1])[:19] + "    Total price: " + str(row[3]) +
                	"    Finalized: " + str(row[4]) + "    Customer ID: " + str(row[2]))
            mylist.pack( side = "top", fill = "x" )
            scroll_bar.config( command = mylist.yview )

        #closing connection with database
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    #Label and Button for All orders
    label_check = tk.Label(root, text='Press the button to see all\nthe orders in the database',bg='#ffffff', font=('Sans Serif', 10))
    canvas1.create_window(135, 200, window=label_check)

    button_check= tk.Button(text='See all orders', command=select_all_orders, bg='#b3409b', fg='white', font=('Sans Serif', 10))
    canvas1.create_window(135,300, window=button_check)


    def finalize_with_id():
        #connecting to the database and executing SQL line
        try:
            connection = psycopg2.connect(user=user, password=password,
                                          host=host, database=database)

            #getting values from the entry
            id = entry_id.get()

            PostgreSQL_select_Query = ("UPDATE orders SET finalized = true WHERE id = %s")
            cursor = connection.cursor()
            cursor.execute(PostgreSQL_select_Query, (id,))
            connection.commit()

            #output in the main window
            label_successfull_update_finalized = tk.Label(root, text='Record updated successfully ', bg='#ffffff', font=('Sans Serif', 10))
            canvas1.create_window(945, 350, window=label_successfull_update_finalized)

        #closing connection with database
        finally:
                if (connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")

    #Label and Button for finalizing orders
    label_final = tk.Label(root, text='Enter ID of the order\nto make it finalized',bg='#ffffff', font=('Sans Serif', 10))
    canvas1.create_window(945, 200, window=label_final)

    button_final= tk.Button(text='Finalize order', command=finalize_with_id, bg='#b3409b', fg='white', font=('Sans Serif', 10))
    canvas1.create_window(945, 300, window=button_final)

    def select_order_details():
        #define screen size
        w=400
        h=400
        screen=Tk()
        screen.title("Webshop GUI: order details")
        # get screen width and height
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        # calculate position x, y
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        screen.geometry('%dx%d+%d+%d' % (w, h, x, y))
        scroll_bar = Scrollbar(screen)
        scroll_bar.pack(side = RIGHT,fill=Y)
        mylist = Listbox(screen,  yscrollcommand = scroll_bar.set )

        #connecting to the database and executing SQL line
        try:
            connection = psycopg2.connect(user=user, password=password,
                                          host=host, database=database)

            PostgreSQL_select_Query = ("SELECT * from order_details")
            cursor = connection.cursor()
            cursor.execute(PostgreSQL_select_Query)
            connection.commit()

            #output in the new window
            for row in cursor.fetchall():
                mylist.insert(END, "Quantity: " + str(row[2]) + "   Order ID: " + str(row[0])[:19] + "   Product ID: " + str(row[1]))
            mylist.pack( side = "top", fill = "x" )
            scroll_bar.config( command = mylist.yview )

        #closing connection with database
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    #Label and Button for All orders
    label_all = tk.Label(root, text='Press the button to see all the\norder details in the database',bg='#ffffff', font=('Sans Serif', 10))
    canvas1.create_window(675, 200, window=label_all)

    button_all= tk.Button(text='See orders details', command=select_order_details, bg='#b3409b', fg='white', font=('Sans Serif', 10))
    canvas1.create_window(675, 300, window=button_all)

    def select_specific_order_details():
        #define screen size
        w=400
        h=400
        screen=Tk()
        screen.title("Webshop GUI: order details by order ID")
        # get screen width and height
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        # calculate position x, y
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        screen.geometry('%dx%d+%d+%d' % (w, h, x, y))
        scroll_bar = Scrollbar(screen)
        scroll_bar.pack(side = RIGHT,fill=Y)
        mylist = Listbox(screen,  yscrollcommand = scroll_bar.set )

        #connecting to the database and executing SQL line
        try:
            connection = psycopg2.connect(user=user, password=password,
                                          host=host, database=database)

            #getting values from the entry
            id = entry_specific_order.get()

            PostgreSQL_select_Query = ("SELECT * from order_details WHERE orderid = %s ")
            cursor = connection.cursor()
            cursor.execute(PostgreSQL_select_Query, (id,))
            connection.commit()

            #output in the new window
            for row in cursor.fetchall():
                 mylist.insert(END, "Quantity: " + str(row[2]) + "   Order ID: " + str(row[0])[:19] + "   Product ID: " + str(row[1]))
            mylist.pack( side = "top", fill = "x" )
            scroll_bar.config( command = mylist.yview )

        #closing connection with database
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    #Label and Button for order details
    label_specific_order = tk.Label(root, text='Enter order ID to see\ndetails of the specific order',bg='#ffffff', font=('Sans Serif', 10))
    canvas1.create_window(405, 200, window=label_specific_order)

    button_specific_order= tk.Button(text='See order details', command=select_specific_order_details, bg='#b3409b', fg='white', font=('Sans Serif', 10))
    canvas1.create_window(405, 300, window=button_specific_order)

#--------------------------------------------------------SECTION 2 OF THE MENU-------------------------------------------------------------------------------------

def Manage_Inventory():
    #delete all widgets
    canvas1.delete("all")
    #call the main design
    beauty()

    #entries
    #Quantity entry for updating inventory
    entry_quantity = tk.Entry(root)
    entry_quantity.insert(0,'Enter quantity')
    canvas1.create_window(405, 240, window=entry_quantity)

    #product id entry for updating the inventory
    entry_product_id = tk.Entry(root)
    entry_product_id.insert(0,'Enter product ID')
    canvas1.create_window(405, 260, window=entry_product_id)

    #product id entry for deleting item
    entry_product_id_delete = tk.Entry(root)
    entry_product_id_delete.insert(0,'Enter product ID')
    canvas1.create_window(675, 250, window=entry_product_id_delete)


    def all_products():
        #define screen size
        w=1050
        h=400
        screen=Tk()
        screen.title("Webshop GUI: products list")
        # get screen width and height
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        # calculate position x, y
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        screen.geometry('%dx%d+%d+%d' % (w, h, x, y))
        scroll_bar = Scrollbar(screen)
        scroll_bar.pack(side = RIGHT,fill=Y)
        mylist = Listbox(screen,  yscrollcommand = scroll_bar.set )

        #connecting to the database and executing SQL line
        try:
            connection = psycopg2.connect(user=user, password=password,
                                          host=host, database=database)

            PostgreSQL_select_Query = ("SELECT * from products")
            cursor = connection.cursor()
            cursor.execute(PostgreSQL_select_Query)
            connection.commit()

            #output in the main window
            inventory = cursor.rowcount
            label_all_products = tk.Label(root, text='Overall number of products: ' + str(inventory), bg='#ffffff', font=('Sans Serif', 10))
            canvas1.create_window(135, 350, window=label_all_products)

            #output in the new window
            for row in cursor.fetchall():

                mylist.insert(END, "Product ID: " + str(row[0]) + "   Name: " + str(row[1]) + "   Price: " + str(row[2]) +
                	"    Decription: " + str(row[3]) + "    Image: " + str(row[4]) + "   Units in stock: " + str(row[5]))
            mylist.pack( side = "top", fill = "x" )
            scroll_bar.config( command = mylist.yview )

        #closing connection with database
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    #label and button for all inventory products
    label_check_inventory = tk.Label(root, text='Press the button to see\nall products in the inventory',bg='#ffffff', font=('Sans Serif', 10))
    canvas1.create_window(135, 200, window=label_check_inventory)

    button_check_inventory= tk.Button(text='See inventory products', command=all_products, bg='#b3409b', fg='white', font=('Sans Serif', 10))
    canvas1.create_window(135, 300, window=button_check_inventory)

    def update_inventory():
        #connecting to the database and executing SQL line
        try:
            connection = psycopg2.connect(user=user, password=password,
                                          host=host, database=database)

            #getting values from the entry
            units = entry_quantity.get()
            id = entry_product_id.get()

            PostgreSQL_select_Query = ("UPDATE products SET units = %s WHERE id = %s")
            cursor = connection.cursor()
            cursor.execute(PostgreSQL_select_Query, (units, id,))
            connection.commit()

            #output in the main window
            label_successfull_update_products = tk.Label(root, text='Records updated successfully', bg='#ffffff', font=('Sans Serif', 10))
            canvas1.create_window(405, 350, window=label_successfull_update_products)

        #closing connection with database
        finally:
                if (connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")

    #label and button for updating the inventory
    label_inventory_update = tk.Label(root, text='Update the inventory by\nentering quantity and\nID of the product',bg='#ffffff', font=('Sans Serif', 10))
    canvas1.create_window(405, 200, window=label_inventory_update)

    button_inventory_update= tk.Button(text='Update inventory', command=update_inventory, bg='#b3409b', fg='white', font=('Sans Serif', 10))
    canvas1.create_window(405, 300, window=button_inventory_update)

    def delete_product():
        #connecting to the database and executing SQL line
        try:
            connection = psycopg2.connect(user=user, password=password,
                                          host=host, database=database)

            #getting values from the entry
            id = entry_product_id_delete.get()

            PostgreSQL_select_Query = ("DELETE FROM products WHERE id = %s")
            cursor = connection.cursor()
            cursor.execute(PostgreSQL_select_Query, (id,))
            connection.commit()

            #output in the main window
            label_successfull_update_finalized = tk.Label(root, text='Product deleted successfully', bg='#ffffff', font=('Sans Serif', 10))
            canvas1.create_window(675, 350, window=label_successfull_update_finalized)

        #closing connection with database
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    #label and button for deleting the product
    label_delete_product = tk.Label(root, text='Delete the product by\nentering its ID',bg='#ffffff', font=('Sans Serif', 10))
    canvas1.create_window(675, 200, window=label_delete_product)

    button_delete_product= tk.Button(text='Delete product', command=delete_product, bg='#b3409b', fg='white', font=('Sans Serif', 10))
    canvas1.create_window(675, 300, window=button_delete_product)

    def new_product():
        #new window with new variable names, so the widgets would be attached to the "screen" and not "root"
        screen=tk.Tk()
        screen.title("Webshop GUI: add new product")
        canvas2 = tk.Canvas(screen, width=400, height=400, relief='raised', bg='#ffffff')
        canvas2.pack()

        #define screen size
        w=400
        h=400
        # get screen width and height
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        # calculate position x, y
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        screen.geometry('%dx%d+%d+%d' % (w, h, x, y))

        #entry for product name in new window
        label_1= tk.Label(screen, text='Enter product name',bg='#ffffff', anchor=W, font=('Sans Serif', 10))
        canvas2.create_window(80, 100, window=label_1)
        entry_product_name = tk.Entry(screen)
        entry_product_name.insert(0,'...')
        canvas2.create_window(250, 100, window=entry_product_name)

        #entry for product price in new window
        label_2= tk.Label(screen, text='Enter product price',bg='#ffffff', font=('Sans Serif', 10))
        canvas2.create_window(80, 120, window=label_2)
        entry_product_price = tk.Entry(screen)
        entry_product_price.insert(0,'...')
        canvas2.create_window(250, 120, window=entry_product_price)

        #entry for product description in new window
        label_3= tk.Label(screen, text='Enter product description', font=('Sans Serif', 10) ,bg='#ffffff')
        canvas2.create_window(80, 140, window=label_3)
        entry_product_description = tk.Entry(screen)
        entry_product_description.insert(0, '...')
        canvas2.create_window(250, 140, window=entry_product_description)

        #entry for product units in new window
        label_4= tk.Label(screen, text='Enter units', bg='#ffffff', font=('Sans Serif', 10))
        canvas2.create_window(80, 160, window=label_4)
        entry_product_unit = tk.Entry(screen)
        entry_product_unit.insert(0,'...')
        canvas2.create_window(250, 160, window=entry_product_unit)

        #entry for file name in new window
        label_5= tk.Label(screen, text='Enter image file name', bg='#ffffff', font=('Sans Serif', 10))
        canvas2.create_window(80, 180, window=label_5)
        entry_product_img = tk.Entry(screen)
        entry_product_img.insert(0,'...')
        canvas2.create_window(250, 180, window=entry_product_img)

        #entry for product id in new window
        label_0= tk.Label(screen, text='Enter product ID', bg='#ffffff', font=('Sans Serif', 10))
        canvas2.create_window(80, 80, window=label_0)
        entry_product_id = tk.Entry(screen)
        entry_product_id.insert(0,'...')
        canvas2.create_window(250, 80, window=entry_product_id)


        def add_product():
            #connecting to the database and executing SQL line
            try:
                    connection = psycopg2.connect(user=user, password=password,
                                                  host=host, database=database)

                    #getting values from the entry
                    id = entry_product_id.get()
                    img = entry_product_img.get()
                    name = entry_product_name.get()
                    price = entry_product_price.get()
                    description = entry_product_description.get()
                    units = entry_product_unit.get()

                    PostgreSQL_select_Query = ("INSERT INTO products(id, name, price, description, image, units) VALUES (%s, %s, %s, %s, %s, %s)")
                    cursor = connection.cursor()
                    cursor.execute(PostgreSQL_select_Query, (id, name, price, description, img, units))
                    connection.commit()

                    #output in the main window
                    label_successfull_update_finalized = tk.Label(root, text='Product inserted successfully ', bg='#ffffff', font=('Sans Serif', 10))
                    canvas1.create_window(945, 350, window=label_successfull_update_finalized)

            #closing connection with database
            finally:
                    if (connection):
                        cursor.close()
                        connection.close()
                        print("PostgreSQL connection is closed")

        #button for adding the product in a new window
        button_new_add = tk.Button(screen, text='Add New Product', command=add_product, bg='#b3409b', fg='white', font=('Sans Serif', 10))
        canvas2.create_window(180, 300, window=button_new_add)
        screen.mainloop()

    #button and label for poping up a new window for adding the product
    label_new_product = tk.Label(root, text='By pressing you will be\nredirected to a new window\nto add a new product',bg='#ffffff', font=('Sans Serif', 10))
    canvas1.create_window(945, 200, window=label_new_product)
    button_new_product= tk.Button(text='Add new product', command=new_product, bg='#b3409b', fg='white', font=('Sans Serif', 10))
    canvas1.create_window(945, 300, window=button_new_product)

#---------------------------------------------------SECTION THREE OF THE MENU------------------------------------------------------------------------

def Customers():
    #delete all widgets
    canvas1.delete("all")
    #call the main design
    beauty()

    def all_customers():
        #define screen size
        w=800
        h=400
        screen=Tk()
        screen.title("Webshop GUI: customers list")
        # get screen width and height
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        # calculate position x, y
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        screen.geometry('%dx%d+%d+%d' % (w, h, x, y))

        scroll_bar = Scrollbar(screen)
        scroll_bar.pack(side = RIGHT,fill=Y)
        mylist = Listbox(screen,  yscrollcommand = scroll_bar.set )

        #connecting to the database and executing SQL line
        try:
            connection = psycopg2.connect(user=user, password=password,
                                          host=host, database=database)

            PostgreSQL_select_Query = ("SELECT * from customers")
            cursor = connection.cursor()
            cursor.execute(PostgreSQL_select_Query)
            connection.commit()

            #output in the main window
            customer_count = cursor.rowcount
            label_all_products = tk.Label(root, text='Overall number of customers: ' + str(customer_count), bg='#ffffff', font=('Sans Serif', 10))
            canvas1.create_window(675, 350, window=label_all_products)

            #output in the new window
            for row in cursor.fetchall():
                mylist.insert(END, "Customer ID: " + str(row[0]) + "   Name: " + str(row[1]) + "   Last name: " + str(row[2]) + "   Address: " + str(row[3])+" "+str(row[4])+" "+str(row[5])+" "+str(row[6])+" "+str(row[7]))
            mylist.pack( side = "top", fill = "x" )
            scroll_bar.config( command = mylist.yview )

        #closing connection with database
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    #label and button for all customers list
    label_check_inventory = tk.Label(root, text='Press the button to see\nall the customers',bg='#ffffff', font=('Sans Serif', 10))
    canvas1.create_window(675, 200, window=label_check_inventory)
    button_check_customers= tk.Button(text='See all customers', command=all_customers, bg='#b3409b', fg='white', font=('Sans Serif', 10))
    canvas1.create_window(675, 300, window=button_check_customers)

    def order_customer():
        #define screen size
        w=400
        h=400
        screen=Tk()
        screen.title("Webshop GUI: customers an their orders list")
        # get screen width and height
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        # calculate position x, y
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        screen.geometry('%dx%d+%d+%d' % (w, h, x, y))

        scroll_bar = Scrollbar(screen)
        scroll_bar.pack(side = RIGHT,fill=Y)
        mylist = Listbox(screen,  yscrollcommand = scroll_bar.set )

        #connecting to the database and executing SQL line
        try:
            connection = psycopg2.connect(user=user, password=password,
                                          host=host, database=database)

            PostgreSQL_select_Query = (" Select customers.id, orders.id from orders join customers on orders.customerid = customers.id")
            cursor = connection.cursor()
            cursor.execute(PostgreSQL_select_Query)
            connection.commit()

            #output in the new window
            for row in cursor.fetchall():
                mylist.insert(END, "Customer ID: " + str(row[0]) + "   Order ID: " + str(row[1]))
            mylist.pack( side = "top", fill = "x" )
            scroll_bar.config( command = mylist.yview )

        #closing connection with database
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    #label and button for customers and their orders
    label_customer_order = tk.Label(root, text='Press the button to see\ncustomers an their orders',bg='#ffffff', font=('Sans Serif', 10))
    canvas1.create_window(405, 200, window=label_customer_order)
    button_customer_order = tk.Button(text='See customers orders', command=order_customer, bg='#b3409b', fg='white', font=('Sans Serif', 10))
    canvas1.create_window(405, 300, window=button_customer_order)

#menu creation
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="Manage Orders", command=Manage_Orders)
menu.add_cascade(label="Manage Inventory", command=Manage_Inventory)
menu.add_cascade(label="Manage Customers", command=Customers)
menu.add_cascade(label="Exit", command=root.quit)

#window fixed size
root.resizable(0, 0)
root.mainloop()
