# Import necessary modules for the GUI
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from .cw_requirements import read_file, view_broswer, views_country
from .additional import logged_in_visitors, non_logged_in_visitors, visitor_authenticated
from .graphs import *
from tkinter import filedialog
from tkinter import ttk 

'''
GUI for the program 
'''
# Define a class for the main application window
import tkinter as tk

# Set a large font for labels
LARGE_FONT = ("Helvetica", 14)

# Create the main application class inheriting from tk.Tk
class DataVisualise(tk.Tk):

    # Initialize the application
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        # Pack the container to fill both X and Y directions
        container.pack(side="top", fill="both", expand=True)

        # Configure the grid in the container
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Initialize a dictionary to store frames
        self.frames = {}

        # Define frames for different pages
        for F in (HomePage, CountryPlot, ContinentPlot, BrowserPlot, FormatBrowserPlot, AvidReaderPlot, AlsoLikes, VisitorOverview, LogInView, DocOverview, UserLoc, LogInAuthenticate):

            frame = F(container, self)

            self.frames[F] = frame

            # Set the frame to occupy the entire grid
            frame.grid(row=0, column=0, sticky="nsew")

            # Configure the grid in the frame
            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)

        # Show the home page initially
        self.show_frame(HomePage)

        # Set the initial size and position of the window
        window_width = 550
        window_height = 600
        window_x = (self.winfo_screenwidth() - window_width) // 2
        window_y = (self.winfo_screenheight() - window_height) // 4
        self.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

        # Set the title of the window
        self.title("Group 26 - Coursework 2")

    # Function to show a specific frame
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

# Define the home page frame
class HomePage(tk.Frame):

    # Initialize the home page
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="What would you like to visualize?", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Create buttons for different visualizations, each calling a specific frame
        button = tk.Button(self, text="2a - Countries Plots", command=lambda: controller.show_frame(CountryPlot))
        button.pack(pady=10)

        button2 = tk.Button(self, text="2b - Continent Plots", command=lambda: controller.show_frame(ContinentPlot))
        button2.pack(pady=10)

        button4 = tk.Button(self, text="3a - Browser Plots", command=lambda: controller.show_frame(BrowserPlot))
        button4.pack(pady=10)

        button3 = tk.Button(self, text="3b - Formatted Browser Plots", command=lambda: controller.show_frame(FormatBrowserPlot))
        button3.pack(pady=10)

        button9 = tk.Button(self, text="4 - Avid Readers", command=lambda: controller.show_frame(AvidReaderPlot))
        button9.pack(pady=10)

        button5 = tk.Button(self, text="5 & 6 - Also Likes Graph", command=lambda: controller.show_frame(AlsoLikes))
        button5.pack(pady=10)

        button7 = tk.Button(self, text="Document Overview [ADDITIONAL 1]", command=lambda: controller.show_frame(DocOverview))
        button7.pack(pady=10)

        button5 = tk.Button(self, text="Visitor Overview [ADDITIONAL 2]", command=lambda: controller.show_frame(VisitorOverview))
        button5.pack(pady=10)

        button8 = tk.Button(self, text="User Location [ADDITIONAL 3]", command=lambda: controller.show_frame(UserLoc))
        button8.pack(pady=10)

        button6 = tk.Button(self, text="Logged In vs Non-Logged In [ADDITIONAL 4]", command=lambda: controller.show_frame(LogInView))
        button6.pack(pady=10)

        button10 = tk.Button(self, text="User Authentication [ADDITIONAL 5]", command=lambda: controller.show_frame(LogInAuthenticate))
        button10.pack(pady=10)


