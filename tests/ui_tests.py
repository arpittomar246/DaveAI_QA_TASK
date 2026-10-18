
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Website we are testing
BASE_URL = "https://www.iamdave.ai"

class TestDaveAIWebsite(unittest.TestCase):

    def setUp(self): # setup with run before running test cases    
            self.driver = webdriver.Chrome() # open new chrome browser
            self.driver.maximize_window() #maximize the window
            self.driver.implicitly_wait(10) #waits for 15 sec for page to get loaded otherwise fails
            self.driver.get(BASE_URL) # opens the URL
    
    def tearDown(self): # this will run after everytest case
            self.driver.quit() # close the browser


    # Test 1 -> Website loads and shows the title and logo
    def test_homepage_title_and_logo(self):
       
        self.assertIn("DaveAI", self.driver.title) #the browser title should have title as DaveAI
        time.sleep(3)
        logos = self.driver.find_elements(By.CSS_SELECTOR, "img[src*='DaveAI_Logo']") #finds the logo image
        
        #check that at least one logo on screen
        visible_logo_found = False
        for logo in logos:
            if logo.is_displayed():
                visible_logo_found = True
                break
        self.assertTrue(visible_logo_found) #logo should be visible on screen


    # Test 2 ->  The main heading is present on the homepage
    def test_main_heading_is_present(self):
        headings = self.driver.find_elements(By.TAG_NAME, "h1") #Find heading of page
       # check if any heading contains the expected text
        heading_found = False
        for heading in headings:
            # textContent reads the text
            if "automotive intelligence" in heading.get_attribute("textContent").lower():
                heading_found = True
                break
        self.assertTrue(heading_found)


    # Test 3 ->  Clicking "Book Demo" opens the demo page
    def test_book_demo_button_opens_demo_page(self):
       
        demo_links = self.driver.find_elements(By.XPATH, "//a[contains(@href, 'book-demo')]") #find the link that will go to book demo page
        for link in demo_links: # this loop will click the first one that is visible on the screen
            if link.is_displayed():
                link.click()
                break
            
        time.sleep(3) # give wait time to load
        self.assertIn("book-demo", self.driver.current_url) # checks address should have book demo


    
    # Test 4 -> Go from homepage to the demo page and type an email in the form
    def test_demo_form_accepts_email_input(self):
        
        # this block will find all "Book Demo" links and click 
        demo_links = self.driver.find_elements(By.XPATH, "//a[contains(@href, 'book-demo')]")
        for link in demo_links:
            if link.is_displayed():
                link.click()
                break

        time.sleep(3) # wait time to load

        # finds the email box and enters the email
        email_box = self.driver.find_element(By.CSS_SELECTOR, "input[type='email']")
        email_box.send_keys("arpit.tomar@iamdave.ai")
        time.sleep(2)
        self.assertEqual(email_box.get_attribute("value"), "arpit.tomar@iamdave.ai") # checks if email is entered



