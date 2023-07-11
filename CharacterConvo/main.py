from selenium import webdriver
from selenium.webdriver import ActionChains
import time

browser = webdriver.Chrome('D:\Github\CharacterConvo\chromedriver 114.exe')
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


class Conversation:  # this class is the conversation itself
    def __init__(self, search_name):  # name is the name of the character

        print("INITIALIZING " + str(search_name))

        browser.get("https://beta.character.ai/search?")  # open the character.ai search bar
        search_bar = browser.find_element_by_xpath('//input[contains(@id, "search-input")]')
        search_bar.send_keys(search_name)  # search the name of the character
        # attempt to find the character being searched for
        possible_characters = browser.find_elements_by_xpath('//span[contains(@class, "p-0")]')
        for i in possible_characters:  # iterate over possible characters
            if (" " + self.search_name) in possible_characters[i].getText():  # find the exact match
                self.name = str(possible_characters[i].getText().replace('"&nbsp"', ''))  # delete that
                # move to the chat screen
                action = ActionChains(browser)
                action.click(on_element=possible_characters[i])  # click on that character
                action.perform()
                break  # exit loop, we want the first result that matches

        # WE ARE NOW AT THE CHARACTER CHAT PAGE
        print("INITIALIZED " + self.name)


def menu():  # this is just for input
    search_name = str(input("*INPUT THE NAME OF THE CHARACTER YOU WISH TO SPEAK TO: "))
    conversations.append(Conversation(search_name))


menu()
