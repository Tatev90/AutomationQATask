# Get careers count from the right side of the Careers Section
import time

from testsfiles import browser


def careersCount():
    careers_count = browser.browser.find_element_by_class_name("job-count")
    return careers_count.text


time.sleep(2)


# Click on Careers Section
def careersTab():
    careers_tab = browser.browser.find_element_by_xpath("//*[@id='menu-item-3337']/a")
    careers_tab.click()
