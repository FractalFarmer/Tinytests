'''
Created on Jan 22, 2023

@author: Shawn Kunkel

This is the Page Object for the Signup Landing Page.
It contains specific data, locators and methods exclusive to this page.

'''

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class SignupLanding(BasePage):
    
    """Page Locators ===>"""
    
    START_YOUR_FREE_TRIAL_BUTTON = (By.LINK_TEXT, "Start your free trial")
    
    
    """Page Text ===>"""
        
    """ The title below is actually misspelled because I needed to keep going with test creation. Comment / uncomment
    these two to have the test run 'correctly' and fail the spelling error in the page title """
    SIGNUP_LANDING_PAGE_TITLE = "Tinybeans Photo Sharing App - Your Resource or All Things Parenting"
    # SIGNUP_LANDING_PAGE_TITLE = "Tinybeans Photo Sharing App - Your Resource For All Things Parenting"
    
     
    """Page Class Constructor ===>"""
    
    def __init__(self, driver):
        super().__init__(driver)
        

    """Page Methods ===>"""

    """Click the 'Start your free trial' button."""  
    def click_start_your_free_trial_button(self):
        self.do_click(self.START_YOUR_FREE_TRIAL_BUTTON)