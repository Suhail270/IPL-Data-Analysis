import json

file_path = './sample_small.json'

def read_file(file_path):

    documents = {}
    visitors = {}

    try: 
        with open(file_path) as f:   # Read data from the file
            json_data = []

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

def avid_readers(visitors):
    count_dict = {}

    for i in visitors.keys():
        for j in visitors[i]:
            if "event_readtime" in j:
                time = j["event_readtime"]
                if i in count_dict:
                    count_dict[i].append(time)
                else:
                    count_dict[i] = [time]
        # count_dict[i] = sum(count_dict[i]) 

    for i in count_dict.keys():
        count_dict[i] = sum(count_dict[i])
    
    sorted_readers = sorted(count_dict.items(), key=lambda item: item[1], reverse=True)

    return sorted_readers[0:10]



