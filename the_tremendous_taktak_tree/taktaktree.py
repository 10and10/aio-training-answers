input_file = open("taktakin.txt", "r")
output_file = open("taktakout.txt", "w")
input_content = int(input_file.read())
full_moon_counter = 0

if input_content >= 2 and input_content <= 1000000:
    while (input_content - 1) % 11 != 0:
        input_content = input_content * 2
        full_moon_counter = full_moon_counter + 1
    output_content = input_content
    output_file.write(f"{str(full_moon_counter)} {str(output_content)}")
    # output_file.write(str(full_moon_counter) + " " + str(output_content))
else:
    pass

input_file.close()
output_file.close()
