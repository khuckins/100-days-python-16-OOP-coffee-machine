class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self, cost):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            res = input(f"How many {coin}?: ").lower()
            coin_inserted = 0
            if res == 'cancel':
                return coin_inserted

            while True:
                try:
                    coin_inserted = int(res)
                    break
                except ValueError:
                    print("Input must be a number. Input 'cancel' to cancel your order.")
                    res = input(f"How many {coin}?: ")
                    if res == 'cancel':
                        return coin_inserted

            self.money_received += coin_inserted * self.COIN_VALUES[coin]
            if self.money_received >= cost:
                break
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins(cost)
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Not enough money provided. Money refunded.")
            self.money_received = 0
            return False
