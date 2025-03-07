def read_input(input_source):
    if isinstance(input_source, str):
        try:
            with open(input_source, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return input_source
    else:
        raise ValueError("Input must be a string representing text or a file path.")

def count_parantheses(input_string):
    count = 0
    for char in input_string:
        if char == '(':
            count+=1
        elif char == ')':
            count-=1
    return count


# Example usage:
# For a string input
input_string = "example.txt"
parantheses_input = read_input(input_string)
count = count_parantheses(parantheses_input)
print(count)