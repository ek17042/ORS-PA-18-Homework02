def can_string_be_float(user_value):

    allowed_characters = ["0","1","2","3","4","5","6","7","8","9",".","-"]

    for x in user_value:
        if x not in allowed_characters:
            return False

    nr_of_dots = 0

    for x in user_value:
        if x == ".":
            nr_of_dots = nr_of_dots + 1

    if nr_of_dots > 1:
        return False

    nr_of_minuses = 0

    for x in user_value:
        if x == "-":
            nr_of_minuses = nr_of_minuses + 1

    if nr_of_minuses > 1:
        return False

    if nr_of_minuses == 1:
        if user_value[0] != "-":
            return False

    return True
def main():
    user_value = input("Enter string which will be evaluated: ")
    if can_string_be_float(user_value):
        print(float(user_value))
    else:
        print("String cannot be onverted to float!")
    #print(float(user_value))
main()