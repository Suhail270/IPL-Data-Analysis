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

def test_also_likes(documents, doc_reader_count):
    # Iterate through each document UUID in the documents dictionary
    for i in documents.keys():
        # Get the result of the also_likes function for the current document UUID
        # Check if the result has more than one document (indicating readership overlap)
        if len(list(doc_reader_count.keys())) > 1:
            # Print the document UUID and the result
            print(i, doc_reader_count)

'''
Additional Feature: Sorts dictionaries in descending order based on the values.
'''

def sortingfunc_test(doc_reader_count, reverse):

    if type(doc_reader_count) is dict:
        # Sort the document-reader count dictionary based on the count
        return dict(sorted(doc_reader_count.items(), key=lambda item: item[1], reverse=reverse))
    else:
        # Sort the list of tuples based on the count
        return sorted(doc_reader_count.items(), key=lambda item: item[1], reverse=reverse)
    
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
            print("\nInvalid document UUID. Please try again.\n")
            valid = False
    
    # Check if the visitor UUID is valid
    if visitor_uuid is not None and visitors is not None:
        if visitor_uuid not in visitors:
            print("\nInvalid visitor UUID. Please try again.\n")
            valid = False
    
    return valid
