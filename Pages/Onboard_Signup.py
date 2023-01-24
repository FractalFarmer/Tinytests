'''
Created on Jan 22, 2023

@author: Shawn Kunkel

This is the Page Object for the Signup Page.
It contains specific data, locators and methods exclusive to this page.

'''

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class Signup(BasePage):
    
    """Page Locators ===>"""
    
    USER_FIRST_NAME_INPUT_TEXTFIELD = (By.ID, "firstname")
    USER_LAST_NAME_INPUT_TEXTFIELD = (By.ID, "lastname")
    USER_EMAIL_INPUT_TEXTFIELD = (By.ID, "emailAddress")
    
    CONTINUE_WITH_EMAIL_BUTTON = (By.ID, "loginButton")
    
    
    """Page Text ===>"""
    
    SIGNUP_PAGE_TITLE = "Sign-Up - Tinybeans"
    
    
    """Page Class Constructor ===>"""
    
    def __init__(self, driver):
        super().__init__(driver)
        

    """Page Methods ===>"""
      
    """Sends a text value to the first name text field"""
    def enter_first_name(self, text):
        self.do_send_keys(self.USER_FIRST_NAME_INPUT_TEXTFIELD, text)
        
    """Sends a text value to the last name text field"""
    def enter_last_name(self, text):
        self.do_send_keys(self.USER_LAST_NAME_INPUT_TEXTFIELD, text)
        
    """Sends a text value to the email text field"""
    def enter_email(self, text):
        self.do_send_keys(self.USER_EMAIL_INPUT_TEXTFIELD, text)
        
    """Clicks the 'Continue With Email' button"""    
    def click_continue_with_email_button(self):
        self.do_click(self.CONTINUE_WITH_EMAIL_BUTTON)        
        
