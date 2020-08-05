"""---------------------------------------------------------------------------------------------------------------------
Name: Aryaman Singh & Yunpenn Cheng
Email ID: asin0039@student.monash.edu & yche0049@student.monash.edu
Demonstrator: Najam Nazar
Unit: FIT 2107
COURSE: Software Engineering & Information Technology
--------------------------------------------------------TASKS 1---------------------------------------------------------
"""

# importing all the data
from datetime import datetime
import argparse
import requests

# -------------------------------------------------------ARG PARSE------------------------------------------------------


# this is the argparse
def get_args():
    parser = argparse.ArgumentParser(description='Weather Forecast App For FIT2107 Assignment 3 Developed by Yunpeng Cheng & Aryaman Singh')
    # Arguments to get data
    parser.add_argument('-api', default='', required=True, type=str, help='Enter your API key received from OpenWeatherMap.org')
    parser.add_argument('-city', default='', type=str, help='Enter the name of city')
    parser.add_argument('-z', default='', type=str, help='Enter the zip code of city, for example 3168, AU for Clayton')
    parser.add_argument('-gc', default='', type=str, nargs=2, help='Enter the geographic coordinates of city, longitude and latitude are separated by space, for example 56 143')
    parser.add_argument('-cid', default=-1, type=int, help='Enter the ID of city')
    parser.add_argument('-temp', default='celsius', type=str, choices=['celsius', 'fahrenheit'], help='Enter the unit for temperature, ​celsius OR fahrenheit')
    # Arguments to process received data
    parser.add_argument('-time', action='store_true', help='Display the time')
    parser.add_argument('-pressure', action='store_true', help='Display the pressure')
    parser.add_argument('-cloud', action='store_true', help='Display the cloud level')
    parser.add_argument('-humidity', action='store_true', help='Display the humidity')
    parser.add_argument('-wind', action='store_true', help='Display the wind speed')
    parser.add_argument('-sunset', action='store_true', help='Display the sunset time')
    parser.add_argument('-sunrise', action='store_true', help='Display the sunrise time')
    parser.add_argument('-help', action='store_true', help='Display the help message')

    #args = parser.parse_args()
    return parser


# ------------------------------------------------------COMPOSE URL-----------------------------------------------------

def compose_url(args):
    """
    This function checks if the data inserted is eligible to output a correct url!

    :param args: takes in the args which contains the arguments made by the user
    :return: Check the arguments which were called and make a counter to check if the requirement is met
    """
    # Check how many arguments has user entered for locations (should not be more than 1)
    arg_count = 0
    if args.city != '':
        arg_count = arg_count + 1
    if args.cid != -1:
        arg_count = arg_count + 1
    if args.gc != '':
        arg_count = arg_count + 1
    if args.z != '':
        arg_count = arg_count + 1

    # url is saved for later use
    url = 'http://api.openweathermap.org/data/2.5/weather?'
    # If user entered more than one arguments, return and exit,
    # otherwise compose the url
    if arg_count != 1:
        return -1
    elif args.city != '':
        url = url + 'q=' + args.city
    elif args.cid != -1:
        url = url + 'id=' + str(args.cid)
    elif args.gc != '':
        url = url + 'lon=' + args.gc[0] + '&lat=' + args.gc[1]
    elif args.z != '':
        url = url + 'zip=' + args.z

    # Change Celsius to metric, Fahrenheit to imperial of args.temp based on
    # requirements of open weather endpoint, and return the composed url
    if args.temp == 'celsius':
        url = url + '&units=metric&appid=' + args.api
        return url
    elif args.temp == 'fahrenheit':
        url = url + '&units=imperial&appid=' + args.api
        return url
    else:
        # return -2 if something wrong with the temperature
        return -2

# ---------------------------------------------------SEND REQUESTS------------------------------------------------------


def send_request(url):
    """
    Gives out all the data in JSON

    :param url: Takes URL and requests data from the website
    :return: gives out the result value in JSON
    """
    response = requests.get(url)
    # gives out JSON for the requests made
    result = response.json()
    return result

# -----------------------------------------------------PARSE RESULTS----------------------------------------------------


def parse_result(result, args):
    """

    :param result: Result contains all the data retrieved by the URL
    :param args: Contains the user data which needs to be output
    :return: Error if there are no features chosen by the user or returns the desirable function
    """
    output = ''

    if args.temp:
        output = output + 'The temperature ranges from ' + str(result['main']['temp_min']) + ' - ' + str(result['main']['temp_max'])
    if args.time:
        output = 'On ' + str(datetime.fromtimestamp(result['dt'])) + ', ' + output
    if args.pressure:
        output = output + ', Pressure is ' + str(result['main']['pressure']) + 'hPa'
    if args.cloud:
        output = output + ', Cloudness is ' + str(result['clouds']['all']) + '%'
    if args.humidity:
        output = output + ', Humidity is ' + str(result['main']['humidity']) + '%'
    if args.wind:
        output = output + ', Wind speed of ' + str(result['wind']['speed']) + ' from ' + str(result['wind']['deg']) + ' degrees'
    if args.sunset:
        output = output + ', The sunset time is ' + str(datetime.fromtimestamp(result['sys']['sunset']))
    if args.sunrise:
        output = output + ', The sunrise time is ' + str(datetime.fromtimestamp(result['sys']['sunrise']))

    # If the array is empty, then gives an Error
    if output is '':
        output = 'Error: Add some feature!'

    # returns the output
    return output

# ------------------------------------------------------PROCESS---------------------------------------------------------


def process(result, args):
    """
    Checks if the URL is legit, if not then gives error. But if it is then it gives parsed data which can be
    printed in the console.

    :param result: Result contains all the data retrieved by the URL
    :param args: Contains the user data which needs to be output
    :return: Error if the URL doesnt responds and also print the Error Code
    """
    # the url 200 is correct
    if result['cod'] == 200:
        status = parse_result(result, args)

        # returns the parsed info
        return status
    else:
        # the url is not correct, would print the error number
        return str(result['cod']) + ' error '

# -----------------------------------------------------PROCESS2---------------------------------------------------------


def process2(args):
    """
    Composes the url if the all the arguments are correctly inserted but then gives error if its not.

    :param args: Contains the user data which needs to be output
    :return: Composes the URL and gives error if there are more locations repeated or some other unit of temperature
    is used other than Celsius or Fahrenheit
    """

    url = compose_url(args)
    # the args have more than 1 locations mentioned
    if url == -1:
        return 'You must specify only one of city name, city id, geographic coordinates or zip code'
    # temperature is presented in some other units
    elif url == -2:
        return 'Unknown temperature unit'
    else:
        # returns the url if args are all correct
        return url

# ------------------------------------------------------MAIN------------------------------------------------------------


def main():
    """
    contains all the main functions required to make the program work
    :return: returns the function to print to the console
    """
    parser = get_args()
    args = parser.parse_args()
    url = process2(args)
    result = send_request(url)
    status = process(result, args)

    return status


if __name__ == '__main__':
    final_output = main()
    print(final_output)

# ----------------------------------------------------------END---------------------------------------------------------
