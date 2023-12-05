from datetime import datetime

'''
Additional Feature: Goes through all the documents and returns the document UUID with the highest number of unique 
visitors and the corresponding count.
'''

def max_unique_visitors(documents, visitors):
    # Variables to store the maximum number of unique visitors and the corresponding document UUID
    max_visitors_count = 0
    document_with_max_visitors = None

    # Iterate through each document UUID in the documents dictionary
    for doc_uuid in documents:
        
        # Calculate the number of unique visitors
        unique_visitors_count = len(visitors)

        # Update max_visitors_count and document_with_max_visitors if a higher count is found
        if unique_visitors_count > max_visitors_count:
            max_visitors_count = unique_visitors_count
            document_with_max_visitors = doc_uuid
    
    return document_with_max_visitors, max_visitors_count

'''
Additional Feature: Goes through the dataset until it finds records that are suitable to test the also_likes functionality
and prints them.
'''

def also_likes_testing(documents, doc_reader_count, also_likes):
    # Iterate through each document UUID in the documents dictionary
    for i in documents.keys():
        also_like_func = also_likes(documents, i)
        # Get the result of the also_likes function for the current document UUID
        # Check if the result has more than one document (indicating readership overlap)
        for j in also_like_func:
            for k in also_like_func[j]:
                   if also_like_func[j][k] > 1 and len(list(also_like_func[j].keys())) > 1:
                     # Print the document UUID and the result
                     print(i, also_like_func[i])

'''
Additional Feature: Sorts dictionaries in ascending/descending order based on the values.
'''

def sortingfunc_test(doc_reader_count, reverse):
    # if type(doc_reader_count) is dict:
        # Sort the document-reader count dictionary based on the count (inner dictionary)
    return dict(sorted(doc_reader_count.items(), key=lambda item: item[1], reverse=reverse))
    # else:
    #     # Sort the list of tuples based on the count
    #     return sorted(doc_reader_count.items(), key=lambda item: item[1], reverse=reverse)
    
def find_doc(json_data, country_count):
     
    doc_uuids_with_multiple_countries = []

    # Iterate through the JSON data
    for entry in json_data:
        doc_uuid = entry.get("subject_doc_id")

        # Check if the length of the country_count dictionary is greater than 1
        if len(country_count) > 1:
            doc_uuids_with_multiple_countries.append(doc_uuid)

    return doc_uuids_with_multiple_countries

def validation(doc_uuid=None, visitor_uuid=None, documents=None, visitors=None):
    valid = True
    # Check if the document UUID is valid
    if doc_uuid is not None and doc_uuid is not None:
        if doc_uuid not in documents:
            valid = "document"
    
    # Check if the visitor UUID is valid
    if visitor_uuid is not None and visitors is not None:
        if visitor_uuid not in visitors:
            valid = "visitor"     

    if valid is not True:
        raise Exception("Invalid {x} UUID. Please try again.".format(x=valid))
    else:       
        return valid

'''
Additional Feature: Returns the most common time of the day when a specified document is read. If no document ID is specified,
the function returns the most common time of the day when all documents are read.
'''

def most_popular_time_documents(documents, doc_uuid=None):
    # Dictionary to store the number of views for each hour
    timestamp_count = {}

    if documents is not None:

        if doc_uuid is not None:
        # Iterate through each event for the specified document UUID
            for event in documents[doc_uuid]:
                # Get the timestamp for the current event
                timestamp = datetime.fromtimestamp(int(event.get("ts")))

                if timestamp not in timestamp_count:
                    # Initialize the count for the timestamp
                    timestamp_count[timestamp] = 1
                else:
                    # Increment the count for the timestamp
                    timestamp_count[timestamp] += 1
        
        else:
            # Iterate through each document UUID in the documents dictionary
            for doc_uuid in documents:
                # Iterate through each event for the current document UUID
                for event in documents[doc_uuid]:
                    # Get the timestamp for the current event
                    timestamp = datetime.fromtimestamp(int(event.get("ts")))

                    if timestamp not in timestamp_count:
                        # Initialize the count for the timestamp
                        timestamp_count[timestamp] = 1
                    else:
                        # Increment the count for the timestamp
                        timestamp_count[timestamp] += 1
    
    return timestamp_count

