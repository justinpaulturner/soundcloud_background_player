from Soundcloud import Soundcloud

d = Soundcloud()

d.launch_chrome(headless = True)
d.load_cookies()
d.open_likes_page()
d.click_on('play')
d.click_on('repeat')
d.click_on('repeat')


while True:
    if input("I hope you like the tunes.\nCOMMANDS: play, pause, next, back, shuffle.\n") == "next":
        d.click_on("next")
    elif input("I hope you like the tunes.\nCOMMANDS: play, pause, next, back, shuffle.\n") == "back":
        d.click_on("back")
        d.click_on("back")
    elif input("I hope you like the tunes.\nCOMMANDS: play, pause, next, back, shuffle.\n") == "shuffle":
        d.click_on("shuffle")
    elif input("I hope you like the tunes.\nCOMMANDS: play, pause, next, back, shuffle.\n") == "pause":
        d.click_on("play")
    elif input("I hope you like the tunes.\nCOMMANDS: play, pause, next, back, shuffle.\n") == "play":
        d.click_on("play")