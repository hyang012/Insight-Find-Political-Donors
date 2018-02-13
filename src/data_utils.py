def set_up_percentile_input(file_path):
    return open(file_path, 'r')

# Get the content of the percentile file, if the file is not empty
# and contains numerical value, convert it to integer and return
def get_percentile_input(file):
    percentile = file.readline()
    try:
        file.close()
        return int(percentile)
    except ValueError:
        raise Exception('Percentile file content is not valid')
    
def split_line(raw_line):
    return raw_line.split('|')


