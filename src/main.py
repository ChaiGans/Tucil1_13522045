def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
        
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        max_buffer_size = int(file.readline().strip())

        matrix_width, matrix_height = map(int, file.readline().strip().split())

        matrix = []
        for _ in range(matrix_height):
            row = list(map(str, file.readline().strip().split()))
            matrix.append(row)

        number_of_sequences = int(file.readline().strip())

        sequences = []
        sequences_rewards = []
        for _ in range(number_of_sequences):
            sequence = file.readline().strip().split()
            sequences.append(sequence)
            reward = int(file.readline().strip()) 
            sequences_rewards.append(reward)

    return max_buffer_size, matrix, sequences, matrix_width, matrix_height, sequences_rewards

# Input method 1
filename = 'test/input.txt'
max_buffer_size, matrix, sequences, matrix_width, matrix_height, sequences_rewards = read_file(filename)

print("Buffer Size:", max_buffer_size)
print_matrix(matrix)
print("Sequences:", sequences)
print("Rewards:", sequences_rewards)
