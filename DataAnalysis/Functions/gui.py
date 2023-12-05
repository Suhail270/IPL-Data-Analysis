import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from .cw_requirements import read_file, view_broswer, views_country
from .graphs import *
from tkinter import filedialog
from tkinter import ttk 

'''
GUI for the program 
'''
import tkinter as tk


LARGE_FONT= ("Helvetica", 14)

class DataVisualise(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, CountryPlot, ContinentPlot, BrowserPlot, FormatBrowserPlot, AlsoLikes, VisitorOverview, LogInView, DocOverview, UserLoc):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)

        self.show_frame(HomePage)

        window_width = 700
        window_height = 500
        window_x = (self.winfo_screenwidth() - window_width) // 2
        window_y = (self.winfo_screenheight() - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

# class FilePage(tk.Frame):

#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self,parent)
#         label = tk.Label(self, text="Enter the file path for the dataset", font=LARGE_FONT)
#         label.pack(pady=10,padx=10)

#         file_path_label = tk.Label(self, text="File Path:")
#         file_path_label.pack(pady=5)
#         self.file_path_entry = tk.Entry(self, width=50)
#         self.file_path_entry.pack(pady=10)

#         button2 = tk.Button(self, text="Next ->",
#                             command=lambda: controller.show_frame(HomePage))
#         button2.pack(pady=10)

#         def get_file_path(self):
#             return self.file_path_entry.get()
        
class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="What would you like to visualize?", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Countries Plots",
                            command=lambda: controller.show_frame(CountryPlot))
        button.pack(pady=10)

        button2 = tk.Button(self, text="Continent Plots",
                            command=lambda: controller.show_frame(ContinentPlot))
        button2.pack(pady=10)

        button4 = tk.Button(self, text="Browser Plots",
                            command=lambda: controller.show_frame(BrowserPlot))
        button4.pack(pady=10)

        button3 = tk.Button(self, text="Formatted Browser Plots",
                            command=lambda: controller.show_frame(FormatBrowserPlot))
        button3.pack(pady=10)

        button5 = tk.Button(self, text="Also Likes Graph",
                            command=lambda: controller.show_frame(AlsoLikes))
        button5.pack(pady=10)

        button7 = tk.Button(self, text="Document Overview",
                            command=lambda: controller.show_frame(DocOverview))
        button7.pack(pady=10)

        button5 = tk.Button(self, text="Visitor Overview",
                            command=lambda: controller.show_frame(VisitorOverview))
        button5.pack(pady=10)

        button8 = tk.Button(self, text="User Location",
                            command=lambda: controller.show_frame(UserLoc))
        button8.pack(pady=10)


        button6 = tk.Button(self, text="Logged In Users",
                            command=lambda: controller.show_frame(LogInView))
        button6.pack(pady=10)



