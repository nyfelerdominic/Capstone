import mariadb
import time
import config
import cv2
import pytesseract
from os import system, name
################################################################################
def retrieve_employee_info_by_plate_num(plate_num_input):
    try:
        conn = mariadb.connect(
        user=config.user,
        password=config.password,
        host=config.host,
        port=config.port,
        database=config.database
    )
        
        cur = conn.cursor()

        query = "SELECT Name, PhoneNum, Email FROM employees WHERE PlateNum = %s"
    
        cur.execute(query, (plate_num_input,))
    
        result = cur.fetchall()
    
        if not result: 
            print("Plate Number is not found\n")
        else: 
            for row in result:
                Name, PhoneNum, Email = row
                print(f"Name: {Name}, Plate Num: {plate_num_input}, Phone Num: {PhoneNum}, Email: {Email}\n")
            
    except mariadb.Error as e:
        print("Error: ", e)
        
    finally:
        if 'cursor' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()
################################################################################
def add_employee(name, plate_num, phone_num, email):
    try:
        conn = mariadb.connect(
        user=config.user,
        password=config.password,
        host=config.host,
        port=config.port,
        database=config.database
    )
        
        cur = conn.cursor()
        
        query = "INSERT INTO employees (Name, PlateNum, PhoneNum, Email) VALUES (%s, %s, %s, %s)"
        
        cur.execute(query, (name, plate_num, phone_num, email))
        
        conn.commit()
        
        print(f"Employee {name} added successfully.\n")
        
    except mariadb.Error as e:
        print("Error: ", e)
        
    finally:
        if 'cursor' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()
################################################################################
def delete_employee(plate_num):
    try:
        conn = mariadb.connect(
        user=config.user,
        password=config.password,
        host=config.host,
        port=config.port,
        database=config.database
    )
        
        cur = conn.cursor()
        
        query = "DELETE FROM employees WHERE PlateNum = %s"
        
        cur.execute(query, (plate_num,))
        
        conn.commit()
        
        print(f"Employee with plate number {plate_num} removed successfully.\n")
        
    except mariadb.Error as e:
        print("Error: ", e)
        
    finally:
        if 'cursor' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()
################################################################################
def show_table():
    try:
        conn = mariadb.connect(
        user=config.user,
        password=config.password,
        host=config.host,
        port=config.port,
        database=config.database
    )
        
        cur = conn.cursor()
        
        query = "SELECT * FROM employees"
        
        cur.execute(query)
        
        rows = cur.fetchall()
        
        for row in rows:
            print(row)
        
    except mariadb.Error as e:
        print("Error: ", e)
        
    finally:
        if 'cursor' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()
################################################################################
def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
################################################################################
def ocr(img):
  print("\nOutput for plate :")
  # Perform text extraction
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  data = pytesseract.image_to_string(img, config='-l eng --psm 7 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789- ')
  return data
################################################################################
def default_menu():
    clear_screen()
    while True:
        print("Select an option")
        print("1) Retrieve data")
        print("2) Add employee")
        print("3) Remove employee")
        print("4) Show all employees")
        print("q) Quit")
        
        choice = input("-> ")
        
        if choice == '1':
            plate_num_input = input("Enter Plate Number: ")
            clear_screen()
            retrieve_employee_info_by_plate_num(plate_num_input)
        
        elif choice == '2':
            name = input("Enter Name: ")
            plate_num = input("Enter Plate Number: ")
            phone_num = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            clear_screen()
            add_employee(name, plate_num, phone_num, email)
        
        elif choice == '3':
            plate_num = input("Enter plate number: ")
            clear_screen()
            delete_employee(plate_num)
            
        elif choice == '4':
            clear_screen()
            show_table()
            
        elif choice.lower() == 'q':
            clear_screen()
            print("Saving Progress...")
            time.sleep(3)
            clear_screen()
            break
        
        else:
            clear_screen()
            print("Invalid input, try again.\n")
################################################################################
def auto_main():
    plate_found = cv2.imread("cropped_plate.jpg")
    data = ocr(plate_found)
    print(data)

    #Remove end line from data output
    data = data.replace("\x0a", "")
    
    retrieve_employee_info_by_plate_num(data)
################################################################################
if __name__ == "__main__":
    # auto_main()
    default_menu()