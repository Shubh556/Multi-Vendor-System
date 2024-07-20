import datetime  # Import the datetime module

# Define a function to generate an order number
def generate_order_number(pk):
    # Get the current date and time in the format YYYYMMDDHHMM (Year, Month, Day, Hour, Minute)
    current_datetime = datetime.datetime.now().strftime('%Y%m%d%H%M')
    # Concatenate the current date and time with the primary key (pk) to create a unique order number
    order_number = current_datetime + str(pk)
    return order_number  # Return the generated order number
