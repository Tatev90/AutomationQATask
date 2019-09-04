import time

from Location.testsfiles import browser

time.sleep(2)


# Check the careers count equals to the count of the open vacancies
def openVacancies():
    open_vacancies = (browser.browser.find_elements_by_class_name("smartrecruitersJobListElement"))
    return len(open_vacancies)


# No vacancy for Manual QA Engineer
def manualQA():
    open_vacancies = (browser.browser.find_elements_by_class_name("smartrecruitersJobListElement"))
    for vacancies in open_vacancies:
        currentvacancies = vacancies.find_elements_by_class_name("s-careers-title")[0]

        if currentvacancies.text == "Manual QA Engineer":
            return True

    return False


# Click on Automation Qa Engineer
def automationQA():
    open_vacancies = (browser.browser.find_elements_by_class_name("smartrecruitersJobListElement"))
    for vacancies in open_vacancies:
        currentvacancies = vacancies.find_elements_by_class_name("s-careers-title")[0]
        if currentvacancies.text == "Automation QA Engineer":
            currentvacancies.click()
            return True
    return False


# Fill the form and upload a file

# Click on Submit button
#
# Make sure the reCaptcha error appears
#
# print(careersCount, openVacancies)
