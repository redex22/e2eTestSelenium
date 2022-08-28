import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from myOwnFramework.HomePage import HomePage
from myOwnFramework.ShopPage import ShopPage
from myOwnFramework.utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_e2e(self):
        self.driver.implicitly_wait(5)
        homePage = HomePage(self.driver)

        # find and send keys to the name, email and password parameters
        homePage.getname().send_keys("Ricardo")
        homePage.getemail().send_keys("hola@correo.com")
        homePage.getpassword().send_keys("1234")

        self.driver.execute_script("window.scrollTo(20,document.body.scrollHeight)")

        # check the box of I love Ice creams
        homePage.geticecreambox().click()

        # select female in the checkbox dropdown
        genderBox = Select(homePage.getgenderbox())
        genderBox.select_by_visible_text("Female")

        # selecting the employed button
        homePage.getemployedbutton().click()

        # pressing submit
        homePage.getsubmit().click()

        # wrapping the alert
        alert = homePage.getalert().text

        self.driver.find_element(By.TAG_NAME, "html").send_keys(Keys.HOME)

        # comparing the success alert to pass the test
        assert "Success!" in alert

        # clicking on shop for a redirection to the shop page
        shopPage = homePage.getshoppage()

        # getting all the products boxes and wrapping them into a variable

        cardBoxes = shopPage.getcardboxes()

        # iterating through all the cardBoxes until I find the desired one and I add it to the cart
        for card in cardBoxes:
            title = card.find_element(By.XPATH, "div/h4/a").text
            if title == "Nokia Edge":
                card.find_element(By.TAG_NAME, "button").click()

        # clicking and going to the checkout cart
        shopPage.getbuybutton().click()

        # clicking on checkout
        shopPage.getcheckoutbutton().click()

        # sending keys into the delivery location box and expliciting wait to select U.S.A
        shopPage.getlocationbox().send_keys("uni")
        self.verifybylinktext("United States of America")
        shopPage.getcountry().click()

        # check the terms and conditions checkbox and in purchase
        shopPage.getconditioncheckbox().click()
        shopPage.getpurchase().click()

        final_alert = shopPage.getfinalalert().text
        assert "Success!" in final_alert

        # driver.find_element(By.XPATH, "(//button[contains(text(),'Add')])[4]").click()

        time.sleep(3)