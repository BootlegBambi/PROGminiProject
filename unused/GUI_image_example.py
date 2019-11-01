import tkinter as tk
# Install pillow & request module. See: https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html#install-package
from PIL import ImageTk, Image
import requests
from io import BytesIO

root = tk.Tk()

# Image url's loaded from get_image_url function.
img_url = "http://i.annihil.us/u/prod/marvel/i/mg/3/40/4bb4680432f73/portrait_incredible.jpg"  # Comes from the Marvel API
# img_url = "http://i.pinimg.com/originals/24/92/00/249200c431fe811110761709b303fcaf.jpg"  # Image not available url
response = requests.get(img_url)
img_data = response.content
img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))  # Needs fixed width and height to work with image not available


panel = tk.Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")
root.mainloop()
