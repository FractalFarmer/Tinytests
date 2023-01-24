'''
Created on Jan 22, 2023

@author: Shawn Kunkel

This is the parent Page for all Pages. Child Pages will inherit the properties contained herein

'''

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    
    """Page Class Constructor ===>"""
        
    def __init__(self, driver):
        self.driver = driver


    """Page Methods ===>"""

    """Sends 'Down Arrow' keypress to the selected location"""            
    def arrow_DOWN(self, by_locator):
        self.driver.find_element(by_locator).send_keys(Keys.DOWN)
  
    """Sends 'Up Arrow' keypress to the selected location"""            
    def arrow_UP(self, by_locator):
        self.driver.find_element(by_locator).send_keys(Keys.ARROW_UP)

    """Sends 'Left Arrow' keypress to the selected location"""            
    def arrow_LEFT(self, by_locator):
        self.driver.find_element(by_locator).send_keys(Keys.ARROW_LEFT)
    
    """Sends 'Right Arrow' keypress to the selected location"""            
    def arrow_RIGHT(self, by_locator):
        self.driver.find_element(by_locator).send_keys(Keys.ARROW_RIGHT)
    
    """Sends 'ENTER' keypress to the selected location"""            
    def press_ENTER(self, by_locator):
        self.driver.find_element(by_locator).send_keys(Keys.ENTER)
    
    """Click handler, uses the locator passed to it"""    
    def do_click(self, by_locator):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(by_locator)).click()
        
    """Sends text to the specified locator. This is not to be confused with a key typing call""" 
    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        
    """Returns the text from the element at a specified locator"""    
    def get_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    """Returns the title of the current page"""
    def get_title(self, title):
        #WebDriverWait(self.driver, 10).until(EC.title_contains(title))
        return self.driver.title    
    
    """Determines whether or not an element at the locator is enabled in the DOM and visible; returns boolean""" 
    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        return bool(element)
    
    """This function uses a call to JavaScript to scoll to the element specified by the locator"""
    def scroll_to(self, by_locator):
            element = self.driver.find_element(by_locator)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element);

    def verify_page_title(self, titlevar):
        title = self.get_title(titlevar)
        assert title == titlevar
                    
            













            
            
            
            
            
            