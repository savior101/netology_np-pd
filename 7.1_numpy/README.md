## Домашнее задание к лекции "Библиотека numpy. Вычислительные задачи"
### Задание 1
Создайте numpy array с элементами от числа N до 0 (например, для N = 10 это будет array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])).
### Задание 2
Создайте диагональную матрицу с элементами от N до 0. Посчитайте сумму ее значений на диагонали.
### Задание 3
Решите систему уравнений:\
4x + 2y + z = 4\
x + 3y = 12\
5y + 4z = -3
### Задание 4
Имеется матрица покупок в интернет-магазине. Столбец А - ID пользователя. Остальные столбцы - количество покупок категорий товаров этим пользователем\
Матрица в виде numpy array:
```python
users_stats = np.array(
    [
        [2, 1, 0, 0, 0, 0],
        [1, 1, 2, 1, 0, 0],
        [2, 0, 1, 0, 0, 0],
        [1, 1, 2, 1, 0, 1],
        [0, 0, 1, 2, 0, 0],
        [0, 0, 0, 0, 0, 5],
        [1, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 3],
        [1, 0, 0, 2, 1, 4]
    ], 
    np.int32
)
```
На сайт заходит очередной посетитель, о покупках которого известно следующее:
```python
next_user_stats = np.array([0, 1, 2, 0, 0, 0])
```
Найдите индекс самого похожего пользователя max_index.