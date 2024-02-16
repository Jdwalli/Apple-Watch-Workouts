def calculate_time_delta(start_time, end_time, unit = 'seconds'):
    time_difference = end_time - start_time

    if unit == 'seconds':
        return time_difference.total_seconds()
    elif unit == 'minutes':
        return time_difference.total_seconds() / 60
    elif unit == 'hours':
        return time_difference.total_seconds() / 3600