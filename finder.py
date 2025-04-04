def extract_digits_from_file(filename):
    """Reads the file and returns a string of only digit characters."""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    return ''.join(filter(str.isdigit, content))

def find_sequence_position(digits, sequence):
    """Finds the first occurrence of the digit sequence."""
    return digits.find(sequence)

def get_next_digits(digits, position, length):
    """Gets the next 'length' digits following the found sequence."""
    start = position + length
    return digits[start:start + length]

def analyze_sequence(filename, sequence):
    if not sequence.isdigit():
        raise ValueError("The sequence must contain digits only.")
    if len(sequence) > 10:
        raise ValueError("The sequence must not exceed 10 digits.")

    digits = extract_digits_from_file(filename)
    position = find_sequence_position(digits, sequence)

    if position != -1:
        next_digits = get_next_digits(digits, position, len(sequence))
        print(f"Suite :'{sequence}' ala position {position}")
        print(f"Next {len(sequence)} digits: {next_digits if next_digits else '[none]'}")
    else:
        print(f"Sequence '{sequence}' not found.")

analyze_sequence('new_pi.txt', '35190902')

