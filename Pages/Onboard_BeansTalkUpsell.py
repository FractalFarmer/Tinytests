'''
Created on Jan 22, 2023

@author: Shawn Kunkel

This is the Page Object for the BeansTalk Upsell Page.
It contains specific data, locators and methods exclusive to this page.

'''

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class BeansTalkUpsell(BasePage):
    
    """Page Locators ===>"""
    
    SKIP_BUTTON = (By.LINK_TEXT, "Skip")
    START_FREE_TRIAL_BUTTON = (By.LINK_TEXT, "Start Free Trial")
    
    
    """Page Text ===>"""
    
    BEANS_TALK_UPSELL_PAGE_TITLE = "Tinybeans - Where Parents Go"
    BEANS_TALK_UPSELL_HEADER = "Try Tinybeans Beanstalk"
    
    
    """Page Class Constructor ===>"""
    
    def __init__(self, driver):
        super().__init__(driver)
        

    """Page Methods ===>"""
      
    """Click the 'Start Free Trial' button."""  
    def click_start_free_trial_button(self):
        self.do_click(self.START_FREE_TRIAL_BUTTON)
            
    """Click the 'Skip' button."""              
    def click_skip_button(self):
        self.do_click(self.SKIP_BUTTON)