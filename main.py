lst_in = [[1, 2, 3],
          [1, 2, 3],
          [1, 2, 3]]


b = lst_in[::]

b[0][0] = 44
print(b)
print(lst_in)