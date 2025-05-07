def calculate_mean(numbers):
    if not numbers:
        return 0
    return sum (numbers) / len(numbers)

#Example
scores =[77, 85, 25, 49, 56]
mean = calculate_mean(scores)
print("Mean score:", mean)