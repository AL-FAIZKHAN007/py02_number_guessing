# Number Guessing Game
A number guessing game built with Python. Try to guess the secret number within limited attempts based on your chosen difficulty level!
## Features
* Multiple difficulty levels:<br>
 -**Easy** → 1–50 range, 10 attempts<br>
 -**Medium** → 1–100 range, 7 attempts<br>
 -**Hard** → 1–200 range, 5 attempts
* Smart hints based on how close your guess is
* Score tracking system
* Input validation and error handling
* Option to replay the game
## Requirements
* Python 3
* Module random
## How to Run
1. Clone the repository:<br>
git clone https://github.com/AL-FAIZKHAN007/py02_number_guessing.git
2. Navigate to the project directory:<br>
cd py02_number_guessing
3. Run the script:<br>
python3.13 guess_number.py
## How to Play
1. Choose a difficulty level (1, 2 or 3)
2. Guess the number within the given attempts
3. Receive hints:<br>
 -Very close! → within 5 numbers<br>
 -Getting warmer. → within 15 numbers<br>
 -Far away. → more than 15 numbers away
4. Score decreases with each wrong attempt
5. Play again to improve your total score!
## Project Structure
* py02_number_guessing/<br>
  -guess_number.py<br>
  -README.md
## License
This project is open-source and free to use.
