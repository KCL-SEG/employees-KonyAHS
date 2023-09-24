"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, empName):
        self.empName = empName

    def get_pay(self):
        pass
    

    def __str__(self):
        return self.empName
        

class SalaryEmployee(Employee):
    def __init__(self, name, salary, commission = 0,  number = 0):
        super().__init__(name)
        self.salary = salary
        self.commission = commission
        self.number = number
    
    def get_pay(self):
        return self.salary + self.commission + self.commission*(max(0,self.number-1))
    
    def __str__(self):
        returnString = Employee.__str__(self)
        returnString += f" works on a monthly salary of {self.salary}"
        
        if self.commission:
            if self.number:
                #Commission + per contract
                returnString += f" and receives a commission for {self.number} contract(s) at {self.commission}/contract.  Their total pay is {self.get_pay()}."
                return returnString
            
            #Commission
            returnString += f" and receives a bonus commission of {self.commission}.  Their total pay is {self.get_pay()}."
            return returnString
        
        #No commission
        return returnString + f". Their total pay is {self.get_pay()}."
            
class HourlyEmployee(Employee):
    def __init__(self, name, hours ,hourlyRate, commission = 0,  number = 0):
        super().__init__(name)
        self.hours = hours
        self.hourlyRate = hourlyRate
        self.commission = commission
        self.number = number
    
    def get_pay(self):
        return self.hours * self.hourlyRate + self.commission + self.commission*(max(0,self.number-1))
    
    def __str__(self):
        returnString = Employee.__str__(self)
        returnString += f" works on a contract of {self.hours} hours at {self.hourlyRate}/hour"
        
        if self.commission:
            if self.number:
                #Commission + per contract
                returnString += f" and receives a commission for {self.number} contract(s) at {self.commission}/contract.  Their total pay is {self.get_pay()}."
                return returnString
            
            #Commission
            returnString += f" and receives a bonus commission of {self.commission}.  Their total pay is {self.get_pay()}."
            return returnString
        
        #No commission
        return returnString + f". Their total pay is {self.get_pay()}."            
            
        

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryEmployee('Billie',4000)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryEmployee('Robbie', 2000, 1500)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryEmployee('Renee',3000, 200, 4)


# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyEmployee('Charlie', 100, 25)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyEmployee('Ariel',120,30,600)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyEmployee('Jan',150,25, 220,3)

print(billie)
print(robbie)
print(jan)
print(billie)