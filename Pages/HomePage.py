'''
Created on Jan 22, 2023

@author: Shawn Kunkel

This is the Page Object for the Home Page.
It contains specific data, locators and methods exclusive to this page.

'''

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class HomePage(BasePage):
    
    """Page Locators ===>"""
    
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".outside > .feather") # this is the orange search icon
    START_TRIAL_BUTTON = (By.LINK_TEXT, "Start a Trial")
    
    SEARCH_INPUT_TEXTFIELD = (By.CSS_SELECTOR, "#search-form #search-input")

    TINYBEANS_LOGO = (By.XPATH, "/html/body/div[1]/footer/div[1]/div[1]/div/a")
    
    
    """Page Text ===>"""
    
    HOME_PAGE_TITLE = "Tinybeans - Where Parents Go"
    
    
    """Page Class Constructor ===>"""
        
    def __init__(self, driver):
        super().__init__(driver)
        
    
    """Page Methods ===>"""
    
    """Sends text to the Search field"""
    def enter_search_text(self, text):
        self.do_send_keys(self.SEARCH_INPUT_TEXTFIELD, text)
        
    """Clicks on the orange 'magnifying glass' search icon"""     
    def click_search_button(self):
        self.do_click(self.SEARCH_BUTTON)
        
    """Clicks the 'Start a Trial' button"""    
    def click_start_a_trial_button(self):
        self.do_click(self.START_TRIAL_BUTTON)
    
    """Clicks on the Tinybeans logo found near the bottom of the page"""
    def click_tinybeans_logo(self):
        self.do_click(self.TINYBEANS_LOGO)


    