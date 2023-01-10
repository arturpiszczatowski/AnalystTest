import numpy as np
import matplotlib.pyplot as plt


# 1 MMcf = 1,000,000 MMBtu
def mmcf_to_mmbtu(mmcf):
    return mmcf * 1000000


def max_profit_func(gas_prices, storage):
    max_profit = 0
    # to control whether storage is empty or not
    empty = True
    day = 0

    while day < len(gas_prices) - 1:
        if empty:
            # searching for next lowest price (taking into account same price days)
            while gas_prices[day] >= gas_prices[day + 1]:
                day += 1
                if day >= len(gas_prices) - 1:
                    break
            # to avoid buying without an option of selling for profit by the end of the gas price series
            if day < len(gas_prices) - 1:
                max_profit -= gas_prices[day] * storage
                plt.scatter(day, gas_prices[day], marker='o', color='g')
                empty = False
                # print(f"Bought on day {day} for {gas_prices[day]}")

        else:
            # searching for next highest price
            while gas_prices[day] < gas_prices[day + 1]:
                day += 1
                if day >= len(gas_prices) - 1:
                    break
            max_profit += gas_prices[day] * storage
            plt.scatter(day, gas_prices[day], marker='o', color='r')
            empty = True
            # print(f"Sold on day {day} for {gas_prices[day]}")

    return max_profit


# $/MMbtu
day_gas_price = np.array(
    [2.91, 2.775, 2.855, 2.89, 2.595, 2.99, 2.925, 2.685, 3.95, 3.56, 3.49, 3.92, 3.255, 3.195, 3.305, 3.39, 3.21, 3.33,
     4.03, 4.05, 4.105, 3.565, 3.24, 3.335, 3.365, 3.26, 3.21, 3.525, 3.405, 3.35, 3.02, 2.755], float)

plt.plot(day_gas_price)
plt.xlabel('Day')
plt.ylabel('Price [$/MMbtu]')

# MMcf
capacity = 200
# MMbtu
capacity = mmcf_to_mmbtu(capacity)

print("Max profit from given gas price series: ${:,.2f}".format(max_profit_func(day_gas_price, capacity)))
plt.legend(["price", "buy", "sell"])
plt.grid(True)
plt.show()
