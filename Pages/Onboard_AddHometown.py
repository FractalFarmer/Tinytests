'''
Created on Jan 22, 2023

@author: Shawn Kunkel

This is the Page Object for the Add Hometown Page.
It contains specific data, locators and methods exclusive to this page.

'''

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class AddHometown(BasePage):
    
    """Page Locators ===>"""
    
    HOMETOWN_INPUT_TEXTFIELD = (By.ID, "hometown")
    
    SAVE_AND_CONTINUE_BUTTON = (By.LINK_TEXT, "Save and Continue")
    SKIP_BUTTON = (By.LINK_TEXT, "Skip")
    
    
    """Page Text ===>"""
    
    ADD_HOMETOWN_PAGE_TITLE = "Tinybeans - Where Parents Go"
    ADD_HOMETOWN_HEADER = "Add a hometown"
    
    
    """Page Class Constructor ===>"""
    
    def __init__(self, driver):
        super().__init__(driver)
        

    """Page Methods ===>"""
      
    """Sends a text value to the Hometown text field and returns a boolean"""
    def enter_hometown(self, text):
        self.do_send_keys(self.HOMETOWN_INPUT_TEXTFIELD, text)
        
        self.arrow_DOWN(self.HOMETOWN_INPUT_TEXTFIELD)
        self.press_ENTER(self.HOMETOWN_INPUT_TEXTFIELD)
        hometown = self.get_text(self.HOMETOWN_INPUT_TEXTFIELD)
        
        if hometown == text:
            print ("Hometown appears as entered.") 
            return True #Hometown appears as entered
        
        else:
            print ("Could not correctly enter Hometown.\nExpected: ", text, "\nFound: ", hometown, " instead.")         
            return False #Hometown entered does not match attempt to click Maps API suggestion/autocomplete menuitem

    """Click the 'Save and continue' button, with the caveat that this particular instance of this call checks to make sure that the text in the Hometown field matches what was entered. The Google Map API isnt properly integrated, so I am polling its suggestion result that I clicked"""         
    def click_save_and_continue_button(self, text):
        if self.enter_hometown(self, text):
            self.do_click(self.SAVE_AND_CONTINUE_BUTTON)
        else:
            print("FAILED! Hometown not found!")
            
    """Click the 'Skip' button."""        
    def click_skip_button(self):
        self.do_click(self.SKIP_BUTTON)
        
        