'''
Additional Feature: Returns the most common time of the day when a specified visitor reads the documents.
'''

def most_popular_time_visitors(visited_documents, all_documents):
    # Dictionary to store the number of views for each hour
    timestamp_count = {}                     
    for document in visited_documents:
        # Iterate through each event for the current document UUID
        for event in all_documents[document]:
            # Get the timestamp for the current event
            timestamp = datetime.fromtimestamp(int(event.get("ts")))

            if timestamp not in timestamp_count:
                # Initialize the count for the timestamp
                timestamp_count[timestamp] = 1
            else:
                # Increment the count for the timestamp
                timestamp_count[timestamp] += 1
    
    return timestamp_count

    
'''
Additional Feature: Pseudo-labels users as school/office or home based on the time stamp.
'''

# Function to determine the location (home or office/school) of a given IP address in the context of visitor events
def ip_to_location(documents, ip_address=None):
    # Dictionary to store count of home and office/school views
    views = {"Home": 0, "Office/School": 0}
    
    # List to store unique hours (for non-specified IP addresses)
    l = []

    # Iterate through each document UUID in the documents dictionary
    for doc_uuid in documents:
        # Iterate through each event for the current document UUID
        for event in documents[doc_uuid]:
            
            # If a specific IP address is provided, check for its presence in the event
            if ip_address is not None:
                if "visitor_ip" in event and event["visitor_ip"] == ip_address:
                    time = datetime.fromtimestamp(int(event.get("ts")))
            
            # If no specific IP address is provided, consider all events and track hours for non-specified IP addresses
            else:
                time = datetime.fromtimestamp(int(event.get("ts")))
                if time.hour not in l:
                    l.append(time.hour)
                # Check if the event timestamp falls within office/school hours (9am to 5pm)
                if time.hour >= 9 and time.hour <= 17:
                    views["Office/School"] += 1
                else:
                    views["Home"] += 1
    
    return views

'''
Additional Feature: Counts logged-in visitors based on their username and source
'''

def logged_in_visitors(visitors):
    logged_in_visitors = {}

    for visitor in visitors:
        for entries in visitors[visitor]:
            # Check for the presence of both "visitor_username" and "visitor_source" in the event
            if "visitor_username" in list(entries.keys()) and "visitor_source" in list(entries.keys()):
                # Update the count of logged-in visitors for each source
                if entries["visitor_source"] in list(logged_in_visitors.keys()):
                    logged_in_visitors[entries["visitor_source"]] += 1
                else:
                    logged_in_visitors[entries["visitor_source"]] = 1
    
    return logged_in_visitors

'''
Additional Feature: Counts non logged-in visitors based on their source
'''

def non_logged_in_visitors(visitors):
    non_logged_in_visitors = {}
    
    for visitor in visitors:
        for entries in visitors[visitor]:
            # Check for the absence of "visitor_username" and the presence of "visitor_source" in the event
            if "visitor_username" not in list(entries.keys()) and "visitor_source" in list(entries.keys()):
                # Update the count of non-logged-in visitors for each source
                if entries["visitor_source"] in list(non_logged_in_visitors.keys()):
                    non_logged_in_visitors[entries["visitor_source"]] += 1
                else:
                    non_logged_in_visitors[entries["visitor_source"]] = 1

    return non_logged_in_visitors

'''
Additional Feature: Determines whether a visitor is logged in based on the visitor UUID
'''

def visitor_authenticated(visitor_uuid, visitors):

    # Goes through the list of visitors
    for visitor in visitors.keys():
        # If the visitor UUID is found
        if visitor == visitor_uuid:
            for entry in visitors[visitor]:
                # Verifies if the user is logged in by checking if the "visitor_username" is present
                if "visitor_username" in list(entry.keys()):
                    return entry["visitor_username"]
    return False