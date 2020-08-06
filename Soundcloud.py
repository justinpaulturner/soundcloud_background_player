from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from pathlib import Path
import pickle
import time
import subprocess

class Soundcloud:
    
    def __init__(self):
        self.base_url = 'http://www.soundcloud.com/'
        self.current_dir = Path(__file__).parent.absolute()
        self.driver_pkl_file_path = self.current_dir / "driver_path.pkl"
        self.cookies_pkl_file_path = self.current_dir / "cookies.pkl"
        if self.driver_pkl_file_path.exists():
            self.load_driver_path()
        
    def launch_chrome(self, headless = False):
        """Launches a chrome browser."""
        if headless:
            chrome_options = Options()
            chrome_options.add_argument("--no-sandbox") # linux only
            chrome_options.add_argument("--headless")
            self.driver = webdriver.Chrome(self.driver_path, options = chrome_options)
        else:
            self.driver = webdriver.Chrome(self.driver_path)
        
    def find_element(self, x_path):
        """Returns the element if it exists. If it does not exist, it waits 2 seconds and tries again."""
        if self.exists_by_xpath(x_path):
            return self.driver.find_element_by_xpath(x_path)
        else:
            time.sleep(2)
            return self.driver.find_element_by_xpath(x_path)
    
    def find_elements(self, x_path):
        return self.driver.find_elements_by_xpath(x_path)
    
    def exists_by_xpath(self, x_path):
        """Returns bool on if the element given exists"""
        try:
            self.driver.find_element_by_xpath(x_path)
        except NoSuchElementException:
            return False
        return True

    def open(self, url):
        """Goes to the Soundcloud page given."""
        url = self.base_url + url
        self.driver.get(url)

    def get_title(self):
        """Returns the title of the page."""
        return self.driver.title

    def get_url(self):
        """Returns the current URL of the driver."""
        return self.driver.current_url

    def hover(self, x_path):
        element = self.find_element(x_path)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def find_files(self,file_name):
        command = ['locate', file_name]
        output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0]
        output = output.decode()
        self.search_results = output.split('\n')
        return self.search_results

    def save_driver_path(self):
        print("Trying to find the path to your chromedriver. See the list below:")
        try:
            self.find_files('chromedriver')
            for path in self.search_results:
                print(path)
        except:
            print('Search function to find a chromedriver on your system failed. This search only works on linux.')
        self.driver_path = input("What is the path to your chromedriver?\n")
        pickle.dump( self.driver_path , open(self.driver_pkl_file_path,"wb"))
        
    def load_driver_path(self):
        self.driver_path = pickle.load(open(self.driver_pkl_file_path, "rb"))
        
    def load_cookies(self):
        """Loads cookies from the pickle cookies file. Browser needs to exist already"""
        self.open("")
        cookies = pickle.load(open(self.cookies_pkl_file_path, "rb"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.open("")
        
    def save_cookies(self):
        """Saves the current cookies. Use this after you log in for the first time."""
        self.open("")
        pickle.dump( self.driver.get_cookies() , open(self.cookies_pkl_file_path,"wb"))
        
    def open_likes_page(self):
        """Opens the likes page."""
        self.open("you/likes")
        
    def click_on_recent_like(self):
        play_button_x_path = """//*[@id="content"]/div/div/div[2]/div/section/div/div[2]/div/ul/li[1]/div/div[1]/div[1]/a"""
        button = self.find_element(play_button_x_path)
        self.driver.implicitly_wait(2)
        ActionChains(self.driver).move_to_element(button).click(button).perform()
        
    