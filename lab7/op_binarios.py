# Esta funcion debe devolver los resultados de las operaciones and, or y xor
def calcula_todas_las_ops(num1, num2):
  op_and = num1 & num2
  op_or = num1 | num2
  op_xor = num1 ^ num2

  print(f"op_and: {op_and} op_or: {op_or} op_xor: {op_xor}")


calcula_todas_las_ops(4, 1) # 100 001


  # d3    d2  d1
# 1   0   0 &
# 0   0   1
#------
#  000   -> 0

# d1: 0 & 1 = 0
# d2: 0 & 0 = 0
# d3: 1 & 0 = 0

# 000 = 0


# 100 |
# 001
#------
# 101 ->    5   

# d1: 0 | 1 = 1
# d2: 0 | 0 = 0
# d3: 1 | 0 = 1

# 101 = 5

# 100 ^
# 001
#------
# 101   -> 5


calcula_todas_las_ops(0, 1)
calcula_todas_las_ops(5, 1)