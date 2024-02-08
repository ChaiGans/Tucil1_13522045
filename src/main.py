from functions import *
import os

def CLEAR_TERMINAL():
    os.system('cls' if os.name == 'nt' else 'clear')

def METHOD_CHOICE_MESSAGE():
    print("|| 1. From file .txt                ||")
    print("|| 2. Random                        ||")
    print("|| 3. Exit Program                  ||")
    print("======================================")

def GREETING_MESSAGE():
    print("======================================")
    print("||  Cyberpunk 2077 Breach Protocol  ||")
    print("||       Dev: Elbert Chailes        ||")
    print("======================================")

def ERROR_MESSAGE(start_choice, end_choice):
    print("Your input is out of bound of the choices")
    print("Please input from range " + str(start_choice), "to", str(end_choice))

def FORMATTED_OUTPUT(maximum_reward, formatted_sequence, move_coordinates, time_execution):
    print(maximum_reward)
    print(formatted_sequence)
    print_coordinate(move_coordinates)
    print()
    print(time_execution, "ms")  
    print()

def REUSE_PROGRAM_CONFIRMATION():
    confirmation = input("Do you want to reuse the program? (y/n) ")
    choice_correct = False
    while (not choice_correct):
        if (confirmation == "y"):
            choice_correct = True
            return True
        elif (confirmation == "n"):
            return False
        else:
            print("We do not understand your command, please enter (y/n) only.")
            confirmation = input("Do you want to reuse the program ? (y/n) ")

def OUTPUT_TO_FILE_CONFIRMATION(formatted_sequence, move_coordinates, time_execution):
    confirmation = input("Do you want to save your solution? (y/n) ")
    choice_correct = False
    while (not choice_correct):
        if (confirmation == "y"):
            choice_correct = True
            filename = input("Enter filename : ")
            with open(filename, "w") as file1:
                file1.write(str(maximum_reward) + "\n")
                file1.write(formatted_sequence + "\n")
                for coordinate in move_coordinates:
                    file1.write(",".join(map(str, coordinate)) + "\n")
                file1.write("%s ms" % time_execution)
        elif (confirmation == "n"):
            choice_correct = True
        else:
            print("We do not understand your command, please enter (y/n) only.")
            confirmation = input("Do you want to save your solution? (y/n) ")


def PRINT_INFORMATION(matrix, sequences, sequences_rewards, max_buffer_size):
    print("Max Buffer Size:", max_buffer_size)
    print("Matrix:")
    print_matrix(matrix)
    print("Sequences:", sequences)
    print("Sequence Rewards:", sequences_rewards)  

# direction (true: vertical, false: horcaizontal)
def bruteforce (buffer_size, matrix, direction, currentX, currentY, current_journey: list, sequences, sequences_rewards, matrix_width, matrix_height):
    global possible_move, maximum_reward
    if (buffer_size == 0):
        copy_current_journey = current_journey.copy()
        # print(copy_current_journey)
        current_reward = count_reward(copy_current_journey, sequences, sequences_rewards, matrix)
        if (current_reward > maximum_reward):
            maximum_reward = current_reward
            possible_move = copy_current_journey
        return None
    else:
        if (direction):
            for j in range (matrix_width):
                if [currentX, j] not in current_journey:
                    current_journey.append([currentX, j])
                    bruteforce(buffer_size-1, matrix, False, currentX, j, current_journey, sequences, sequences_rewards, matrix_width, matrix_height)
                    current_journey.pop()
                else:
                    pass
        else:
            for i in range (matrix_height):
                if [i, currentY] not in current_journey:
                    current_journey.append([i, currentY])
                    bruteforce(buffer_size-1, matrix, True, i, currentY, current_journey, sequences, sequences_rewards, matrix_width, matrix_height)
                    current_journey.pop()
                else:
                    pass

GREETING_MESSAGE()
while True:
    METHOD_CHOICE_MESSAGE()
    method_choice = int(input("Enter your choice : "))
    if (method_choice == 1):
        filename = input("Input the filename : ")
        try:
            read_file(filename)
        except Exception as error:
            print("Your input is not valid or could not be read by the program")
    elif (method_choice == 2):
        # Input method 2

        # Initialization for global variable that is used in bruteforce function
        possible_move = ['']  
        maximum_reward = 0

        # Asking input from user
        # unique_token that is available initialization
        unique_token_amount = int(input())
        unique_token = ['' for i in range(unique_token_amount)]
        unique_token_input = input().split()
        for i in range (len(unique_token)):
            unique_token[i] = unique_token_input[i]

        # buffer_size initialization
        max_buffer_size = int(input())

        # matrix initialization
        matrix_width, matrix_height = map(int, input().split())
        matrix = matrix_randomize(matrix_width, matrix_height, unique_token)

        # sequence initialization
        sequence_amount = int(input())
        maximal_sequence_size = int(input())
        sequences = sequence_randomize(sequence_amount, maximal_sequence_size, unique_token)

        # sequence_rewards initialization
        sequences_rewards = reward_randomize(sequence_amount)

        # information of randomization result of input two method
        PRINT_INFORMATION(matrix, sequences, sequences_rewards, max_buffer_size)

        # begin bruteforce
        start_time = time.time()
        bruteforce(max_buffer_size, matrix, True, 0, 0, [], sequences, sequences_rewards, matrix_width, matrix_height)
        # bruteforce ended

        # format needed information
        formatted_sequence = ' '.join(currentjourney_to_sequence(possible_move, matrix))
        move_coordinates = index_to_coordinate(possible_move)
        time_execution = (time.time() - start_time) * 1000

        # output as formatted
        FORMATTED_OUTPUT(maximum_reward, formatted_sequence, move_coordinates, time_execution)

        # asking user to output to file
        OUTPUT_TO_FILE_CONFIRMATION(formatted_sequence, move_coordinates, time_execution)

        # asking user if they want to reuse the program
        if not REUSE_PROGRAM_CONFIRMATION() :
            exit()
        else:
            CLEAR_TERMINAL()
            GREETING_MESSAGE()

    elif (method_choice == 3):
        exit()

    else:
        ERROR_MESSAGE(1,3)

