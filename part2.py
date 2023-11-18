import json


file_path = './sample_small.json'

def read_file(file_path):

    documents = {}
    visitors = {}

    try: 
        with open(file_path) as f:   # Read data from the file
            json_data = []
            doc_uuid = "140224195414-e5a9acedd5eb6631bb6b39422fba6798"

            for line in f:
                json_data.append(json.loads(line))

                if "subject_doc_id" in json_data[len(json_data)-1]:
                    doc_uuid = json_data[len(json_data)-1]["subject_doc_id"]

                    content = json_data[len(json_data)-1]

                    if doc_uuid in documents:
                        documents[doc_uuid].append(content)
                    else:
                        documents[doc_uuid] = [content]
                
                
                if "visitor_uuid" in json_data[len(json_data)-1]:
                    visitor_id = json_data[len(json_data)-1]["visitor_uuid"]
                    
                    if visitor_id in visitors:
                        visitors[visitor_id].append(content)
                    else:
                        visitors[visitor_id] = [content]  
        
    except FileNotFoundError:
        print("The file path could not be found")
    
    return documents, visitors


documents, visitors = read_file(file_path)
