# AIPI510Pre
Pre-module Assignment for AIPI 510

## How to run the tool
1. (Optional) Create a virtual environment
2. Run `git clone <repo> && cd AIPI510Pre`
3. Run `pip install -r requirements.txt`
4. To run the tool: `python src/main.py`
5. To run the tests: `pytest`

## `python src/main.py -h` output
```
usage: AIPI510 Pre-assignment [-h] [--limit LIMIT] [--orig] [--result] [--sort SORT] [--save SAVE] filename

This command line tool processes csv file in a certain way

positional arguments:
  filename       String path to the csv file to process

options:
  -h, --help     show this help message and exit
  --limit LIMIT  Maximum number of rows to print during processing. Defaults to 5
  --orig         Print the csv data before processing
  --result       Print the csv data after processing
  --sort SORT    Sort the data by the values in the SORT column number speficied
  --save SAVE    String path to the SAVE file where the processed csv data should be stored
```

## Notes
- Developed and tested with Python 3.11.3
- If introducing new dependencies, please make sure to run `pip freeze > requirements.txt`
