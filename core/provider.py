from validators import Validators

class Provider(object):
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.validators = Validators()
    
    
    def open_dataset(self):
        if(self.validators.validate_file(self.file_path)):
            self.data_set = open(self.file_path, "r")
            print(self.data_set.read())
         

         
    

    
if __name__ == "__main__":
    print("ingresa la ruta")
    ruta = input()
    provider = Provider(ruta)   
    provider.open_dataset()
    