import tkinter as tk

'''
GUI for the program 
'''

def create_tkinter_gui():
    # Create the main window
    root = tk.Tk()
    root.title("Data Visualization")

    # Set window size and position
    window_width = 700
    window_height = 400
    window_x = (root.winfo_screenwidth() - window_width) // 2  # Center horizontally
    window_y = (root.winfo_screenheight() - window_height) // 2  # Center vertically
    root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

    # Heading
    heading_label = tk.Label(root, text="What would you like to visualise?", font=("Helvetica", 14))
    heading_label.pack(pady=10)

    # Buttons
    button1 = tk.Button(root, text="Country Histogram")
    button1.pack(pady=10)

    button2 = tk.Button(root, text="Continent Histogram")
    button2.pack(pady=10)

    button3 = tk.Button(root, text="Formatted Browser Histogram")
    button3.pack(pady=10)

    # Start the Tkinter event loop
    root.mainloop()

create_tkinter_gui()