import math

input_file = open("mixin.txt", "r")
output_file = open("mixout.txt", "w")

input_content = (input_file.read())
numbers = input_content.split()

whole_number = math.floor(int(numbers[0]) / int(numbers[1]))
if int(numbers[0]) % int(numbers[1]) != 0:
    fraction = str(int(numbers[0]) - int((numbers[1])) * whole_number) + "/" + str(numbers[1])
    output_file.write(str(whole_number) + " " + fraction)
else:
    output_file.write(str(whole_number))