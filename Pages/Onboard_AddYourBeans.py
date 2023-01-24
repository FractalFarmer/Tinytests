'''
Created on Jan 22, 2023

@author: Shawn Kunkel

This is the Page Object for the Add Your Beans Page.
It contains specific data, locators and methods exclusive to this page.

'''

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class AddYourBeans(BasePage):
    
    """Page Locators ===>"""
    
    SAVE_AND_CONTINUE_BUTTON = (By.LINK_TEXT, "Save and Continue")
    # SKIP_BUTTON = (By.LINK_TEXT, "Skip")
    SKIP_BUTTON = (By.CSS_SELECTOR, ".tny-skip")
    
    """Page Text ===>"""
    
    ADD_YOUR_BEANS_PAGE_TITLE = "Tinybeans - Where Parents Go"
    ADD_YOUR_BEANS_HEADER = "Add your beans"
    
    
    """Page Class Constructor ===>"""
    
    def __init__(self, driver):
        super().__init__(driver)
        

    """Page Methods ===>"""
      
    """Click the 'Save and continue' button."""  
    def click_save_and_continue_button(self):
        self.do_click(self.SAVE_AND_CONTINUE_BUTTON)
            
    """Click the 'Skip' button."""              
    def click_skip_button(self):
        self.do_click(self.SKIP_BUTTON)
        