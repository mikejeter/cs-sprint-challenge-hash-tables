def has_negatives(a):
    """
    YOUR CODE HERE
    """
    hash_table = {}

    result = []

    for num in a:
        if num not in hash_table:
            hash_table[num] = 1

    for num in a:
        if (num * -1) in hash_table and num > 0:
            result.append(num)

    print(result)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
