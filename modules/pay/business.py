from core import Time
from core import FormatTimeException
from core import Provider

class Business(object):
    
    def __init__(self):
        self.time = Time()
        self.provider = Provider()
        self.dataset = self.provider.get_table()
    
        
    def payments(self, data_set:dict)->dict:
        payments = dict()
        for people in data_set:
            payments[people] = self.week_work(data_set[people])
        return payments
            
    def week_work(self,weeks:list)->float:
        payment = 0
        try:
            for week in weeks:
                payment = payment + self.day_work(week)
            return round(payment,2)
        except FormatTimeException as e:
            return e
            
            
    def day_work(self,days:list)->float:
        pay_week = 0
        for day in days:
            pay_week = pay_week + self.calculate_hour(day,days[day])
        return pay_week
            
    def calculate_hour(self, day:str, hours:list)->float:
        pay_hour = 0
        for hour in hours:
            h, m = self.time.get_hours(hour[0],hour[1])
            for schedule in self.dataset[day]:
                pay_hour = pay_hour + self.calculate_payment(day,schedule,hour,h,m)
        return pay_hour
        
    def calculate_payment(self,day:str, schedule:list, hour:list, h:int, m:int)->float:
        pay = 0
        schedule_start = schedule[0]
        schedule_end = '24:00' if schedule[1] == '00:00' else schedule[1]
        hour_start = hour[0]
        hour_end = '24:00' if hour[1] == '00:00' else hour[1]
        if self.time.smaller_or_equal_than(schedule_start,hour_start) and self.time.greater_or_equal_than(schedule_end,hour_start):
            if self.time.greater_or_equal_than(schedule_end,hour_end):
                pay = (h*schedule[2]) + ((schedule[2]*m)/60)
            else:
                h_minus, m_minus = self.time.convert_to_time(self.time.subtraction(schedule_end,hour_start))
                pay = (h_minus*schedule[2]) + ((schedule[2]*m_minus)/60)
        elif self.time.greater_or_equal_than(hour_end,schedule_start) and self.time.smaller_or_equal_than(hour_end, schedule_end):
            h_minus, m_minus = self.time.convert_to_time(self.time.subtraction(hour_end,schedule_start))
            pay = (h_minus*schedule[2]) + ((schedule[2]*m_minus)/60)
            
        return round(pay,2)