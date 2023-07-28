def count_positives_sum_negatives(arr):
    if not arr:
        return []
    positive_count = 0
    negative_sum =0
    
    for x in arr:
        if x > 0:
            positive_count += 1
        elif x < 0:
            negative_sum += x
    return [positive_count, negative_sum]
