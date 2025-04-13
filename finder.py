def extract_digits_from_file(filename:str)->str:
    with open(filename, 'r', encoding='utf-8') as f:content = f.read()
    return content

def find_sequence_position(digits:str, sequence:str)->int:
    return digits.find(sequence)

def get_next_digits(digits, position, length):
    start:int = position + length
    return digits[start:start + length]

def analyze_sequence(filename, sequence)->str:
    position:int=-1
    next_digits:str=''
    if not sequence.isdigit() or len(sequence) > 10:return(position,next_digits)
    digits = extract_digits_from_file(filename)
    position = find_sequence_position(digits, sequence)
    if position != -1:next_digits = get_next_digits(digits, position, len(sequence))
    return (position,next_digits)

def test()->None:
    pass

#analyze_sequence('pi.txt', '79458151')

if __name__=="__main__":
    pass

