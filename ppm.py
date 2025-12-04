class PPM:
    def __init__(self, input_file, output_file):

        self.list = self.convert_to_list(input_file)

    def convert_to_list(self, input_file):

        # open, read the file, and split each line into a list

        with open(input_file, 'r') as file:

            lines = file.read().splitlines()

        # split each pixel into a list

        for line in lines:

            #number_of_groups = len(line)//3
            for num in range(0,len(line)):
                line[:num].split()
                num += 3
            



        return lines
    

def main():
    my_ppm = PPM("cake.ppm", "new_cake.ppm")
    print(my_ppm.list)

main()

