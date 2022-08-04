input_file = open("countin.txt", "r")
output_file = open("countout.txt", "w")
input_number = int(input_file.read())
print_number = 1

while print_number <= input_number:
    output_file.write(str(print_number) + "\n")
    print_number += 1

input_file.close()
output_file.close()