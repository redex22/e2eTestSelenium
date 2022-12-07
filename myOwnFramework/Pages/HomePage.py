from selenium.webdriver.common.by import By
from myOwnFramework.Pages.ShopPage import ShopPage


class HomePage:

    # Paths to the elements of the page needed for the test case
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    iceCreamBox = (By.XPATH, "//label[normalize-space()='Check me out if you Love IceCreams!']")
    genderBox = (By.CSS_SELECTOR, "#exampleFormControlSelect1")
    employedButton = (By.CSS_SELECTOR, "#inlineRadio2")
    submit = (By.XPATH, "//input[@value='Submit']")
    homeAlert = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    shopPage = (By.XPATH, "//a[normalize-space()='Shop']")

    def __init__(self, driver):
        self.driver = driver

    def getname(self):
        """Returns the name input box of the page"""
        return self.driver.find_element(*HomePage.name)

    def getemail(self):
        """Returns the email input box of the page"""
        return self.driver.find_element(*HomePage.email)

    def getpassword(self):
        """Returns the password input box of the page"""
        return self.driver.find_element(*HomePage.password)

    def geticecreambox(self):
        """Returns the Ice Cream check box of the page"""
        return self.driver.find_element(*HomePage.iceCreamBox)

    def getgenderbox(self):
        """Returns the gender box element"""
        return self.driver.find_element(*HomePage.genderBox)

    def getemployedbutton(self):
        """Returns the employed button"""
        return self.driver.find_element(*HomePage.employedButton)

    def getsubmit(self):
        """Returns the submit button"""
        return self.driver.find_element(*HomePage.submit)

    def getalert(self):
        """Returns the alert box"""
        return self.driver.find_element(*HomePage.homeAlert)

    def getshoppage(self):
        """Clicks on the shop page button and returns a Shop Page object"""
        self.driver.find_element(*HomePage.shopPage).click()
        shopPage = ShopPage(self.driver)
        return shopPage
