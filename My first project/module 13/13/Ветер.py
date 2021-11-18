def get_wind_class(speed):
    if 1 <= speed <= 4:
        return "weak [1]"
    elif 5 <= speed <= 10:
        return 'moderate [2]'
    elif 11 <= speed <= 18:
        return "strong [3]"
    elif 19 <= speed:
        return 'hurricane [4]'
print(get_wind_class(3))