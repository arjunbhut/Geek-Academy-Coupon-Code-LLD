from sys import argv
from input_handler import input_handler
def main():

    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    input_handler(Lines)

    
if __name__ == "__main__":
    main()