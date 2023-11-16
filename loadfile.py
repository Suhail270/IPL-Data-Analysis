import json
from collections import Counter

'''
json_data = json file
document_uuid = user entered unique id
'''
def views_by_country(json_data, document_uuid): 
    # Filter data for the specified document UUID
    filtered_data = [entry for entry in json_data if entry.get("subject_doc_id") == document_uuid]

    # Extract country information
    countries = [entry["visitor_country"] for entry in filtered_data]

    # Count occurrences of each country
    country_counts = Counter(countries)

    return country_counts


def readfile():
        file_path = './sample_smakl.json'

        try: 
            # Read data from the file
            with open(file_path) as f:
                json_data = [json.loads(line) for line in f]
        except FileNotFoundError:
             print("The file path could not be found")
        except json.JSONDecodeError as e:
             print("Error decoding JSON: {e}")
        # Specify the document UUID for analysis
        document_uuid = "140206010823-b14c9d966be950314215c17923a04af7"

        # Analyze views by country for the specified document UUID
        result = views_by_country(json_data, document_uuid)

    
        print(result)
readfile()
