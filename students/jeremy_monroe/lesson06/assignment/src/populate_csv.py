"""
When run this module will populate a csv file with 1,000,000 additional records
using randomly generated data.
"""

import csv
import uuid
from random import randint
from faker import Faker

FAKE = Faker()

# Just kidding. It will only add 100 records unless you uncomment the other
# repetitions variable.
REPETITIONS = 1000
# REPETITIONS = 1000000

def add_records(filename):
    """
    Populates a newly created csv file expanding on the data already stored in
    exercise.csv.
    """
    uuid_generator = (str(uuid.uuid4()) for new_uuid in range(REPETITIONS))
    random_date = (generate_random_date() for date in range(REPETITIONS))
    random_cc_number = (FAKE.credit_card_number(card_type=None) for number
                        in range(REPETITIONS))
    random_sentence = (FAKE.sentence(nb_words=10, variable_nb_words=True,
                                     ext_word_list=None) for
                       sentence in range(REPETITIONS))
    new_record_gen = ([index+10, next(uuid_generator), index+10, index+10,
                       next(random_cc_number), next(random_date),
                       next(random_sentence)] for index in range(REPETITIONS))

    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)

        for _ in range(REPETITIONS):
            writer.writerow(next(new_record_gen))

    # for i in range(10):
    #    print(next(new_record_gen))


def generate_random_date():
    """ Generates and returns a random date between the years 1700 and 2300 """
    random_str_time = '{}/{}/{}'.format(str(randint(1, 12)).zfill(2),
                                        str(randint(1, 31)).zfill(2),
                                        randint(1700, 2300))

    return random_str_time


if __name__ == "__main__":
    FILENAME = "data/exercise.csv"
    add_records(FILENAME)