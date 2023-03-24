# user info
name = input("Enter employee\'s name: ")
hours_worked = eval(input("Enter number of hours worked in a week: "))
hourly_pay = eval(input("Enter hourly pay rate: "))
federal_tax = eval(input("Enter federal tax withholding rate (ex. 0.12): "))
state_tax = eval(input("Enter state tax withholding rate (ex. 0.06): "))

# calculations for check
fed_tax_display = federal_tax * 100
state_tax_display = state_tax * 100
gross_pay = hours_worked * hourly_pay
fed_withhold = federal_tax * gross_pay
state_withhold = state_tax * gross_pay
total_deduct = fed_withhold + state_withhold
net_pay = gross_pay - total_deduct

# check output
print("\n\t" + name.upper() + " pay information".upper() + "\n\n" + format("Pay", ">30") + "\n" + format("Hours Worked:  ", ">40") + format(hours_worked, ">10.2f") + "\n" + format("Pay Rate: $", ">40") + format(hourly_pay, ">10.2f") + "\n" + format("Gross Pay: $", ">40") + format(gross_pay, ">10.2f") + "\n\n" + format("Deductions", ">34") + "\n" + format("Federal Withholding (" + str(fed_tax_display) + "%): $", ">40") + format(fed_withhold, ">10.2f") + "\n" + format("State Withholding (" + str(state_tax_display) + "%): $", ">40") + format(state_withhold, ">10.2f") + "\n" + format("Total Deduction: $", ">40") + format(total_deduct, ">10.2f") + "\n\n" + format("Net Pay: $", ">40") + format(net_pay, ">10.2f"))
