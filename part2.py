import json
from collections import Counter
import pycountry_convert as pc
import tkinter as tk

file_path = './sample_small.json'

'''
This function reads the JSON file specified by the file_path and returns the documents, visitors, and the entire JSON data.
The data structures returned by this are invoked and used throughout rest of the parts.
'''

def read_file(file_path):
    # Initialize dictionaries to store documents and visitors
    documents = {}
    visitors = {}

    try:
        # Open the file specified by the file_path
        with open(file_path) as f:
            # Initialize an empty list to store JSON data
            json_data = []

            # Iterate through each line in the file
            for line in f:
                # Parse the JSON data from the line and append it to the list
                json_data.append(json.loads(line))

                # Check if the JSON data contains "env_doc_id"
                if "env_doc_id" in json_data[len(json_data)-1]:
                    # Extract the document UUID and content from the JSON data
                    doc_uuid = json_data[len(json_data)-1]["env_doc_id"]
                    content = json_data[len(json_data)-1]

                    # Check if the document UUID is already in the documents dictionary
                    if doc_uuid in documents:
                        # Append the content to the existing list
                        documents[doc_uuid].append(content)
                    else:
                        # Create a new list with the content for the document UUID
                        documents[doc_uuid] = [content]

                # Check if the JSON data contains "visitor_uuid"
                if "visitor_uuid" in json_data[len(json_data)-1]:
                    # Extract the visitor ID from the JSON data
                    visitor_id = json_data[len(json_data)-1]["visitor_uuid"]

                    # Check if the visitor ID is already in the visitors dictionary
                    if visitor_id in visitors:
                        # Append the content to the existing list
                        visitors[visitor_id].append(content)
                    else:
                        # Create a new list with the content for the visitor ID
                        visitors[visitor_id] = [content]

    except FileNotFoundError:
        # Handle the case where the specified file path is not found
        print("The file path could not be found")

    # Return the documents, visitors, and the entire JSON data
    return documents, visitors, json_data


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

'''
Additional Feature: Sorts dictionaries in descending order based on the values.
'''

def sortingfunc_test(doc_reader_count, reverse=True):

    if type(doc_reader_count) is dict:
        # Sort the document-reader count dictionary based on the count in descending order
        return dict(sorted(doc_reader_count.items(), key=lambda item: item[1], reverse=True))
    else:
        return sorted(doc_reader_count.items(), key=lambda item: item[1], reverse=True)

'''
Identifies the most avid readers. It determines, for each user, the total time spent reading documents. The top 10 readers, 
based on this analysis is stored in a dictionary where the key is the visitor and the value pair is the accumulation of the time
spent reading each of their documents.
'''

def avid_readers(visitors):
    # Dictionary to store the reading time for each visitor
    count_dict = {}

    # Iterate through each visitor
    for i in visitors.keys():
        # Iterate through each event for the visitor
        for j in visitors[i]:
            # Check if the event contains "event_readtime"
            if "event_readtime" in j:
                # Extract the reading time
                time = j["event_readtime"]
                # Check if the visitor is already in the count_dict
                if i in count_dict:
                    # Append the reading time to the existing list
                    count_dict[i].append(time)
                else:
                    # Create a new list with the reading time for the visitor
                    count_dict[i] = [time]

    # Calculate the total reading time for each visitor
    for i in count_dict.keys():
        count_dict[i] = sum(count_dict[i])

    # Sort visitors based on their total reading time in descending order
    sorted_readers = sortingfunc_test(count_dict)

    # Return the top 10 visitors with the highest total reading time
    return sorted_readers[0:10]

'''
Takes a document UUID and returns all visitor UUIDs of readers of that document.
'''

def doc_to_visitor(documents, doc_uuid):
    # List to store unique visitors for a given document UUID
    visitors = []
    
    # Iterate through each event for the specified document UUID
    for i in documents[doc_uuid]:
        # Check if the event contains "visitor_uuid"
        if "visitor_uuid" in i:
            # Add the visitor UUID to the list if it's not already present
            if i["visitor_uuid"] not in visitors:
                visitors.append(i["visitor_uuid"])
    
    return visitors

