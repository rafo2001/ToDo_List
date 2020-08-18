def get_percentage(real_number, round_digis=None):
    if round_digis is None:
        return f"{int(real_number * 100)}%"
    else:
        return f"{round(real_number * 100, round_digis)}%"
