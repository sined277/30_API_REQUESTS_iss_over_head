from tkinter import *
import requests


def get_quote():
    # Make a GET request to the Kanye West quote API
    response = requests.get(url="https://api.kanye.rest")
    # Parse the JSON response into a dictionary
    data = response.json()
    # Update the text in the quote_text canvas item with the quote from the response
    canvas.itemconfig(quote_text, text=data['quote'])


# Create the main window
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# Create a canvas to display the background image and the Kanye quote
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

# Create a button to get a new Kanye quote
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

# Start the main event loop
window.mainloop()
