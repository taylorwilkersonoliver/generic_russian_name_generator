"""Lobot, also known by the nickname Lo, was a male human from the planet Bespin.

With the assistance of his AJ^6 cyborg construct, Lobot was paid to run battlefield calculations for the Galactic Empire.
In order to use this translator you must have a valid Google Cloud Platform account, project, and "key.json" file.
You may refer to https://cloud.google.com/translate/docs/ for more information.

Typical usage example:

    foreign_text = "Ilunga"
    lobot = Lobot(foreign_text)
    print(lobot.results)

Args:

    The class accepts any ASCII text string from any language, automatically detects the language, and translates
    the text into the "target_language" which you can set according to your preferred language in the configuration file.
    The default target language is set to "en-us" (American English).

Returns:

    The "convert_string_to_int_list" function converts a string of foreign text, including integers, symbols, and spaces,
    into a list of integers.
        string_to_ints = lobot.convert_string_to_int_list(foreign_text)

    The "convert_int_list_to_characters" function converts the result of "convert_string_to_int_list" back to the
    original text.
        ints_to_string = lobot.convert_int_list_to_characters(string_to_ints)

    The "translate_text" function detects the language of text input, translates the text into the language specified
    by the "target_language" variable, and returns the translated text.
        translated_text = lobot.translate_text(foreign_text)

    The "individual_character_decoder" function converts an integer list into the ASCII equivalent, translates that
    into the language specified by the "target_language" variable, and returns the translated result. A helper function
    "icd_string" can be used to concatenate the list back into a string if desired.
        icd_string = lobot.individual_character_decoder(integer_list=string_to_ints))
        # or
        icd_string = lobot.icd_string

"""
from google.cloud import translate
from google.cloud import translate_v2 as translatev2
from typing import List

import config
import os

ppp = config.ppp


