import csv
# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

#Moroni Bamvakiades Ramos
#11/09/2023
#Python documentation, Checkpoint, Chat GPT, Codeium


def main():
    KEY_INDEX = 0
    products_dict = read_dictionary("products.csv", KEY_INDEX)

    print("Inkom Emporium")
    print()
    
    
    

      # Open a file named request.csv and store a reference to the opened file in a variable named request_file.
    with open("request.csv", "rt") as request_file:
        # Use the csv module to create a reader object that will read from the opened file.
        reader = csv.reader(request_file)
        
        # The first row of the CSV file contains column headings and not data, so this statement skips the first row of the CSV file.
        next(reader)

        for row_list in reader:
            if len(row_list) >= 1:  # Check if row_list has at least 1 element (product number)
                product_key = row_list[0]
                if  product_key in products_dict:
                    product_info = products_dict[product_key]
                    product_name = product_info[1]
                    product_price = float(product_info[2])
                    if len(row_list) >= 2:  # Check if row_list has the requested quantity
                        quantity = int(row_list[1])
                    else:
                        quantity = 0  # Default quantity to 0 if not provided
                    total = quantity * product_price
                    print(f"{product_name}: {quantity} @ {product_price}")
                else:
                    print(f"Invalid product key: {product_key} - Skipping")
            else:
                print("Invalid row in request.csv - Skipping")
                
        print() 
         
    
    total_quantity = 0  # Initialize total quantity
    subtotal = 0  # Initialize subtotal

         
         
    
    with open("request.csv", "rt") as request_file:
        reader = csv.reader(request_file)
        next(reader)  # Skip the header

        for row_list in reader:
            if len(row_list) >= 2:
                quantity = int(row_list[1])
                total_quantity += quantity

        
        print(f"Number of items:{total_quantity}")
        
        
    with open("request.csv", "rt") as request_file:
        # Use the csv module to create a reader object that will read from the opened file.
        reader = csv.reader(request_file)
        
        # The first row of the CSV file contains column headings and not data, so this statement skips the first row of the CSV file.
        next(reader)

        for row_list in reader:
            if len(row_list) >= 1:  # Check if row_list has at least 1 element (product number)
                    product_key = row_list[0]            
                    product_info = products_dict[product_key] 
                    product_price = float(product_info[2])
                    quantity = int(row_list[1])
                    subtotal += product_price * quantity
                    value = "{:.2f}".format(subtotal)
                   
                   
        tax_rate = 0.06
        sales_tax_amount = float(value) * float(tax_rate)           
        rounded_sales_tax_amount = "{:.2f}".format(sales_tax_amount)
        print(f"Subtotal:{value}")      
        print(f"Sales Tax: {rounded_sales_tax_amount}")
        print(f"Total: {float(value) + float(rounded_sales_tax_amount)}")      
           
    # Call the now() method to get the current
    # date and time as a datetime object from
    # the computer's operating system.
    current_date_and_time = datetime.now()  
    
    print()
    print("Thank you for shopping at the Inkom Emporium.")
    
    # Use an f-string to print the current
    # day of the week and the current time.
    print(f"{current_date_and_time:%A %I:%M %p}")
        
   
    



def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters:
        filename (str): the name of the CSV file to read.
        key_column_index (int): the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}
    
    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

    
        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)
        
        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:

                # From the current row, retrieve the data
                # from the column that contains the key.
                
                key = row_list[key_column_index]
            
                # Store the data from the current
                # row into the dictionary.
                dictionary[key] = row_list 
                

    # Return the dictionary.
    return dictionary
                    
if __name__ == "__main__":
    main()