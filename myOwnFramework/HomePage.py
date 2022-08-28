from selenium.webdriver.common.by import By

from myOwnFramework.ShopPage import ShopPage


class HomePage:

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
        return self.driver.find_element(*HomePage.name)

    def getemail(self):
        return self.driver.find_element(*HomePage.email)

    def getpassword(self):
        return self.driver.find_element(*HomePage.password)

    def geticecreambox(self):
        return self.driver.find_element(*HomePage.iceCreamBox)

    def getgenderbox(self):
        return self.driver.find_element(*HomePage.genderBox)

    def getemployedbutton(self):
        return self.driver.find_element(*HomePage.employedButton)

    def getsubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getalert(self):
        return self.driver.find_element(*HomePage.homeAlert)

    def getshoppage(self):
        self.driver.find_element(*HomePage.shopPage).click()
        shopPage = ShopPage(self.driver)
        return shopPage
