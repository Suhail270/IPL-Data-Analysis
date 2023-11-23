import matplotlib.pyplot as plt
from part2 import views_country, group_country, format_browser

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
    # print(continent, count)

    # Plot the graph
    plt.hist(continent,bins = len(continent), color='#FAA0A0', weights=count)

    plt.xlabel('Continent')
    plt.ylabel('Number of Occurrences')
    plt.title('Continent Histogram')
    plt.tight_layout()

    # Show the plot
    plt.show()

'''
Plots a histogram for the number of views from different browsers
'''

def format_browser_histogram(browser_count):

    # Gets the occurence of each browser using view_browser.
    format_browser_count = format_browser(browser_count)

    # Extract the browsers and their counts 
    formated_browser, count = zip(*format_browser_count.items())

    # Plot the graph
    plt.hist(formated_browser,bins = len(formated_browser), color='#F8C8DC', weights=count)

    plt.xlabel('Formatted Browser')
    plt.ylabel('Number of Occurrences')
    plt.title('Formatted Browser Histogram')
    # plt.tight_layout()

    # Show the plot
    plt.show()

# documents, visitors, json_data = read_file(file_path)
# doc_uuid = "140224101516-e5c074c3404177518bab9d7a65fb578e"

# part2a, countries = views_country(json_data, doc_uuid)

# browser_count = view_broswer(json_data)

# format_browser_histogram(browser_count)