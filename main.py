
def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'a+', encoding='UTF-8') as file:
        for line in file:
            for search_string in line:
                file.write(new_string)


if __name__ == "__main__":
    append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")