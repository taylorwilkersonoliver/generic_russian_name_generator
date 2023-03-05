"""Configuration specific to this project.

Typeical Usage:
    tv = TestVariables
    print(tv.project_id)
    print(tv.target_language)
    print(tv.test1)
    print(tv.test2)
    print(tv.test3)
    print(tv.test4)
    print(tv.test5)
    print(tv.surname_variables)
    print(tv.all_variables)
"""
import os
from config_boilerplate import ppp, debug, dc

##################################################################
# Delete these before pushing this to git:                       #
# https://support.google.com/googleapi/answer/6158862            #
gkey = 'beep boop beep boop beep boop beep boop'                 #
# https://openweathermap.org/                                    #
api_key_openweathermap_org = "waffle banana apple brisket sauce" #
##################################################################

# Defining this here to be able to print with f("something", dc.somecolor) without having to define it elsewhere.
f = dc.fprint

# Configuration and Debug:
target_language = 'en-us'
project_id = 'thermal-elixir-332702'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'
headers = \
            {
                'User-Agent':
                    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) '
                    'AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/54.0.2840.71 Safari/537.36'
             }

"""This project requires the following API keys
Google:
https://cloud.google.com

Open Weather Map:
https://openweathermap.org
"""
# gkey = "REPLACE_THIS_WITH_YOUR_API_KEY"
# api_key_openweathermap_org = "REPLACE_THIS_WITH_YOUR_API_KEY"


class TestVariables:
    """Variables for use in tests.
    Test variable 1, 2, 3, and 4 are Russian surnames.
    Test variable 5 is a string of mixed text character encoding, symbols, and non-ascii characters.
    """

    def __init__(self):
        self.project_id = project_id
        self.target_language = target_language
        self.test1 = "Андреев"
        self.test2 = "Макаров"
        self.test3 = "Никитин"
        self.test4 = "Захаро"
        self.test5 = "GјфZЌv’ј%)‚ЏюiДѕХks=?„SoЃ[Ж[1]ЊZvс%з0JN2 IЗмs-Q2_'АЪх?mгЮ©ХщфЅ–‡M”"
        self.surname_variables = [self.test1, self.test2, self.test3, self.test4, self.test5]
        self.all_variables = [self.test1, self.test2, self.test3, self.test4, self.test5]
