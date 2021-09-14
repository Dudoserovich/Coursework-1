from itertools import chain


# естественное слияние
class NaturalMerge:
    def __init__(self):
        self.comparison = 0
        self.permutation = 0

    def natural_sort(self, array):
        l_r = self.__distribution(array)
        while len(l_r[0]) != 0 and len(l_r[1]) != 0:
            l_r = self.__distribution(self.__merge(l_r[0], l_r[1]))
        return list(chain.from_iterable(l_r[0] + l_r[1]))

    # стадия распределения
    def __distribution(self, array):
        self.permutation += len(array) # перестановки
        if len(array) == 2:
            self.permutation += len(array)
        if len(array) < 2:
            return array[:]
        else:
            left = []
            right = []
            i = 0
            check = False  # False - левый список, иначе правый
            while i <= len(array) - 1:
                block_left = []
                block_right = []
                # запись в вспомогательный список
                while i != len(array) - 1 and array[i] <= array[i + 1]:
                    self.comparison += 1
                    if not check:
                        block_left.append(array[i])
                    else:
                        block_right.append(array[i])
                    i += 1
                if i <= len(array) - 1 and array[i - 1] <= array[i]:  # добавляем не добавленный элемент
                    self.comparison += 1
                    if not check:
                        block_left.append(array[i])
                        i += 1
                    else:
                        block_right.append(array[i])
                        i += 1
                if i + 1 < len(array) and i != len(array) - 1 and array[i] > array[i + 1]:
                    self.comparison += 1
                    if not check:
                        block_left.append(array[i])
                        i += 1
                        if i == len(array) - 1:
                            block_left.append(array[i])
                    else:
                        block_right.append(array[i])
                        i += 1
                        if i == len(array) - 1:
                            block_right.append(array[i])
                elif i + 1 == len(array):
                    if not check:
                        block_left.append(array[i])
                        left.append(block_left)
                        i += 1
                        break
                    else:
                        block_right.append(array[i])
                        right.append(block_right)
                        i += 1
                        break
                # записываем список в основной список
                if not check and len(block_left) != 0:
                    left.append(block_left)
                elif check and len(block_right) != 0:
                    right.append(block_right)
                if i + 1 >= len(array):
                    return [left, right]
                if array[i - 1] > array[i]:
                    check = not check
        # если наш список состоит из 2ух чисел, то возвращаем отсортированный список
        if len(left) == len(right) == 1:
            return sorted([left, right])
        elif len(array) == 2:
            return [sorted(list(chain.from_iterable(left)))], []
        return [left, right]

    # стадия слияния
    def __merge(self, left, right):
        if len(left) == 0 or len(right) == 0:
            return list(chain.from_iterable(left + right))
        result = []
        check: bool
        if len(left) < len(right):
            size = len(left)
            check = False
        else:
            size = len(right)
            check = True
        for k in range(size):
            # записываем отсортированную последовательность
            result.append(sorted(left[k] + right[k]))
        if len(right) == len(left):
            return list(chain.from_iterable(result))
        elif check:
            result.append(left[size])
        else:
            result.append(right[size])
        self.permutation += len(list(chain.from_iterable(result)))
        return list(chain.from_iterable(result))
