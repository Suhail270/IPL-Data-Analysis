import json
from collections import Counter
import pycountry_convert as pc

'''
Counts the occurrences of each country based on the specified document UUID.
'''
def views_country(json_data, doc_uuid): 

    # Filter data for the specified document UUID
    group_uuid = [entry for entry in json_data if entry.get("subject_doc_id") == doc_uuid]
    # Extract country information
    # global countries
    countries = [entry["visitor_country"] for entry in group_uuid]
    #Counts the occurence of each country
    country_count = Counter(countries)
    return country_count,countries

'''
Maps countries to continents and counts occurrences of country in a continent.
'''
def group_country(countries):

    # Map countries to continents
    map_country = [pc.country_alpha2_to_continent_code(country) for country in countries]
    print(map_country)
    # Convert continent codes to continent names
    country_continent = [pc.convert_continent_code_to_continent_name(continent) for continent in map_country]
    print(country_continent)
    # Count occurrence of each continent
    continent_count = Counter(country_continent)
    return continent_count

'''
Counts the occurrences of each browser
'''
def view_broswer(json_data):

    #Extract browser information
    browser = (entry["visitor_useragent"] for entry in json_data)
    # Counts the occurence of the browser
    # global browser_count
    browser_count = Counter(browser)
    return browser_count

'''
Formats browser strings to display main browser name and counts occurrences.
'''  
def format_browser(browser_count):

    #Empty list to string formatted browser strings
    browsers = []
    for char in browser_count:
        browser_string = char.split('/')[0] # Split each browser string at the first '/' character and take the first part
        browsers.append(browser_string)
    # Count the occurrences of each formatted browser string
    browser_string_count = Counter(browsers)
    return browser_string_count


def readfile():
    
    file_path = './sample_small.json'

    try: 
        with open(file_path) as f:   # Read data from the file
            json_data = [json.loads(line) for line in f]
            doc_uuid = "140224195414-e5a9acedd5eb6631bb6b39422fba6798"
            part2a,countries= views_country(json_data, doc_uuid)
            part2b = group_country(countries)
            part3a = view_broswer(json_data)
            part3b = format_browser(part3a)
            print(part2a)
            print(part2b)
            # print(part3a)
            print(part3b)
    except FileNotFoundError:
        print("The file path could not be found")
      
readfile()
