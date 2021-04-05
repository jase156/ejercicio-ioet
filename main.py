from modules.pay import ModelPay
from modules.pay import ViewPay
from modules.pay import ControllerPay
from modules.pay import Business

if __name__ == "__main__":
    run = ControllerPay(ModelPay(),ViewPay(), Business())
    run.admin_main_menu()
    