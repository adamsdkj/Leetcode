from typing import List

def insertion_sort(arry: List) -> List:
    for index in range(1, len(arry)):
        index2 = index - 1
        for number in arry[index2::-1]:
            if arry[index] < number:
                tmp = number
                arry[index2] = arry[index]
                arry[index] = number
                index = index2
            index2 -= 1
    return arry

if __name__ == "__main__":
    arr = [10, 2, 7, 0, -1]
    print(insertion_sort(arr))