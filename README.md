<h1 align="center">Tugas Kecil 1 IF2211 Strategi Algoritma</h1>
<h2 align="center">Semester II tahun 2023/2024</h2>
<h3 align="center">Penyelesaian Cyberpunk 2077 Breach Protocol dengan Algoritma Brute Force</p>

## Table of Contents

- [Short Description](#short-description)
- [Creator](#creator)
- [Built With](#built-with)
- [Installation](#installation)
- [Guides](#guides)
- [Website Overview](#website-overview)
- [Links](#links)


## Short Description
This program is designed to solve the Cyberpunk 2077 Breach Protocol mini-game using a brute-force algorithm. The majority of the program is written in Python, with a web-based GUI implemented using ReactJS for the frontend framework and Flask for the backend framework.

Cyberpunk 2077 Breach Protocol is a hacking mini-game within the Cyberpunk 2077 video game. It simulates local network hacking of ICE (Intrusion Countermeasures Electronics) in Cyberpunk 2077. The components of this mini-game include:
- Tokens - consisting of two alphanumeric characters such as E9, BD, and 55.
- Matrix - composed of tokens that will be selected to form a sequence of codes.
- Sequences - a series of tokens (two or more) that must be matched.
- Buffer - the maximum number of tokens that can be arranged sequentially.
  
Rules of the Breach Protocol mini-game include:
- Players move in a pattern of horizontal, vertical, horizontal, vertical (alternating) until all sequences are successfully matched or the buffer is full.
- Players start by selecting one token at the top row position of the matrix.
- Sequences are matched against the tokens in the buffer.
- One token in the buffer can be used in more than one sequence.
- Each sequence has varying reward weights.
- Sequences must have a minimum length of two tokens.
  
For more detailed information on Cyberpunk 2077 Breach Protocol, refer to this [link](https://cyberpunk.fandom.com/wiki/Quickhacking).

## Creator
| NIM      | Nama                    | Kelas                                                                                                                                                                                                               |
|----------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 13522045 | Elbert Chailes    | K-01                                                            |

## Built With

- [React](https://react.dev/)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Tailwind](https://tailwindcss.com/)

## Installation
## WEB-BASED GUI
If you want to run this program you will need to do these steps

1. Clone this repository :
```shell
git clone git@github.com:ChaiGans/Tucil1_13522045.git
```

2. Navigate to the `src` directory:
```shell
cd .\Tucil1_13522045\
cd src
```

3. Open another terminal in the same folder directory. Now, you should have two terminals open, both in the `Tucil1_13522045/src` directory.

### First Terminal (To run frontend server)
4. Change directory to the frontend folder and execute the following commands:
```shell
cd frontend
npm install
npm run dev
```
5. Open a web browser and navigate to [http://localhost:5173/](http://localhost:5173/). Note: The port number may vary if the default port is in use. Check the terminal to determine which port the server is running on.
   
### Second terminal (To run backend server)
6. Change directory to the backend folder:
```shell
cd backend
```

Now, we need to set venv in order to run the program

*For windows user*
```shell
py -3 -m venv .venv
.venv\Scripts\activate
```

*For linux/macOS user*
```shell
python3 -m venv .venv
. .venv/bin/activate
```

**If flask is never installed on your device, please do below step prior running the program, because the backend server cant be run without flask.**
```shell
pip install Flask
```

7. Start the Flask server by typing the following command:
```shell
flask run --debug
```
8. The backend server should now be running at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## CLI
1. Clone this repository :
```shell
git clone git@github.com:ChaiGans/Tucil1_13522045.git
```

2. Navigate to the `src` directory:
```shell
cd .\Tucil1_13522045\
cd src
```

3. Open terminal in current directory and just type `python main.py`

## Guides
### Input file method
1. Select a file with the .txt extension and ensure that the input format is correct. Any deviation from the specified format may result in errors on the website.
2. Once the file is selected, simply click the `Solve` button, and the solution will be displayed on the screen.
3. Users have the option to either save the solution or close the popup solution window. They can then select another file or switch to another input method.

### Random Input Method
1. Choose the buffer size from the available options.
2. Enter unique tokens to define the variables that will appear in the matrix and sequences.
3. Input the desired matrix width and height to be randomized, then click the `Randomize` button to generate the matrix. The generated matrix will be displayed on the screen, indicating a successful generation.
4. Specify the number of sequences to be generated and the maximum length for each sequence. After clicking the `Randomize` button, the sequences and their corresponding rewards will appear on the screen, indicating successful generation.
5. Ensure that all required information has been entered correctly, and verify that the matrix and sequences are displayed on the screen.
6. Click the `Solve` button to find the output solution, which will be displayed in a popup window.

### How to save solution
1. After the solution appears in the popup window, click the `Save Solution` button. This will prompt an input field asking for a .txt filename.
2. Enter the desired filename, ensuring that it ends with the .txt extension, as the program can only write to .txt files.
3. Check the local directory for the outputted file, which can be found in src/backend/output/[filename].

### FOR CLI USERS
Just note that there is no specific guides on how to use the terminal program, just run the main.py program and make sure to follow the guides and instructions on what is being asked by the terminal. For the random input method, just make sure that you have the format with you, so you could run the program perfectly.

## Website Overview
![masukan_uji_7](https://github.com/ChaiGans/Tucil1_13522045/assets/113753352/1192fd55-1939-4d56-acb1-4b78b656d79f)
![masukan_uji_1](https://github.com/ChaiGans/Tucil1_13522045/assets/113753352/f1e2b601-f944-4c17-bda6-afaecb5db138)
![konfirmasi_savesolution](https://github.com/ChaiGans/Tucil1_13522045/assets/113753352/fef406c4-7e39-40ce-94cc-79107504150e)

## Links
- Repository : https://github.com/ChaiGans/Tucil1_13522045/
- Issue tracker :
   - If you encounter any issues with the program, come across any disruptive bugs, or have any suggestions for improvement, please don't hesitate to reach out by sending an email to elbertchailes888@gmail.com. Your feedback is greatly appreciated.
