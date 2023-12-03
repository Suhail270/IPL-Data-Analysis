import matplotlib.pyplot as plt
from Functions.cw_requirements import views_country, group_country, format_browser, doc_to_visitor
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

def also_likes_graph(documents, doc_uuid, visitor_uuid=None):

    graph = graphviz.Digraph()

    if visitor_uuid is None:
        graph.node('doc', label=doc_uuid[-4:], shape='box', style='filled', color='#d0f4de')

        visitors = doc_to_visitor(documents, doc_uuid)
        # print(visitors)

        for visitor in visitors:
            # print(visitor)
            graph.node(visitor, label=visitor[-4:])
            graph.edge(visitor, 'doc')

    else:
        graph.node('doc', label=doc_uuid[-4:], shape='box', style='filled', color='#d0f4de')
        
        graph.node('vis', label=visitor_uuid[-4:], style='filled', color='#d0f4de')

        graph.edge('vis', 'doc')

    dot_file_path = './also_likes_graph.dot'
    graph.render(dot_file_path, view=False)


