import wget
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Download:

    def __init__(self, web_url):
        self.url = web_url
        ChrOpt = webdriver.ChromeOptions()
        # for external download and save in the specific folder
        ChrOpt.add_experimental_option('prefs',
                                       {
                                           "download.default_directory": "C:\Projects\ProjectSeleniumWork\prog\Try_options",
                                           "plugins.always_open_pdf_externally": True
                                       })
        # to violate error regarding SSL
        ChrOpt.set_capability("acceptInsecureCerts", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=ChrOpt)

    def download_file(self):
        try:
            # get the URL
            self.driver.get(self.url)
            self.driver.maximize_window()
            # create object for the actionchains
            a = ActionChains(self.driver)
            hover1 = self.driver.find_element(By.LINK_TEXT, "Documents")
            # use the move_to_element() to hover
            a.move_to_element(hover1).perform()
            self.driver.find_element(By.XPATH,
                                     "//*[contains(@class,'menu__item is-leaf leaf menu-mlid-5887')]/a").click()
            sleep(2)
            all_link = self.driver.find_elements(By.CSS_SELECTOR, "a[role='link'][title*='Download']")
            num = 0
            for l in all_link:
                l.click()
                sleep(2)
                # use the alert function to handle the alert popup
                alert = Alert(self.driver)
                alert.accept()
                num += 1
                # to control the download count
                if num >= 1:
                    break
            sleep(5)
            hover2 = self.driver.find_element(By.LINK_TEXT, "Media")
            # use the move_to_element() to hover
            a.move_to_element(hover2).perform()
            self.driver.find_element(By.CSS_SELECTOR, "li[class*='menu__item is-leaf leaf menu-mlid-3773']>a").click()
            sleep(2)
            # select the all img elements
            all_img = self.driver.find_elements(By.CSS_SELECTOR, "div.field-content>img")
            # initialize the count
            count = 0
            for i in all_img:
                link = i.get_attribute('src')
                # use the required location to store
                path = "C:\Projects\ProjectSeleniumWork\prog\Img"
                # use wget library for download
                wget.download(link, out=path)
                count += 1
                # use if to control the number of images to download
                if count >= 1:
                    break
            sleep(5)
        except:
            print("An exception occurred")

    def shutdown(self):
        self.driver.close()


url = "https://labour.gov.in/"
d = Download(url)
d.download_file()
d.shutdown()
