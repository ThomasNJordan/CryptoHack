def open_file(file_path):
    # Initialize variables
    n = None
    e = None
    ct = None

    # Read the values from the file
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # Split the line into variable name and value
            parts = line.strip().split(' = ')
            if len(parts) == 2:
                variable_name = parts[0].strip()
                value = parts[1].strip()

                if variable_name == 'n':
                    n = int(value)
                elif variable_name == 'e':
                    e = int(value)
                elif variable_name == 'ct':
                    ct = int(value)

    # Check if values were successfully read
    if n is None or e is None or ct is None:
        print("Failed to read values from the file.")
        return KeyError

    return n, e, ct