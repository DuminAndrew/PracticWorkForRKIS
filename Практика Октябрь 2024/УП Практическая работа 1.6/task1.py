with open('numsTask1.txt', 'r') as file:
    words = file.read().split()
    odd_length_words = [word for word in words if len(word) % 2 != 0]
    print(odd_length_words)
