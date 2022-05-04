from datetime import datetime

discount_amount = 0.00
sales_tax = 0.00
total = 0.
purchase = 0.00
done = False

#current_date_and_time = datetime.now()
#weekday = current_date_and_time.weekday()
# USES current_date_and_time.weekday() for each day
#MON 0, TUE = 1, WED = 2, THU = 3 FRI = 4 SAT = 5 SUN = 6

weekday = 1
while not done :
    subtotal = (input("Please enter the subtotal, Use [ Done ] for exit: "))
    
    if subtotal.lower() == "done" :
        done = True
    else:
        subtotal = float(subtotal)
        if subtotal >= 50 and weekday == 1 or weekday == 2 :
            discount_amount = subtotal * 0.10
            sales_tax = (subtotal - discount_amount) * 0.06
            total = subtotal - discount_amount + sales_tax
        elif subtotal < 50 and weekday == 1 or weekday == 2 :
            purchase = 50.00 - subtotal
            sales_tax = subtotal * 0.06
            total = subtotal + sales_tax
        else:        
            sales_tax = subtotal * 0.06
            total = subtotal + sales_tax

        print(f"Sales tax amount:{sales_tax:.2f}")
        if discount_amount > 0.00:
            print(f"Discount amount: {discount_amount:.2f}")
        if purchase > 0.00 :
            print(f" You need to buy more ${purchase:.2f} to receive 10% of discount!")   
        print(f"Total: {total:.2f}")
        discount_amount = 0.00
        sales_tax = 0.00
        total = 0.00
        purchase = 0.00
