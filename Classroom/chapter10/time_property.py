class Time:
    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    @property
    def hour(self):
        return self._hour
    @hour.setter
    def hour(self, value):
        if not 0 <= value < 24:
            raise ValueError("Hour must be between 0 and 23")
        self._hour = value
        
    @property
    def minute(self):
        return self._minute
    @minute.setter
    def minute(self, value):
        if not 0 <= value < 60:
            raise ValueError("Minute must be between 0 and 59")
        self._minute = value
    
    @property
    def second(self):
        return self._second
    @second.setter
    def second(self, value):
        if not 0 <= value < 60:
            raise ValueError("Second must be between 0 and 59")
        self._second = value
        
    #custom value updater method
    def timeUpdate(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f"{self.hour%12 if self.hour > 0 else 12}:{self.minute}:{self.second}"
    
time1 = Time(10, 30, 45)
print(time1)  

time1.timeUpdate(23, 45, 59)
print(time1)  

