import matplotlib.pyplot as plt
from Functions.cw_requirements import *
from .additional import most_popular_time_documents, most_popular_time_visitors, logged_in_visitors, non_logged_in_visitors, ip_to_location
import graphviz

'''
Plots a histogram for the number of views from each country
'''

def countries_histogram(json_data, doc_uuid):

    # Gets the occurence of each country using views_country. 
    # Ignores the second value returned
    country_count, _ = views_country(json_data, doc_uuid)

    # Extract the country and its counts 
    country, count = zip(*country_count.items())
    # print(country, count)

    # Plot the graph
    plt.hist(country,bins = len(country), color='#C3B1E1', weights=count)

    plt.xlabel('Country')
    plt.ylabel('Number of Occurrences')
    plt.title('Country Histogram')
    plt.tight_layout()

    hist_country = plt.show()

    # Return the country histogram
    return hist_country


'''
Plots a bar graph for the number of views from each country
'''

def countries_bar(json_data, doc_uuid):

     # Gets the occurence of each country using views_country. 
    # Ignores the second value returned
    country_count, _ = views_country(json_data, doc_uuid)

    # Extract the country and its counts 
    country, count = zip(*country_count.items())

    # Plot the graph
    plt.bar(country, count, color='#C3B1E1')

    plt.xlabel('Country')
    plt.ylabel('Number of Occurrences')
    plt.title('Country Bar Graph')
    plt.tight_layout()

    # Show the plot
    bar_country = plt.show()


    return bar_country

'''
Plots a pie chart for the number of views from each country
'''

def countries_pie(json_data, doc_uuid):

     # Gets the occurence of each country using views_country. 
    # Ignores the second value returned
    country_count, _ = views_country(json_data, doc_uuid)

    # Extract the country and its counts 
    country, count = zip(*country_count.items())

    # Plot the pie chart
    plt.pie(count, labels=country, autopct='%1.1f%%', startangle=90,textprops={'rotation': 45})
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title('Country Pie Chart', x=0.05)

    # Show the plot
    pie_country = plt.show()


    return pie_country



'''
Plots a histogram for the number of views from each continent
'''

def continents_histogram(countries):

    # Gets the occurence of each continent using group_country. 
    continent_count = group_country(countries)

    # Extract the continents and their counts 
    continent, count = zip(*continent_count.items())

    # Plot the graph
    plt.hist(continent,bins = len(continent), color='#FAA0A0', weights=count)

    plt.xlabel('Continent')
    plt.ylabel('Number of Occurrences')
    plt.title('Continent Histogram')
    plt.tight_layout()

    # Show the plot
    hist_continent = plt.show()

    return hist_continent

'''
Plots a bar graph for the number of views from each continent
'''

def coontinents_bar(countries):

   # Gets the occurence of each continent using group_country. 
    continent_count = group_country(countries)

    # Extract the continents and their counts 
    continent, count = zip(*continent_count.items())

    # Plot the graph
    plt.bar(continent, count, color='#FAA0A0')

    plt.xlabel('Continent')
    plt.ylabel('Number of Occurrences')
    plt.title('Continent Bar Graph')
    plt.tight_layout()

    # Show the plot
    bar_continent = plt.show()


    return bar_continent

'''
Plots a pie chart for the number of views from each continent
'''

def continent_pie(countries):
    # Gets the occurence of each continent using group_country. 
    continent_count = group_country(countries)

    # Extract the continents and their counts 
    continent, count = zip(*continent_count.items())

    # Plot the pie chart
    plt.pie(count, labels=continent, autopct='%1.1f%%', startangle=90,textprops={'rotation': 45})
    # colors=['#ff99c8', '#d0f4de', '#a9def9', '#e4c1f9']
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title('Continent Pie Chart', x=0.05)

    # Show the plot
    continent_pie = plt.show()

    return continent_pie

'''
Plots a histogram for the number of views from different browsers
'''

