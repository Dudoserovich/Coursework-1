import operator


# простое слияние
class SimpleMerge:

    def __init__(self):
        self.comparison = 0
        self.permutation = 0

    def merge_sort(self, array, compare=operator.lt):
        if len(array) < 2:
            return array[:]
        else:
            self.permutation += len(array) # перестановка в 2 различных массивах
            middle = int(len(array) / 2)
            left = self.merge_sort(array[:middle], compare)
            right = self.merge_sort(array[middle:], compare)
            return self.merge(left, right, compare)

    def merge(self, left, right, compare):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            self.comparison += 1
            self.permutation += 1 # считаем количество перестановок для слияния
            if compare(left[i], right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
            self.permutation += 1 # считаем количество перестановок для слияния
        while j < len(right):
            result.append(right[j])
            j += 1
            self.permutation += 1 # считаем количество перестановок для слияния
        return result
