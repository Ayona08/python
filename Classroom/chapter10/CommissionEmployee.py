class CommissionEmployee(object):
    def __init__(self, f_name, l_name, social_security, gross_sales, commission_rate):
        self.f_name = f_name
        self.l_name = l_name
        self.social_security = social_security
        self.gross_sales = gross_sales
        self.commission_rate = commission_rate

    @property
    def gross_sales(self):
        return self._gross_sales
    
    @gross_sales.setter
    def gross_sales(self, value):
        if value < 0:
            raise ValueError("Gross sales cannot be negative")
        self._gross_sales = value

    @property
    def commission_rate(self):
        return self._commission_rate
    @commission_rate.setter
    def commission_rate(self, value):
        if value < 0 or value > 1:
            raise ValueError("Commission rate must be between 0 and 1")
        self._commission_rate = value

    def earning(self):
        return self.gross_sales * self.commission_rate
    
    def __str__(self):
        return f"Employee Name: \n"+\
        f"First Name: {self.f_name},Last Name: {self.l_name}\n"+\
        f"Earning : {self.earning()}"
    
'''c1 = CommissionEmployee("Animesh", "Patra", 2241016255, 90000, 0.5 )
print (c1)'''