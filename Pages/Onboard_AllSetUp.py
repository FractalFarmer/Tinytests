'''
Created on Jan 22, 2023

@author: Shawn Kunkel

This is the Page Object for the All Set Up Page.
It contains specific data, locators and methods exclusive to this page.

'''

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class AllSetUp(BasePage):
    
    """Page Locators ===>"""
    
    GO_TO_TINYBEANS_BUTTON = (By.LINK_TEXT, "Go to Tinybeans.com")
    
    
    """Page Text ===>"""
    
    ALL_SET_UP_PAGE_TITLE = "Tinybeans - Where Parents Go"
    ALL_SET_UP_HEADER = "Your account is all setup!"
    
    
    """Page Class Constructor ===>"""
    
    def __init__(self, driver):
        super().__init__(driver)
        

    """Page Methods ===>"""

    """Click the 'Go to Tinybeans.com' button."""  
    def click_go_to_tinybeans_button(self):
        self.do_click(self.GO_TO_TINYBEANS_BUTTON)