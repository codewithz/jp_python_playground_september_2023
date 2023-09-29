# You will take an input of salary
# If salary is between 5000 and 50000 , it is fine
# else throw SalaryNotInRangeError

class SalaryNotInRange(Exception):
    """
    Exceptions raised for errors in salary range
    """

    def __init__(self,salary,message="Salary is not in range of 5000 -- 50000"):
        self.salary=salary
        self.message=message
        super().__init__(self.message)





# ---------------------------------

salary=int(input("Enter salary:"))

if 5000 <= salary <= 50000:
    print("Salary :",salary)
else:
    raise SalaryNotInRange(salary)
    # Throw /Raise exception