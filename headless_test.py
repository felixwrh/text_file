from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time
from selenium import webdriver
import unittest

class HeadlessBrowserTest(unittest.TestCase):
    def setUp(self):

        # Necessary configuration to get the headless browser test working.
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument("--disable-devshm-using")
        options.add_argument("--window-size=1920,1080")

        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = True
        firefox_binary = "/usr/bin/firefox"
        self.driver = webdriver.Firefox(
            options=options, capabilities=cap, firefox_binary=firefox_binary)

    def test_headless_browser(self):
        self.driver.get('47.254.243.88')
        time.sleep(5)
        passwordBox = self.driver.find_element_by_name('password')
        passwordBox.send_keys('minecraft')

        self.driver.find_element_by_tag_name("button").click()
        time.sleep(5)

        label = self.driver.find_element_by_tag_name('label')
        labelText = label.get_attribute('innerHTML')

        self.assertEqual(labelText, "Password:")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


