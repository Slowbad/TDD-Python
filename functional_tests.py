from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument('--test-type')
        self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_rerieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)

        # When she hits enter, the page updates, and now the page lsits
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feather to make a fly" (Edith is very methodical)

        # The page updates again, and now shows both items on her list

        # Edith wonders whether the stie will remember her list. Then she sees
        # that the stie has generate a unique URL for her -- ther eis some
        # explanatory text to that effect.

        # She visits that URl = her to-do list is still there.

        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
