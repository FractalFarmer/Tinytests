'''
Created on Jan 22, 2023

@author: Shawn Kunkel

This is an end-to-end smoke / acceptance test to cover some of the basic functionality on tinybeans.com

'''

import pytest
import time

from Config.config import TestData
from Tests.test_base import BaseTest

from Pages.BasePage import BasePage
from Pages.HomePage import HomePage
from Pages.Onboard_AddHometown import AddHometown
from Pages.Onboard_AddYourBeans import AddYourBeans
from Pages.Onboard_AddYourPet import AddYourPet
from Pages.Onboard_AllSetUp import AllSetUp
from Pages.Onboard_BeansTalkUpsell import BeansTalkUpsell
from Pages.Onboard_Signup import Signup
from Pages.SignupLanding import SignupLanding
from Pages.SignupModal import SignUpModal

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

window_vars = {}

@pytest.mark.usefixtures("init_driver")
class Test_SmokeTest(BaseTest):

        
    def wait_for_window(self, timeout = 2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = window_vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    
    def test_smoke_test_1(self):
        
        """ Initialize the Page Objects """
        self.basePage = BasePage(self.driver)
        self.homepage = HomePage(self.driver)
        self.addHometown = AddHometown(self.driver)
        self.addYourBeans = AddYourBeans(self.driver) 
        self.addYourPet = AddYourPet(self.driver)
        self.allSetup = AllSetUp(self.driver)
        self.beansTalkUpsell = BeansTalkUpsell(self.driver)
        self.signUp = Signup(self.driver)
        self.signUpLanding = SignupLanding(self.driver)
        self.signUpModal = SignUpModal(self.driver)

        """ Open the browser and go to the test page URL """
        self.driver.get(TestData.BASE_URL)

        """ Determine if the Sign Up Modal is present, by looking for the close button, then clicking it if found """
        flag = self.signUpModal.is_close_button_visible()
        assert flag
        self.signUpModal.click_close_button()

        """ Verify the Home Page title """
        self.basePage.verify_page_title(HomePage.HOME_PAGE_TITLE)
        
        """ Click the 'Start a Trial' button on the Home Page """
        self.homepage.click_start_a_trial_button()
        
        """ Verify the SignUp landing Page title """
        self.basePage.verify_page_title(SignupLanding.SIGNUP_LANDING_PAGE_TITLE)
        
        """ The Signup landing Page opens in a new tab. The following creates an array for the tab window handles """
        window_vars["window_handles"] = self.driver.window_handles
        
        """ Click the 'Start your free trial' button on the Signup landing Page """
        self.signUpLanding.click_start_your_free_trial_button()
        
        """ The window handles are managed here. The original tab gets closed & the new tab is switched to """
        window_vars["new_window"] = self.wait_for_window(20000)
        window_vars["root"] = self.driver.current_window_handle
        self.driver.switch_to.window(window_vars["new_window"])
        self.driver.switch_to.window(window_vars["root"])
        self.driver.close()
        self.driver.switch_to.window(window_vars["new_window"])

        """ Verify the SignUp Page title """
        self.basePage.verify_page_title(Signup.SIGNUP_PAGE_TITLE)
        
        """ Switch to the frame containing user data entry fields """
        self.driver.switch_to.frame(1)
        
        """ Populate user data entry fields """
        self.signUp.enter_first_name(TestData.USER_FIRST_NAME)
        self.signUp.enter_last_name(TestData.USER_LAST_NAME)
        self.signUp.enter_email(TestData.USER_EMAIL)
        
        """ Click the 'Continue with email' button on the Signup Page """        
        self.signUp.click_continue_with_email_button()
        
        """ 3 second wait """
        time.sleep(3)

        """ Verify the Add Hometown Page title """
        self.basePage.verify_page_title(AddHometown.ADD_HOMETOWN_PAGE_TITLE)
        
        """ Switch focus to default content """
        self.driver.switch_to.default_content()
   
        """ 3 second wait """
        time.sleep(3)
        
        """ Enter Hometown into Hometown field. This and the subsequent key presses will 
        be part of a (currently broken) function that'll handle the Maps API widget and 
        confirm proper widget item has been selected. The following is the blunt approach """
        self.driver.find_element(By.ID, "hometown").send_keys("Bega, NSW, Australia")
        
        """ 1 second wait """
        time.sleep(1)
        
        """ The keypresses that interact with the Maps API widget, selecting the first item in the suggestions list """
        self.driver.find_element(By.ID, "hometown").send_keys(Keys.DOWN)
        self.driver.find_element(By.ID, "hometown").send_keys(Keys.ENTER)
        
        """ Click the 'Save and Continue' button on the Add Hometown Page """ 
        self.driver.find_element(By.LINK_TEXT, "Save and Continue").click()
        
        time.sleep(3)
        
        """ Switch focus to default content """
        self.driver.switch_to.default_content()
        
        """ Verify the Add Your Beans Page title """
        self.basePage.verify_page_title(AddYourBeans.ADD_YOUR_BEANS_PAGE_TITLE)      

        """ THIS IS WHERE THE END TO END TEST CURRENTLY FAILS. I'm explicitly retrieving the skip button element and scrolling
        to it with javascript. This is a test workaround that still doesnt expose the element to click interaction, though it 
        does scroll to it. I suspect that this may be an ember.js - specific issue within the container that I am trying to 
        interact with """
        element = self.driver.find_element(By.CLASS_NAME, "tny-skip")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element);
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element)).click()
        
        print ("Debug: Got past the click without an error message")
 
        time.sleep(3)

        """ Verify the Add Your Pet Page title """
        self.basePage.verify_page_title(AddYourPet.ADD_YOUR_PET_PAGE_TITLE)         

        """ Switch focus to default content """
        self.driver.switch_to.default_content()
        
        """ Click the Cat radio element. This works if I manually click 'Skip' on the previous page. It currently 
        fails because the test script can't get past the previous page's 'Skip' button """
        self.addYourPet.click_cat_radio_element()
        
        """ Populate the fields on the 'Add Your Pet' Page """
        self.addYourPet.enter_pets_name(TestData.USER_CAT1_NAME)
        self.addYourPet.enter_pets_birthday(TestData.USER_CAT1_DOB)
        self.addYourPet.click_save_and_continue_button()
        
        time.sleep(3)
        
        """ Verify the BeansTalk upsell Page title """
        self.basePage.verify_page_title(BeansTalkUpsell.BEANS_TALK_UPSELL_PAGE_TITLE)    
        
        self.beansTalkUpsell.click_skip_button()
        
        time.sleep(3)
        
        """ Verify the 'All Set Up' Page title """
        self.basePage.verify_page_title(AllSetUp.ALL_SET_UP_PAGE_TITLE)          
        
        """ Click the 'Go To Tinybeans' button """
        self.allSetup.click_go_to_tinybeans_button()
        
        time.sleep(3)
        
        """ Check to see if the Signup Modal is visible & either close it or report it's absence """
        if self.signUpModal.is_close_button_visible():
            self.signUpModal.click_close_button()
        else:
            print ("SIGNUP MODAL NOT FOUND") # it won't be found this time, because it only appears on the very first visit to the page. By design?

        """ Verify the Home Page title """
        self.basePage.verify_page_title(HomePage.HOME_PAGE_TITLE)  

        """ Enter selected string into the Search field """
        self.homepage.enter_search_text(TestData.HOG_WILD_SEARCH_TEXT)
        
        """ Click the Seach button """
        self.homepage.click_search_button()
        
        """ Taking a 5 second break to wait for any search results """
        time.sleep(5)
        
        """ The following looks for the correct search results, then clicks on it if found or reports it not found.
        If the correct result is located, then it goes looking for the tinybeans logo so that it can click on it. 
        However, this logo does not appear on the search results page, as the page is an endless scroll of other articles.
        That said, this logo CAN be found on the Home Page and interacted with """
        element = self.driver.find_element(By.LINK_TEXT, TestData.HOG_WILD_LINK_TEXT)
        if element.is_displayed():
            self.homepage.do_click(element)
            time.sleep(3)
            title = self.driver.title()
            assert title == TestData.HOG_WILD_PAGE_TITLE
            if self.is_enabled(HomePage.TINYBEANS_LOGO):
                self.driver.execute_script("arguments[0].scrollIntoView(true);", HomePage.TINYBEANS_LOGO);
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(HomePage.TINYBEANS_LOGO)).click()
            else:
                print ("Tinybeans logo not found on this page.") #This is the actual result for the search results page, because the tinybeans logo does not appear on it.
        else:
            print (TestData.HOG_WILD_LINK_TEXT + "link not found")
        
        