emp_name=(input("Enter employe name:"))
emp_desigination=(input("enter employee desigination:"))
salary=int(input("Enter employee salary:"))
special_allowances=int(input("Enter employee special allowances:"))
bonus=int(input("Enter employee bonus:"))
Gross_monthly_salary=salary+special_allowances
print("employee name:",emp_name)
print("employee desigination",emp_desigination)
print("employee salary:",salary)
print("special allowances:",special_allowances)
print("employee bonus:",bonus)
print("Gross monthly salary:",Gross_monthly_salary)

#gross anuual salary
Gross_annual_salary=Gross_monthly_salary*12+bonus
print("gross annual salarly:",Gross_annual_salary)

#taxable income 
taxable_income=0
if(Gross_annual_salary>500000):
    taxable_income=Gross_annual_salary*15/100
    print("taxable income:",Gross_annual_salary-taxable_income)
elif(Gross_annual_salary>400000):
    taxable_income=Gross_annual_salary*10/100
    print("taxable income:",Gross_annual_salary-taxable_income)
else:
    taxable_income=Gross_annual_salary*2/100
    print("taxable income:",Gross_annual_salary-taxable_income)
     

