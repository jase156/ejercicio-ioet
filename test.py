import unittest
from core import * 
from modules import *

class Test(unittest.TestCase):
    
    file_path = 'C:\\Users\\javie\\OneDrive\\Escritorio\\dataset.txt'
    bad_file_path = 'C:\\Users\\javie\\OneDrive\\Escritorio\\salario.txt'
    file_type = "txt"
    hour = ["01:00", "02:00"]
    result_hour = [1,0]
    minus = 60
    day = 'MO'
    schedule = ["00:01","09:00",25]
    data_set = {'RENE': [{'MO': [['10:00', '12:00'], ['13:00', '14:00']], 'TU': [['10:00', '12:00']], 'TH': [['01:00', '03:00']], 'SA': [['14:00', '18:00']], 'SU': [['20:00', '21:00']]}]}
    name = "RENE"
    pay = 230
    
    def setUp(self):
        self.validators = Validators()
        self.time = Time()
        self.provider = Provider()
        self.model = ModelPay()
        self.business = Business()
        self.provider.file_path = self.file_path
        self.provider.file_type = self.file_type
    
    #Test Core
    #Test Validators
    def test_validate_file_ture(self):
        self.assertTrue(self.validators.validate_file(self.file_path))
    
    def test_validate_type_file_true(self):
        self.assertTrue(self.validators.validate_type_file(self.file_path,self.file_type))
    
    def test_validate_file_false(self):
        self.assertFalse(self.validators.validate_file("{}a".format(self.file_path)))
    
    def test_validate_type_file_false(self):
        self.assertFalse(self.validators.validate_type_file(self.file_path,"{}a".format(self.file_type)))
    
    #Test Time
    def test_get_hours_return_2_item(self):
        self.assertCountEqual(self.time.get_hours(self.hour[0], self.hour[1]),[1,0])  
    
    def test_get_hours_exception(self):
        self.assertRaises(FormatTimeException, self.time.get_hours, self.hour[0], '')
    
    def test_get_hours_values(self):
        h,m = self.time.get_hours(self.hour[0], self.hour[1])
        self.assertEquals(h,self.result_hour[0])
        self.assertEquals(m,self.result_hour[1])
        
    def test_greater_than_true(self):
        self.assertTrue(self.time.greater_than(self.hour[1], self.hour[0]))
    
    def test_greater_than_false(self):
        self.assertFalse(self.time.greater_than(self.hour[0], self.hour[1]))
        
    def test_greater_or_equal_than__equal_true(self):
        self.assertTrue(self.time.greater_or_equal_than(self.hour[1], self.hour[1]))
    
    def test_greater_or_equal_than_equal_false(self):
        self.assertFalse(self.time.greater_or_equal_than(self.hour[0], self.hour[1]))
        
    def test_greater_or_equal_than__greater_true(self):
        self.assertTrue(self.time.greater_or_equal_than(self.hour[1], self.hour[0]))
    
    def test_greater_or_equal_than_greater_false(self):
        self.assertFalse(self.time.greater_or_equal_than(self.hour[0], self.hour[1]))

    def test_smaller_than_true(self):
        self.assertTrue(self.time.smaller_than(self.hour[0], self.hour[1]))
    
    def test_smaller_than_false(self):
        self.assertFalse(self.time.smaller_than(self.hour[1], self.hour[0]))
        
    def test_smaller_or_equal_than__equal_true(self):
        self.assertTrue(self.time.smaller_or_equal_than(self.hour[1], self.hour[1]))
    
    def test_smaller_or_equal_than_equal_false(self):
        self.assertFalse(self.time.smaller_or_equal_than(self.hour[1], self.hour[0]))
        
    def test_smaller_or_equal_than__smaller_true(self):
        self.assertTrue(self.time.smaller_or_equal_than(self.hour[0], self.hour[1]))
    
    def test_smaller_or_equal_than_smaller_false(self):
        self.assertFalse(self.time.smaller_or_equal_than(self.hour[1], self.hour[0]))
    
    def test_equals_true(self):
        self.assertTrue(self.time.equals(self.hour[1],self.hour[1]))
    
    def test_equals_false(self):
        self.assertFalse(self.time.equals(self.hour[1],self.hour[0]))
    
    def test_subtraction_true(self):
        self.assertEqual(self.time.subtraction(self.hour[1],self.hour[0]),self.minus)
    
    def test_subtraction_true(self):
        self.assertNotEqual(self.time.subtraction(self.hour[1],self.hour[0]),self.minus-10)
        
    #Provider   
    def test_open_data_set_exception_not_file(self):
        self.provider.file_path = "{}a".format(self.provider.file_path)
        self.assertRaises(TypeFileException)
        
    def test_open_data_set_exception_type_file(self):
        self.file_type = "{}a".format(self.file_type)
        self.assertRaises(TypeFileException)
        
    def test_read_data_set_true(self):
        self.assertTrue(self.provider.read_data_set())
        
    def test_constructor_json_type(self):
        self.assertIs(type(self.provider.constructor_json()),dict)
        
    def test_constructor_json_not_empty(self):
        empty = False
        if self.provider.constructor_json():
            empty = True
        self.assertTrue(empty)
    
    def test_constructor_json_empty(self):
        self.provider.file_path = self.bad_file_path
        empty = False
        if self.provider.constructor_json():
            empty = True
        self.assertFalse(empty)
    
    #Model
    def test_read_schedule_not_empty(self):
        empty = False
        if self.model.read_schedule(self.file_path):
            empty = True
        self.assertTrue(empty)
    
    def test_read_schedule_not_empty(self):
        empty = False
        if self.model.read_schedule(self.bad_file_path):
            empty = True
        self.assertFalse(empty)
        
    #Business
    def test_calculate_payment_value(self):
        self.assertEqual(self.business.calculate_payment(self.day,self.schedule,self.hour,self.result_hour[0],self.result_hour[1]),self.schedule[2])
    
    def test_calculate_payment_bad_value(self):
        self.assertNotEqual(self.business.calculate_payment(self.day,self.schedule,self.hour,(self.result_hour[0]+1),self.result_hour[1]),self.schedule[2])
    
    def test_payments_value(self):
        self.assertEqual(self.business.payments(self.data_set)[self.name],self.pay)
    
    def test_payments_bad_value(self):
        self.assertNotEqual(self.business.payments(self.data_set)[self.name],self.pay-10)
        
        
if __name__ == "__main__":
    unittest.main()