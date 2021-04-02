class ViewPay(object):
    
    @staticmethod
    def show_main_menu():
        print("///////////////////////////////")
        print("//       Gestor de pago      //")
        print("//            ACME           //")
        print("//                           //")
        print("//  1.-Calculo de pago       //")
        print("//  2.-Salir                 //")
        print("//                           //")
        print("///////////////////////////////")
        
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
    def show_calculate_pay_menu():
        print("///////////////////////////////////")
        print("//         Gestor de pago        //")
        print("//              ACME             //")
        print("//                               //")
        print("//  Opción 1 : Ingresar ruta de  //")
        print("//             archivo           //")
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