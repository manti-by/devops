def max_func(*args):
    max_val = args[0]
    for arg in args:
        if arg > max_val:
            max_val = arg
    return max_val


def min_func(*args):
    min_val = args[0]
    for arg in args:
        if arg < min_val:
            min_val = arg
    return min_val


def main(*func_type):
    if not func_type:
        print("Error")

    for arg in func_type:
        if arg == "max":
            max_number = max_func(10, 20, 30, 50, 100, 40, 200, 150)
            print(f"The maximum of the function is {max_number}")
        elif arg == "min":
            min_number = min_func(5, 1, 4, 6, 9,11, 50, 0.5, 0.61, 0.32)
            print(f"The minimum of the function is {min_number}")
        elif arg is None:
            print("No function arguments")
        else:
            max_number = max_func(10, 20, 30, 50, 100, 40, 200, 150)
            print(f"The maximum of the function is {max_number}")
            min_number = min_func(5, 1, 4, 6, 9,11, 50, 0.5, 0.61, 0.32)
            print(f"The minimum of the function is {min_number}")


if __name__ == "__main__":
    main()

