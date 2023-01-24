'''
Created on Jan 22, 2023

@author: Shawn Kunkel

This is the Page Object for the Add Your Pet Page.
It contains specific data, locators and methods exclusive to this page.

'''

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class AddYourPet(BasePage):
    
    """Page Locators ===>"""
    
    
    CAT_RADIO_ELEMENT = (By.ID, "petRadios2")
    # CAT_RADIO_ELEMENT = (By.CSS_SELECTOR, ".col-md-2:nth-child(2) .form-check-label")
    
    PETS_BIRTHDAY_INPUT_TEXTFIELD = (By.ID, "birthday")
    PETS_NAME_INPUT_TEXTFIELD = (By.ID, "name")
    
    SAVE_AND_CONTINUE_BUTTON = (By.LINK_TEXT, "Save and Continue")
    SKIP_BUTTON = (By.LINK_TEXT, "Skip")
    
    ADD_YOUR_PET_HEADER_LOCATOR = (By.XPATH, "/html/body/div[3]/div/div[4]/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/p[2]")
    
    
    """Page Text ===>"""
    
    ADD_YOUR_PET_PAGE_TITLE = "Tinybeans - Where Parents Go"
    ADD_YOUR_PET_HEADER = "Add your pet"

    
    """Page Class Constructor ===>"""
    
    def __init__(self, driver):
        super().__init__(driver)
        

    """Page Methods ===>"""

    def click_cat_radio_element(self):
        self.do_click(self.CAT_RADIO_ELEMENT)
      
    """Click the 'Save and continue' button."""  
    def click_save_and_continue_button(self):
        self.do_click(self.SAVE_AND_CONTINUE_BUTTON)
            
    """Click the 'Skip' button."""              
    def click_skip_button(self):
        self.do_click(self.SKIP_BUTTON)
        
    """Sends a text value to the 'pet's name' text field"""
    def enter_pets_name(self, text):
        self.do_send_keys(self.PETS_NAME_INPUT_TEXTFIELD, text)
        
    """Sends a text value to the 'birthday' text field"""
    def enter_pets_birthday(self, text):
        self.do_send_keys(self.PETS_BIRTHDAY_INPUT_TEXTFIELD, text)
        