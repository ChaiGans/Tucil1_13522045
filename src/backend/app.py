from flask import Flask, request, jsonify
from functions import *
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# define global variable
maximum_reward = 0
formatted_sequence = []
move_coordinates = []
time_execution = 0

# direction (true: vertical, false: horcaizontal)
def bruteforce(buffer_size, matrix, direction, currentX, currentY, current_journey: list, sequences, sequences_rewards, matrix_width, matrix_height):
    global possible_move, maximum_reward, last_index_optimal
    if (buffer_size == 0):
        copy_current_journey = current_journey.copy()
        current_reward = count_reward(copy_current_journey, sequences, sequences_rewards, matrix)
        if (current_reward != 0):
            current_last_index = optimal_sequence(currentjourney_to_sequence(copy_current_journey,matrix), sequences)
            if current_reward > maximum_reward or (current_reward == maximum_reward and current_last_index < last_index_optimal):
                last_index_optimal = current_last_index
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

def PRINT_INFORMATION(matrix, sequences, sequences_rewards, max_buffer_size):
    print("Max Buffer Size:", max_buffer_size)
    print("Matrix:")
    print_matrix(matrix)
    print("Sequences:", sequences)
    print("Sequence Rewards:", sequences_rewards)  

def FORMATTED_OUTPUT(maximum_reward, formatted_sequence, move_coordinates, time_execution):
    print(maximum_reward)
    print(formatted_sequence)
    print_coordinate(move_coordinates)
    print()
    print(time_execution, "ms")  
    print()

@app.route("/", methods=['GET', 'POST'])
def get_data():
    global maximum_reward, possible_move, last_index_optimal, time_execution, formatted_sequence, move_coordinates

    if request.method == 'POST':
        data = request.json

        # Asking input from user
        # unique_token that is available initialization
        unique_token_input = data['possibleToken'].split(' ')
        unique_token = ['' for i in range(len(unique_token_input))]
        for i in range (len(unique_token)):
            unique_token[i] = unique_token_input[i]

        # buffer_size initialization
        max_buffer_size = int(data['bufferSize'])
        last_index_optimal = max_buffer_size

        # information of randomization result of input two method
        PRINT_INFORMATION(data['matrix'], data['sequence'], data['reward'], max_buffer_size)

        maximum_reward = 0
        formatted_sequence = []
        move_coordinates = []
        time_execution = 0

        # begin bruteforce
        start_time = time.time()
        bruteforce(max_buffer_size, data['matrix'], True, 0, 0, [], data['sequence'], data['reward'], int(data['matrixWidth']), int(data['matrixHeight']))
        # bruteforce ended

        # format needed information
        time_execution = (time.time() - start_time) * 1000
        if (maximum_reward != 0):
            formatted_sequence = ' '.join(currentjourney_to_sequence(possible_move, data['matrix'])[0:last_index_optimal])
            move_coordinates = index_to_coordinate(possible_move[0:last_index_optimal])

            # output as formatted
            FORMATTED_OUTPUT(maximum_reward, formatted_sequence, move_coordinates, time_execution)

        else:
            print(maximum_reward)
            print()
            print(time_execution, "ms")  
            print()

        return jsonify({'message': 'POST request received'})
    else:
        return jsonify({'message': 'GET request received'})

@app.route("/results", methods=['GET'])
def send_data():
    global maximum_reward, formatted_sequence, move_coordinates, time_execution
    return jsonify(maximum_reward, formatted_sequence, move_coordinates, time_execution)

@app.route("/save/", methods=['POST'])
def save_file():
    if request.method == 'POST':
        folder_path = "output/"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        filename = os.path.join(folder_path, request.json['filename'])
        with open(filename, "w") as file1:
            file1.write(str(maximum_reward) + "\n")
            if maximum_reward != 0:
                file1.write(formatted_sequence + "\n")
                for coordinate in move_coordinates:
                    file1.write(", ".join(map(str, coordinate)) + "\n")
            file1.write("\n%s ms" % time_execution)

@app.route('/upload/', methods=['POST'])
def upload_file():
    global maximum_reward, possible_move, last_index_optimal, time_execution, formatted_sequence, move_coordinates

    if (request.method == 'POST'):

        file = request.files['file']
        file.save('input.txt')

        max_buffer_size, matrix, sequences, matrix_width, matrix_height, sequences_rewards = read_file('input.txt')

        PRINT_INFORMATION(matrix, sequences, sequences_rewards, max_buffer_size)

        maximum_reward = 0
        formatted_sequence = []
        move_coordinates = []
        time_execution = 0

        # begin bruteforce
        start_time = time.time()
        bruteforce(max_buffer_size, matrix, True, 0, 0, [], sequences, sequences_rewards, matrix_width, matrix_height)
        # bruteforce ended

        # format needed information
        time_execution = (time.time() - start_time) * 1000
        if (maximum_reward != 0):
            formatted_sequence = ' '.join(currentjourney_to_sequence(possible_move, matrix)[0:last_index_optimal])
            move_coordinates = index_to_coordinate(possible_move[0:last_index_optimal])

            # output as formatted
            FORMATTED_OUTPUT(maximum_reward, formatted_sequence, move_coordinates, time_execution)

        else:
            print(maximum_reward)
            print()
            print(time_execution, "ms")  
            print()


        return jsonify({'message': 'POST request received'})

if __name__ == "__main__":
    app.run(debug=True)
