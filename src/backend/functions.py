import time
import random

random.seed(time.time())

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

def matrix_randomize(matrix_width, matrix_height, unique_token):
    initial_matrix = [['' for _ in range (matrix_width)] for _ in range (matrix_height)]
    for i in range (matrix_height):
        for j in range (matrix_width):
            initial_matrix[i][j] = unique_token[random.randint(0, len(unique_token)-1)]
    return initial_matrix


def sequence_randomize(sequence_amount, maximal_sequence_size, unique_token):
    result_sequences = []
    for i in range (sequence_amount):
        sequence_size = random.randint(2, maximal_sequence_size)
        initial_sequence = ['' for _ in range (sequence_size)]
        for j in range (sequence_size):
            initial_sequence[j] = unique_token[random.randint(0, len(unique_token)-1)]
        result_sequences.append(initial_sequence)
    return result_sequences

def reward_randomize(sequence_amount):
    result_rewards = []
    for _ in range (sequence_amount):
        result_rewards.append(random.randint(10, 50))
    return result_rewards

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

# def currentjourney_to_sequence (current_journey):
#     a = []
#     for i in range (len(current_journey)):
#         a.append(matrix[current_journey[i][0]][current_journey[i][1]])
#     return a

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


# index_max = possible_move[0][1]
# for i in range(1, len(possible_move)):
#     if possible_move[i][1] > possible_move[index_max][1]:
#         index_max = i

# max_reward = possible_move[index_max][1]

# def count_reward (sequence):
#     reward = 0
#     system = True
#     for i in range (len(sequences)):
#         for j in range (len(sequence) - len(sequences[i]) + 1):
#             for k in range (len(sequences[i])):
#                 if (sequences[i][k] != sequence[j+k]):
#                     system = False
#             if (system):
#                 reward += sequences_rewards
#     return reward
