# EXCERCISE-2 

print("---- CLIENTS HISTORY ----\n") # \n se ek line ka gap milega

# POOCHE- KITNE CLIENTS H?
total_clients = int(input("Aapke paas abhi kitne clients hain? "))
price_per_clients = float(input("Price batao per client (in Euro): "))

# Calculation
monthly_revenue = total_clients * price_per_clients
annual_revenue = monthly_revenue * 12

# Output ko thoda nicely print kiya
print("\n" + "="*30)
print(f"👥 Total Clients     : {total_clients}")
print(f"💶 Price Per Client   : €{price_per_clients:,.2f}")
print("-"*30)
print(f"💰 MONTHLY PAISA     : €{monthly_revenue:,.2f}")
print(f"👑 Annual Revenue    : €{annual_revenue:,.2f}")
print("="*30)
