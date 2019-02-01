

global output_verbose
global output_information

output_verbose = True
output_information = True


def print_verbose(*lines):
    """prints the given set of lines, if the output_verbose flag is set to True"""
    if output_verbose:
        for line in lines:
            print(line)

def print_info(*lines):
    """prints the given set of lines, if the output_information flag is set to True"""
    if output_information:
        for line in lines:
            print(line)

def print_error(*lines):
    """prints the given set of lines, if the output_verbose flag is set to True"""
    for line in lines:
        print(line)
