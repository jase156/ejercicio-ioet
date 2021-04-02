class Controller(object):
    def read_schedule(self, ruta):
        print(provider.get_schedule(ruta))