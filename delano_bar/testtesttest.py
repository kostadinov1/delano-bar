

# VALID PARIS

def pair_sum(arr, k):
    valid_pairs = []

    for i in range(len(arr)):
        current = arr[i]
        if i == len(arr) -1:
            break
        next_one = arr[i + 1]
        sum = current + next_one
        if sum == k:
            valid_pairs.append((current, next_one,))
    return valid_pairs


print(pair_sum([1, 3, 2, 2], 4))
