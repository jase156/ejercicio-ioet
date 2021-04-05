from core import Provider
class ModelPay(object):
    
    def __init__(self):
        self.provider = Provider()
    
    def read_schedule(self, ruta:str)->dict:
        return self.provider.get_schedule(ruta)

    