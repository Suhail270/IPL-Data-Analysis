import json
from collections import Counter
import pycountry_convert as pc
import tkinter as tk
from .additional import sortingfunc_test
from ua_parser import user_agent_parser

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
                if "subject_doc_id" in json_data[len(json_data)-1]:
                    # Extract the document UUID and content from the JSON data
                    doc_uuid = json_data[len(json_data)-1]["subject_doc_id"]
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
        return documents, visitors, json_data

    except FileNotFoundError:
        # Handle the case where the specified file path is not found
        raise Exception("File does not exist at specified location.")

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
    return country_count, countries


'''
Maps countries to continents and counts occurrences of country in a continent.
'''
def group_country(countries):

    # Map countries to continents
    map_country = [pc.country_alpha2_to_continent_code(country) for country in countries]
    # Convert continent codes to continent names
    country_continent = [pc.convert_continent_code_to_continent_name(continent) for continent in map_country]
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
    sorted_readers = sortingfunc_test(count_dict, True)

    # Return the top 10 visitors with the highest total reading time
    return list(sorted_readers.keys())[0:10], list(sorted_readers.values())[0:10]

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
Takes the document UUID, visitor UUID (optional) and a sorting function (optional) as parameters. 
The function returns a list of “liked” documents, i.e., documents that have been read by the readers of the specified document UUID 
sorted by the sorting function parameter.
'''

def also_likes(documents, doc_uuid, visitor_uuid=None, sorting_func=None):
    visitor_doc_relationship = {}
    # Dictionary to store the count of readers for each document
    doc_reader_count = {}
    most_common_visitors = {}

    doc_counter = {}

    doc_visitor_mapping = {}

    visitors = doc_to_visitor(documents, doc_uuid)

    # print("\n\nVISITORS: ", visitors,"\n\n")

    for visitor in visitors:
        if visitor not in list(visitor_doc_relationship.keys()):
            # print("\nVISITOR DOC: ",visitor, visitor_to_doc(documents, visitor),"\n\n")
            visitor_doc_relationship[visitor] = visitor_to_doc(documents, visitor)
    
    # print("VISITOR DOC DICT: ", visitor_doc_relationship,"\n\n")

    # print("\n\nDOC READER COUNT: ", doc_reader_count,"\n\n")
    
    for visitor in visitor_doc_relationship:
        for document in visitor_doc_relationship[visitor]:
            if document in doc_counter:
                doc_counter[document] += 1
            else:
                doc_counter[document] = 1

    # print(doc_counter)

    doc_counter = dict(sorted(doc_counter.items(), key=lambda item: item[1], reverse=True))
    doc_counter = {key: doc_counter[key] for key in list(doc_counter)[:7]}
    
    # print("\n\nDOC COUNTER: ", doc_counter,"\n\n")

    visitor_counter = {}
    
    for document in doc_counter:
        visitors = doc_to_visitor(documents, document)
        for visitor in visitors:
            if visitor not in visitor_counter:
                visitor_counter[visitor] = 1
            else:
                visitor_counter[visitor] += 1

    visitor_top_counter = visitor_counter.copy()

    visitor_top_counter = dict(sorted(visitor_top_counter.items(), key=lambda item: item[1], reverse=True))
    visitor_top_counter = {key: visitor_top_counter[key] for key in list(visitor_top_counter)[:3]}

    if visitor_uuid is not None and visitor_uuid not in list(visitor_top_counter.keys()):
        if visitor_uuid in list(visitor_counter.keys()):
            visitor_top_counter[visitor_uuid] = visitor_counter[visitor_uuid]
        else:
            visitor_top_counter[visitor_uuid] = 0


    for visitor in list(visitor_top_counter.keys()):

        visited_documents = visitor_to_doc(documents, visitor)

        for document in visited_documents:
            if document not in list(doc_counter.keys()):
                visited_documents.remove(document)

        doc_visitor_mapping[visitor] = visited_documents

    # print("\n\nVISITOR COUNTER: ", visitor_counter,"\n\n")

    #         # if document not in doc_reader_count:
                
    #         #     doc_visitors = doc_to_visitor(documents, document)
                
    #         #     for i in doc_visitors:
    #         #         if i not in visitors:
    #         #             doc_visitors.remove(i)
                
    #         #     doc_reader_count[document] = doc_visitors
    
    # for doc_visitors in doc_reader_count:
    #     for visitor_count in doc_reader_count[doc_visitors]:
    #         if visitor_count in most_common_visitors:
    #             most_common_visitors[visitor_count] += 1
    #         else:
    #             most_common_visitors[visitor_count] = 1

    # # most_common_visitors = dict(sorted(most_common_visitors.items(), key=lambda item: item[1], reverse=True))

    # output = {}

    # for document in doc_reader_count:
    #     for visitor in doc_reader_count[document]:
    #         if visitor in list(most_common_visitors.keys()):
    #             if visitor not in list(output.values()):
    #                 output[document] = [visitor]
    #             else:
    #                 output[document].append(visitor)

    # # output_visitors = {}

    # # for visitor in most_common_visitors:
    # #     doc_to_vis_count = 0
    # #     documents_visited = visitor_to_doc(documents, visitor)
    # #     for doc in documents_visited:
    # #         if doc in list(doc_reader_count.keys()):
    # #             doc_to_vis_count += 1
            


    # doc_reader_count = dict(sorted(doc_reader_count.items(), key=lambda item: len(item[1]), reverse=True))
    # most_common_visitors = dict(sorted(most_common_visitors.items(), key=lambda item: item[1], reverse=True))

    # doc_reader_count = {key: doc_reader_count[key] for key in list(doc_reader_count)[:7]}
    # # most_common_visitors = {key: doc_reader_count[key] for key in list(doc_reader_count)[:7]}



    return doc_counter, visitor_top_counter, doc_visitor_mapping

# def also_likes(documents, doc_uuid, visitor_uuid=None, sorting_func=None):
#     # Dictionary to store the relationship between visitors and documents
#     visitor_doc_relationship = {}
#     # Dictionary to store the count of readers for each document
#     doc_reader_count = {}
#     # Dictionary to store the count of occurrences of each visitor across all documents
#     most_common_visitors = {}

#     # Get the list of visitors for the specified document UUID
#     visitors = doc_to_visitor(documents, doc_uuid)

#     # Create a mapping between visitors and the distinct documents they visited
#     for visitor in visitors:
#         visitor_doc_relationship[visitor] = set(visitor_to_doc(documents, visitor))

#     # Count the number of readers for each document
#     for visited_documents in visitor_doc_relationship.values():
#         for document in visited_documents:
#             # Check if the document is not already in the count_dict
#             if document not in doc_reader_count:
#                 doc_reader_count[document] = {}
            
#             # Increment the count for the document and add the visitor to the list
#             doc_reader_count[document][visitor] = doc_reader_count[document].get(visitor, 0) + 1

#     # Sort the documents based on the specified sorting function
#     if sorting_func is not None:
#         if sorting_func == '1':
#             doc_reader_count = sortingfunc_test(doc_reader_count, reverse=False)
#         elif sorting_func == '2':
#             doc_reader_count = sortingfunc_test(doc_reader_count, reverse=True)

#     # Count occurrences of each visitor across all documents
#     for visitor in visitor_doc_relationship:
#         if doc_uuid in list(visitor_doc_relationship[visitor]):
#             if visitor in most_common_visitors:
#                 most_common_visitors[visitor] += 1
#             else:
#                 most_common_visitors[visitor] = 1

#     most_common_visitors = dict(sorted(most_common_visitors.items(), key=lambda item: item[1], reverse=True))

#     # Return the sorted document-reader count and the most common visitors
#     return doc_reader_count, most_common_visitors


