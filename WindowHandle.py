from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By


class WinHandle:

    def __init__(self, url):
        self.web_url = url
        # install driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def window_switch(self):
        try:
            # get url
            self.driver.get(self.web_url)
            # maximize window
            self.driver.maximize_window()
            sleep(3)
            # capture the primary window
            primary_window = self.driver.current_window_handle
            self.driver.find_element(By.XPATH, "//a[@class='dropdwnbtn accessibility-plugin-ac newMenu' and @href='/faq']").click()
            sleep(2)
            self.driver.find_element(By.XPATH, "//a[@class='dropdwnbtn accessibility-plugin-ac newMenu' and @href='/our-partner']").click()
            sleep(2)
            window = self.driver.window_handles
            for w in window:
                # switch to the other window and find them using URL
                self.driver.switch_to.window(w)
                if self.driver.current_url == "https://www.cowin.gov.in/faq":
                    # print the current page in the console
                    print(self.driver.current_url)
                    self.driver.close()
                    sleep(2)
                elif self.driver.current_url == 'https://www.cowin.gov.in/our-partner':
                    # print the current page in the console
                    print(self.driver.current_url)
                    self.driver.close()
                    sleep(2)
            # return back to the primary window
            self.driver.switch_to.window(primary_window)
            sleep(5)
        except:
            print("An exception occurred")

    def shutdown(self):
        self.driver.close()


url = "https://www.cowin.gov.in/"
# pass the url
wh = WinHandle(url)
# call the methods
wh.window_switch()
wh.shutdown()

