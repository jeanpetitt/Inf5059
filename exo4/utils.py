def merge_intervals(intervals):
    """
    merge a list of intervals that overlap.
    :param intervals: list of tuples (start_time, end_time)
    :return: list of intervals merged
    """
    if not intervals:
        return []

    # sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]

        if start <= last_end:  # overlapping -> fusion
            merged[-1] = (last_start, max(last_end, end))
        else:  # not chevauchement -> add interval
            merged.append((start, end))

    return merged

intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
merged_intervals = merge_intervals(intervals)

print(f"Merged intervals : {merged_intervals}")
# Case where intervalle are not overlap
merged_intervals = merge_intervals([(1, 2), (3, 4), (5, 6)])
print(f"Merged intervals : {merged_intervals}")  

# Case where we have overlapping
merged_intervals = merge_intervals([(1, 5), (2, 6), (3, 7)])
print(f"Merged intervals : {merged_intervals}")  

# Case with one interval
merged_intervals = merge_intervals([(5, 10)])
print(f"Merged intervals : {merged_intervals}")  

