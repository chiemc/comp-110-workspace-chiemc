def get_tax(price: int, tax_rate: float) -> float:
    return price * tax_rate


def total_cost(cost: int, tax: float) -> float:
    return cost + get_tax(price=cost, tax_rate=tax)


print(total_cost(cost=100, tax=0.07))

# line numbers are for the sake of this code bc it saves weird
# order to write frames depends on order in which functions are called
# heap: id: 0 fn 1-2|id: 1 fn 5-6
# stack/call stack: globals, get_tax id: 0, total_cost id:1
# stack/call stack: (new frame): total_cost, RA: 9, cost:100 tax:0.07, RV: 107.0
# stack/call stack: (new frame): get_tax, RA: 6, price: 100 tax_rate: 0.07
# stack/call stack: RV: 100*0.07=7.0
# output: 107.0
