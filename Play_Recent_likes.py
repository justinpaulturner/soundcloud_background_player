from Soundcloud import Soundcloud

d = Soundcloud()

d.launch_chrome(headless = True)
d.load_cookies()
d.open_likes_page()
d.click_on_recent_like()

while True:
    if input("End the program? (Y/N)\n\n") == "Y":
        d.driver.quit()