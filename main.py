import random
import json
import tqdm
import pprint
from datetime import datetime
from typing import Tuple, Dict, Any

from hardcoded_data import first_names, last_names, cities
from lookup_identity_data import WebScraper
from translator import Lobot
from weather import Weather


class BaseClass:

    def __init__(self):
        self.ws = WebScraper()
        self.rf = random.randint(0, 74)
        self.rl = random.randint(0, 24)
        self.c = random.randint(0, 400)
        self.current_identity = self.specific_identity(self.rf, self.rl, self.c)
        self.first_name = self.specific_identity(self.rf, self.rl, self.c)[0]
        self.last_name = self.specific_identity(self.rf, self.rl, self.c)[1]
        self.city = self.specific_identity(self.rf, self.rl, self.c)[2]
        self.w = Weather(self.specific_identity(self.rf, self.rl, self.c)[2]['City'])
        self.weather_data = json.loads(self.w.current_local_weather())
        self.local_temperature_c = "{:.2f}".format(self.weather_data['main']['temp'] - 273.15)
        self.local_temperature_f = "{:.2f}".format(float(self.local_temperature_c) * 1.8 + 32)
        self.local_sky = self.weather_data['weather'][0]['description']
        self.local_sunrise = datetime.utcfromtimestamp(float(self.weather_data['sys']['sunrise'])).strftime(
            '%Y-%m-%d %H:%M:%S')
        self.local_sunset = datetime.utcfromtimestamp(float(self.weather_data['sys']['sunset'])).strftime(
            '%Y-%m-%d %H:%M:%S')

    def randomize_identity(self):
        """Set new random  identity indexes."""
        self.rf = random.randint(0, 74)
        self.rl = random.randint(0, 24)
        self.c = random.randint(0, 400)
        self.first_name = self.specific_identity(self.rf, self.rl, self.c)[0]
        self.last_name = self.specific_identity(self.rf, self.rl, self.c)[1]
        self.city = self.specific_identity(self.rf, self.rl, self.c)[2]
        self.w = Weather(self.specific_identity(self.rf, self.rl, self.c)[2]['City'])
        return {
            "rf": self.rf,
            "rl": self.rl,
            "c": self.c,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "city": self.city,
            "w": self.w
        }

    def specify_identity(self, rf, rl, c):
        """Set new random  identity indexes."""
        self.rf = rf  # random.randint(0, 74)
        self.rl = rl  # random.randint(0, 24)
        self.c = c  # random.randint(0, 400)
        self.first_name = self.specific_identity(self.rf, self.rl, self.c)[0]
        self.last_name = self.specific_identity(self.rf, self.rl, self.c)[1]
        self.city = self.specific_identity(self.rf, self.rl, self.c)[2]
        self.w = Weather(self.specific_identity(self.rf, self.rl, self.c)[2]['City'])
        return {
            "rf": self.rf,
            "rl": self.rl,
            "c": self.c,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "city": self.city,
            "w": self.w
        }

    def random_identity(self) -> Tuple:
        """Returns a random identity."""
        rf = self.rf
        rl = self.rl
        c = self.c
        first_name = first_names[rf][0]["Name"]
        last_name = last_names[rl][0]["Name"]
        city = cities[c][0]["City"]
        population = cities[c][0]["Population"]
        data = f"{rf}_{rl}_{c}"
        return first_name, last_name, city, population, data

    # noinspection PyMethodMayBeStatic
    def specific_identity(self, rf: int, rl: int, c: int) -> Tuple[Any, Any, Any]:
        """Lookup a specific identity a combination of indexes."""
        rf, rl, c = int(rf), int(rl), int(c)
        if 75 > rf > -1:
            _rf = rf
        else:
            _rf = 0
        if 25 > rl > -1:
            _rl = rl
        else:
            _rl = 0
        if 401 > c > -1:
            _c = c
        else:
            _c = 0
        return first_names[_rf][0], last_names[_rl][0], cities[_c][0]

    def webscrape_single_surname(self) -> str:
        """Performs a web scrape of a wikipedia page and returns one of 1707 Russian surnames."""
        surnames = self.ws.get_surnames()
        random_surname = surnames[random.randint(0, len(surnames) - 1)]
        return random_surname

    def update_surname_list(self) -> Dict:
        """Update the list of surnames in the provided hardcoded data."""
        lobot = Lobot('test')
        print(lobot.text)
        count = len(last_names)
        surnames = self.ws.get_surnames()
        for i in tqdm.tqdm(surnames):
            lobot.text = i
            print(f"\ntranslating {lobot.text} from cyrillyc to english")
            this = {count: {'Name': lobot.translate_text(lobot.text), 'Cyrillyc': i}}
            last_names.update(this)
            count = count + 1
        return last_names

    # noinspection PyMethodMayBeStatic
    def lookup_index(self, index_type: str, index: str):
        """Lookup the corresponding first name, last name, or city for a given index."""
        if index_type == "first_name":
            first_name = first_names[int(index)][0]
            return first_name
        elif index_type == "last_name":
            last_name = last_names[int(index)][0]
            return last_name
        elif index_type == "city":
            city = cities[int(index)][0]
            return city
        else:
            return "Aliems"


