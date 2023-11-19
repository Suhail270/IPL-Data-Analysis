import argparse

from Functions.cw_requirements import (doc_to_visitor, 
                              also_likes, 
                              views_country, 
                              group_country, 
                              format_browser, 
                              view_broswer, 
                              read_file)

from Functions.additional import (max_unique_visitors, 
                         test_also_likes, 
                         sortingfunc_test, 
                         find_doc)

from Functions.graphs import (countries_histogram, 
                     continents_histogram, 
                     format_browser_histogram)

# file_path = 'DataAnalysis/Dataset/sample_small.json'

def parse_arguments():
    parser = argparse.ArgumentParser(description='Execute different functions based on task id.')
    parser.add_argument('-u', '--user_uuid', required=True, help='User UUID')
    parser.add_argument('-d', '--doc_uuid', required=True, help='Document UUID')
    parser.add_argument('-t', '--task_id', required=True, help='Task ID')
    parser.add_argument('-f', '--file_name', required=True, help='File name')

    return parser.parse_args()

def execute_task(args):
    file_path = args.file_name
    doc_uuid = args.doc_uuid
    user_uuid = args.user_uuid

    print(file_path)
    print(doc_uuid)
    print(user_uuid)
    
    documents, visitors, json_data = read_file(file_path)

    if args.task_id == "2a":
        countries_histogram(json_data, doc_uuid)
        # result = views_country(json_data, args.doc_uuid)
        # print(result)


if __name__ == "__main__":
    args = parse_arguments()
    execute_task(args)

# documents, visitors, json_data = read_file(file_path)
# doc_uuid = "120831070849-697c56ab376445eaadd13dbb8b6d34d0"
# visitors = doc_to_visitor(documents, doc_uuid)

# part2a, countries = views_country(json_data, doc_uuid)

# print(view_broswer(json_data))
# browser_count = view_broswer(json_data)

# print(format_browser_histogram(browser_count))

# country_count, _ = views_country(json_data, doc_uuid)

# print(find_doc(json_data, country_count))

# print(views_country(json_data, doc_uuid))
# print(group_country(countries))

# print(continents_histogram(countries))

# print(countries_histogram(json_data, doc_uuid))

# part2a, countries = views_country(json_data, doc_uuid)
# part2b = group_country(countries)
# part3a = view_broswer(json_data)
# part3b = format_browser(part3a)
# print(part2a)
# print(part2b)
# print(part3a)
# print(part3b)

# doc_uuid, doc_vis_count = max_unique_visitors(documents, visitors)

# doc_uuid = "130323125939-5f4318404cda4025a2463c66435ad7c8"
# also_likes = also_likes(documents, doc_uuid, sorting_func=sortingfunc_test)

# print(also_likes)