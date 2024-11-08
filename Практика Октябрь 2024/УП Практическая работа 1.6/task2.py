with open('numsTask2.txt', 'r') as file:
    words = file.read().splitlines()
    long_string = ' '.join(words)
    print(long_string)
