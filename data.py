with open('file_with_everything.txt', "r") as file:
    lines = file.readlines()[1:]

output_lines = ["processor name,\tcores,\tfrequency,\tgeneration\t\n"]  # Add the header line with commas

for line in lines:
    elements = line.split()
    processor_name = elements[0]
    num_cores = elements[3]
    frequency = elements[7] if elements[7] != "N/A" else elements[10]
    generation = elements[2]  # Extract the generation value from the elements list
    output_lines.append("{},\t{},\t{},\t{}\n".format(processor_name, num_cores, frequency, generation))  # Use commas and tabs for formatting

with open('output_file.txt', "w") as file:
    file.writelines(output_lines)
