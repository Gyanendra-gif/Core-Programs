"""
@Author: Gyanendra
@Date: 14/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 14/01/2021 
@Title : Strings in Python
"""
import logging
import sys
import textwrap

def function_formatted_text(str):
    """
    Description:
        Function is Used to get the display formatted text (width=50) as output.
    Parameter:
        Sample String 
    Return:
        Updated String
    """
    my_string = (textwrap.fill(str, width=50))
    return my_string
             

if __name__ == "__main__":

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', 
                              '%m-%d-%Y %H:%M:%S')

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(formatter)

    file_handler = logging.FileHandler('E:\Python Workspace\Core-Programs\data_structure\Strings\string_file.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stdout_handler)

    sample_str = """Folks who come by here are mostly regulars. At a time like this with illness taking so many people away each day,
                    it is a great pleasure to see the regulars come by and say hello. It iss nice to know you are okay,
                    you are still kicking, you are still writing. Keep writing.
                    Please use the open space below to share your first 50 words on the topic “happy to see you.”"""
    result = function_formatted_text(sample_str)
    logger.info("Here is the sorted string of {} after replaced specific char is {} ".format(sample_str, result))
 
  