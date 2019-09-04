import time

from Location.pages import careerspage, homepage, automationqapage

careersCount = homepage.careersCount()
print("Careers count in home page is: " + careersCount)
homepage.careersTab()

time.sleep(2)

openVacancies = careerspage.openVacancies()
print("The number of open vacancies is: " + str(openVacancies))

if int(careersCount) == openVacancies:
    print("The careers count equals to the count of open vacancies")
else:
    print("The careers count does not equal to the count of open vacancies")

    time.sleep(2)

if careerspage.manualQA():
    print("There should not be Manual QA position")
else:
    print("There is not manual QA position")

if careerspage.automationQA():
    print("Automation QA vacancy is opened")
else:
    print("There is no vacancy for automation QA Engineer")
    time.sleep(2)

automationqapage.setFirstName("Tatev")
automationqapage.setLastname("Melikyan")
automationqapage.setEmail("tatevmelikyan90@gmail.com")
automationqapage.choosefile()
automationqapage.submit()
