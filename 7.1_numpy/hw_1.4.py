import numpy as np

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
next_user_stats = np.array([0, 1, 2, 0, 0, 0])


def cosine(a, b):
    a_lenght = np.linalg.norm(a)
    b_lenght = np.linalg.norm(b)
    return np.dot(a, b) / (a_lenght * b_lenght)


max_val = max_index = 0
for i, v in enumerate(users_stats):
    val = cosine(next_user_stats, v)
    if val > max_val:
        max_val = val
        max_index = i
print(max_index)