'''
Takes a visitor UUID and returns all document UUIDs that have been read by this visitor.
'''

def visitor_to_doc(documents, visitor_uuid):
    # List to store documents visited by a given visitor UUID
    docs = []
    
    # Iterate through each document UUID in the documents dictionary
    for i in documents.keys():
        # Iterate through each event for the current document UUID
        for j in documents[i]:
            # Check if the event contains "visitor_uuid" matching the specified visitor UUID
            # and if the document UUID is not already in the list
            if "visitor_uuid" in j and j["visitor_uuid"] == visitor_uuid and i not in docs:
                docs.append(i)
    
    return docs

'''
Additional Feature: Goes through all the documents and returns the document UUID with the highest number of unique 
visitors and the corresponding count.
'''

def max_unique_visitors(documents):
    # Variables to store the maximum number of unique visitors and the corresponding document UUID
    max_visitors_count = 0
    document_with_max_visitors = None

    # Iterate through each document UUID in the documents dictionary
    for doc_uuid in documents:
        # Get the unique visitors for the current document UUID
        visitors = doc_to_visitor(documents, doc_uuid)
        
        # Calculate the number of unique visitors
        unique_visitors_count = len(visitors)

        # Update max_visitors_count and document_with_max_visitors if a higher count is found
        if unique_visitors_count > max_visitors_count:
            max_visitors_count = unique_visitors_count
            document_with_max_visitors = doc_uuid
    
    return document_with_max_visitors, max_visitors_count

'''
Takes the document UUID, visitor UUID (optional) and a sorting function (optional) as parameters. 
The function returns a list of “liked” documents, i.e., documents that have been read by the readers of the specified document UUID 
sorted by the sorting function parameter.
'''

def also_likes(documents, doc_uuid, visitor_uuid=None, sorting_func=None):
    # Dictionary to store the relationship between visitors and documents
    visitor_doc_relationship = {}
    # Dictionary to store the count of readers for each document
    doc_reader_count = {}

    # Get the list of visitors for the specified document UUID
    visitors = doc_to_visitor(documents, doc_uuid)
    
    # Create a mapping between visitors and the documents they visited
    for visitor in visitors:
        visitor_doc_relationship[visitor] = visitor_to_doc(documents, visitor)

    # Count the number of readers for each document
    for i in visitor_doc_relationship.values():
        for document in i:
            # Check if the document is not already in the count_dict
            if document not in list(doc_reader_count.keys()):
                # Initialize the count for the document
                doc_reader_count[document] = 1
            else:
                # Increment the count for the document
                doc_reader_count[document] += 1
    
    # Sort the documents based on the specified sorting function
    if sorting_func is not None:
        doc_reader_count = sorting_func(doc_reader_count)

    # Return the sorted document-reader count
    return doc_reader_count

'''
Additional Feature: Goes through the dataset until it finds records that are suitable to test the also_likes functionality
and prints them.
'''

def test_also_likes(documents):
    # Iterate through each document UUID in the documents dictionary
    for i in documents.keys():
        # Get the result of the also_likes function for the current document UUID
        result = also_likes(documents, i)
        # Check if the result has more than one document (indicating readership overlap)
        if len(list(result.keys())) > 1:
            # Print the document UUID and the result
            print(i, result)


documents, visitors, json_data = read_file(file_path)
doc_uuid = "130323125939-5f4318404cda4025a2463c66435ad7c8"

part2a, countries = views_country(json_data, doc_uuid)
part2b = group_country(countries)
part3a = view_broswer(json_data)
part3b = format_browser(part3a)
print(part2a)
print(part2b)
print(part3a)
print(part3b)


doc_uuid, doc_vis_count = max_unique_visitors(documents)

doc_uuid = "130323125939-5f4318404cda4025a2463c66435ad7c8"
also_likes = also_likes(documents, doc_uuid, sorting_func=sortingfunc_test)

# print(also_likes)
