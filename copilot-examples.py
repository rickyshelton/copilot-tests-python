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
    print('The temperature in Bristol is {temp}'.format(temp=get_bbc_temperature()))
    print('A headline: {headline}'.format(headline=get_bbc_headline()))
    print('The sorted numbers are {numbers}'.format(numbers=sort_numbers()))
    print('The name of my new puppy is {name}'.format(name=get_puppy_name()))


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


# get the current temperature in Bristol, UK
def get_temperature():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Bristol,uk&appid=b6907d289e10d714a6e88b30761fae22'
    response = requests.get(url)
    return response.json()['main']['temp']


# scrape the bbc website for the current temperature in Bristol UK
def get_bbc_temperature():
    url = 'https://www.bbc.co.uk/weather/2654675'
    response = requests.get(url)
    return response.text.split('<span class="wr-value--temperature">')[1].split('</span>')[0]


# scrape the bbc news website for a random headline
def get_bbc_headline():
    url = 'https://www.bbc.co.uk/news'
    response = requests.get(url)
    return response.text.split('<h3 class="gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text">')[1].split('</h3>')[0]


# implement a quick sort of a list of numbers
def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        pivot = numbers[0]
        less = [i for i in numbers[1:] if i <= pivot]
        greater = [i for i in numbers[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


# generate a list of 100 random numbers and sort it using quick sort
def sort_numbers():
    numbers = [random.randint(1, 500) for i in range(100)]
    return quick_sort(numbers)


# return a good name for my new puppy
def get_puppy_name():
    return 'Fido'



if __name__ == "__main__":
    main()
