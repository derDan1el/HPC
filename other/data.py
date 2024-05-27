with open('file_with_everything.txt', "r") as file:
    lines = file.readlines()[1:]

output_lines = ["processor name,\tcores,\tfrequency,\tgeneration\t\n"]  # Add the header line with commas

for line in lines:
    elements = line.split()
    processor_name = elements[0]
    num_cores = elements[3]
    frequency1 = elements[8] # Performancecore Base Frequency (GHz)
    frequency2 = elements[9] # Efficientcore Base Frequency (GHz)
    generation = elements[2]  # Extract the generation value from the elements list

    if (frequency1 == "N/A") and (frequency2 == "N/A"):
        frequency = elements[10] # Processor Base Frequency (GHz)
    elif frequency1 == "N/A":
        frequency = frequency2
    elif frequency2 == "N/A":
        frequency = frequency1
    else:
        frequency = f"({frequency1}:{frequency2})"

    output_lines.append("{},\t{},\t{},\t{}\n".format(processor_name, num_cores, frequency,
                                                     generation))  # Use commas and tabs for formatting

with open('output_file.txt', "w") as file:
    file.writelines(output_lines)