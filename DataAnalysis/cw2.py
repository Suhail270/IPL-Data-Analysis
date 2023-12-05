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
                         most_popular_time_visitors,
                         ip_to_location,
                         logged_in_visitors,
                         non_logged_in_visitors,
                         visitor_authenticated)

from Functions.graphs import (countries_histogram, 
                     continents_histogram, 
                     browser_histogram,
                     format_browser_histogram)

from Functions.gui import startGUI

import pycountry
import pycountry_convert as pc

# file_path = 'DataAnalysis/Dataset/sample_small.json'
# Example usage - python cw2.py -u aaa4eaf77abab0b2 -d 130323125939-5f4318404cda4025a2463c66435ad7c8 -t 6f -f Dataset/sample_small.json
# Example usage - python3.11 cw2.py -u 98ac6a1ca9476771 -d 140222104953-4a9c401847f56cbad2cb7376727cb4fe -t 5c -f Dataset/sample_3m_lines.json

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

        country_count, _ = views_country(json_data, doc_uuid)
        print("\nDocument UUID: {uuid}\n".format(uuid=doc_uuid))

        for i in country_count:
            print("Country - {country} | Number of Views - {count}\n".format(country = pycountry.countries.get(alpha_2=i).name, count = country_count[i]))
        
        countries_histogram(json_data, doc_uuid)

    elif args.task_id == "2b":

        data, countries = views_country(json_data, doc_uuid)
        print("\nDocument UUID: {uuid}\n".format(uuid=doc_uuid))
        
        for i in data:
            print("Continent - {continent} | Number of Views - {count}\n".format(continent = pc.convert_continent_code_to_continent_name((pc.country_alpha2_to_continent_code(i))), count = data[i]))

        continents_histogram(countries)
    
    elif args.task_id == "3a":
        browser_count = view_broswer(json_data)

        print("\nAll Broswers (Unformatted):\n")
        for i in browser_count:
            print("{browser}: {count}".format(browser=i, count=browser_count[i]))
        print()

        browser_histogram(browser_count)
    
    elif args.task_id == "3b":
        browser_count = view_broswer(json_data)
        # Gets the occurence of each browser using view_browser.
        format_browser_count = format_browser(browser_count)
        print("All Broswers (Formatted):\n")
        for i in format_browser_count:
            print("{browser}: {count}".format(browser=i, count=format_browser_count[i]))
        format_browser_histogram(format_browser_count)

    elif args.task_id == "4":
        top_10, values = avid_readers(visitors)
        print("Top 10 avid readers:\n")
        for i in range(len(top_10)):
            print("Reader {num}'s UUID: {uuid}\nReading Time - {time}\n".format(num=i+1, uuid=top_10[i], time=values[i]))

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

        visitor_input = input('''\nWould you like to use the visitor UUID you entered into the terminal as a parameter?
                              
1. Yes
2. No
                              
Enter Option (1 or 2): ''')
        
        while visitor_input not in ['''1''', '''2''']:
            print("\nInvalid input. Please try again.\n")
            visitor_input = input('''Would you like to use the visitor UUID you entered into the terminal as a parameter?
1. Yes
2. No
                              
Enter Option (1 or 2): ''')

        if visitor_input == '''1''':                 
            documents, visitors, mapping = also_likes(documents, doc_uuid, visitor_uuid=visitor_uuid)
        else:
            documents, visitors, mapping = also_likes(documents, doc_uuid)
            
        print("\nReaders of Document UUID: {uuid} have also read:\n".format(uuid=doc_uuid))

        for i in documents:
            if documents[i]>1:
                ending = "s."
            else:
                ending = "."
            
            print("{document}: Read by {count} other reader{suffix}".format(document=i, count=documents[i], suffix=ending))


        print("\n\nVisitors:\n")

        for i in visitors:
            if len(mapping[i]) > 0:
                print("Visitor", i, "read", visitors[i], "other documents including", mapping[i][0] + ".")
            else:
                print("Visitor", i, "has not read any associated documents.")
        print()

    
    elif args.task_id == "5d":

        visitor_input = input('''\nWould you like to use the visitor UUID you entered into the terminal as a parameter?
                              
1. Yes
2. No
                              
Enter Option (1 or 2): ''')
        
        while visitor_input not in ['''1''', '''2''']:
            print("\nInvalid input. Please try again.\n")
            visitor_input = input('''Would you like to use the visitor UUID you entered into the terminal as a parameter?
1. Yes
2. No
                              
Enter Option (1 or 2): ''')

        if visitor_input == '''1''':                 
            visitor_id = visitor_uuid
        else:
            visitor_id = None

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
            sort = False

        elif sort_func == "2":        
            sort = True

        documents, visitors, mapping = also_likes(documents, doc_uuid, visitor_id, sort)
        print("\nReaders of Document UUID: {uuid} have also read:\n".format(uuid=doc_uuid))

        for i in documents:
            if documents[i]>1:
                ending = "s."
            else:
                ending = "."
            
            print("{document}: Read by {count} other reader{suffix}".format(document=i, count=documents[i], suffix=ending))


        print("\n\nVisitors:\n")

        for i in visitors:
            if len(mapping[i]) > 0:
                print("Visitor", i, "read", visitors[i], "other documents including", mapping[i][0] + ".")
            else:
                print("Visitor", i, "has not read any associated documents.")
        print()
    
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
        print("Most Popular Times for visitor {visitor_uuid}:\n".format(visitor_uuid=visitor_uuid))
        for i in list(result.keys()):
            print("{time}: {num} views".format(time=i, num=result[i]))

    elif args.task_id == "6d":
        result = ip_to_location(documents)
        for i in result:
            print(i, result[i])

    elif args.task_id == "6e":

        logged_in_users = logged_in_visitors(visitors)
        non_logged_in_users = non_logged_in_visitors(visitors)

        print("\nTotal Number of Visitors: {count}\n".format(count = len(visitors)))

        print("\nNumber of Logged In Users: {count}\n".format(count = sum(list(logged_in_users.values()))))

        print("Source\t\tCount")

        for i in logged_in_users:
            print(i.capitalize() + "\t" + str(logged_in_users[i]))

        print("\nNumber of Non-Logged In Users: {count}\n".format(count = sum(list(non_logged_in_users.values()))))

        print("Source\t\tCount")

        for i in non_logged_in_users:
            print(i.capitalize() + "\t" + str(non_logged_in_users[i]))

    elif args.task_id == "6f":
        
        result = visitor_authenticated(visitor_uuid, visitors)

        print("\nVisitor UUID: {uuid}\n".format(uuid=visitor_uuid))

        if result is not False:
            print("The visitor is logged in.\nUsername: " + result + "\n")
        
        else:
            print("The visitor is not logged in.\n")


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