# Import necessary libraries and modules
import matplotlib.pyplot as plt
from Functions.cw_requirements import *
from .additional import most_popular_time_documents, most_popular_time_visitors, logged_in_visitors, non_logged_in_visitors, ip_to_location
import graphviz

'''
Plots a histogram for the number of views from each country
'''

def countries_histogram(json_data, doc_uuid):

    # Gets the occurrence of each country using views_country.
    # Ignores the second value returned
    country_count, _ = views_country(json_data, doc_uuid)

    # Extract the country and its counts
    country, count = zip(*country_count.items())

    # Plot the graph
    plt.hist(country, bins=len(country), color='#C3B1E1', weights=count)

    # Set labels and title
    plt.xlabel('Country')
    plt.ylabel('Number of Occurrences')
    plt.title('Country Histogram')
    
    # Adjust layout for better presentation
    plt.tight_layout()

    # Display the plot
    hist_country = plt.show()

    # Return the country histogram
    return hist_country

'''
Plots a bar graph for the number of views from each country
'''

def countries_bar(json_data, doc_uuid):

    # Gets the occurrence of each country using views_country.
    # Ignores the second value returned
    country_count, _ = views_country(json_data, doc_uuid)

    # Extract the country and its counts
    country, count = zip(*country_count.items())

    # Plot the graph
    plt.bar(country, count, color='#C3B1E1')

    # Set labels and title
    plt.xlabel('Country')
    plt.ylabel('Number of Occurrences')
    plt.title('Country Bar Graph')

    # Adjust layout for better presentation
    plt.tight_layout()

    # Show the plot
    bar_country = plt.show()

    # Return the bar graph
    return bar_country

'''
Plots a pie chart for the number of views from each country
'''

def countries_pie(json_data, doc_uuid):

    # Gets the occurrence of each country using views_country.
    # Ignores the second value returned
    country_count, _ = views_country(json_data, doc_uuid)

    # Extract the country and its counts
    country, count = zip(*country_count.items())

    # Plot the pie chart
    plt.pie(count, labels=country, autopct='%1.1f%%', startangle=90, textprops={'rotation': 45})
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Set the title
    plt.title('Country Pie Chart', x=0.05)

    # Show the pie chart
    pie_country = plt.show()

    # Return the pie chart
    return pie_country


'''
Plots a histogram for the number of views from each continent
'''

def continents_histogram(countries):

    # Gets the occurrence of each continent using group_country. 
    continent_count = group_country(countries)

    # Extract the continents and their counts 
    continent, count = zip(*continent_count.items())

    # Plot the graph
    plt.hist(continent, bins=len(continent), color='#FAA0A0', weights=count)

    # Set labels and title
    plt.xlabel('Continent')
    plt.ylabel('Number of Occurrences')
    plt.title('Continent Histogram')

    # Adjust layout for better presentation
    plt.tight_layout()

    # Show the plot
    hist_continent = plt.show()

    # Return the histogram for continents
    return hist_continent

'''
Plots a bar graph for the number of views from each continent
'''

def coontinents_bar(countries):

   # Gets the occurrence of each continent using group_country. 
    continent_count = group_country(countries)

    # Extract the continents and their counts 
    continent, count = zip(*continent_count.items())

    # Plot the graph
    plt.bar(continent, count, color='#FAA0A0')

    # Set labels and title
    plt.xlabel('Continent')
    plt.ylabel('Number of Occurrences')
    plt.title('Continent Bar Graph')

    # Adjust layout for better presentation
    plt.tight_layout()

    # Show the bar graph
    bar_continent = plt.show()

    # Return the bar graph for continents
    return bar_continent

'''
Plots a pie chart for the number of views from each continent
'''

def continent_pie(countries):
    # Gets the occurrence of each continent using group_country. 
    continent_count = group_country(countries)

    # Extract the continents and their counts 
    continent, count = zip(*continent_count.items())

    # Plot the pie chart
    plt.pie(count, labels=continent, autopct='%1.1f%%', startangle=90, textprops={'rotation': 45})

    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Set the title
    plt.title('Continent Pie Chart', x=0.05)

    # Show the pie chart
    continent_pie = plt.show()

    # Return the pie chart for continents
    return continent_pie

'''
Plots a histogram for the number of views from different browsers
'''

def browser_histogram(browser_count):

    # Extract the browsers and their counts 
    browser, count = zip(*browser_count.items())

    # Plot the graph
    plt.hist(browser, bins=len(browser), color='#F8C8DC', weights=count)

    # Set labels and title
    plt.xlabel('Browser')
    plt.xticks(rotation=90)
    plt.ylabel('Number of Occurrences')
    plt.title('Browser Histogram')

    # Show the plot
    hist_browser = plt.show()

    # Return the histogram for browsers
    return hist_browser

'''
Plots a bar graph for the number of views from different browsers
'''

