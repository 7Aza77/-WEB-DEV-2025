def split_and_join(line):
    # Split the string into a list on spaces
    words = line.split(" ")
    # Join the list using hyphens
    return "-".join(words)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
