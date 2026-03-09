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

def bucket_sort(arr: List, k) -> List:
    max_element = max(arr) + 1
    
    result = [[] for _ in range(0, k)]
    final_result = []
    for element in arr:
        index = (element * k) // max_element
        result[index].append(element)

    for bucket in result:
        final_result.extend(insertion_sort(bucket))

    return final_result

if __name__ == "__main__":
    arr = [10, 20, 30, 99, 2, 3, 0, 3, 9, 2]
    print(bucket_sort(arr, 5))