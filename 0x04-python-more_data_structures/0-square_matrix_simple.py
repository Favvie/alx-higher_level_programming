#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
     list = []
     for sublist in matrix:
          subArr = []
          for item in sublist:
               subArr.append(item ** 2)
          list.append(subArr)
     return list
