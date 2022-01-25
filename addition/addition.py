import time

start_time = time.time()

input_file = open("addin.txt", "r")
output_file = open("addout.txt", "w")

input_content = (input_file.read())
numbers = input_content.split()
total = int(numbers[0]) + int(numbers[1])
output_file.write(str(total))

input_file.close()
output_file.close()

end_time = time.time()

time_taken = end_time - start_time
print("This program takes " + str(round(time_taken * 1000000)) + " nanoseconds to run.")