def browser_histogram(browser_count):

    # Extract the browsers and their counts 
    browser, count = zip(*browser_count.items())

    # Plot the graph
    plt.hist(browser,bins = len(browser), color='#F8C8DC', weights=count)

    plt.xlabel('Browser')
    plt.xticks(rotation=90)
    plt.ylabel('Number of Occurrences')
    plt.title('Browser Histogram')
    # plt.tight_layout()

    # Show the plot
    hist_browser = plt.show()

    return hist_browser

'''
Plots a bar graph for the number of views from different browsers
'''

def browser_bar(browser_count):

    # Extract the browsers and their counts 
    browser, count = zip(*browser_count.items())

    # Plot the graph
    plt.bar(browser, count, color='#F8C8DC')

    plt.xlabel('Browser')
    plt.xticks(rotation=90)
    plt.ylabel('Number of Occurrences')
    plt.title('Browser Histogram')
    # plt.tight_layout()

    # Show the plot
    bar_browser = plt.show()

    return bar_browser

'''
Plots a histogram for the number of views from different browsers (formatted)
'''

def format_browser_histogram(browser_count):

    # Gets the occurence of each browser using view_browser.
    format_browser_count = format_browser(browser_count)

    # Extract the browsers and their counts 
    formated_browser, count = zip(*format_browser_count.items())

    # Plot the graph
    plt.hist(formated_browser, bins=len(formated_browser), color='#F8C8DC', weights=count)

    plt.xlabel('Formatted Browser')
    plt.xticks(rotation=90)
    plt.ylabel('Number of Occurrences')
    plt.subplots_adjust(bottom=0.483)
    plt.title('Formatted Browser Histogram')
    # plt.tight_layout()

    # Show the plot
    histFormatBrowser = plt.show()

    return histFormatBrowser

'''
Plots a bar graph for the number of views from different browsers (formatted)
'''

def format_browser_bar(browser_count):

    # Gets the occurence of each browser using view_browser.
    format_browser_count = format_browser(browser_count)

    # Extract the browsers and their counts 
    formated_browser, count = zip(*format_browser_count.items())

    # Plot the graph
    plt.bar(formated_browser, count, color='#F8C8DC')

    plt.xlabel('Formatted Browser')
    plt.xticks(rotation=90)
    plt.ylabel('Number of Occurrences')
    plt.subplots_adjust(bottom=0.483)
    plt.title('Formatted Browser Histogram')
    # plt.tight_layout()

    # Show the plot
    barFormatBrowser = plt.show()

    return barFormatBrowser

'''
Plots a pie chart for the number of views from different browsers (formatted)
'''

def format_browser_pie(browser_count):

    # Gets the occurence of each browser using view_browser.
    format_browser_count = format_browser(browser_count)

    # Extract the browsers and their counts 
    formated_browser, count = zip(*format_browser_count.items())

    # Plot the pie chart
    plt.pie(count, labels=formated_browser, autopct='%1.1f%%', startangle=90,textprops={'rotation': 45})
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title('Country Pie Chart', x=0.05)

    # Show the plot
    barFormatBrowser = plt.show()

    return barFormatBrowser

def doc_overview_graph(documents, doc_uuid=None):

    if doc_uuid is not None:
        timestamp_count = most_popular_time_documents(documents,doc_uuid)
    else:
        timestamp_count = most_popular_time_documents(documents,doc_uuid= None)

    timestamps, counts = zip(*sorted(timestamp_count.items()))

    plt.plot(timestamps, counts, marker='o')
    plt.xlabel('Timestamps')
    plt.ylabel('Counts')
    plt.title('Popular Times')
    plt.xticks(rotation=45)

    doc_time = plt.show()

    return doc_time


def visitor_overview_graph(documents, visitor_uuid):

    visited_documents = visitor_to_doc(documents, visitor_uuid)

    timestamp_count = most_popular_time_visitors(visited_documents, documents)
    
    timestamps, counts = zip(*sorted(timestamp_count.items()))

    plt.plot(timestamps, counts, marker='o')
    plt.xlabel('Timestamps')
    plt.ylabel('Counts')
    plt.title('Popular Times')
    plt.xticks(rotation=45)

    vis_time = plt.show()

    return vis_time

