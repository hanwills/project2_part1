import json
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):

    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime("%A %d %B %Y")


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius

    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
    celsiustemp = round((temp_in_farenheit - 32) *  5/9, 1)
    return celsiustemp

# convert_f_to_c(32)
# convert_f_to_c(97)

def calculate_mean(total, num_items):

    """Calculates the mean.
    
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    mean = round(total / num_items)
    return mean

    # print(mean)
# random_numbers = [5, 7, 24, 8]
# sum_of_random_numbers = sum(random_numbers)
# print(calculate_mean(sum_of_random_numbers,len(random_numbers)))
# results = calculate_mean(sum_of_random_numbers, len(random_numbers))
# print(results)

def process_weather(forecast_file):

    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
with open("data/forecast_5days_a.json") as forecast_file:
        forecast_data = json.load(forecast_file)

daily_forecast = forecast_data["DailyForecasts"]

#Dates
for date in daily_forecast:
    date_1 = date["Date"]
    print(date_1)

#min temp for all days
    for date in daily_forecast:
        temperature = date["Temperature"]
        minimum_1 = temperature["Minimum"]
        minimum_2 = minimum_1["Value"]

#max temp for all days
    for date in daily_forecast:
        temperature_2 = date["Temperature"]
        maximum_1 = temperature_2["Maximum"]
        maximum_2 = maximum_1["Value"]

#long phrase description for each day
    for date in daily_forecast:
        day_long = date["Day"]
        day_long_phrase = day_long["LongPhrase"]

#long phrase description for each night
    for date in daily_forecast:
        night_long = date["Night"]
        night_long_phrase = night_long["LongPhrase"]


#Day % chance of rain
    for date in daily_forecast:
        day_rain = date["Day"]
        chance_day_rain = day_rain["PrecipitationProbability"]


#night % chance of rain
    for date in daily_forecast:
        night_rain = date["Night"]
        chance_night_rain = night_rain["PrecipitationProbability"]
 # Retrieve Temperature
    for item in forecast_data["DailyForecasts"]:
        min_temp = (item["Temperature"]["Minimum"]["Value"])
        max_temp = (item["Temperature"]["Maximum"]["Value"])

        # print( f"Minimum: {min_temp}, Maximum: {max_temp}")

    
    output = " " #this is just a break for formatting
    output += f"-------- {date_1} --------\n"
    output += f"Minimum Temperature: {minimum_2}\n"
    output += f"Maximum Temperature: {maximum_2}\n"
    output += f"Daytime: {day_long_phrase}\n"
    output += f"    Chance of rain: {chance_day_rain}\n"
    output += f"Nighttime:  {night_long_phrase}\n"
    output += f"    Chance of rain: { chance_night_rain}\n"
    # print( "output")

# for temperature in daily_forecast:
#     min_temp = 

if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))
if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))
    print(process_weather("data/forecast_5days_b.json"))
    print(process_weather("data/forecast_8days.json"))