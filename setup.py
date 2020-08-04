# This is the setup file. Run this once before running the Play_Rwecent_Likes file
from Soundcloud import Soundcloud
import pickle

d = Soundcloud()
d.save_driver_path()
d.launch_chrome()
d.open("")
input("Please log in via Facebook or another o-auth method. Signing in via email does not work.\nPress any button when logged in.")
d.save_cookies()
print("Setup complete. You can now run the Play_Recent_Likes.py file.")
