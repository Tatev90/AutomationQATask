from selenium import webdriver

browser = webdriver.Chrome(executable_path="/home/tatev/Documents/Tools/chromedriver_linux64/chromedriver")
url = 'https://www.sflpro.com'
browser.get(url)
browser.maximize_window()


def execute_script(param, element):
    return None
