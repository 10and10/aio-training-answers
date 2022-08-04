input_file = open("dishin.txt", "r")
output_file = open("dishout.txt", "w")
input_numbers = input_file.read()

all_numbers = input_numbers.split("\n")
amount_of_numbers_in_set = int(all_numbers[0])

if amount_of_numbers_in_set >= 1 and amount_of_numbers_in_set <= 1000:
    all_numbers.pop(0)
    int_all_numbers = []
    total = 0

    for num in all_numbers:
        num = int(num)
        int_all_numbers.append(num)

    for i in int_all_numbers:
        total += i
    average = total // amount_of_numbers_in_set

    minimum = min(int_all_numbers)
    maximum = max(int_all_numbers)

    output_file.write(str(minimum))
    output_file.write(" " + str(maximum))
    output_file.write(" " + str(average))
else:
    print("The valid number should be between 1 and 1000 inclusive.")

input_file.close()
output_file.close()