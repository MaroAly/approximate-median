def approximate_median(intervals, frequencies):
    # Calculate cumulative frequencies
    cumulative_frequencies = []
    cumulative_sum = 0
    for f in frequencies:
        cumulative_sum += f
        cumulative_frequencies.append(cumulative_sum)

    # Find median interval
    n = cumulative_sum
    median_interval_index = 0
    for i in range(len(cumulative_frequencies)):
        if cumulative_frequencies[i] >= n / 2:
            median_interval_index = i
            break

    # Compute approximate median value using linear interpolation
    L = intervals[median_interval_index][0]
    N = n
    F = cumulative_frequencies[median_interval_index - 1] if median_interval_index > 0 else 0
    w = intervals[median_interval_index][1] - L
    f = frequencies[median_interval_index]
    
    median = L + (N / 2 - F) * w / f
    
    return median

# example
intervals = [(1,5), (6,15), (16,20), (21,50), (51,80), (81,110)]
frequencies = [200, 450, 300, 1500, 700, 44]

approximate_median_value=approximate_median(intervals,frequencies)
print(f"The approximate median value is: {approximate_median_value}")
