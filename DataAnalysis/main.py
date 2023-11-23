import argparse
import sys

from Functions.cw_requirements import (doc_to_visitor, 
                              also_likes, 
                              views_country, 
                              group_country, 
                              format_browser, 
                              view_broswer, 
                              read_file,
                              visitor_to_doc,
                              avid_readers)

from Functions.additional import (max_unique_visitors, 
                         also_likes_testing, 
                         sortingfunc_test, 
                         find_doc,
                         validation,
                         most_popular_time_documents,
                         most_popular_time_visitors)

from Functions.graphs import (countries_histogram, 
                     continents_histogram, 
                     browser_histogram,
                     format_browser_histogram)

from Functions.gui import startGUI

# file_path = 'DataAnalysis/Dataset/sample_small.json'
# Example usage - python main.py -u aaa4eaf77abab0b2 -d 130323125939-5f4318404cda4025a2463c66435ad7c8 -t 6a -f Dataset/sample_small.json

'''
Defines the syntax for passing command line arguments. Failure to adhering to this syntax will raise an exception.
'''

def parse_arguments():
    parser = argparse.ArgumentParser(description='Execute different functions based on task id.')
    parser.add_argument('-u', '--user_uuid', help='User UUID')
    parser.add_argument('-d', '--doc_uuid', help='Document UUID')
    parser.add_argument('-t', '--task_id', help='Task ID')
    parser.add_argument('-f', '--file_name', help='File name')

    args = parser.parse_args()

     # Check if either all or none of the arguments are provided
    all_arguments_present = all(vars(args).values())
    none_of_the_arguments_present = not any(vars(args).values())

    if not (all_arguments_present or none_of_the_arguments_present):
        parser.error('''\n\nIf you would like to start the GUI, enter no arguments. Your terminal command should be:
python main.py.
      
If you would like to execute a function, please enter all arguments. Your terminal command should be:
python main.py -u <user_uuid> -d <doc_uuid> -t <task_id> -f <file_name>.\n\n''')

    return args

'''
Executes function based on the task id passed.
'''

def execute_task(args):
    file_path = args.file_name
    doc_uuid = args.doc_uuid
    visitor_uuid = args.user_uuid
    
    documents, visitors, json_data = read_file(file_path)

    valid = validation(doc_uuid=doc_uuid, documents=documents, visitor_uuid=visitor_uuid, visitors=visitors)

    if valid == False:
        sys.exit(1)

    if args.task_id == "2a":
        countries_histogram(json_data, doc_uuid)

    elif args.task_id == "2b":
        _ , countries = views_country(json_data, doc_uuid)
        continents_histogram(countries)
    
    elif args.task_id == "3a":
        browser_count = view_broswer(json_data)
        browser_histogram(browser_count)
    
    elif args.task_id == "3b":
        browser_count = view_broswer(json_data)
        format_browser_histogram(browser_count)

    elif args.task_id == "4":
        top_10 = avid_readers(visitors)
        print("Top 10 avid readers:\n")
        for i in range(len(top_10)):
            print("Reader {num}'s UUID: {uuid}".format(num=i+1, uuid=top_10[i]))

    elif args.task_id == "5a":
        visitor_ids = doc_to_visitor(documents, doc_uuid)
        print("Document UUID: {uuid}".format(uuid=doc_uuid))
        print("Number of Visitors: {num}\n".format(num=len(visitor_ids)))
        for i in range(len(visitor_ids)):
            print("Visitor {num}'s UUID: {uuid}".format(num=i+1, uuid=visitor_ids[i]))
        
    elif args.task_id == "5b":
        document_ids = visitor_to_doc(documents, visitor_uuid)
        print("Visitor UUID: {uuid}".format(uuid=visitor_uuid))
        print("Number of Documents Read: {num}\n".format(num=len(document_ids)))
        for i in range(len(document_ids)):
            print("Document {num}'s UUID: {uuid}".format(num=i+1, uuid=document_ids[i]))
    
    elif args.task_id == "5c":
        print("Document UUID: {uuid}".format(uuid=doc_uuid))
        also_like_func = also_likes(documents, doc_uuid)
        print("Readers of Document UUID: {uuid} have also read:\n".format(uuid=doc_uuid))
        for i in also_like_func:
            print(i)
    
    elif args.task_id == "5d":

        sort_func = input('''\nWhat sorting function would you like to use?
                            
1. Documents displayed in ascending order based on the number of readers
2. Documents displayed in descending order based on the number of readers
                            
Enter Option (1 or 2): ''')
        while sort_func not in ["1", "2"]:

            print("\nInvalid input. Please try again.\n")

            sort_func = input('''What sorting function would you like to use?
                            
1. Documents displayed in ascending order based on the number of readers
2. Documents displayed in descending order based on the number of readers
                            
Enter Option (1 or 2): ''')
            
        if sort_func == "1":
            sorting_text = "Ascending Order"

        elif sort_func == "2":        
            sorting_text = "Descending Order"

        also_like_func = also_likes(documents, doc_uuid, None, sort_func)
        print("Document UUID: {uuid}".format(uuid=doc_uuid))
        print("Readers of Document UUID: {uuid} have also read:\n".format(uuid=doc_uuid))

        for i in also_like_func:
            print("{document} - Read by {num} other readers".format(document=i, num=also_like_func[i]))
            
        print("\nSorting Function: {sort}".format(sort=sorting_text))
    
    elif args.task_id == "6a":
        result = most_popular_time_documents(documents)
        print("Most Popular Times:\n")
        for i in list(result.keys()):
            print("{time}: {num} views".format(time=i, num=result[i]))

    elif args.task_id == "6b":
        result = most_popular_time_documents(documents, doc_uuid)
        print("Most Popular Times for document {doc_uuid}:\n".format(doc_uuid=doc_uuid))
        for i in list(result.keys()):
            print("{time}: {num} views".format(time=i, num=result[i]))

    elif args.task_id == "6c":
        documents_visited = visitor_to_doc(documents, visitor_uuid)
        result = most_popular_time_visitors(documents_visited, documents)
        print(result)
        print("Most Popular Times for visitor {visitor_uuid}:\n".format(visitor_uuid=visitor_uuid))
        for i in list(result.keys()):
            print("{time}: {num} views".format(time=i, num=result[i]))

if __name__ == "__main__":
    
    try:
        # If no command line arguments are passed, the GUI is invoked.
        args = parse_arguments()

        if not any(vars(args).values()):
            print("Starting GUI...")
            startGUI()
        else:
            execute_task(args)
    
    except Exception as e:
        print(e)
        sys.exit(1)