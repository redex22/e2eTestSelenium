import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from myOwnFramework.HomePage import HomePage
from myOwnFramework.utilities.BaseClass import BaseClass


class TestEnd2End(BaseClass):

    def test_e2e(self, loadhomepagedata):
        log = self.getlogger()
        self.driver.implicitly_wait(5)
        homePage = HomePage(self.driver)

        # find and send keys to the name, email and password parameters
        log.debug("Sending name, email and password keys")
        homePage.getname().send_keys(loadhomepagedata["firstname"])
        homePage.getemail().send_keys(loadhomepagedata["email"])
        homePage.getpassword().send_keys(loadhomepagedata["password"])

        self.driver.execute_script("window.scrollTo(20,document.body.scrollHeight)")

        # check the box of I love Ice creams
        log.debug("clicking on the ice cream box")
        homePage.geticecreambox().click()

        # select female in the checkbox dropdown
        log.debug("selecting gender")
        self.selectbygender(homePage.getgenderbox(), loadhomepagedata["gender"])

        # selecting the employed button
        log.debug("clicking on the employed button")
        homePage.getemployedbutton().click()

        # pressing submit
        log.debug("clicking on submit")
        homePage.getsubmit().click()

        # wrapping the alert
        alert = homePage.getalert().text
        log.info(f"The alert message in HomePage is: {alert}")

        # gets back the page to the scroll top
        self.driver.find_element(By.TAG_NAME, "html").send_keys(Keys.HOME)

        # comparing the success alert to pass the test
        assert "Success!" in alert

        # clicking on shop for a redirection to the shop page
        log.info("Entering the Shop Page")
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
        log.info("Going to checkout")
        shopPage.getcheckoutbutton().click()

        # sending keys into the delivery location box and expliciting wait to select U.S.A
        log.debug("Sending the delivery location key")
        shopPage.getlocationbox().send_keys("uni")
        self.verifybylinktext("United States of America")
        shopPage.getcountry().click()

        # check the terms and conditions checkbox and in purchase
        shopPage.getconditioncheckbox().click()
        shopPage.getpurchase().click()

        final_alert = shopPage.getfinalalert().text
        log.info(f"Final sucess alert is: {final_alert}")
        assert "Success!" in final_alert

        # driver.find_element(By.XPATH, "(//button[contains(text(),'Add')])[4]").click()

        time.sleep(3)

    @pytest.fixture(params=[{"firstname": "Ricardo",
                             "email": "hola@correo.com",
                             "password": "1234",
                             "gender": "Male"}])
    def loadhomepagedata(self, request):
        return request.param
