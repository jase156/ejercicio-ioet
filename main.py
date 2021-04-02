from modules import ModelPay
if __name__ == "__main__":
    print("ingresa la ruta")
    ruta = input()
    pay = ModelPay()
    pay.read_schedule(ruta)