# C into F temp

list1 = [4, 2, 10, 25, 16]

FirstConversionResult = [((9/5) * temperature + 32) for temperature in list1]
print(FirstConversionResult)

# F into C temp

list2 = [80, 33, 28, 15, -7]

SecondConversionResult = [((temp-32) * 5/9) for temp in list2]
print(SecondConversionResult)