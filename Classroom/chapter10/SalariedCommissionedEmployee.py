from CommissionEmployee import CommissionEmployee
class SalariedCommissionedEmployee(CommissionEmployee):
    def __init__(self, f_name, l_name, social_security, gross_sales, commission_rate, base_salary):
        super().__init__(f_name, l_name, social_security, gross_sales, commission_rate)
        self.base_salary = base_salary
    
    def earning(self):
        return super().earning() + self.base_salary
    
    def __str__(self):
        return super().__str__() + f'\nBase Salary: {self.base_salary}'
    
'''c2 = SalariedCommissionedEmployee("Animesh", "Patra", 2241016255, 90000, 0.5, 100000 )
print (c2)'''
    

