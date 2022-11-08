import numpy as np

print('Сумма значений диагонали диагональной матрицы от N до 0:',
      sum(np.diag(np.diag(np.arange(int(input('Введите N: ')) - 1, -1, -1)))))
