from src.accounting.mailpayment import MailPayment
from src.accounting.directdepositpayment import DirectDepositPayment
from src.accounting.pickuppayment import PickupPayment

class PaymentMethod:

    def __init__(self, payment_method):
        self.__payment_method = payment_method

    def pay(self, person):
        if self.__payment_method == "Pickup":
            return PickupPayment
        elif self.__payment_method == "Direct Deposit":
              return DirectDepositPayment.make_deposit()
        elif self.__payment_method == "Mail Payment":
              return MailPayment