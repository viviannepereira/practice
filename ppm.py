import re

class PPM:
    def __init__(self, input_file, output_file):

        self.list = self.convert_to_list(input_file)
        self.output_file = output_file
        self.magic_number = self.list[0][0][0]
        self.columns = self.list[1][0][1]
        self.rows = self.list[1][0][0]
        self.max_colour_val = self.list[2][0][0]

    def convert_to_list(self, input_file):

        # open, read the file, and split each line into a list

        with open(input_file, 'r') as file:

            lines = file.read().splitlines()

        # split each pixel into a list

        chunk_size = 3

        index = 0

        for line in lines:

            line = line.split()

            new_list = []

            for num in range(0, len(line), chunk_size):

                new_list.append(line[num:num + chunk_size])

            lines[index] = new_list

            index += 1


        return lines
    

def main():
    while True:

        input_file = input("Please name the file you would like to manipulate: ")

        match_object = re.search(r"^[\d\w-_]+\.ppm$", input_file)

        if match_object is not None:
            break
        print("Incorrect file format, please try again.")

    my_ppm = PPM("mini_squares.ppm", "new_squares.ppm")
    

main()

