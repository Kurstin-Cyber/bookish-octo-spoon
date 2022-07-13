def is_unique(my_string):
    for i in range(len(my_string) - 1):
        for j in range(i + 1, len(my_string)):
            if my_string[i] == my_string[j]:
                return False

    return True


print(is_unique("abc"))
print(is_unique("Kurstin"))
print(is_unique("Matthew"))
print(is_unique("Tuesday"))
