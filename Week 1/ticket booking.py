ticket_price = 250
n0_0f_tickets = int(input("no. of tickets : "))
total_price = (ticket_price*n0_0f_tickets)
discount = 100
applicable = total_price>=500
print("Discount Applicable.")
total_price-=discount
print("Amount to be payed")
print(total_price)