class Engine(BaseClass):
    def __init__(self):
        super().__init__()
        self.bc = BaseClass()


def run():
    running = True
    command = ''
    engine = Engine()
    p = pprint.pprint
    current_identity = engine.randomize_identity()
    while running:
        if command == 'exit':
            running = False
        elif command == "rf":
            print(engine.rf)
            command = input('Input command: ')
        elif command == "rl":
            print(engine.rl)
            command = input('Input command: ')
        elif command == "c":
            print(engine.c)
            command = input('Input command: ')
        elif command == "first_name":
            p(engine.first_name)
            command = input('Input command: ')
        elif command == "last_name":
            p(engine.last_name)
            command = input('Input command: ')
        elif command == "city":
            p(engine.city)
            command = input('Input command: ')
        elif command == "weather_data":
            p(engine.weather_data)
            command = input('Input command: ')
        elif command == "local_temperature_c":
            print(engine.local_temperature_c)
            command = input('Input command: ')
        elif command == "local_temperature_f":
            print(engine.local_temperature_f)
            command = input('Input command: ')
        elif command == "local_sky":
            print(engine.local_sky)
            command = input('Input command: ')
        elif command == "local_sunrise":
            print(engine.local_sunrise)
            command = input('Input command: ')
        elif command == "local_sunset":
            print(engine.local_sunset)
            command = input('Input command: ')
        elif command == "randomize_identity":
            current_identity = engine.randomize_identity()
            p(current_identity)
            command = input('Input command: ')
        elif command == "specific_identity":
            rf = input("Input first_name index: ")
            if not rf.isnumeric:
                input("Input first_name index: ")
            else:
                rl = input("Input last_name index: ")
                if not rl.isnumeric:
                    input("Input last_name index: ")
                else:
                    c = input("Input city index: ")
                    if not c.isnumeric:
                        input("Input city index: ")
                    else:
                        p(engine.specific_identity(int(rf), int(rl), int(c)))
            command = input('Input command: ')
        elif command == "webscrape_single_surname":
            print(engine.webscrape_single_surname())
            command = input('Input command: ')
        elif command == "current_identity":
            p(current_identity)
            command = input('Input command: ')
        elif command == "lookup first_name":
            index = input("Index: ")
            print(engine.lookup_index("first_name", index))
            del index
            command = input('Input command: ')
        elif command == "lookup last_name":
            index = input("Index: ")
            print(engine.lookup_index("last_name", index))
            del index
            command = input('Input command: ')
        elif command == "current_local_weather":
            pprint.pprint(engine.w.current_local_weather())
            command = input('Input command: ')
        elif command == "lookup city":
            index = input("Index: ")
            print(engine.lookup_index("city", index))
            del index
            command = input('Input command: ')
        elif command == "help":
            print(
                "\tCommand: ws - Returns the WebScraper class object.\n"
                "\tCommand: rf - Returns the first name index variable.\n"
                "\tCommand: rl - Returns the last name index variable.\n"
                "\tCommand: c - Returns the city index variable\n"
                "\tCommand: first_name - Returns the first name contianing the English and Cyrrilyc spelling.\n"
                "\tCommand: last_name - Returns the last name variable containing the English and Cyrrilyc spelling.\n"
                "\tCommand: city - Returns the city object contianing the city name and population.\n"
                "\tCommand: w - Returns the Weather class object.\n"
                "\tCommand: weather_data - Returns the weather_data json output.\n"
                "\tCommand: local_temperature_c - Returns local temperature in celsius.\n"
                "\tCommand: local_temperature_f - Returns local temperature in fahrenheit.\n"
                "\tCommand: local_sky - Returns local sky conditions.\n"
                "\tCommand: local_sunrise - Returns local sunrise time.\n"
                "\tCommand: local_sunset - Returns local sunset time.\n"
                "\tCommand: random_identity - Changes to a new random identity.\n"
                "\tCommand: specific_identity - Returns a specific identity object using the rf, rl, and c index variables.\n"
                "\tCommand: webscrape_single_surname - Returns a single surname out of 1707 possible surnames.\n"
                "\tCommand: webscrape_single_surname - Returns a single surname out of 1707 possible surnames.\n"
                "\tCommand: current_identity - Display current identity.\n"
                "\tCommand: lookup first_name - Lookup the first_name that corresponds with a specific index.\n"
                "\tCommand: lookup last_name - Lookup the last_name that corresponds with a specific index.\n"
                "\tCommand: lookup city - Lookup the city that corresponds with a specific index.\n"
            )
            command = input('Input command: ')
        if command == "run tests":
            command = input('Test Base Class? (yes, no)')
            if command == "yes":
                from tests import base_class_test
                base_class_test()
                command = input('Input command: ')
            elif command == "no":
                command = input('Test Lobot?  (yes, no)')
                if command == "yes":
                    from tests import lobot_test
                    lobot_test()
                    command = input('Input command: ')
                else:
                    command = input('Input command: ')
        else:
            command = input('Input command: ')


if __name__ == '__main__':
    run()
