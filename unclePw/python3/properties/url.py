#coding=utf-8


from python3.modules.sys.control.login_controller import LoginControl,ExitLoginControl
from python3.modules.sys.control.register_controller import RegisterControl,RegisterCheck
from python3.modules.selenium.control.selenium_control import SelectClass,TableInput
url=[
    # (r'/code_auto',GetJsonData),
    (r'/login',LoginControl),
    (r'/',LoginControl),

    (r'/register',RegisterControl),
    (r'/registerCheck',RegisterCheck),
    (r'/exit',ExitLoginControl),

    (r'/select_class',SelectClass),
    (r'/table_input',TableInput)

    # (r'/uploadfile',uploadFile),
    # (r'/bill',AddBill),
    # (r'/billShow',ShowBill),
    # (r'/getBillCategory',GetBillCategory)
]