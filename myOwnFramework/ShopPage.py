from selenium.webdriver.common.by import By


class ShopPage:

    cardBoxes = (By.XPATH, "//div[@class='card h-100']")
    buyButton = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    checkOutButton = (By.XPATH, "//button[normalize-space()='Checkout']")
    locationBox = (By.ID, "country")
    country = (By.LINK_TEXT, "United States of America")
    conditionsCheckBox = (By.CSS_SELECTOR, "label[for='checkbox2']")
    purchase = (By.CSS_SELECTOR, "input[value='Purchase']")
    finalAlert = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def __init__(self, driver):
        self.driver = driver

    def getcardboxes(self):
        return self.driver.find_elements(*ShopPage.cardBoxes)

    def getbuybutton(self):
        return self.driver.find_element(*ShopPage.buyButton)

    def getcheckoutbutton(self):
        return self.driver.find_element(*ShopPage.checkOutButton)

    def getlocationbox(self):
        return self.driver.find_element(*ShopPage.locationBox)

    def getcountry(self):
        return self.driver.find_element(*ShopPage.country)

    def getconditioncheckbox(self):
        return self.driver.find_element(*ShopPage.conditionsCheckBox)

    def getpurchase(self):
        return self.driver.find_element(*ShopPage.purchase)

    def getfinalalert(self):
        return self.driver.find_element(*ShopPage.finalAlert)