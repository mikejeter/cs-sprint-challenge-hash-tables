def intersection(arrays):
    """
    YOUR CODE HERE
    """
    result = []

    hash_table = {}

    for subs in arrays:
        for num in subs:
            if num not in hash_table:
                hash_table[num] = 1
            else:
                result.append(num)

    print(result)
    result = dict.fromkeys(result)
    print(result)
    result = list(result)
    print(result)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
