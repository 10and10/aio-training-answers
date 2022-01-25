input_file = open("sitin.txt", "r")
output_file = open("sitout.txt", "w")
file_content = input_file.read()
all_values = file_content.split()

sitting =  int(all_values[0]) * int(all_values[1])
standing = int(all_values[2]) - sitting
output_file.write(str(sitting) + " " + str(standing))

input_file.close()
output_file.close()