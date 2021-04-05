class ViewPay(object):
    
    @staticmethod
    def show_message_error(text):
        print("{}".format(text))

    
    @staticmethod
    def show_main_menu():
        print("///////////////////////////////////")
        print("//         Gestor de pago        //")
        print("//              ACME             //")
        print("//                               //")
        print("//  1.-Calculo de pago           //")
        print("//  2.-Salir                     //")
        print("//                               //")
        print("///////////////////////////////////")
        
        #Pedir entrada de texto
        print('Opción',end=": ")
        return input()
    
    @staticmethod
    def show_set_dataset_menu():
        print("///////////////////////////////////")
        print("//         Gestor de pago        //")
        print("//              ACME             //")
        print("//                               //")
        print("//  Opción 1 : Calculo de pago   //")
        print("//                               //")
        print("//  1.-Ingresar ruta de archivo  //")
        print("//  2.-Regresar                  //")
        print("//                               //")
        print("///////////////////////////////////")
        
        #Pedir entrada de texto
        print('Opción',end=": ")
        return input()
    
    @staticmethod
    def show_input_file():
        print("///////////////////////////////////")
        print("//         Gestor de pago        //")
        print("//              ACME             //")
        print("//  1.-Regresar                  //")
        print("//                               //")
        print("//  Ingrese la ruta              //")
        print("//                               //")
        print("///////////////////////////////////")
        
        #Pedir entrada de texto
        print('Opción',end=": ")
        return input()

    @staticmethod
    def show_calculate_pay_menu(file):
        print("///////////////////////////////////")
        print("//         Gestor de pago        //")
        print("//              ACME             //")
        print("//                               //")
        print("//  Opción 1 : {}  //".format(file))
        print("//                               //")
        print("//                               //")
        print("//  1.-Calculo total de          //")
        print("//     empleados                 //")
        print("//  2.-Calculo por empleado      //")
        print("//  3.-Regresar                  //")
        print("//                               //")
        print("///////////////////////////////////")
        
        #Pedir entrada de texto
        print('Opción',end=": ")
        return input()

    @staticmethod
    def show_pay_all(payments):
        print("///////////////////////////////////")
        for people in payments:
            print("{} = {}".format(people,payments[people]))
        print("")
        print("1.- Regresar")    
        print("///////////////////////////////////")
        
        #Pedir entrada de texto
        print('Opción',end=": ")
        return input()
    
    @staticmethod
    def input_name():
        
        #Pedir entrada de texto
        print('Ingrese el nombre',end=": ")
        return input()