import time

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def print_coordinate(matrix):
    for row in matrix:
        print(", ".join(map(str, row)))
        
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

def last_index_subarray(sequence, subarray):
    if len(subarray) > len(sequence):
        return -1

    for i in range(len(sequence) - len(subarray) + 1):
        if sequence[i:i+len(subarray)] == subarray:
            return i+len(subarray)

    return -1

def optimal_sequence(sequence, sequences):
    optimal_index = -1
    for sub in sequences:
        last_index = last_index_subarray(sequence, sub)
        if last_index > optimal_index:
            optimal_index = last_index
    return optimal_index

def currentjourney_to_sequence (current_journey, matrix):
    a = []
    for i in range (len(current_journey)):
        a.append(matrix[current_journey[i][0]][current_journey[i][1]])
    return a

def is_subarray(sequence, subarray):
    if len(subarray) > len(sequence):
        return False

    for i in range(len(sequence) - len(subarray) + 1):
        if sequence[i:i+len(subarray)] == subarray:
            return True

    return False

def count_reward(current_journey, sequences, sequences_rewards, matrix):
    reward = 0
    sequence = currentjourney_to_sequence(current_journey, matrix)
    for i in range(len(sequences)):
        if (is_subarray(sequence, sequences[i])):
            reward += sequences_rewards[i]
    return reward

def index_to_coordinate(sequence):
    for i in range (len(sequence)):
        sequence[i][0] += 1
        sequence[i][1] += 1
        sequence[i][0], sequence[i][1] = sequence[i][1], sequence[i][0]
    return sequence