def make_readable(seconds):
    hours = seconds/60**2
    minutes = (seconds%60**2)/60
    seconds = (seconds%60**2%60)
    return "%02d:%02d:%02d" % (hours, minutes, seconds)
