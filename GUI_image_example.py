import tkinter as tk
# Install pillow & request module. See: https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html#install-package
from PIL import ImageTk, Image
import requests
from io import BytesIO

root = tk.Tk()


img_url = "http://i.annihil.us/u/prod/marvel/i/mg/3/40/4bb4680432f73/portrait_incredible.jpg"  # Comes from the Marvel API
response = requests.get(img_url)
img_data = response.content
img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))


panel = tk.Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")
root.mainloop()