# Define a class for plotting country-related visualizations
class CountryPlot(tk.Frame):

    # Initialize the frame
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create labels and entry for document UUID
        label = tk.Label(self, text="The number of viewers from each country for the document:", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        doc_uuid_label = tk.Label(self, text="Document UUID:")
        doc_uuid_label.pack(pady=5)
        self.doc_uuid_entry = tk.Entry(self, width=50)
        self.doc_uuid_entry.pack(pady=10)

        # Create buttons for plotting different visualizations
        buttonplot = tk.Button(self, text="Plot Histogram", command=lambda: self.plot_country_histogram(self.doc_uuid_entry.get()))
        buttonplot.pack(pady=10)

        buttonbar = tk.Button(self, text="Plot Bar Graph", command=lambda: self.plot_country_bar(self.doc_uuid_entry.get()))
        buttonbar.pack(pady=10)

        buttonpie = tk.Button(self, text="Plot Pie Chart", command=lambda: self.plot_country_pie(self.doc_uuid_entry.get()))
        buttonpie.pack(pady=10)

        button1 = tk.Button(self, text="Back to Home", command=lambda: self.back_to_home(controller))
        button1.pack(pady=10)

    # Function to go back to the home page
    def back_to_home(self, controller):
        # Show the home page
        controller.show_frame(HomePage)

        # Clear the text box
        self.doc_uuid_entry.delete(0, tk.END)
    
    # Function to plot country histogram
    def plot_country_histogram(self, doc_uuid):
        # Get documents, visitors, and json_data from the file
        documents, visitors, json_data = read_file(file_path)

        # Plot the country histogram for the specified document UUID
        countries_histogram(json_data, doc_uuid)

    # Function to plot country bar graph
    def plot_country_bar(self, doc_uuid):
        documents, visitors, json_data = read_file(file_path)
        countries_bar(json_data, doc_uuid)

    # Function to plot country pie chart
    def plot_country_pie(self, doc_uuid):
        documents, visitors, json_data = read_file(file_path)
        countries_pie(json_data, doc_uuid)

# Define a class for plotting continent-related visualizations
class ContinentPlot(tk.Frame):

    # Initialize the frame
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="The number of viewers from each continent for the document:", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Create labels and entry for document UUID
        doc_uuid_label = tk.Label(self, text="Document UUID:")
        doc_uuid_label.pack(pady=5)
        self.doc_uuid_entry = tk.Entry(self, width=50)
        self.doc_uuid_entry.pack(pady=10)

        # Create buttons for plotting different visualizations
        buttonplot = tk.Button(self, text="Plot Histogram", command=lambda: self.plot_continent_histogram(self.doc_uuid_entry.get()))
        buttonplot.pack(pady=10)

        buttonbar = tk.Button(self, text="Plot Bar Graph", command=lambda: self.plot_continent_bar(self.doc_uuid_entry.get()))
        buttonbar.pack(pady=10)

        buttonpie = tk.Button(self, text="Plot Pie Chart", command=lambda: self.plot_continent_pie(self.doc_uuid_entry.get()))
        buttonpie.pack(pady=10)

        button1 = tk.Button(self, text="Back to Home", command=lambda: self.back_to_home(controller))
        button1.pack(pady=10)

    # Function to plot continent histogram
    def plot_continent_histogram(self, doc_uuid):
        documents, visitors, json_data = read_file(file_path)
        _, countries = views_country(json_data, doc_uuid)
        continents_histogram(countries)

    # Function to plot continent bar graph
    def plot_continent_bar(self, doc_uuid):
        documents, visitors, json_data = read_file(file_path)
        _, countries = views_country(json_data, doc_uuid)
        coontinents_bar(countries)

    # Function to plot continent pie chart
    def plot_continent_pie(self, doc_uuid):
        documents, visitors, json_data = read_file(file_path)
        _, countries = views_country(json_data, doc_uuid)
        continent_pie(countries)

    # Function to go back to the home page
    def back_to_home(self, controller):
        # Show the home page
        controller.show_frame(HomePage)
        # Clear the text box
        self.doc_uuid_entry.delete(0, tk.END)

# Define a class for plotting browser-related visualizations
class BrowserPlot(tk.Frame):

    # Initialize the frame
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="The browsers used to access the documents:", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Create buttons for plotting different visualizations
        buttonplot = tk.Button(self, text="Plot Histogram", command=lambda: self.plot_browser())
        buttonplot.pack(pady=10)

        buttonbar = tk.Button(self, text="Plot Bar Graph", command=lambda: self.plot_browser_bar())
        buttonbar.pack(pady=10)

        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button1.pack(pady=10)

    # Function to plot browser histogram
    def plot_browser(self):
        documents, visitors, json_data = read_file(file_path)
        browser_count = view_broswer(json_data)
        browser_histogram(browser_count)

    # Function to plot browser bar graph
    def plot_browser_bar(self):
        documents, visitors, json_data = read_file(file_path)
        browser_count = view_broswer(json_data)
        browser_bar(browser_count)


# Define a class for plotting formatted browser-related visualizations
class FormatBrowserPlot(tk.Frame):

    # Initialize the frame
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="The various browsers used to access the documents:", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Create buttons for plotting different visualizations
        buttonplot = tk.Button(self, text="Plot Histogram", command=lambda: self.plot_format_browser())
        buttonplot.pack(pady=10)

        buttonbar = tk.Button(self, text="Plot Bar Graph", command=lambda: self.plot_format_browser_bar())
        buttonbar.pack(pady=10)

        buttonpie = tk.Button(self, text="Plot Pie Chart", command=lambda: self.plot_format_browser_pie())
        buttonpie.pack(pady=10)

        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button1.pack(pady=10)

    # Function to plot formatted browser histogram
    def plot_format_browser(self):
        documents, visitors, json_data = read_file(file_path)
        browser_count = view_broswer(json_data)
        format_browser_histogram(browser_count)

    # Function to plot formatted browser bar graph
    def plot_format_browser_bar(self):
        documents, visitors, json_data = read_file(file_path)
        browser_count = view_broswer(json_data)
        format_browser_bar(browser_count)

    # Function to plot formatted browser pie chart
    def plot_format_browser_pie(self):
        documents, visitors, json_data = read_file(file_path)
        browser_count = view_broswer(json_data)
        format_browser_pie(browser_count)

# Define a class for plotting avid reader-related visualizations
class AvidReaderPlot(tk.Frame):

    # Initialize the frame
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="The top 10 avid readers of a document", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Label to display result
        self.result_label = tk.Label(self, text="", font=("Helvetica", 11))
        self.result_label.pack(pady=10)

        # Create a button to plot avid reader bar graph
        buttonplot = tk.Button(self, text="Plot Bar Graph", command=lambda: self.plot_avid_reader())
        buttonplot.pack(pady=10)

        # Create a button to go back to the home page
        button1 = tk.Button(self, text="Back to Home", command=lambda: self.back_to_home(controller))
        button1.pack(pady=10)

    # Function to plot avid reader bar graph and display the top 10 avid readers
    def plot_avid_reader(self):
        documents, visitors, json_data = read_file(file_path)

        # Get the top 10 avid readers and their reading times
        top_10, values = avid_readers(visitors)
        result_text = "Top 10 avid readers:\n\n"
        
        # Format and display the result
        for i in range(len(top_10)):
            result_text += "\nReader {num}'s UUID: {uuid}\nReading Time - {time}\n".format(num=i+1, uuid=top_10[i], time=values[i])

        self.result_label.config(text=result_text)

        # Plot the avid reader bar graph
        avid_reader_bar(visitors)

    # Function to go back to the home page and clear the text box and result label
    def back_to_home(self, controller):
        # Show the home page
        controller.show_frame(HomePage)
        
        # Reset the result text and update the label
        self.result_text = ""
        self.result_label.config(text=self.result_text)


# Define a class for the "Also Likes" visualization
class AlsoLikes(tk.Frame):

    # Initialize the frame
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Set up labels, entry fields, and dropdown menu
        label = tk.Label(self, text="Also Likes Graph", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        doc_uuid_label = tk.Label(self, text="Document UUID:")
        doc_uuid_label.pack(pady=5)
        self.doc_uuid_entry = tk.Entry(self, width=50)
        self.doc_uuid_entry.pack(pady=10)

        vis_uuid_label = tk.Label(self, text="Visitor UUID: (Optional)")
        vis_uuid_label.pack(pady=5)
        self.vis_uuid_entry = tk.Entry(self, width=50)
        self.vis_uuid_entry.pack(pady=10)

        # Create a StringVar to store the selected option
        self.dropdown_var = tk.StringVar(self)
        self.dropdown_var.set("None")  # Set the default value to None

        # Create a label and dropdown menu
        label = tk.Label(self, text="Sort Order: (Optional)")
        label.pack(pady=10)

        dropdown_menu = ttk.Combobox(self, textvariable=self.dropdown_var, values=["None", "Ascending", "Descending"])
        dropdown_menu.pack(pady=10)

        # Label to display the result
        self.result_label = tk.Label(self, text="", font=("Helvetica", 10))
        self.result_label.pack(pady=10)

        # Create buttons to trigger the visualization and return to the home page
        buttonplot = tk.Button(self, text="Also Likes Graph", command=lambda: self.invoke_also_likes(controller))
        buttonplot.pack(pady=10)

        button1 = tk.Button(self, text="Back to Home", command=lambda: self.back_to_home(controller))
        button1.pack(pady=10)

    # Function to plot the "Also Likes" graph based on user input
    def plot_also_likes(self, doc_uuid, vis_uuid=None, sort_func=None):
        documents, visitors, json_data = read_file(file_path)
        
        # Determine the sorting function and whether a visitor UUID is provided
        if vis_uuid is None or vis_uuid == '':
            if sort_func == "None":
                al_documents, visitors, mapping = also_likes_graph(documents, doc_uuid)
            elif sort_func == "Ascending":
                al_documents, visitors, mapping = also_likes_graph(documents, doc_uuid, visitor_uuid=None, sorting_func=False)
            else:
                al_documents, visitors, mapping = also_likes_graph(documents, doc_uuid, visitor_uuid=None, sorting_func=True)
        else:
            if sort_func == "None":
                al_documents, visitors, mapping =  also_likes_graph(documents, doc_uuid, visitor_uuid=vis_uuid, sorting_func=True)
            elif sort_func == "Ascending":
                al_documents, visitors, mapping = also_likes_graph(documents, doc_uuid, vis_uuid, sorting_func=False)
            else:
                al_documents, visitors, mapping = also_likes_graph(documents, doc_uuid, vis_uuid, sorting_func=True)
        
        # Format and display the result
        result_text = "\nReaders of Document UUID: {uuid} have also read:\n\n".format(uuid=doc_uuid)
        for i in al_documents:
            if al_documents[i]>1:
                ending = "s."
            else:
                ending = "."

            result_text += "{document} - Read by {count} other reader{suffix}\n".format(document=i, count=al_documents[i], suffix=ending)
        
        result_text += "\n\nVisitors:\n\n"

        for i in visitors:
            if len(mapping[i]) > 0:
                result_text += "Visitor {vis_id} read {count} other documents including {eg_doc}.\n".format(vis_id = i, count = visitors[i], eg_doc = mapping[i][0])
            else:
                result_text += "Visitor {vis_id} has not read any associated documents.\n".format(vis_id = i)
                
        result_text += ""

        # Update the label with the result
        self.result_label.config(text=result_text)

    # Function to go back to the home page and clear the input fields and result label
    def back_to_home(self, controller):
        # Show the home page
        controller.show_frame(HomePage)
        
        # Clear the text boxes
        self.doc_uuid_entry.delete(0, tk.END)
        self.vis_uuid_entry.delete(0, tk.END)
        
        # Reset the result text and update the label
        self.result_text = ""
        self.result_label.config(text=self.result_text)

    # Function to trigger the "Also Likes" visualization based on user input
    def invoke_also_likes(self, controller):
        doc_uuid, visitor_uuid, sort = self.doc_uuid_entry.get(), self.vis_uuid_entry.get(), self.dropdown_var.get()
        self.plot_also_likes(doc_uuid, visitor_uuid, sort)

# Define a class for the "Visitor Overview" visualization
class VisitorOverview(tk.Frame):

    # Initialize the frame
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Set up labels and entry field
        label = tk.Label(self, text="Most Popular for a visitor to view documents", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        vis_uuid_label = tk.Label(self, text="Visitor UUID:")
        vis_uuid_label.pack(pady=5)
        self.vis_uuid_entry = tk.Entry(self, width=50)
        self.vis_uuid_entry.pack(pady=10)

        # Create a button to trigger the visualization and return to the home page
        buttonplot = tk.Button(self, text="Plot", command=lambda: self.plot_vis_time(self.vis_uuid_entry.get()))
        buttonplot.pack(pady=10)  

        button1 = tk.Button(self, text="Back to Home", command=lambda: self.back_to_home(controller))
        button1.pack(pady=10) 

    # Function to go back to the home page and clear the input field
    def back_to_home(self, controller):
        # Show the home page
        controller.show_frame(HomePage)
        # Clear the text box
        self.vis_uuid_entry.delete(0, tk.END) 

    # Function to trigger the "Visitor Overview" visualization based on user input
    def plot_vis_time(self, vis_uuid):
        documents, visitors, json_data = read_file(file_path)
        visitor_overview_graph(documents, vis_uuid)


# Define a class for the "User Location" visualization
class UserLoc(tk.Frame):

    # Initialize the frame
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Set up label and button
        label = tk.Label(self, text="Location of User", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        buttonplot = tk.Button(self, text="Plot", command=lambda: self.plot_location())
        buttonplot.pack(pady=10)    

        # Create a button to return to the home page
        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button1.pack(pady=10)

    # Function to trigger the "User Location" visualization
    def plot_location(self):
        documents, visitors, json_data = read_file(file_path)
        ip_to_loc_graph(documents)

# Define a class for the "Log In View" visualization
class LogInView(tk.Frame):

    # Initialize the frame
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Set up label and button
        label = tk.Label(self, text="Logged in and Logged Out Users", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        buttonplot = tk.Button(self, text="Plot", command=lambda: self.plot_log_in())
        buttonplot.pack(pady=10)

        # Create a label to display the result
        self.result_label = tk.Label(self, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

        # Create a button to return to the home page
        button1 = tk.Button(self, text="Back to Home", command=lambda: self.back_to_home(controller))
        button1.pack(pady=10)

    # Function to trigger the "Log In View" visualization
    def plot_log_in(self):
        documents, visitors, json_data = read_file(file_path)

        # Get counts of logged in and non-logged in users
        logged_in_users = logged_in_visitors(visitors)
        non_logged_in_users = non_logged_in_visitors(visitors)

        # Prepare the result text
        result_text = "\nTotal Number of Visitors: {count}\n".format(count=len(visitors))
        result_text += "\n\nNumber of Logged In Users: {count}\n".format(count=sum(list(logged_in_users.values())))

        result_text += "\n  Source\t\tCount"

        for i in logged_in_users:
            result_text += "\n" + i.capitalize() + "  \t\t" + str(logged_in_users[i])

        result_text += "\n\nNumber of Non-Logged In Users: {count}\n".format(count=sum(list(non_logged_in_users.values())))
        result_text += "\n Source\t\tCount"

        for i in non_logged_in_users:
            result_text += "\n" + i.capitalize() + "\t\t" + str(non_logged_in_users[i])

        # Update the label with the result
        self.result_label.config(text=result_text)

        # Trigger the bar graph visualization
        logged_in_graph(visitors)
    
    # Function to go back to the home page and clear the result label
    def back_to_home(self, controller):
        # Show the home page
        controller.show_frame(HomePage)
        # Clear the text box
        self.result_text = ""
        self.result_label.config(text=self.result_text)


# Define a class for the "Document Overview" visualization
class DocOverview(tk.Frame):

    # Initialize the frame
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Set up label, entry field, and button
        label = tk.Label(self, text="Most Popular for a visitor to view documents", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        doc_uuid_label = tk.Label(self, text="Document UUID: (Optional)")
        doc_uuid_label.pack(pady=5)
        self.doc_uuid_entry = tk.Entry(self, width=50)
        self.doc_uuid_entry.pack(pady=10)

        buttonplot = tk.Button(self, text="Plot", command=lambda: self.plot_doc_time(self.doc_uuid_entry.get()))
        buttonplot.pack(pady=10)  

        button1 = tk.Button(self, text="Back to Home", command=lambda: self.back_to_home(controller))
        button1.pack(pady=10) 

    # Function to go back to the home page and clear the input field
    def back_to_home(self, controller):
        # Show the home page
        controller.show_frame(HomePage)
        # Clear the text box
        self.doc_uuid_entry.delete(0, tk.END) 

    # Function to trigger the "Document Overview" visualization based on user input
    def plot_doc_time(self, doc_uuid):
        documents, visitors, json_data = read_file(file_path)
        if doc_uuid is None or doc_uuid == '':
            doc_overview_graph(documents)
        else:
            doc_overview_graph(documents, doc_uuid)

# Define a class for the "Log In Authenticate" frame
class LogInAuthenticate(tk.Frame):

    # Initialize the frame
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Set up label, entry fields, and buttons
        label = tk.Label(self, text="Check if the visitor is logged in or not", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        vis_uuid_label = tk.Label(self, text="Visitor UUID:")
        vis_uuid_label.pack(pady=5)
        self.vis_uuid_entry = tk.Entry(self, width=50)
        self.vis_uuid_entry.pack(pady=10)

        # Create a label to display the result
        self.result_label = tk.Label(self, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

        # Create a button to check the visitor's log-in status
        buttonplot = tk.Button(self, text="Check Visitor", command=lambda: self.user_check(self.vis_uuid_entry.get()))
        buttonplot.pack(pady=10)

        # Create a button to return to the home page
        button1 = tk.Button(self, text="Back to Home", command=lambda: self.back_to_home(controller))
        button1.pack(pady=10) 

    # Function to check the log-in status of the visitor
    def user_check(self, visitor_uuid):
        documents, visitors, json_data = read_file(file_path)

        # Get the result of visitor authentication
        result = visitor_authenticated(visitor_uuid, visitors)

        # Prepare the result text
        result_text = "\nVisitor UUID: {uuid}\n".format(uuid=visitor_uuid)

        if result is not False:
            result_text += "The visitor is logged in.\n\nUsername: " + result + "\n"
        else:
            result_text += "\nThe visitor is not logged in.\n"

        # Update the label with the result
        self.result_label.config(text=result_text)

    # Function to go back to the home page and clear the input field
    def back_to_home(self, controller):
        # Show the home page
        controller.show_frame(HomePage)
        # Clear the text box
        self.vis_uuid_entry.delete(0, tk.END) 
        # Clear the result label
        self.result_text = ""
        self.result_label.config(text=self.result_text)


# Function to get the file path from the user
def get_file_path():
    file_path = filedialog.askopenfilename(title="Select a JSON file", filetypes=[("JSON files", "*.json")])
    return file_path

# Function to start the GUI
def startGUI():
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window

    global file_path
    file_path = get_file_path()
    
    if not file_path:
        # User canceled the file selection
        return

    app = DataVisualise()
    app.mainloop()


