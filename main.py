import app.io.input as my_input


def main():
    print(my_input.read_console(), my_input.read_file_pandas("data/test.csv"), my_input.read_file_python("data/test.csv"))


if __name__ == '__main__':
    main()

