import time
import random

random.seed(time.time())

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def print_coordinate(matrix):
    for row in matrix:
        print(",".join(map(str, row)))
        
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
filename = 'input.txt'
# max_buffer_size, matrix, sequences, matrix_width, matrix_height, sequences_rewards = read_file(filename)

# Input method 2
unique_token_amount = int(input())
unique_token = ['' for i in range(unique_token_amount)]
unique_token_input = input().split()
for i in range (len(unique_token)):
    unique_token[i] = unique_token_input[i]
max_buffer_size = int(input())
matrix_width, matrix_height = map(int, input().split())
sequence_amount = int(input())
maximal_sequence_size = int(input())

def matrix_randomize(matrix_width, matrix_height, unique_token):
    initial_matrix = [['' for _ in range (matrix_width)] for _ in range (matrix_height)]
    for i in range (matrix_height):
        for j in range (matrix_width):
            initial_matrix[i][j] = unique_token[random.randint(0, len(unique_token)-1)]
    return initial_matrix
matrix = matrix_randomize(matrix_width, matrix_height, unique_token)
print_matrix(matrix)

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

sequences = sequence_randomize(sequence_amount, maximal_sequence_size, unique_token)
sequences_rewards = reward_randomize(sequence_amount)
print(sequences)
print(sequences_rewards)

print("Max Buffer Size:", max_buffer_size)
print("Matrix:")
print_matrix(matrix)
print("Sequences:", sequences)
print("Sequence Rewards:", sequences_rewards)

# def currentjourney_to_sequence (current_journey):
#     a = []
#     for i in range (len(current_journey)):
#         a.append(matrix[current_journey[i][0]][current_journey[i][1]])
#     return a

def currentjourney_to_sequence (current_journey):
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

def count_reward(current_journey):
    reward = 0
    sequence = currentjourney_to_sequence(current_journey)
    for i in range(len(sequences)):
        if (is_subarray(sequence, sequences[i])):
            reward += sequences_rewards[i]
    return reward

def index_to_coordinate(sequence):
    for i in range (len(sequence)):
        sequence[i][0] += 1
        sequence[i][1] += 1
    return sequence

# direction (true: vertical, false: horcaizontal)
possible_move = ['']  
maximum_reward = 0
def bruteforce (buffer_size, matrix, direction, currentX, currentY, current_journey: list):
    global possible_move, maximum_reward
    if (buffer_size == 0):
        copy_current_journey = current_journey.copy()
        # print(copy_current_journey)
        current_reward = count_reward(copy_current_journey)
        if (current_reward > maximum_reward):
            maximum_reward = current_reward
            possible_move = copy_current_journey
        return None
    else:
        if (direction):
            for j in range (matrix_width):
                if [currentX, j] not in current_journey:
                    current_journey.append([currentX, j])
                    bruteforce(buffer_size-1, matrix, False, currentX, j, current_journey)
                    current_journey.pop()
                else:
                    pass
        else:
            for i in range (matrix_height):
                if [i, currentY] not in current_journey:
                    current_journey.append([i, currentY])
                    bruteforce(buffer_size-1, matrix, True, i, currentY, current_journey)
                    current_journey.pop()
                else:
                    pass

start_time = time.time()

# for j in range (matrix_width):
bruteforce(max_buffer_size, matrix, True, 0, 0, [])

# index_max = possible_move[0][1]
# for i in range(1, len(possible_move)):
#     if possible_move[i][1] > possible_move[index_max][1]:
#         index_max = i

# max_reward = possible_move[index_max][1]
formatted_sequence = ' '.join(currentjourney_to_sequence(possible_move))
move_coordinates = index_to_coordinate(possible_move)
time_execution = (time.time() - start_time) * 1000

print(maximum_reward)
print(formatted_sequence)
print_coordinate(move_coordinates)
print()
print(time_execution, "ms")  
print()

confirmation = input("Apakah ingin menyimpan solusi? (y/n) ")
if (confirmation == "y"):
    filename = input("Masukkan filename : ")
    with open(filename, "w") as file1:
        file1.write(str(maximum_reward) + "\n")
        file1.write(formatted_sequence + "\n")
        for coordinate in move_coordinates:
            file1.write(",".join(map(str, coordinate)) + "\n")
        file1.write("%s ms" % time_execution)
else:
    print("Terima kasih ! Program selesai")

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
