def remove_even_numbers(input_file):
    with open(input_file, 'r') as f:
        numbers = list(map(int, f.read().strip().split()))
    
    odd_numbers = [num for num in numbers if num % 2 != 0]
    
    with open(input_file, 'w') as f:
        f.write(' '.join(map(str, odd_numbers)))

input_file = 'nums.txt'

remove_even_numbers(input_file)