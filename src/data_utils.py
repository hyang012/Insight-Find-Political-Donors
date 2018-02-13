""" A module that contains the functions related to reading
    and processing data from the input file.
    
"""

def set_up_percentile_input(file_path):
    return open(file_path, 'r')

def get_percentile_input(file):
    """ Read the first line from the percentile.txt file.
    
    Args:
        file(file object): A file object for the percentile.txt file.
    
    Returns:
        An integer representing the percentile value that is read from
        the file.
    
    Raises:
        Exception: If the first line of the file cannot be converted
            into an integer.
        Exception: If the percentile is not within the range from 1 to 100.
            
    """
    
    percentile = file.readline()
    try:
        file.close()
        percentile = int(percentile)
        if percentile > 100 or percentile < 1:
            raise Exception('Percentile is not within the range from 1 to 100')
        return percentile
    except ValueError:
        raise Exception('Percentile file content is not valid')
    
def split_line(raw_line):
    return raw_line.split('|')


