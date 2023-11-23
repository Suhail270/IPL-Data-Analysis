import matplotlib.pyplot as plt
from Functions.cw_requirements import views_country, group_country, format_browser

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

    fig, ax = plt.subplots()
    # Plot the graph
    plt.hist(country,bins = len(country), color='#C3B1E1', weights=count)

    plt.xlabel('Country')
    plt.ylabel('Number of Occurrences')
    plt.title('Country Histogram')
    plt.tight_layout()

    # plt.show()

    # Return the figure and axis.
    return fig, ax


'''
Plots a histogram for the number of views from each continent
'''

def continents_histogram(countries):

    # Gets the occurence of each continent using group_country. 
    continent_count = group_country(countries)

    # Extract the continents and their counts 
    continent, count = zip(*continent_count.items())

    # Plot the graph
    plt.bar(continent, count, color='#FAA0A0')

    plt.xlabel('Continent')
    plt.ylabel('Number of Occurrences')
    plt.title('Continent Histogram')
    plt.tight_layout()

    # Show the plot
    plt.show()

'''
Plots a histogram for the number of views from different browsers
'''

def browser_histogram(browser_count):

    # Extract the browsers and their counts 
    browser, count = zip(*browser_count.items())

    # Plot the graph
    plt.bar(browser, count, color='#F8C8DC')

    plt.xlabel('Browser')
    plt.ylabel('Number of Occurrences')
    plt.title('Browser Histogram')
    # plt.tight_layout()

    # Show the plot
    plt.show()

'''
Plots a histogram for the number of views from different browsers (formatted)
'''

def format_browser_histogram(browser_count):

    # Gets the occurence of each browser using view_browser.
    format_browser_count = format_browser(browser_count)

    # Extract the browsers and their counts 
    formated_browser, count = zip(*format_browser_count.items())

    # Plot the graph
    plt.bar(formated_browser, count, color='#F8C8DC')

    plt.xlabel('Formatted Browser')
    plt.ylabel('Number of Occurrences')
    plt.title('Formatted Browser Histogram')
    # plt.tight_layout()

    # Show the plot
    plt.show()