from core.validators import Validators
from core.exception import NotFileException, TypeFileException

class Provider(object):
    
    type_file = 'txt'
    
    def __init__(self):
        self.validators = Validators()
    
    
    def open_data_set(self):
        if self.validators.validate_file(self.file_path):
            if self.validators.validate_type_file(self.file_path, self.type_file):
                self.data_set = open(self.file_path, "r")
            else:
                raise TypeFileException(self.type_file)
        else:
            raise NotFileException(self.file_path)
    
    
    def read_data_set(self):
        self.open_data_set()
        try:
            self.data = self.data_set.readlines()
        except Exception as e:
            return False
        return True


         
    def constructor_json(self):
        if self.read_data_set():
            return self.constructor_schedule()
        else:
            return {}
        
                    
    def constructor_week(self):
        data_json = dict()
        for week in self.data:
            key, value = week.split('=')
            if key in data_json:
                data_json[key].append(value)
            else:
                data_json[key] = [value]
        return data_json  
      
        
    def constructor_schedule(self):
        data_json = self.constructor_week()
        schedule = []
        for people in data_json:
            for week in data_json[people]:
                schedule.append(self.constructor_day(week.split(',')))
            data_json[people] = schedule.copy()
            schedule.clear()
        return data_json      
    
    
    def constructor_day(self, schedule):
        day_list = dict()
        for day in schedule:
            day_name = day[0:2]
            hours = day[3:].split('-')
            if day_name in day_list:
                day_list[day_name].append([hours])
            else:
                day_list[day_name] = [hours]
        return day_list
                

    def get_schedule(self, file_path):
        self.file_path = file_path
        return  self.constructor_json()