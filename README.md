# Dictionary Project

## Overview
This project aims to automate searching for word definitions in a dictionary using Python. The program loads a dictionary dataset from a JSON file, allowing users to input words and retrieve their definitions. It also includes features like case-insensitive searching, handling misspellings, and suggesting close matches for words not found in the dictionary.

## Features
- Load JSON data into a Python dictionary.
- Case-insensitive word searching.
- Handling of misspelled words with suggestions for close matches.
- Simple command-line interface for user interaction.

## Requirements
- Python 3.x
- `difflib` library (usually comes pre-installed with Python)

## Installation
1. Clone the repository or download the project files.
2. Ensure you have Python installed on your system.
3. Run the `dictionary.py` file to start the program.

## Usage
1. Run the `dictionary.py` file.
2. Enter a word when prompted to get its definition.
3. Follow the instructions to handle misspelled words and receive suggestions.
4. Enter 'Q' to quit the program.

## Test Sample
```
$ python dictionary.py
Enter a word to get its definition (Q to quit): Rainn
Did you mean 'rain' instead of 'Rainn'? Enter Y for yes, or N for no: Y
Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.

Enter a word to get its definition (Q to quit): Python
A high-level programming language.

Enter a word to get its definition (Q to quit): Q
```

## Data Source
The dictionary dataset used in this project can be downloaded from [[here](https://github.com/mutemip/dictionary-data)](link_to_data_source).

## Credits
This project was created by Peter Baah Kpabitey.

## License
This project is licensed under the [MIT License](LICENSE).

