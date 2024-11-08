def check_tickets(input_file, output_file):
    with open(input_file, 'r') as f:
        winning_numbers = set(map(int, f.readline().strip().split()))
        
        n = int(f.readline().strip())
        
        results = []
        
        for _ in range(n):
            ticket_numbers = set(map(int, f.readline().strip().split()))
            matches = len(winning_numbers.intersection(ticket_numbers))
            if matches >= 3:
                results.append("Lucky")
            else:
                results.append("Unlucky")
    
    with open(output_file, 'w') as f:
        f.write("\n".join(results) + "\n")

input_file = 'input.txt'
output_file = 'output.txt'

check_tickets(input_file, output_file)
