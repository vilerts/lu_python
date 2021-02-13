from fold_class_v6.parent_package.package1.subpackage.mult_div import *
from fold_class_v6.parent_package.package1.sum_dif import *

def runCalculator(var1, var2, operator):
  result = 0
  if operator == "+":
    result = calcualteSum(var1, var2)
  elif operator == "-":
    result = calculateDifference(var1, var2)
  elif operator == "/":
    result = calculateDivison(var1, var2)
  elif operator == "*":
    result = calculateMultiplication(var1, var2)
  return result
