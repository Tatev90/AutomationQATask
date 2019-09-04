from Location.testsfiles import browser


# scroll to submit button
def setFirstName(firstname):
    firstname_field = browser.browser.find_element_by_xpath(
        "//*[@id='wpcf7-f3772-o2']/form/div[2]/div[1]/div[2]/div[1]/div/span/input")
    firstname_field.send_keys(firstname)


def setLastname(lastname):
    lastname_field = browser.browser.find_element_by_xpath(
        "//*[@id='wpcf7-f3772-o2']/form/div[2]/div[1]/div[2]/div[2]/div/span/input")
    lastname_field.send_keys(lastname)


def setEmail(email):
    email_address = browser.browser.find_element_by_xpath(
        "//*[@id='wpcf7-f3772-o2']/form/div[2]/div[1]/div[3]/div/span/input")
    email_address.send_keys(email)


def choosefile():
    choose_file = browser.browser.find_element_by_xpath(
        "//*[@id='wpcf7-f3772-o2']/form/div[2]/div[1]/div[4]/p/span/div/input")
    choose_file.send_keys("/home/tatev/PycharmProjects/AutomationTest/Location/pages/TatevMelikyanCV.pdf")


def submit():
    submit_file = browser.browser.find_element_by_xpath("//*[@id='wpcf7-f3772-o2']/form/div[2]/div[1]/div[6]/input")
    submit_file.click()
