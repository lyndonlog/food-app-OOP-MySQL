import mysql.connector
from mysql.connector import Error

#code function below will be use when ordering again.
def order_again_text():
    print("\n\nORDER AGAIN?\n"
          "--------------------------------------------------------------\n"
          "[0] Porksilog (1pc porkchop with egg and rice)         = 60 pesos\n"
          "[1] Tapsilog (Beef Tapa with egg and rice)=            = 60 pesos\n"
          "[2] Hotsilog (1pc jumbo size hotdog with egg and rice) = 35 pesos\n"
          "[3] Shanghai-silog (4 pcs shanghai with egg and rice) = 50 pesos\n"
          "---------------------------------------------------------------")
#Class
class Menu:
    def __init__(self, name, price, quantity, total_order, menu_button, result_price):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total_order = total_order
        self.menu_button = menu_button
        self.result_price = result_price

    # Computation of total price and quantities.
    def order(self):
        global total_price
        for dish in menus:
            if input_order == dish.menu_button:
                print(f"You choose {dish.name}")
                dish.quantity = int(input('How many? press 0 to cancel:  '))
                dish.total_order = dish.total_order + dish.quantity
                dish.price = dish.price * dish.quantity
                dish.result_price = dish.result_price + dish.price
                total_price = total_price + dish.price
                print(f"TOTAL PRICE: {total_price}")
                order_again_text()

    #function for displaying the result of the program
    def result(self):
        global total_price
        print(f"\n\n\nORDER RESULT:\n"
              f"Porksilog: {menu1.total_order}          {menu1.result_price} Pesos\n"
              f"Tapsilog: {menu2.total_order}           {menu2.result_price} Pesos\n"
              f"Hotsilog: {menu3.total_order}           {menu3.result_price} Pesos\n"
              f"Shanghai-silog: {menu4.total_order}     {menu4.result_price} Pesos\n"
              f"----------------------------------\n"
              f"TOTAL PRICE:          {total_price} Pesos\n"
              f"THANK YOU!\n")

    #exiting the program
    def exit_program(self):
        quit('YOUR ORDER HAS BEEN CANCELLED. THANK YOU!')
    #fucntion use for invalid key
    def invalid_data(self):
        print('INVALID KEY, PLEASE TRY AGAIN.')



# Code below are the objects of Class Menu.
total_price = 0
menu1 = Menu('Porkchop', 60, 0, 0, '0', 0)
menu2 = Menu('Tapsilog', 55, 0, 0, '1', 0)
menu3 = Menu('Hotsilog', 35, 0, 0, '2', 0)
menu4 = Menu('Shanghai-silog', 50, 0, 0, '3', 0)
menus_button = [menu1.menu_button, menu2.menu_button, menu3.menu_button, menu4.menu_button]
menus = [menu1, menu2, menu3, menu4]

#code below for the visualization of the text-based food app program.
print("Welcome to Tapsicret!\n"
      "What do you want to order?\n"
      "--------------------------------------------------------------\n"
      "[0] Porksilog (1pc porkchop with egg and rice)         = 60 pesos\n"
      "[1] Tapsilog (Beef Tapa with egg and rice)=            = 60 pesos\n"
      "[2] Hotsilog (1pc jumbo size hotdog with egg and rice) = 35 pesos\n"
      "[3] Shanghai-silog (4 pcs shanghai with egg and rice) = 50 pesos\n"
      "---------------------------------------------------------------\n"
      )




while True:
    input_order = input("Press [0],[1],[2] [3],[c] if done, or [e] to exit\n""Enter Here:")
    if input_order in menus_button:
        menu1.order()

    elif input_order == 'c':
        menu1.result()
        break
    elif input_order == 'e':
        menu1.exit_program()
    else:
        menu1.invalid_data()
"""
 The code below is to insert the order data into mySQL such as quantity of each meal ordered and the total price.
 You can comment-out or disable temporary the code below if you want to try the OOP/Class code above
"""
try:
    con = mysql.connector.connect(host='localhost', database='food', user='root', password='samplepassword')
    cur = con.cursor()
    cur.execute("INSERT INTO foodtable (porksilog, tapsilog, hotsilog, shanghaiSilog, total_price) "
                "VALUES (%s,%s,%s,%s,%s)", (menu1.total_order, menu2.total_order, menu3.total_order,
                                            menu4.total_order, total_price))
    con.commit()
    cur.close()
    print(f'DATA HAS BEEN INSERTED INTO MySQL DATABASE')
except Error as error:
    print(f'INSERTION OF DATA FAILED! {error}')
finally:
    if con.is_connected():
        con.close()
        print('MySQL is now closed.')
