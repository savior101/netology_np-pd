import numpy as np
from numpy import linalg

odds = np.array([[4, 2, 1], [1, 3, 0], [0, 5, 4]])
equals = np.array([4, 12, -3])

result = linalg.solve(odds, equals)
print(f'Ответ:\n'
      f'x = {round(result[0], 2)}\n'
      f'y = {round(result[1], 2)}\n'
      f'z = {round(result[2], 2)}')
print('\nПроверка:')
if np.allclose(np.dot(odds, result), equals):
    print('Система уравнений решена верно')
else:
    print('Система уравненений решена не верно')
