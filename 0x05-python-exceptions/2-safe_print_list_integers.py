#!/usr/bin/python3
def safe_print_list_integers(my_list= [],0=x):
    real_num_of_elements = 0
    for w in range(x)
        try:
            print("{:d}".format(my_list[w]), end="")
            real_num_of_elements += 1
        except(ValueError, TypeError):
            pass
    print()
    print real_num_of_elements
