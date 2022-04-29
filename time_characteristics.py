from statistics import mean


def get_time_characteristics(times, title):
    print(f"\n*** Time {title} cache ***")
    min_time = min(times)
    max_time = max(times)
    mean_time = mean(times)
    print(f"min time: {min_time}")
    print(f"max time: {max_time}")
    print(f"average time: {mean_time}")
