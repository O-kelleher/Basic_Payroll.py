employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked this week: "))
pay_rate = float(input("Enter Hourly pay rate: "))
tax_rate = float(input("Enter ATO tax withholding rate: "))
medicare_levy_rate = float(input("Enter Medicare Levy rate: "))
gross_pay = (pay_rate * hours_worked)
tax = (gross_pay * tax_rate)
tax_percent = "{:.0%}".format(tax_rate)
medicare_percent = "{:.0%}".format(medicare_levy_rate)
medicare_levy = (gross_pay * medicare_levy_rate)
net_pay = (gross_pay-(tax+medicare_levy))

print("Employee Name:" + employee_name)
print("Hours Worked:" + str(hours_worked))
print("Pay Rate: $" + str(pay_rate))
print("Gross Pay: $" + str(gross_pay))
print("Deductions:")
print(" ATO tax (" + tax_percent + "): $" + str(tax))
print(" Medicare Levy (" + medicare_percent + "): $" + str(medicare_levy))
print(" Total Deductions: $" + str((medicare_levy + tax)))

print("Net Pay: $" + str(net_pay))