def browser_bar(browser_count):

    # Extract the browsers and their counts 
    browser, count = zip(*browser_count.items())

    # Plot the graph
    plt.bar(browser, count, color='#F8C8DC')

    # Set labels and title
    plt.xlabel('Browser')
    plt.xticks(rotation=90)
    plt.ylabel('Number of Occurrences')
    plt.title('Browser Bar Graph')

    # Show the plot
    bar_browser = plt.show()

    # Return the bar graph for browsers
    return bar_browser


'''
Plots a histogram for the number of views from different browsers (formatted)
'''

def format_browser_histogram(browser_count):

    # Gets the occurrence of each browser using view_browser.
    format_browser_count = format_browser(browser_count)

    # Extract the browsers and their counts 
    formated_browser, count = zip(*format_browser_count.items())

    # Plot the graph
    plt.hist(formated_browser, bins=len(formated_browser), color='#F8C8DC', weights=count)

    # Set labels and title
    plt.xlabel('Formatted Browser')
    plt.xticks(rotation=90)
    plt.ylabel('Number of Occurrences')
    plt.subplots_adjust(bottom=0.483)
    plt.title('Formatted Browser Histogram')

    # Show the plot
    histFormatBrowser = plt.show()

    # Return the histogram for formatted browsers
    return histFormatBrowser

'''
Plots a bar graph for the number of views from different browsers (formatted)
'''

def format_browser_bar(browser_count):

    # Gets the occurrence of each browser using view_browser.
    format_browser_count = format_browser(browser_count)

    # Extract the browsers and their counts 
    formated_browser, count = zip(*format_browser_count.items())

    # Plot the graph
    plt.bar(formated_browser, count, color='#F8C8DC')

    # Set labels and title
    plt.xlabel('Formatted Browser')
    plt.xticks(rotation=90)
    plt.ylabel('Number of Occurrences')
    plt.subplots_adjust(bottom=0.483)
    plt.title('Formatted Browser Bar Graph')
    # plt.tight_layout()

    # Show the plot
    barFormatBrowser = plt.show()

    # Return the bar graph for formatted browsers
    return barFormatBrowser

'''
Plots a pie chart for the number of views from different browsers (formatted)
'''

def format_browser_pie(browser_count):

    # Gets the occurrence of each browser using view_browser.
    format_browser_count = format_browser(browser_count)

    # Extract the browsers and their counts 
    formated_browser, count = zip(*format_browser_count.items())

    # Plot the pie chart
    plt.pie(count, labels=formated_browser, autopct='%1.1f%%', startangle=90, textprops={'rotation': 45})
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Set the title
    plt.title('Formatted Browser Pie Chart', x=0.05)

    # Show the pie chart
    barFormatBrowser = plt.show()

    # Return the pie chart for formatted browsers
    return barFormatBrowser

'''
Plots a bar graph for the top 10 avid readers and their time spent reading the document
'''

def avid_reader_bar(visitors):

    # Extract the readers and their time spent
    reader, count = avid_readers(visitors)

    # Plot the graph
    plt.bar(reader, count, color='#F8C8DC')

    # Set labels and title
    plt.xlabel('Reader')
    plt.xticks(rotation=90)
    plt.ylabel('Time Spent')
    plt.subplots_adjust(bottom=0.483)
    plt.title('Avid Readers Bar Graph')
    # plt.tight_layout()

    # Show the bar graph
    barAvidReader = plt.show()

    # Return the bar graph for avid readers
    return barAvidReader

'''
Function to generate a document overview graph based on popular times
'''

def doc_overview_graph(documents, doc_uuid=None):

    # Get timestamp count for the specified document
    if doc_uuid is not None:
        timestamp_count = most_popular_time_documents(documents, doc_uuid)
    else:
        timestamp_count = most_popular_time_documents(documents, doc_uuid=None)

    # Extract timestamps and their counts, sorted
    timestamps, counts = zip(*sorted(timestamp_count.items()))

    # Plot the graph
    plt.plot(timestamps, counts, marker='o')

    # Set labels and title
    plt.xlabel('Timestamps')
    plt.ylabel('Counts')
    plt.title('Popular Times')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Display the plot
    doc_time = plt.show()

    # Return the document overview graph
    return doc_time

'''
Function to generate a visitor overview graph based on popular times
'''

def visitor_overview_graph(documents, visitor_uuid):

    # Get documents visited by the specified visitor
    visited_documents = visitor_to_doc(documents, visitor_uuid)

    # Get timestamp count for the visited documents
    timestamp_count = most_popular_time_visitors(visited_documents, documents)

    # Extract timestamps and their counts, sorted
    timestamps, counts = zip(*sorted(timestamp_count.items()))

    # Plot the graph
    plt.plot(timestamps, counts, marker='o')

    # Set labels and title
    plt.xlabel('Timestamps')
    plt.ylabel('Counts')
    plt.title('Popular Times')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Display the plot
    vis_time = plt.show()

    # Return the visitor overview graph
    return vis_time