class CountryPlot(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="The number of viewers from each country for the document:", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        doc_uuid_label = tk.Label(self, text="Document UUID:")
        doc_uuid_label.pack(pady=5)
        self.doc_uuid_entry = tk.Entry(self, width=50)
        self.doc_uuid_entry.pack(pady=10)

        buttonplot = tk.Button(self, text="Plot Histogram", command=lambda: self.plot_country_histogram(self.doc_uuid_entry.get()))
        buttonplot.pack(pady=10)

        buttonbar = tk.Button(self, text="Plot Bar Graph", command=lambda: self.plot_country_bar(self.doc_uuid_entry.get()))
        buttonbar.pack(pady=10)

        buttonpie = tk.Button(self, text="Plot Pie Chart", command=lambda: self.plot_country_pie(self.doc_uuid_entry.get()))
        buttonpie.pack(pady=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: self.back_to_home(controller))
        button1.pack(pady=10)

    def back_to_home(self, controller):
        # Show the home page
        controller.show_frame(HomePage)

        # Clear the text box
        self.doc_uuid_entry.delete(0, tk.END)
    
    def plot_country_histogram(self, doc_uuid):
        # Get documents, visitors, and json_data from the file
        documents, visitors, json_data = read_file(file_path)

        # Plot the country histogram for the specified document UUID
        countries_histogram(json_data, doc_uuid)

    def plot_country_bar(self, doc_uuid):
        documents, visitors, json_data = read_file(file_path)
        countries_bar(json_data, doc_uuid)

    def plot_country_pie(self, doc_uuid):
        documents, visitors, json_data = read_file(file_path)
        countries_pie(json_data, doc_uuid)

        # self.canvas.figure = fig
        # self.canvas.draw()


class ContinentPlot(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="The number of viewers from each continent for the document:", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        doc_uuid_label = tk.Label(self, text="Document UUID:")
        doc_uuid_label.pack(pady=5)
        self.doc_uuid_entry = tk.Entry(self, width=50)
        self.doc_uuid_entry.pack(pady=10)

        buttonplot = tk.Button(self, text="Plot Histogram", command=lambda: self.plot_continent_histogram(self.doc_uuid_entry.get()))
        buttonplot.pack(pady=10)

        buttonbar = tk.Button(self, text="Plot Bar Graph", command=lambda: self.plot_continent_bar(self.doc_uuid_entry.get()))
        buttonbar.pack(pady=10)

        buttonpie = tk.Button(self, text="Plot Pie Chart", command=lambda: self.plot_continent_pie(self.doc_uuid_entry.get()))
        buttonpie.pack(pady=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: self.back_to_home(controller))
        button1.pack(pady=10)

    def plot_continent_histogram(self, doc_uuid):
        documents, visitors, json_data = read_file(file_path)
        _, countries = views_country(json_data, doc_uuid)
        continents_histogram(countries)

    def plot_continent_bar(self, doc_uuid):
        documents, visitors, json_data = read_file(file_path)
        _, countries = views_country(json_data, doc_uuid)
        coontinents_bar(countries)

    def plot_continent_pie(self, doc_uuid):
        documents, visitors, json_data = read_file(file_path)
        _, countries = views_country(json_data, doc_uuid)
        continent_pie(countries)

    def back_to_home(self, controller):
        # Show the home page
        controller.show_frame(HomePage)
        # Clear the text box
        self.doc_uuid_entry.delete(0, tk.END)

class BrowserPlot(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="The browsers used to access the documents:", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        buttonplot = tk.Button(self, text="Plot Histogram", command=lambda: self.plot_browser())
        buttonplot.pack(pady=10)

        buttonbar = tk.Button(self, text="Plot Bar Graph", command=lambda: self.plot_browser_bar())
        buttonbar.pack(pady=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(HomePage))
        button1.pack(pady=10)

    def plot_browser(self):
        documents, visitors, json_data = read_file(file_path)

        browser_count = view_broswer(json_data)
        
        browser_histogram(browser_count)

    def plot_browser_bar(self):
        documents, visitors, json_data = read_file(file_path)

        browser_count = view_broswer(json_data)
        
        browser_bar(browser_count)


class FormatBrowserPlot(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="The various browsers used to access the documents:", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        buttonplot = tk.Button(self, text="Plot Histogram", command=lambda: self.plot_format_browser())
        buttonplot.pack(pady=10)

        buttonbar = tk.Button(self, text="Plot Bar Graph", command=lambda: self.plot_format_browser_bar())
        buttonbar.pack(pady=10)

        buttonpie = tk.Button(self, text="Plot Pie Chart", command=lambda: self.plot_format_browser_pie())
        buttonpie.pack(pady=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(HomePage))
        button1.pack(pady=10)

    def plot_format_browser(self):
        documents, visitors, json_data = read_file(file_path)
        browser_count = view_broswer(json_data)
        format_browser_histogram(browser_count)


    def plot_format_browser_bar(self):
        documents, visitors, json_data = read_file(file_path)
        browser_count = view_broswer(json_data)
        format_browser_bar(browser_count)

    def plot_format_browser_pie(self):
        documents, visitors, json_data = read_file(file_path)
        browser_count = view_broswer(json_data)
        format_browser_pie(browser_count)

class AlsoLikes(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Also Likes Graph", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

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

        buttonplot = tk.Button(self, text="Also Likes Graph", command=lambda: self.plot_also_likes(self.doc_uuid_entry.get(), self.vis_uuid_entry.get(), self.dropdown_var.get()))
        buttonplot.pack(pady=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: self.back_to_home(controller))
        button1.pack(pady=10)

    def plot_also_likes(self, doc_uuid, vis_uuid=None, sort_func=None):
        documents, visitors, json_data = read_file(file_path)

        if vis_uuid is None or vis_uuid == '':
            if sort_func == "None":
                also_likes_graph(documents, doc_uuid)
            elif sort_func == "Ascending":
                also_likes_graph(documents, doc_uuid, sorting_func=1)
            else:
                also_likes_graph(documents, doc_uuid, sorting_func=2)
        else:
            if sort_func == "None":
                also_likes_graph(documents, doc_uuid, vis_uuid)
            elif sort_func == "Ascending":
                also_likes_graph(documents, doc_uuid, vis_uuid, sorting_func=1)
            else:
                also_likes_graph(documents, doc_uuid, vis_uuid, sorting_func=2)
            

    def back_to_home(self, controller):
        # Show the home page
        controller.show_frame(HomePage)
        # Clear the text box
        self.doc_uuid_entry.delete(0, tk.END)
        self.vis_uuid_entry.delete(0, tk.END)

class VisitorOverview(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Most Popular for a visitor to view documents", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        vis_uuid_label = tk.Label(self, text="Visitor UUID:")
        vis_uuid_label.pack(pady=5)
        self.vis_uuid_entry = tk.Entry(self, width=50)
        self.vis_uuid_entry.pack(pady=10)

        buttonplot = tk.Button(self, text="Plot", command=lambda: self.plot_vis_time(self.vis_uuid_entry.get()))
        buttonplot.pack(pady=10)  

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: self.back_to_home(controller))
        button1.pack(pady=10) 

    def back_to_home(self, controller):
        # Show the home page
        controller.show_frame(HomePage)
        # Clear the text box
        self.vis_uuid_entry.delete(0, tk.END) 

    def plot_vis_time(self, vis_uuid):
        documents, visitors, json_data = read_file(file_path)
        visitor_overview_graph(documents, vis_uuid)

class UserLoc(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Location of User", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        buttonplot = tk.Button(self, text="Plot", command=lambda: self.plot_location())
        buttonplot.pack(pady=10)    

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(HomePage))
        button1.pack(pady=10)

    def plot_location(self):
        documents, visitors, json_data = read_file(file_path)
        ip_to_loc_graph(documents)

class LogInView(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Logged in and Logged Out Users", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        buttonplot = tk.Button(self, text="Plot", command=lambda: self.plot_log_in())
        buttonplot.pack(pady=10)    

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(HomePage))
        button1.pack(pady=10)

    def plot_log_in(self):
        documents, visitors, json_data = read_file(file_path)
        logged_in_graph(visitors)

class DocOverview(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Most Popular for a visitor to view documents", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        doc_uuid_label = tk.Label(self, text="Document UUID: (Optional)")
        doc_uuid_label.pack(pady=5)
        self.doc_uuid_entry = tk.Entry(self, width=50)
        self.doc_uuid_entry.pack(pady=10)

        buttonplot = tk.Button(self, text="Plot", command=lambda: self.plot_doc_time(self.doc_uuid_entry.get()))
        buttonplot.pack(pady=10)  

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: self.back_to_home(controller))
        button1.pack(pady=10) 

    def back_to_home(self, controller):
        # Show the home page
        controller.show_frame(HomePage)
        # Clear the text box
        self.vis_uuid_entry.delete(0, tk.END) 

    def plot_doc_time(self, doc_uuid):
        documents, visitors, json_data = read_file(file_path)
        if doc_uuid is None or doc_uuid == '':
            doc_overview_graph(documents)
        else:
            doc_overview_graph(documents, doc_uuid)

def get_file_path():
    file_path = filedialog.askopenfilename(title="Select a JSON file", filetypes=[("JSON files", "*.json")])
    return file_path
        
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

