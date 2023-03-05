"""Tests for translator and base class."""
import config
from config import f, dc
from translator import Lobot
from main import BaseClass


def lobot_test():
    """This function conducts tests for the Lobot class in the translator module.

    Typical Usage:
        lobot_test()
    """
    tv = config.TestVariables()
    count = 0
    for i in tv.surname_variables:
        # Define a variable for this iteration.
        this_iteration = count
        # Define a known test variable.
        foreign_text = i
        # Initialize the class with a test variable.
        test = Lobot(foreign_text)
        # Test all functions of the class and save the return variables.
        string_to_ints = test.convert_string_to_int_list(foreign_text)
        ints_to_string = test.convert_int_list_to_characters(string_to_ints)
        translated_text = test.translate_text(foreign_text)
        icd_string = test.individual_character_decoder(integer_list=string_to_ints)
        # TODO Fix terminal output colors in the configuration_boilerplate file.
        # Print the results of the test for review.
        print(f"This is {f(tv.project_id, *dc.bold_aqua_note)} test number {f(count, *dc.bold_aqua_note)}, "
              f"target language is {f(tv.target_language, *dc.bold_aqua_note)}.")
        print(f"Initializing Lobot with test variable: {f(foreign_text, *dc.bold_purple_note)}")
        print(f"Converting {f(foreign_text, *dc.bold_purple_note)} to a list of integers, then back into a string: "
              f"\n\tInteger List: \t{string_to_ints}"
              f"\n\tString Result:\t{f(ints_to_string, *dc.bold_green_pass)}")
        print(f"Translating {f(foreign_text, *dc.bold_purple_note)} "
              f"to {f(tv.target_language, *dc.bold_aqua_note)} translated_text:"
              f"\n\tTranslated Text: {f(translated_text, *dc.bold_aqua_note)}")
        print(f"Testing the Individual Character Decoding function using integer list:"
              f"\n\tICD String: {[i for i in icd_string]}")
        print(f"Test {f(this_iteration, *dc.bold_aqua_note)} complete.")
        print(f"\n\n{f(*dc.divider, *dc.highlight_black_text_grey)}\n")
        # Increment the test counter.
        count = count + 1


def base_class_test():
    bc = BaseClass()
    print(f"ws: \n\t\t{bc.ws}")
    print(f"rf: \n\t\t{bc.rf}")
    print(f"rl: \n\t\t{bc.rl}")
    print(f"c: \n\t\t{bc.c}")
    print(f"first_name: \n\t\t{bc.first_name}")
    print(f"last_name: \n\t\t{bc.last_name}")
    print(f"city: \n\t\t{bc.city}")
    print(f"w: \n\t\t{bc.w}")
    print(f"weather_data: \n\t\t{bc.weather_data}")
    print(f"local_temperature_c: \n\t\t{bc.local_temperature_c}")
    print(f"local_temperature_f: \n\t\t{bc.local_temperature_f}")
    print(f"local_sky: \n\t\t{bc.local_sky}")
    print(f"local_sunrise: \n\t\t{bc.local_sunrise}")
    print(f"local_sunset: \n\t\t{bc.local_sunset}")
    print(f"random_identity: \n\t\t{bc.random_identity()}")
    print(f"specific_identity: \n\t\t{bc.specific_identity(bc.rf, bc.rl, bc.c)}")
    print(f"webscrape_single_surname: \n\t\t{bc.webscrape_single_surname()}")


def surname_webscrape_test():
    """This takes a while so only use it if you need all 1707 names."""
    bc = BaseClass()
    surname_list = bc.update_surname_list()
    print(f"update_surname_list: \n\t\t{surname_list}")


if __name__ == '__main__':
    print("Running tests...")
    lobot_test()
