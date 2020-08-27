from Soundcloud import Soundcloud
import time

d = Soundcloud()

d.launch_chrome(headless = True)
d.load_cookies()
d.open_likes_page()
d.scroll_to_bottom()
link_list = d.get_liked_tracks_links_list()

for link in link_list:
    d.driver.get(link)
    time.sleep(.25)
    d.click_on("single_track_play")
    while d.track_is_playing():
        print("Waiting while track plays.",end="\r")
        time.sleep(1)