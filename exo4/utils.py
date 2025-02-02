def merge_intervals(intervals):
    """
    merge a list of intervals that overlap.
    :param intervals: list of tuples (start_time, end_time)
    :return: list of intervals merged
    """
    if not intervals:
        return []

    print(f"Intervals: {intervals}")

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