def ip_to_loc_graph(documents, ip_address=None):

    loc_count = ip_to_location(documents,ip_address=None)

    location, count = zip(*loc_count.items())

    # Plot the pie chart
    plt.pie(count, labels=location, autopct='%1.1f%%', startangle=90,textprops={'rotation': 45})
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title('Country Pie Chart', x=0.05)

    # Show the plot
    ipLocPie = plt.show()

    return ipLocPie


def logged_in_graph(visitors):

    logged_in = logged_in_visitors(visitors)
    non_logged_in = non_logged_in_visitors(visitors)


    sources = list(set(list(logged_in.keys()) + list(non_logged_in.keys())))  # Convert set to list

    logged_in_counts = [logged_in.get(source, 0) for source in sources]
    non_logged_in_counts = [non_logged_in.get(source, 0) for source in sources]

    bar_width = 0.35
    index = range(len(sources))

    sources_capitalized = [source.capitalize() for source in sources]

    plt.bar(sources_capitalized, logged_in_counts, bar_width, label='Logged In', color='#1f77b4')
    plt.bar(sources_capitalized, non_logged_in_counts, bar_width, label='Non-Logged In', bottom=logged_in_counts, color='#ff7f0e')

    plt.xlabel('Visitor Source')
    plt.ylabel('Visitor Count')
    plt.title('Visitor Counts by Source')
    plt.legend()

    log_in_graph = plt.show()

    return log_in_graph


def also_likes_graph(documents, doc_uuid, visitor_uuid=None):

    graph = graphviz.Digraph()

    # if visitor_uuid is not None:
    #     graph.node(visitor_uuid, label=visitor_uuid[-4:], style='filled', color='#d0f4de')

    if visitor_uuid is None:
        documents, visitors, mapping = also_likes(documents, doc_uuid,visitor_uuid=None, sorting_func=2)
    else:
        documents, visitors, mapping = also_likes(documents, doc_uuid,visitor_uuid, sorting_func=2)

    if visitor_uuid is not None:
         graph.node(visitor_uuid, label=visitor_uuid[-4:], style='filled', color='#60d394')

    for visitor in visitors:
        if visitor_uuid is not None and visitor == visitor_uuid:
            graph.node(visitor, label=visitor[-4:], style='filled', color='#60d394')
        else:
            graph.node(visitor, label=visitor[-4:])

        for doc in mapping[visitor]:
            if doc == doc_uuid:
                graph.node('doc', label=doc[-4:], shape='box', style='filled', color='#60d394')
                graph.edge(visitor, 'doc')
            else:
                graph.node(doc, label=doc[-4:], shape='box')
                graph.edge(visitor, doc)
           


    dot_file_path = './also_likes_graph.dot'
    graph.render(dot_file_path, view=True)


    # visitors = doc_to_visitor(documents, doc_uuid)
    # # print(visitors)

    # if visitor_uuid is not None:
    #     graph.node(visitor_uuid, label=visitor_uuid[-4:], style='filled', color='#d0f4de')

    # for visitor in visitors:
    #     # print(visitor)
    #     graph.node(visitor, label=visitor[-4:])
    #     graph.edge(visitor, 'doc')

    #     docs = visitor_to_doc(documents, visitor)
    #     print("Visitor: " + visitor + " - Docs Visited: ", docs)

    #     for doc in docs:

    #         if(doc != doc_uuid):
    #             # print(doc)
    #             graph.node(doc, label=doc[-4:], shape='box')

    #             graph.edge(visitor, doc)

    
# ===================================================

# count = 0

#     for doc in also_like_func:
#         if count == 10:
#             break
#         readers = list(also_like_func[doc].keys())
#         if doc == doc_uuid:
#             graph.node(doc, label=doc[-4:], shape='box', style='filled', color='#d0f4de')
#         else:
#             graph.node(doc, label=doc[-4:], shape='box')
#         for reader in readers:
#             if visitor_uuid is not None and visitor_uuid == reader:
#                 graph.node(visitor_uuid, label=visitor_uuid[-4:], style='filled', color='#d0f4de')
#             graph.node(reader, label=reader[-4:])
#             graph.edge(reader, doc)

#         count += 1

