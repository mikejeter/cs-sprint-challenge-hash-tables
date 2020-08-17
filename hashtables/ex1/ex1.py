def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    hash_table = {}

    if length <= 1:
        
        return None

    for i in range(length):

        weight_remaining = limit - weights[i]

        if weight_remaining in hash_table:

            weight = hash_table[weight_remaining]

            weight_limit = (i, weight)

            return weight_limit

        else:

            hash_table[weights[i]] = i

    return None

print("Output", get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))
