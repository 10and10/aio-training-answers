input_file = open("bendin.txt", "r")
output_file = open("bendout.txt", "w")

def calculate_area(num1, num2, num3, num4):
    return(num1 - num2) * (num3 - num4)

input_content = input_file.read().split()
numbers = []
for number in input_content:
    num_version = int(number)
    numbers.append(num_version)

if numbers[4] >= numbers[0] and numbers[5] >= numbers[1] and numbers[6] <= numbers[2] and numbers[7] <= numbers[3]:
    area_taken = calculate_area(numbers[2], numbers[0], numbers[3], numbers[1]) # if shape is completely inside other shape
elif numbers[2] > numbers[4] or numbers[0] < numbers[6] and numbers[3] > numbers[5] or numbers[1] < numbers[7]:
    rectangle_1 = calculate_area(numbers[2], numbers[0], numbers[3], numbers[1]) # if shape in overlapping 2 axis
    rectangle_2 = calculate_area(numbers[6], numbers[4], numbers[7], numbers[5])
    overlap = calculate_area(numbers[2], numbers[4], numbers[3], numbers[5])
    area_taken = (rectangle_1 + rectangle_2) - overlap
elif numbers[4] < numbers[2] or numbers[6] > numbers[0] and numbers[5] < numbers[3] or numbers[7] > numbers[1]:
    rectangle_1 = calculate_area(numbers[2], numbers[0], numbers[3], numbers[1])
    rectangle_2 = calculate_area(numbers[6], numbers[4], numbers[7], numbers[5])
    overlap = calculate_area(numbers[2], numbers[4], numbers[3], numbers[5])
    area_taken = (rectangle_1 + rectangle_2) - overlap 
else:
    pass   


output_file.write(str(area_taken))
input_file.close()
output_file.close()