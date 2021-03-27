import sys
for path in sys.path:
    print(path)

#################################

import sys
print("\n".join(sys.builtin_module_names))

#################################

import fold_class_v06.func 
radius = int(input("Enter radius: "))
print(f"Area: {fold_class_v06.func.calculateSphereArea(radius)}")
print(f"Volume: {fold_class_v06.func.calculateSphereVolume(radius)}")

#from fold_class_v6.func import calculateSphereArea, calculateSphereVolume
#radius = int(input("Enter radius: "))
#print(f"Area: {calculateSphereArea(radius)}")
#print(f"Volume: {calculateSphereVolume(radius)}")

#from fold_class_v6.func import *
#radius = int(input("Enter radius: "))
#print(f"Area: {calculateSphereArea(radius)}")
#print(f"Volume: {calculateSphereVolume(radius)}")


#################################

from fold_class_v06.parent_package.package2 import calculator,format_expression

var1 = int(input("Enter first number: "))
var2 = int(input("Enter second number: "))
operator = str(input("Enter operator: "))
result = calculator.runCalculator(var1, var2, operator)
print(format_expression.formatResult(var1,var2,operator,result))

#################################
