from modules.pay import ModelPay
from modules.pay import ViewPay
from modules.pay import ControllerPay

if __name__ == "__main__":
    run = ControllerPay(ModelPay(),ViewPay())
    run.admin_main_menu()
    