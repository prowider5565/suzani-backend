from paycomuz import Paycom


class CheckOrder(Paycom):
    def check_order(self, amount, account, *args, **kwargs):
        return self.ORDER_FOUND
        
    def successfully_payment(self, account, transaction, *args, **kwargs):
            print(account)

    def cancel_payment(self, account, transaction, *args, **kwargs):
            print(account)