from core import TypeFileException, NotFileException

class ControllerPay(object):
    
    def __init__(self, model, view, business):
        self.model = model
        self.view = view
        self.business = business
        self.mesagge = "Ingres unicamente las opciones presentadas en pantalla"
    
    def admin_main_menu(self):
        while True:      
            switch = {'1':self.calculate_menu,'2':exit}
            case = self.view.show_main_menu()
            if case in switch:
                switch[case]()
            else:
                self.view.show_message_error(self.mesagge)
    
    
    def calculate_menu(self):
        while True:
            switch = {'1':self.input_file,'2':self.breaks}
            case = self.view.show_set_dataset_menu()
            if case in switch:
                if switch[case]():
                    return False
            else:
                self.view.show_message_error(self.mesagge)
        
    def input_file(self):
        while True:
            switch = {'1':self.breaks}
            try:
                file_path = self.view.show_input_file()
                if file_path in switch:
                    return False   
                self.data_set = self.model.read_schedule(file_path)
                if not self.data_set:
                    self.view.show_message_error("El documento ingresado se encuentra vacio, intente nuevamente con uno nuevo")
                else: 
                    self.select_calculate(file_path)
            except NotFileException as e:
                self.view.show_message_error(e)
            except TypeFileException as e:
                self.view.show_message_error(e)
    
    def select_calculate(self, file):
        while True:
            switch = {'1':self.calculate_pay_all,'2':self.calculate_pay_people,'3':self.breaks}
            case = self.view.show_calculate_pay_menu(file)
            if case in switch:
                if switch[case]():
                    return False
            else:
                self.view.show_message_error(self.mesagge)
            
            
    def calculate_pay_all(self):
        while True:
            switch = {'1':self.breaks}
            payments = self.business.payments(self.data_set)
            case = self.view.show_pay_all(payments)
            if case in switch:
                if switch[case]():
                    return False
            else:
                self.view.show_message_error(self.mesagge)
                
        
    def calculate_pay_people(self):
        while True:
            name = self.view.input_name()
            if name in self.data_set:
                switch = {'1':self.breaks}
                payments = self.business.payments({name:self.data_set[name]})
                case = self.view.show_pay_all(payments)
                if case in switch:
                    if switch[case]():
                        return False
                else:
                    self.view.show_message_error(self.mesagge)
            else:
                self.view.show_message_error("El nombre no se encuentra en el registro")

        
    def breaks(self):
        return True
        
        