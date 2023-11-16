import json
from collections import Counter

'''

'''
def views_country(json_data, doc_uuid): 

    # Filter data for the specified document UUID
    group_uuid = [entry for entry in json_data if entry.get("subject_doc_id") == doc_uuid]
    # Extract country information
    global countries
    countries = [entry["visitor_country"] for entry in group_uuid]
    #Counts occurence of each country
    country_count = Counter(countries)
    return country_count

def group_country(countries):

    #Reference :http://www.macs.hw.ac.uk/~hwloidl/Courses/F21SC/Samples/simple_histo.py
    continents = {'AF':'Africa','AN': 'Antarctica', 'AS': 'Asia', 'EU': 'Europe', 'NA': 'North America', 'SA': 'South America','OC': 'Oceania'}
    #Mapping countries with continents 
    map_country = { 'AF' : 'AS', 'AX' : 'EU', 'AL' : 'EU', 'DZ' : 'AF', 'AS' : 'OC', 'AD' : 'EU', 'AO' : 'AF', 'AI' : 'NA', 'AQ' : 'AN', 'AG' : 'NA', 'AR' : 'SA', 'AM' : 'AS', 'AW' : 'NA', 'AU' : 'OC', 'AT' : 'EU', 'AZ' : 'AS', 'BS' : 'NA', 'BH' : 'AS', 'BD' : 'AS', 'BB' : 'NA', 'BY' : 'EU', 'BE' : 'EU', 'BZ' : 'NA', 'BJ' : 'AF', 'BM' : 'NA', 'BT' : 'AS', 'BO' : 'SA', 'BQ' : 'NA', 'BA' : 'EU', 'BW' : 'AF', 'BV' : 'AN', 'BR' : 'SA', 'IO' : 'AS', 'VG' : 'NA', 'BN' : 'AS', 'BG' : 'EU', 'BF' : 'AF', 'BI' : 'AF', 'KH' : 'AS', 'CM' : 'AF', 'CA' : 'NA', 'CV' : 'AF', 'KY' : 'NA', 'CF' : 'AF', 'TD' : 'AF', 'CL' : 'SA', 'CN' : 'AS', 'CX' : 'AS', 'CC' : 'AS', 'CO' : 'SA', 'KM' : 'AF', 'CD' : 'AF', 'CG' : 'AF', 'CK' : 'OC', 'CR' : 'NA', 'CI' : 'AF', 'HR' : 'EU', 'CU' : 'NA', 'CW' : 'NA', 'CY' : 'AS', 'CZ' : 'EU', 'DK' : 'EU', 'DJ' : 'AF', 'DM' : 'NA', 'DO' : 'NA', 'EC' : 'SA', 'EG' : 'AF', 'SV' : 'NA', 'GQ' : 'AF', 'ER' : 'AF', 'EE' : 'EU', 'ET' : 'AF', 'FO' : 'EU', 'FK' : 'SA', 'FJ' : 'OC', 'FI' : 'EU', 'FR' : 'EU', 'GF' : 'SA', 'PF' : 'OC', 'TF' : 'AN', 'GA' : 'AF', 'GM' : 'AF', 'GE' : 'AS', 'DE' : 'EU', 'GH' : 'AF', 'GI' : 'EU', 'GR' : 'EU', 'GL' : 'NA', 'GD' : 'NA', 'GP' : 'NA', 'GU' : 'OC', 'GT' : 'NA', 'GG' : 'EU', 'GN' : 'AF', 'GW' : 'AF', 'GY' : 'SA', 'HT' : 'NA', 'HM' : 'AN', 'VA' : 'EU', 'HN' : 'NA', 'HK' : 'AS', 'HU' : 'EU', 'IS' : 'EU', 'IN' : 'AS', 'ID' : 'AS', 'IR' : 'AS', 'IQ' : 'AS', 'IE' : 'EU', 'IM' : 'EU', 'IL' : 'AS', 'IT' : 'EU', 'JM' : 'NA', 'JP' : 'AS', 'JE' : 'EU', 'JO' : 'AS', 'KZ' : 'AS', 'KE' : 'AF', 'KI' : 'OC', 'KP' : 'AS', 'KR' : 'AS', 'KW' : 'AS', 'KG' : 'AS', 'LA' : 'AS', 'LV' : 'EU', 'LB' : 'AS', 'LS' : 'AF', 'LR' : 'AF', 'LY' : 'AF', 'LI' : 'EU', 'LT' : 'EU', 'LU' : 'EU', 'MO' : 'AS', 'MK' : 'EU', 'MG' : 'AF', 'MW' : 'AF', 'MY' : 'AS', 'MV' : 'AS', 'ML' : 'AF', 'MT' : 'EU', 'MH' : 'OC', 'MQ' : 'NA', 'MR' : 'AF', 'MU' : 'AF', 'YT' : 'AF', 'MX' : 'NA', 'FM' : 'OC', 'MD' : 'EU', 'MC' : 'EU', 'MN' : 'AS', 'ME' : 'EU', 'MS' : 'NA', 'MA' : 'AF', 'MZ' : 'AF', 'MM' : 'AS', 'NA' : 'AF', 'NR' : 'OC', 'NP' : 'AS', 'NL' : 'EU', 'NC' : 'OC', 'NZ' : 'OC', 'NI' : 'NA', 'NE' : 'AF', 'NG' : 'AF', 'NU' : 'OC', 'NF' : 'OC', 'MP' : 'OC', 'NO' : 'EU', 'OM' : 'AS', 'PK' : 'AS', 'PW' : 'OC', 'PS' : 'AS', 'PA' : 'NA', 'PG' : 'OC', 'PY' : 'SA', 'PE' : 'SA', 'PH' : 'AS', 'PN' : 'OC', 'PL' : 'EU', 'PT' : 'EU', 'PR' : 'NA', 'QA' : 'AS', 'RE' : 'AF', 'RO' : 'EU', 'RU' : 'EU', 'RW' : 'AF', 'BL' : 'NA', 'SH' : 'AF', 'KN' : 'NA', 'LC' : 'NA', 'MF' : 'NA', 'PM' : 'NA', 'VC' : 'NA', 'WS' : 'OC', 'SM' : 'EU', 'ST' : 'AF', 'SA' : 'AS', 'SN' : 'AF', 'RS' : 'EU', 'SC' : 'AF', 'SL' : 'AF', 'SG' : 'AS', 'SX' : 'NA', 'SK' : 'EU', 'SI' : 'EU', 'SB' : 'OC', 'SO' : 'AF', 'ZA' : 'AF', 'GS' : 'AN', 'SS' : 'AF', 'ES' : 'EU', 'LK' : 'AS', 'SD' : 'AF', 'SR' : 'SA', 'SJ' : 'EU', 'SZ' : 'AF', 'SE' : 'EU', 'CH' : 'EU', 'SY' : 'AS', 'TW' : 'AS', 'TJ' : 'AS', 'TZ' : 'AF', 'TH' : 'AS', 'TL' : 'AS', 'TG' : 'AF', 'TK' : 'OC', 'TO' : 'OC', 'TT' : 'NA', 'TN' : 'AF', 'TR' : 'AS', 'TM' : 'AS', 'TC' : 'NA', 'TV' : 'OC', 'UG' : 'AF', 'UA' : 'EU', 'AE' : 'AS', 'GB' : 'EU', 'US' : 'NA', 'UM' : 'OC', 'VI' : 'NA', 'UY' : 'SA', 'UZ' : 'AS', 'VU' : 'OC', 'VE' : 'SA', 'VN' : 'AS', 'WF' : 'OC', 'EH' : 'AF', 'YE' : 'AS', 'ZM' : 'AF', 'ZW' : 'AF' } 
    #Iterates through each country in countries list and gets corresponding continent from the map_country dictionary
    country_continents = [continents.get(map_country.get(country, "Not Found"), "Not Found") for country in countries] 
    # Count occurrence of country in a continent 
    continent_count = Counter(country_continents)  
    return continent_count

def view_broswer(json_data):

    #Extract browser information
    browser = (entry["visitor_useragent"] for entry in json_data)
    # Counts occurence of the browser
    global browser_count
    browser_count = Counter(browser)
    return browser_count
    
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
            doc_uuid = "140206010823-b14c9d966be950314215c17923a04af7"
            part2a = views_country(json_data, doc_uuid)
            part2b = group_country(countries)
            part3a = view_broswer(json_data)
            part3b = format_browser(browser_count)
            print(part2a)
            print(part2b)
            # print(part3a)
            print(part3b)
    except FileNotFoundError:
        print("The file path could not be found")
      
readfile()