'''
Function to generate a location overview graph based on IP addresses
'''

def ip_to_loc_graph(documents, ip_address=None):

    # Get location count for the specified IP address or all documents
    loc_count = ip_to_location(documents, ip_address=None)

    # Extract locations and their counts
    location, count = zip(*loc_count.items())

    # Plot the pie chart
    plt.pie(count, labels=location, autopct='%1.1f%%', startangle=90, textprops={'rotation': 45})

    # Ensure the pie chart is drawn as a circle
    plt.axis('equal')

    # Set the title
    plt.title('Country Pie Chart', x=0.05)

    # Display the plot
    ipLocPie = plt.show()

    # Return the IP location pie chart
    return ipLocPie


'''
Function to generate a graph of logged-in and non-logged-in visitors
'''

def logged_in_graph(visitors):

    # Get counts of logged-in and non-logged-in visitors
    logged_in = logged_in_visitors(visitors)
    non_logged_in = non_logged_in_visitors(visitors)

    # Combine unique sources from both sets
    sources = list(set(list(logged_in.keys()) + list(non_logged_in.keys())))

    # Get counts for logged-in and non-logged-in visitors
    logged_in_counts = [logged_in.get(source, 0) for source in sources]
    non_logged_in_counts = [non_logged_in.get(source, 0) for source in sources]

    # Set the width of the bars
    bar_width = 0.35
    index = range(len(sources))

    # Capitalize source names for better readability
    sources_capitalized = [source.capitalize() for source in sources]

    # Plot the bar graph for logged-in and non-logged-in visitors
    plt.bar(sources_capitalized, logged_in_counts, bar_width, label='Logged In', color='#1f77b4')
    plt.bar(sources_capitalized, non_logged_in_counts, bar_width, label='Non-Logged In', bottom=logged_in_counts, color='#ff7f0e')

    # Set labels and title
    plt.xlabel('Visitor Source')
    plt.ylabel('Visitor Count')
    plt.title('Visitor Counts by Source')
    
    # Display legend
    plt.legend()

    # Display the bar graph
    log_in_graph = plt.show()

    # Return the logged-in graph
    return log_in_graph

'''
Function to generate a graph showing relationships between documents and visitors who also liked them
'''

def also_likes_graph(documents, doc_uuid, visitor_uuid=None, sorting_func=None):

    # Initialize a Graphviz Digraph
    graph = graphviz.Digraph()
    
    # Determine documents, visitors, and mapping based on input parameters
    if visitor_uuid is None and sorting_func == False:
        al_documents, visitors, mapping = also_likes(documents, doc_uuid, sorting_func=False)
    elif visitor_uuid is None and sorting_func is None:
        al_documents, visitors, mapping = also_likes(documents, doc_uuid, visitor_uuid=None, sorting_func=True)
    elif visitor_uuid is not None and sorting_func == False:
        al_documents, visitors, mapping = also_likes(documents, doc_uuid, visitor_uuid=visitor_uuid, sorting_func=False)
    else:
        al_documents, visitors, mapping = also_likes(documents, doc_uuid, visitor_uuid=visitor_uuid, sorting_func=True)

    # Create subgraph for visitors
    with graph.subgraph() as visitor_subgraph:
        visitor_subgraph.attr(rank='same')
        # Highlight the specified visitor if provided
        if visitor_uuid is not None:
            visitor_subgraph.node(visitor_uuid, label=visitor_uuid[-4:], style='filled', color='#60d394')

        # Add nodes for each visitor
        for visitor in visitors:
            # Highlight the specified visitor if provided
            if visitor_uuid is not None and visitor == visitor_uuid:
                visitor_subgraph.node(visitor, label=visitor[-4:], style='filled', color='#60d394')
            else:
                visitor_subgraph.node(visitor, label=visitor[-4:])

            # Create subgraph for documents
            with graph.subgraph() as doc_subgraph:
                doc_subgraph.attr(rank='same') 

                # Add nodes for each document
                for doc in al_documents:
                    # Highlight the specified document if it is the target document
                    if doc == doc_uuid:
                        doc_subgraph.node('doc', label=doc[-4:], shape='box', style='filled', color='#60d394')
                        # Connect the visitor to the document if there is a like relationship
                        if doc in mapping[visitor]:
                            graph.edge(visitor, 'doc')
                    else:
                        doc_subgraph.node(doc, label=doc[-4:], shape='box')
                        # Connect the visitor to the document if there is a like relationship
                        if doc in mapping[visitor]:
                            graph.edge(visitor, doc)

    # Save the Graphviz graph to a file and view it
    dot_file_path = './also_likes_graph.dot'
    graph.render(dot_file_path, view=True)

    # Return information about documents, visitors, and mapping
    return al_documents, visitors, mapping
