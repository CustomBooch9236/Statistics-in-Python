numbers = [1, 2, 3, 4, 5]

sample_var = sum((x - sum(numbers)/len(numbers))**2 for x in numbers)/(len(numbers)-1)

print(sample_var)
