def tallest_people(**kwargs):
    names = []
    height = 0
    for key, value in kwargs.items():
        if value == height:
            names.append(key)
        elif value > height:
            height = value
            names = [key]
    for name in sorted(names):
        print(f"{name} : {height}")
