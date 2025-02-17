name = input('Enter employee name:')
id = int(input('Enter employee ID:'))
basics_alary = float(input('Enter employee salary:'))
allowances = float(input('Enter employee allowances:'))
bonus_percentage = float(input('Enter employee bonuspercentage:'))
gross_monthly_salary=basics_alary+allowances
annual_monthly_salary=(bonus_percentage/100*(gross_monthly_salary*12))+gross_monthly_salary*12
print('Employee details are:')
print('Name:                  ',name)
print('ID:                    ',id)
print('Basic Salary:          ',basics_alary)
print('Gross Monthly Salary:  ',gross_monthly_salary)
print('Annual Monthly Salary: ',annual_monthly_salary)