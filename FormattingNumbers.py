# Formatting with f-strings
username = "Alan"
print(f"Hello {username}")
# Showing dollar amounts
unit_price = 49.99
quantity = 30
print(f"Subtotal: ${quantity * unit_price}")
print(f"Subtotal: ${quantity * unit_price:,.2f}")
# Formatting percent numbers
sales_tax_rate = 0.065
print(f"Sales Tax Rate {sales_tax_rate}")
print(f"Sales Tax Rate {sales_tax_rate:.2%}")
print(f"Sales Tax Rate {sales_tax_rate:.1%}")
print(f"Sales Tax Rate {sales_tax_rate:.9%}")
# Making multiline format strings
user1 = "Alberto"
user2 = "Babs"
user3 = "Carlos"
output=f"{user1} \n{user2} \n{user3}"
print(output)
# Formatting width and alignment
subtotal = quantity*unit_price
sales_tax = sales_tax_rate*subtotal
total = subtotal + sales_tax
s_subtotal = "$" + f"{subtotal:,.2f}"
s_sales_tax = "$" + f"{sales_tax:,.2f}"
s_total = "$" + f"{total:,.2f}"
s_output = f"""
Subtotal:   {s_subtotal:>9}
Sales Tax:  {s_sales_tax:>9}
Total:      {s_total:>9}
"""
print(s_output)
