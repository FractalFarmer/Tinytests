'''
Created on Jan 22, 2023

@author: Shawn Kunkel

This is the Page Object for the Signup Modal.
It contains specific data, locators and methods exclusive to this page.

'''

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class SignUpModal(BasePage):
    
    """Page Locators ===>"""
    
    CLOSE_BUTTON = (By.CSS_SELECTOR, "#elementor-popup-modal-2108040 .eicon-close")
    
    
    """Page Text ===>"""
    
    SIGNUP_MODAL_HEADER = "FALL FOR TINYBEANS!"
    
    
    """Page Class Constructor ===>"""
    
    def __init__(self, driver):
        super().__init__(driver)
        

    """Page Methods ===>"""

    """Click the 'Go to Tinybeans.com' button."""  
    def click_close_button(self):
        self.do_click(self.CLOSE_BUTTON)
        
    def is_close_button_visible(self):
        return self.is_enabled(self.CLOSE_BUTTON)
    
      
        













