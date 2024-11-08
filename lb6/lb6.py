import numpy as np

P = np.array([1/2, 1/3, 1/6])  
F1 = np.array([
    [2.5, 3.5, 4.0],
    [4.5, 2.0, 3.5],
    [3.0, 6.0, 2.5],
    [5.5, 3.5, 3.5]
])  

F2 = np.array([
    [20, 35, 50],
    [60, 30, 50],
    [85, 40, 40],
    [100, 85, 40]
])  

V = np.array([3, 1])  

expected_F1 = F1 @ P
expected_F2 = F2 @ P


norm_F1 = (max(expected_F1) - expected_F1) / (max(expected_F1) - min(expected_F1))
norm_F2 = (expected_F2 - min(expected_F2)) / (max(expected_F2) - min(expected_F2))

compromise_values = V[0] * norm_F1 + V[1] * norm_F2

best_decision_index = np.argmax(compromise_values) + 1  
expected_F1, expected_F2, norm_F1, norm_F2, compromise_values, best_decision_index

print("Очікувані значення збитків (F1^-):", expected_F1)
print("Очікувані значення виробництва (F2^+):", expected_F2)
print("Нормалізовані збитки (F1^-):", norm_F1)
print("Нормалізоване виробництво (F2^+):", norm_F2)
print("Компромісні значення:", compromise_values)
print("Найкращий варіант рішення:", best_decision_index)