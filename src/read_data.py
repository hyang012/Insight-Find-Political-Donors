
def setup_donation_input(filepath):
    input_record = open(filepath, "r")
    return input_record

def setup_percentile_input(filepath):
    input_percentile = open(filepath, "r")
    return input_percentile

def setup_result_output(filepath):
    output_result = open(filepath, "a")
    return output_result
    
def splitLine(rawLine):
    line = rawLine.split('|')
    return line
