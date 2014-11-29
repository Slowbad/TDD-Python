from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--test-type')
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('http://localhost:8000')

assert 'Django' in browser.title
