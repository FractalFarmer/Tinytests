'''
Created on Jan 22, 2023

@author: Shawn Kunkel

Some test configuration data. Much of this will later be paramaterized and passed to the test at launch, 
so that tests can utilize far greater amounts of data

'''

class TestData:
    
    """ Local Browser Driver Paths. Not currently in use, because the browsers are being called as a service. """
    CHROME_DRIVER_PATH = ""
    CHROMIUM_DRIVER_PATH = ""
    FIREFOX_DRIVER_PATH = ""
    EDGE_DRIVER_PATH = ""
    SAFARI_DRIVER_PATH = ""
    
    """ Base URl for the test """
    BASE_URL = "http://tinybeans.com/"
    
    """ Data for this test. Will eventually be paramaterized. """
    USER_FIRST_NAME = "IdLoveToWork"
    USER_LAST_NAME = "WithTheTinyBeansTeam"
    USER_EMAIL = "ToMakeItAn@EvenHappierPlaceForFamilies.com"
    USER_PASSWORD = "" # unused at this point, because no password is created at Sign Up.
    USER_HOMETOWN = "Bega, NSW, Australia"
    USER_CAT1_NAME = "Mrs. Pancakes"
    USER_CAT1_DOB = "Jan 01, 2022"
    
    HOG_WILD_SEARCH_TEXT = "Hog Wild"
    HOG_WILD_LINK_TEXT = "Hog Wild Delivers with Pizza Party Throwdown"
    HOG_WILD_PAGE_TITLE = "Hog Wild Delivers with Pizza Party Throwdown - Tinybeans" 
    