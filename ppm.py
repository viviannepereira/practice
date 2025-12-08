import re

class PPM:
    def __init__(self, input_file, output_file):

        self.list = self.convert_to_list(input_file)

        self.manipulated_list = None

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
    
    def convert_to_file(self):

        with open(self.output_file, 'w') as file:

            file.write(self.magic_number)

            file.write("\n")

            file.write(f"{self.rows} {self.columns}")

            file.write("\n")

            file.write(self.max_colour_val)

            file.write("\n")

            for line in self.manipulated_list:

                for pixel in line:

                    file.write(f"{pixel[0]} {pixel[1]} {pixel[2]}")

                    file.write("  ")

                file.write("\n")


    def negate_red(self):

        temp_list = self.list[3:].copy()
        
        for line in temp_list:

            for pixel in line:

                pixel[0] = str(int(self.max_colour_val) - int(pixel[0]))

        self.manipulated_list = temp_list

        self.convert_to_file()
    
    def flip_horizontal(self):

        temp_list = self.list[3:].copy()

        for line in temp_list:

            line.reverse()

        self.manipulated_list = temp_list

        self.convert_to_file()

    def grey_scale(self):

        temp_list = self.list[3:].copy()

        for line in temp_list:

            for pixel in line:
                
                total = int( ( int(pixel[0]) + int(pixel[1]) + int(pixel[2]) ) // 3 )
                
                pixel[0] = total

                pixel[1] = total

                pixel[2] = total

        self.manipulated_list = temp_list

        self.convert_to_file()

    def flatten_red(self):

        temp_list = self.list[3:].copy()

        for line in temp_list:

            for pixel in line:

                pixel[0] = 0

        self.manipulated_list = temp_list

        self.convert_to_file()
        
def get_ppm_filename(message):

    file = None

    while True:

        file = input(message)

        match_object = re.search(r"^\w+\.ppm$", file)

        if match_object is not None:
        
            break

        print("Incorrect file format, please try again.")

    return file

def get_manipulation():
    print("\n")
    print("Photo Manipulation options:")
    print("\n")
    print("~ Negate Red ~")
    print("Flips red values to create a totally tubular effect!\nRespond 1 if you would like to apply this manipulation.")
    print("\n")
    print("~ Flip Horizontal ~")
    print("Flips your image horizontal, perfect for that totally WACKY mirror selfie you just took. Haha!\nRespond 2 if you would like to apply this manipulation.")
    print("\n")
    print("~ GreyScale ~")
    print("Feeling down? Reflect that through your photos with this filter!\nRespond 3 if you would like to apply this manipulation.")
    print("\n")
    print(" ~ Flatten Red ~")
    print("Do you just hate the colour red and wished it didn't exist and the being who created humans just destroyed our rectinas so we wouldn't be able to see it?\nWell avoid permanent eye damage with this funky filter!\nRespond 4 if you would like to apply this manipulation.")
    print("\n")

    mani_chosen = None

    while True:

        mani_chosen = input("Please respond with a number that corresponds to a listed manipulation: ")

        match_object = re.search(r"^[1-4]$", mani_chosen)

        if match_object is not None:

            break
    
    return int(mani_chosen)



def main():

    input_file = get_ppm_filename("Name the file you want to manipulate: ")

    output_file = get_ppm_filename("What would you like to name the manipulated file?: ")

    manipulation = get_manipulation()

    PPM_object = PPM(input_file, output_file)

    if manipulation == 1:

        PPM_object.negate_red()

    elif manipulation == 2:

        PPM_object.flip_horizontal()

    elif manipulation == 3:

        PPM_object.grey_scale()

    elif manipulation == 4:

        PPM_object.flatten_red()

    print(f"The manipulation has been completed.\nA file by the name of {PPM_object.output_file} was added to your directory.")


    
    
main()

