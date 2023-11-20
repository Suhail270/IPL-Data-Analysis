import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from .cw_requirements import read_file
from .graphs import countries_histogram

'''
GUI for the program 
'''
import tkinter as tk


LARGE_FONT= ("Helvetica", 14)

class DataVisualise(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, CountryPlot, ContinentPlot):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)

        self.show_frame(HomePage)

        # window_width = 0.5
        # window_height = 0.5
        # self.frame.place(rely = window_width, relx = window_height)
        # self.geometry(f"{window_width}x{window_height}+600+100")
        
        # window_width = (self.winfo_screenwidth()) // 1.25
        # window_height = (self.winfo_screenwidth()) // 2.5
        # window_x = (self.winfo_screenwidth()) // 2  # Center horizontally
        # window_y = (self.winfo_screenheight()) // 2  # Center vertically
        # self.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

        # self.frame.place(rely = 0.5, relx = 0.5)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

        
class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent, bg='white')
        label = tk.Label(self, text="What would you like to visualise?", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Countries Histogram",
                            command=lambda: controller.show_frame(CountryPlot))
        button.pack(pady=10)

        button2 = tk.Button(self, text="Continent Histogram",
                            command=lambda: controller.show_frame(ContinentPlot))
        button2.pack(pady=10)


class CountryPlot(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')

        label = tk.Label(self, text="The number of viewers from each country for the document:", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        doc_uuid_label = tk.Label(self, text="Document UUID:")
        doc_uuid_label.pack(pady=5)
        self.doc_uuid_entry = tk.Entry(self, width=50)
        self.doc_uuid_entry.pack(pady=10)

        buttonplot = tk.Button(self, text="Plot Histogram", command=lambda: self.plot_country_histogram(self.doc_uuid_entry.get()))
        buttonplot.pack(pady=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: self.back_to_home(controller))
        button1.pack(pady=10)

        fig, ax = plt.subplots()
        # ax.clear()

        # # Add a canvas to display the plot
        self.canvas = FigureCanvasTkAgg(master=self)
        # # self.canvas.get_tk_widget().config(width=500, height=300)
        self.canvas.get_tk_widget().pack(pady=10, expand=True, fill=tk.BOTH
        )

        ax.clear()


    def back_to_home(self, controller):
        # Show the home page
        controller.show_frame(HomePage)

        # Create a new empty plot on the current axis
        fig, ax = plt.subplots()
        ax.clear()

        # Clear the text box
        self.doc_uuid_entry.delete(0, tk.END)

        # Update the canvas with the new empty plot
        self.canvas.figure = fig
        self.canvas.draw()
    
    def plot_country_histogram(self, doc_uuid):
        # Get documents, visitors, and json_data from the file
        documents, visitors, json_data = read_file(file_path)

        # Plot the country histogram for the specified document UUID
        fig, ax = countries_histogram(json_data, doc_uuid)

        self.canvas.figure = fig
        self.canvas.draw()


class ContinentPlot(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="The number of viewers from each continent for the document:", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(HomePage))
        button1.pack(pady=10)

        # button2 = tk.Button(self, text="Page One",
        #                     command=lambda: controller.show_frame(CountryPlot))
        # button2.pack()
        
def startGUI():
    app = DataVisualise()
    global file_path
    file_path = 'Dataset/sample_small.json'

    # window_width = 700
    # window_height = 500
    # window_x = (app.winfo_screenwidth() - window_width) // 2  # Center horizontally
    # window_y = (app.winfo_screenheight() - window_height) // 2  # Center vertically
    # app.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

    app.mainloop()

