# EXERCISE 3 — Hard ⭐⭐⭐
# ServiceLabs3 Team Salary Calculator

print("====== SERVICELABS3 SALARY CALCULATOR ======\n")

# 1. 3 team members ke naam aur salary input lo
# Member 1
member1_name = input("👤 First team member ka naam: ")
member1_salary = float(input(f"💰 {member1_name} ki monthly salary (in Euro): "))

# Member 2
member2_name = input("\n👤 Second team member ka naam: ")
member2_salary = float(input(f"💰 {member2_name} ki monthly salary (in Euro): "))

# Member 3
member3_name = input("\n👤 Third team member ka naam: ")
member3_salary = float(input(f"💰 {member3_name} ki monthly salary (in Euro): "))

# 2. Total monthly cost calculate karo
total_monthly_cost = member1_salary + member2_salary + member3_salary

# 3. Print karo ek formatted report
print("\n" + "═"*45)
print(" 🏢 SERVICELABS3 - MONTHLY SALARY REPORT ")
print("═"*45)
# Left-align karne ke liye :<15 aur right-align ke liye :>15 use kiya hai taaki report ekdum seedhi dikhe
print(f" {member1_name:<20} : €{member1_salary:,.2f}")
print(f" {member2_name:<20} : €{member2_salary:,.2f}")
print(f" {member3_name:<20} : €{member3_salary:,.2f}")
print("─"*45)
print(f" 🚀 TOTAL MONTHLY COST    : €{total_monthly_cost:,.2f}")
print("═"*45)



