from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def coffee_machine():
  coffee_maker = CoffeeMaker()
  money_machine = MoneyMachine()
  menu = Menu()
  while coffee_maker.get_activation():
    order = coffee_maker.prompt_order()

    if order == "off":
      coffee_maker.set_activation(False)
    elif order == "report":
      coffee_maker.report()
      money_machine.report()
    else:
      ordered_drink = menu.find_drink(order)

      if ordered_drink and coffee_maker.is_resource_sufficient(ordered_drink) and money_machine.make_payment(ordered_drink.cost):
        coffee_maker.make_coffee(ordered_drink)

coffee_machine()