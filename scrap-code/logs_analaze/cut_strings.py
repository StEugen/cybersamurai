

def extract_data(input_file, output_file, start_string, end_string):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    start_index = next((i for i, line in enumerate(lines) if start_string in line), None)
    end_index = next((i for i, line in enumerate(lines) if end_string in line), None)

    if start_index is None or end_index is None or start_index >= end_index:
        print("Invalid start or end strings. Please check the input file.")
        return

    extracted_data = lines[start_index:end_index + 1]

    with open(output_file, 'w') as f:
        f.writelines(extracted_data)

if __name__ == "__main__":
    input_file = input("Enter the input file name: ")
    output_file = input("Enter the output file name: ")
    start_string = input("Enter the start string: ")
    end_string = input("Enter the end string: ")

    extract_data(input_file, output_file, start_string, end_string)

    print("Data extraction completed. Check the output file:", output_file)
