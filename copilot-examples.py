import datetime
import random
import uuid
import requests


# basically everything in this file was generated by CoPilot !


def main():
    print('Hello World')
    dt = get_datetime()
    print(f'The time and date is {dt}')
    print('The random number is {rn}'.format(rn=get_random_number()))
    print('The string "Hello World" in all caps is {uc}'.format(uc=to_upper('Hello World')))
    print('The uuid is {uuid}'.format(uuid=generate_uuid()))
    print('A joke: {joke}'.format(joke=get_joke()))


# a function that returns the current datetime
def get_datetime():
    return datetime.datetime.now()


# a function that returns a random number between 1 and 500
def get_random_number():
    return random.randint(1, 500)


# a function that turns a string to all caps
def to_upper(string):
    return string.upper()


# generate a uuid
def generate_uuid():
    return str(uuid.uuid4())


# get a random joke from the web using a web service
def get_joke():
    url = 'https://sv443.net/jokeapi/v2/joke/Any'
    response = requests.get(url)

    # if response json has joke property, return it
    if 'joke' in response.json():
        return response.json()['joke']
    # if response has setup and delivery properties, return them
    elif 'setup' in response.json() and 'delivery' in response.json():
        return response.json()['setup'] + ' ' + response.json()['delivery']
    # else return empty string
    else:
        return ''


if __name__ == "__main__":
    main()
