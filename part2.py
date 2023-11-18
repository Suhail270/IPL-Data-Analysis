import json

file_path = './sample_small.json'

def read_file(file_path):

    documents = {}
    visitors = {}

    try: 
        with open(file_path) as f:
            json_data = []

            for line in f:
                json_data.append(json.loads(line))

                if "env_doc_id" in json_data[len(json_data)-1]:
                    doc_uuid = json_data[len(json_data)-1]["env_doc_id"]

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

    for i in count_dict.keys():
        count_dict[i] = sum(count_dict[i])
    
    sorted_readers = sorted(count_dict.items(), key=lambda item: item[1], reverse=True)

    return sorted_readers[0:10]

def doc_to_visitor(documents, doc_uuid):
    visitors = []
    for i in documents[doc_uuid]:
        if "visitor_uuid" in i:
            if i["visitor_uuid"] not in visitors:
                visitors.append(i["visitor_uuid"])
    return visitors

def visitor_to_doc(documents, visitior_uuid):
    docs = []
    for i in documents.keys():
        for j in documents[i]:
            if "visitor_uuid" in j:
                if j["visitor_uuid"] == visitior_uuid and j["env_doc_id"] not in docs:
                    docs.append(i)
    return docs

def max_unique_visitors(documents):
    max_visitors_count = 0
    document_with_max_visitors = None

    for doc_uuid in documents:
        visitors = doc_to_visitor(documents, doc_uuid)
        
        unique_visitors_count = len(visitors)

        if unique_visitors_count > max_visitors_count:
            max_visitors_count = unique_visitors_count
            document_with_max_visitors = doc_uuid
    return document_with_max_visitors, max_visitors_count

# def also_likes(documents, doc_uuid):

#     visitor_doc_relationship = {}
#     doc_reader_count = {}

#     visitors = doc_to_visitor(documents, doc_uuid)

#     for visitor in visitors:
#         visitor_doc_relationship[visitor] = visitor_to_doc(documents, visitor)
    
#     # print(visitor_doc_relationship.keys())

#         # for document in i:
#         #     print(document,'\n')

#     # for i in visitor_doc_relationship.values():
#     #     for document in i:
#     #         if document not in list(doc_reader_count.keys()):
#     #             doc_reader_count[document] = 1
#     #         else:
#     #             doc_reader_count[document] += 1    

#     return doc_reader_count

# documents, visitors = read_file(file_path)
doc_uuid, doc_vis_count = max_unique_visitors(documents)
# print(also_likes(documents, doc_uuid))
print(visitor_to_doc(documents, "923f25aa749f67f6"))