class Lobot:
    """Lobot, also known by the nickname Lo, was a male human from the planet Bespin who,
    with the assistance of his AJ^6 cyborg construct, was paid to run battlefield calculations
    for the Galactic Empire.

    Typical Usage:
        from translator import Lobot
        l = Lobot("Ilunga")
        print(l.input_type)      # --> string
        print(l.text)            # --> Ilunga
        print(l.integer_list)    # --> [73, 108, 117, 110, 103, 97]
        print(l.target_language) # --> en-us
        print(l.translation)     # --> 'Member'
        print(l.results)         # --> \
            # (
            #     'Ilunga',
            #     [73, 108, 117, 110, 103, 97],
            #     ['I', 'I', 'u', 'n', 'g', 'a'],
            #     {
            #         'confidence': 0.5221643447875977,
            #         'language': 'xh',
            #         'input': 'Ilunga'
            #     },
            #     'Member'
            # )

    """

    def __init__(self, *args):
        self.default_variable = config.TestVariables().test1
        self.input_level = 0
        self.conversion = {}
        self.target_language = config.target_language
        self.input_type = self.input_handler(args[self.input_level])
        if self.input_type == "string":
            self.text = args[self.input_level]
            self.integer_list = self.convert_string_to_int_list(args[self.input_level])
        elif self.input_type == "integer":
            self.text = self.convert_int_list_to_characters([args[self.input_level]])
        elif self.input_type == "list":
            for i in args[self.input_level]:
                self.input_type = self.input_handler(i)
                if self.input_type == "string":
                    self.text = self.convert_string_to_int_list(args[self.input_level])
                if self.input_type == "integer":
                    self.text = self.convert_int_list_to_characters(args[self.input_level])
        elif self.input_type == "Aliems":
            print("LV-223")
            self.text = "ЪІЋЂЃ"
        self.translation = self.cloud_translate_string(self.text)

    def all_results(self):
        return self.text, \
               self.integer_list, \
               self.individual_character_decoder(self.integer_list), \
               self.detect_language(self.text), \
               self.translation

    @property
    def target_language(self):
        print("Target Language: {}".format(config.target_language))
        return config.target_language

    @target_language.setter
    def target_language(self, value):
        self._target_language = value

    @target_language.getter
    def target_language(self):
        return self._target_language

    def input_handler(self, this):
        """Determine the type of input.

        First, the input types expected are all set to False. Next, using truth statements, the input type is tested.
        Finally, the input type is returned as a string. If the input is not a string, integer, or list, thar be Aliems.

        Args:
            Anything.

        Returns:
            Input type.

        """
        if type(this) == str:
            return "string"
        elif type(this) == int:
            return "integer"
        elif type(this) == List:
            return "list"
        else:
            return "Aliems"

    # noinspection PyDefaultArgument
    def convert_int_list_to_characters(self, numbers: List) -> str:
        """Converts a list of ordinals (ints) into characters.

        Args:
            List of ordinal integers.

        Returns:
            String representation of the ordinal integers in the list.

        """
        if numbers is None:
            numbers = self.default_variable
        out = ''
        for i in numbers:
            out += chr(i)
        return out

    def convert_string_to_int_list(self, string: str) -> List:
        """Converts a string to the ordinal representation of that string.

        Increment through a string and convert each character to the ordinal equivalent.

        Args:
            A string of ASCII characters.

        Returns:
            A list of ordinal integers.

        """
        out = []
        for i in string:
            out.append(ord(i))
        return out

    def detect_language(self, text):
        """Detects the text's language.

        Documentation for this can be found at: https://cloud.google.com/translate/docs/basic/detecting-language

        Returns:
            Language of the string.

        """
        # noinspection PyShadowingNames
        translate_client = translatev2.Client()
        if type(text) == str:
            result = translate_client.detect_language(text)
        else:
            result = translate_client.detect_language(text.decode('UTF-8'))
        return result

    def translate_text(self, text):
        """Translate text using Google Cloud Translate API.

        Documentation for this can be found at: https://cloud.google.com/translate
        text = convert_int_list_to_characters(message).encode('UTF-8')
        Target_language should be a country code, lower case, and set in the configuration file.

        Args:
            String to be translated.

        Returns:
            Translated string.

        """
        client = translate.TranslationServiceClient()
        location = "global"
        parent = f"projects/{config.project_id}/locations/{location}"
        source_language = self.detect_language(text)['language']
        if source_language != "en" and source_language != 'und':
            response = client.translate_text(
                request={
                    "parent": parent,
                    "contents": [text],
                    "mime_type": "text/plain",
                    "source_language_code": self.detect_language(text)['language'],
                    "target_language_code": self.target_language,
                }
            )
            out = ''
            for translation in response.translations:
                out += translation.translated_text
        else:
            out = text
        return out

    # noinspection PyDefaultArgument
    def cloud_translate_int_list(self, message: List):
        """Detect language of text and translate to your desired language.

        Documentation for this can be found at: https://cloud.google.com/translate

        Args:
            Integer list.

        Returns:
            Translated string.

        """
        # proj = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
        out = self.translate_text(text=self.convert_int_list_to_characters(message).encode('UTF-8'))
        return out

    # noinspection PyDefaultArgument
    def cloud_translate_string(self, message=''):
        """Detect language of text and translate to your desired language.

        Documentation for this can be found at: https://cloud.google.com/translate

        Args:
            Untranslated string.

        Returns
            Translated string.

        """
        proj = os.environ['GOOGLE_APPLICATION_CREDENTIALS']

        out = self.translate_text(text=message.encode('UTF-8'))

        return out

    def individual_character_decoder(self, integer_list):
        """Translate each character individually instead of as a word.

        This method can help with translating certain languages like Russian and Chinese.

        Args:
            List of integers.

        Returns:
            List of single character strings.

        """
        out = []
        for i in integer_list:
            # print(test.translate_text(test.convert_int_list_to_characters([i])))
            out.append(self.translate_text(self.convert_int_list_to_characters([i])))
        return out

    def icd_string(self):
        """Shortcut function to use the "individual_character_decoder" function and return the results as a string.

        Args:
            None.

        Returns:
            String representation of integer list after being translated by individual character decoding.

        """
        new_string = ''
        for i in self.individual_character_decoder(self.integer_list):
            new_string += i
        return new_string
