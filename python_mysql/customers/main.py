import os,dotenv
import mysql.connector

dotenv.load_dotenv()

host=os.getenv("HOST")
pass_word=os.getenv("PASSWORD")
db=os.getenv("DATABASE")

db_object=mysql.connector.connect(
    host=host,
    user="root",
    password=pass_word,
    database=db
)

query_obj=db_object.cursor()

try:
    is_run=True
    while is_run:
        customer_id=input("enter your customer id : ")
        while  customer_id=="" or str(customer_id).isalpha():
            print("Invalid customer id. Please enter a customer id")
            customer_id=input("enter your customer id : ")
        if (int(customer_id) >100) or (int(customer_id) < 1):
            print("id cannot be less than 1 and greater than 100")
            customer_id=input("enter your customer id : ")

        else:
            product_name=input("enter your product name : ")
            while (product_name=="") or product_name.isdigit():
                print("Invalid product name. Please enter a product name without any numbers")
                product_name=input("enter your product name : ")
            if len(product_name)>50:
                print("Please enter a product name with maximum length of 50 characters")
                product_name=input("enter your product name : ")

            else:
                price=input("enter your product price : ")
                while  price=="" or str(price).isalpha():
                    print("Please enter a price")
                    price=input("enter your product price : ")
                if int(price)<=0 :
                    print("Invalid product price. Please enter a product price greater than 0")
                    price=input("enter your product price : ")

                else:
                    print("Customer details inserted successfully")
                    is_run= False
    confirm=input(f"if you want to add this{customer_id},{product_name},{price} to {db} database , type yes : ")
    if not confirm.lower() == "yes":
        print("Operation cancelled")
    else:
        query=f"""insert into customer_details values 
         ({customer_id},"{product_name}",{price});"""

        query_obj.execute(query)

        db_object.commit()
        print("Customer details inserted successfully")

        query_obj.execute("""SELECT * FROM customer_details;""")

        data_record=query_obj.fetchall()
        for record in data_record:
            print(record)

        query_obj.close()
        db_object.close()    

    
    
except ValueError as v:
    print(f"error : {v}")    