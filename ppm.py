import re

class PPM:

    def __init__(self, input_file:str, output_file:str):

        # Intialize attributes

        self.list = self.convert_to_list(input_file)

        self.manipulated_list = None

        self.output_file = output_file

        self.magic_number = self.list[0][0][0]

        self.columns = self.list[1][0][1]

        self.rows = self.list[1][0][0]

        self.max_colour_val = self.list[2][0][0]

    def set_manipulated_list(self, list):

        self.manipulated_list = list


    def convert_to_list(self, input_file:str) -> list:

        '''
        Docstring for convert_to_list
        
        :param self: PPM object
        :param input_file: the file the user is manipulating, a string (the name of the file).
        :type input_file: str

        Converts the file the user wants to manipulate into a 3D list.
        
        Returns a 3D list.

        '''

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

        """
        Docstring for convert_to_file
        
        :param self: PPM object

        Converts self.manipulated_list into a PPM file.

        """

        # Opens a new file (named by the user: self.output_file) to write

        with open(self.output_file, 'w') as file:

            # Writes in magic number, dimensions, and max colour value

            file.write(self.magic_number)

            file.write("\n")

            file.write(f"{self.rows} {self.columns}")

            file.write("\n")

            file.write(self.max_colour_val)

            file.write("\n")

            # Writes each pixel in each line

            for line in self.manipulated_list:

                for pixel in line:

                    file.write(f"{pixel[0]} {pixel[1]} {pixel[2]}")

                    file.write("  ")

                file.write("\n")


    def negate_red(self):

        """
        Docstring for negate_red
        
        :param self: PPM object

        PPM photo manipulation that flips every red value then turns the result into a PPM file.

        """
        
        # Makes a copy of the input list

        temp_list = self.list[3:].copy()
        
        for line in temp_list:

            for pixel in line:

                # Flips each red value in every pixel

                pixel[0] = str(int(self.max_colour_val) - int(pixel[0]))

        # Sets the manipulated list as the copied (and now manipulated) list

        self.set_manipulated_list(temp_list)

        # Converts the list into a file

        self.convert_to_file()
    
    def flip_horizontal(self):

        """
        Docstring for flip_horizontal
        
        :param self: PPM object

        PPM photo manipulation that flips the entire photo, horizontally. Turns the result into a PPM file.
        """
        # Makes a copy of the input list

        temp_list = self.list[3:].copy()

        # Reserves each line in the list

        for line in temp_list:

            line.reverse()

        # Sets the manipulated list as the copied (and now manipulated) list

        self.set_manipulated_list(temp_list)

        # Converts the list into a file

        self.convert_to_file()

    def grey_scale(self):

        """
        Docstring for grey_scale
        
        :param self: PPM object

        PPM photo manipulation that turns the entire photo into a grayscale image. Turns the result into a PPM file.
        """

        # Makes a copy of the input list

        temp_list = self.list[3:].copy()

        # Calculates the average of the colour values of each pixel, setting that as the colour value for red, green, and blue.

        for line in temp_list:

            for pixel in line:
                
                total = int( ( int(pixel[0]) + int(pixel[1]) + int(pixel[2]) ) // 3 )
                
                pixel[0] = total

                pixel[1] = total

                pixel[2] = total

        # Sets the manipulated list as the copied (and now manipulated) list

        self.set_manipulated_list(temp_list)

        # Converts the list into a file

        self.convert_to_file()

    def flatten_red(self):

        """
        Docstring for flatten_red
        
        :param self: PPM object

        PPM photo manipulation that sets every red value to zero. Turns the result into a PPM file.

        """

        # Makes a copy of the input list

        temp_list = self.list[3:].copy()

        # Sets each red value in every pixel to zero.

        for line in temp_list:

            for pixel in line:

                pixel[0] = 0

        # Sets the manipulated list as the copied (and now manipulated) list

        self.set_manipulated_list(temp_list)

        # Converts the list into a file

        self.convert_to_file()
        
def get_ppm_filename(message:str) -> str:

    """
    Docstring for get_ppm_filename
    
    :param message: the message (or request) to send to the user, a string.

    Requests a PPM file.

    Returns the name of PPM file requested.

    """

    file = None

    # Repeatedly asks for a PPM file until he recieves one that fits the regex below.

    while True:

        file = input(message)

        match_object = re.search(r"^\w+\.ppm$", file)

        if match_object is not None:
        
            break

        print("Incorrect file format, please try again.")

    return file

def get_manipulation() -> int:

    """
    Docstring for get_manipulation

    Asks user what manipulation they would like to apply to the PPM file previously named.

    Returns an integer (from 1 through 4) that corresponds to a manipulation option.

    """
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

    # Repeatedly asks for an integer between 1 and 4 until it recieves on that matches the regex (I realize that a regex for this was a little overkill...)

    while True:

        mani_chosen = input("Please respond with a number that corresponds to a listed manipulation: ")

        match_object = re.search(r"^[1-4]$", mani_chosen)

        if match_object is not None:

            break
    
    return int(mani_chosen)



def main():

    # Asks for a PPM file that the user wants to manipulate.

    input_file = get_ppm_filename("Name the file you want to manipulate: ")

    # Asks for what the user would like to name the manipulated file.

    output_file = get_ppm_filename("What would you like to name the manipulated file?: ")

    # Asks the user what manipulation they would like to apply.

    manipulation = get_manipulation()

    # Creates a PPM object.

    PPM_object = PPM(input_file, output_file)

    # Applies manipulation corresponding to what the user asked for.

    if manipulation == 1:

        PPM_object.negate_red()

    elif manipulation == 2:

        PPM_object.flip_horizontal()

    elif manipulation == 3:

        PPM_object.grey_scale()

    elif manipulation == 4:

        PPM_object.flatten_red()

    # Lets the user know that the manipulation process has been completed and the output is currently in the same directory as this python file.

    print(f"The manipulation has been completed.\nA file by the name of {PPM_object.output_file} was added to your directory.")


    
    
main()

