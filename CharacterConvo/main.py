from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
options = webdriver.ChromeOptions()
service = ChromeService(executable_path="D:\Github\CharacterConvo\chromedriverMOD.exe")
browser = uc.Chrome(service=service, options=options)

# browser.get("https://www.google.com/imghp?hl=EN")
# search_bar = browser.find_element_by_xpath(search_bar_xpath)
# search_bar.send_keys(words[i])  # input the word
# search_bar.send_keys(u'\ue007')  # press enter
# time.sleep(1)  # wait a bit for the page to load
# grab_image(i)  # download the first image found that meets requirements
# browser.close
# searched_images = browser.find_elements_by_xpath('//img[contains(@src,"data:image")]')
# found_images[num_selector].get_attribute('width')
# browser.find_element_by_xpath('//img[contains(@jsaction, "load:XAeZkd;")]')
conversations = []


wait = WebDriverWait(browser, 120)


def delay():
    time.sleep(5)


class Conversation:  # this class is the conversation itself
    def __init__(self, search_name):  # name is the name of the character
        self.search_name = str(search_name)
        print("*INITIALIZING " + str(search_name))

        browser.get("https://beta.character.ai/search?")  # open the character.ai search bar

        # there may be popups, eliminate them
        wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@tabindex, "-1")]')))
        delay()
        # Find the SVG element within the modal dialog
        popup = browser.find_element(By.XPATH, '//svg[contains(@stroke, "currentColor")]')
        print(popup)
        action = ActionChains(browser)
        action.move_to_element_with_offset(popup, 5, 5)
        action.click()  # X the popup
        action.perform()

        wait.until(EC.presence_of_element_located((By.XPATH, '//input[contains(@id, "search-input")]')))
        search_bar = browser.find_element(By.XPATH, '//input[contains(@id, "search-input")]')
        search_bar.send_keys(self.search_name)  # search the name of the character
        search_bar.send_keys(u'\ue007')  # press enter

        # attempt to find the character being searched for
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[contains(@class, "p-0")]')))
        possible_characters = browser.find_elements(By.XPATH, '//span[contains(@class, "p-0")]')
        for char in possible_characters:  # iterate over possible characters
            print(char.text)
            if (" " + self.search_name) in " " + str(char.text):  # find the exact match
                self.name = str(char.text.replace('"&nbsp"', ''))  # delete that
                # move to the chat screen
                action = ActionChains(browser)
                action.click(on_element=char)  # click on that character
                action.perform()
                break  # exit loop, we want the first result that matches

        # WE ARE NOW AT THE CHARACTER CHAT PAGE
        delay()
        print("*INITIALIZED " + self.name)


def menu():  # this is just for input
    search_name = str(input(">INPUT THE NAME OF THE CHARACTER YOU WISH TO SPEAK TO: "))
    conversations.append(Conversation(search_name))
    time.sleep(100)


menu()
