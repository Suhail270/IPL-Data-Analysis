import json
from collections import Counter
import pycountry_convert as pc
import user_agent
# from user_agent import parse
from ua_parser import user_agent_parser

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

    #Empty list to store formatted browser strings
    browser_string = {}
    for char in browser_count:
        # Use the user_agent_parser library to parse the user-agent string.
        user_agent = user_agent_parser.Parse(char)
        # Check if the browser family extracted from the user-agent is already
        # present in the 'browser_string' dictionary.
        if user_agent['user_agent']['family'] not in browser_string:
            # If not present, add a new entry with the browser family as the key
            # and the count from the original dictionary as the value.
            browser_string[user_agent['user_agent']['family']] = browser_count[char]
        else:
            # If the browser family is already present, increment the count
            # by the count from the original dictionary.
            browser_string[user_agent['user_agent']['family']] += browser_count[char] 
    # Update the input dictionary 'browser_count' with the aggregated counts.
    browser_count = browser_string
    return browser_count

    


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
            # print(part2a)
            # print(part2b)
            # print(part3a)
            print(part3b)
    except FileNotFoundError:
        print("The file path could not be found")
      
readfile()
