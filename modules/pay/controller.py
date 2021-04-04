from core import TypeFileException, NotFileException

class ControllerPay(object):
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.mesagge = "Ingres unicamente las opciones presentadas en pantalla"
    
    def admin_main_menu(self):
        while True:      
            switch = {'1':self.calculate_pay_all,'2':exit}
            case = self.view.show_main_menu()
            if case in switch:
                switch[case]()
            else:
                self.view.show_message_error(self.mesagge)
    
    
    def calculate_pay_all(self):
        while True:
            switch = {'1':self.input_file,'2':self.breaks}
            case = self.view.show_set_dataset_menu()
            if case in switch:
                if not switch[case]():
                    return True
            else:
                self.view.show_message_error(self.mesagge)
        
    def input_file(self):
        while True:
            switch = {'1':self.breaks}
            try:
                file_path = self.view.show_input_file()
                if file_path in switch:
                    return True   
                data_set = self.model.read_schedule(file_path)
            except NotFileException as e:
                self.view.show_message_error(e)
            except TypeFileException as e:
                self.view.show_message_error(e)
            
    
        
    def breaks(self):
        return False
        
        