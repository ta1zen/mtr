p_xi1 = 0.3  
p_xi2 = 0.7  

p_theta1_xi1 = 0.9
p_theta2_xi1 = 0.1
p_theta1_xi2 = 0.4
p_theta2_xi2 = 0.6

old_price = 50
new_prices = [50 * 1.1, 50 * 1.15, 50 * 1.2]
cost_price = 30

sales_high_elasticity = [1900, 1800, 1700]
sales_medium_elasticity = [1800, 1700, 1500]

old_sales = 2000  
old_profit = (old_price - cost_price) * old_sales
print("Прибуток за старою ціною:", old_profit)

expected_profits = []
for i in range(3):
    profit_theta1 = (new_prices[i] - cost_price) * sales_high_elasticity[i]
    profit_theta2 = (new_prices[i] - cost_price) * sales_medium_elasticity[i]
    
    expected_profit = (p_xi1 * (p_theta1_xi1 * profit_theta1 + p_theta2_xi1 * profit_theta2) +
                       p_xi2 * (p_theta1_xi2 * profit_theta1 + p_theta2_xi2 * profit_theta2))
    expected_profits.append(expected_profit)
    print(f"Очікуваний прибуток при підвищенні ціни на {round(new_prices[i]/old_price - 1, 1) * 100}%:", round(expected_profit, 1))

max_profit = max(expected_profits)
best_option = expected_profits.index(max_profit) + 1

print(f"\nНайкращий варіант підвищення ціни — підвищити на {round((new_prices[best_option - 1] / old_price - 1) * 100, 1)}%")

if max_profit > old_profit:
    print("Підняття ціни має сенс, оскільки очікуваний прибуток вищий за прибуток за старою ціною.")
else:
    print("Піднімати ціну недоцільно, оскільки за старою ціною прибуток буде максимальним.")
