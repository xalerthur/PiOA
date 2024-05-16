def subset_sum_backtrack(numbers, target):
    def backtrack(start, path, target):
        if target == 0:
            result.append(path)
            return
        if target < 0:
            return
        for i in range(start, len(numbers)):
            backtrack(i + 1, path + [numbers[i]], target - numbers[i])

    result = []
    backtrack(0, [], target)
    return result


W = [2, 4, 7, 4, 1, 3]
D = 12

result = subset_sum_backtrack(W, D)
print("Возможные подмножества суммы", D, ":")
for subset in result:
    print(subset)
