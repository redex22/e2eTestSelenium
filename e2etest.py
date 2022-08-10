# import selenium webdriver and dependencies
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service


# establish the service object with the geckodriver
# establish the driver with the driver class
# get the link to the driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("./geckodriver.exe")
driver = webdriver.Firefox(service=service_obj)
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# implicit timer for any lag on the page
driver.implicitly_wait(5)

# find and send keys to the name, email and password parameters
driver.find_element(By.NAME, "name").send_keys("Ricardo")
driver.find_element(By.NAME, "email").send_keys("hola@correo.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("1234")

driver.execute_script("window.scrollTo(20,document.body.scrollHeight)")

# check the box of I love Ice creams
driver.find_element(By.XPATH, "//label[normalize-space()='Check me out if you Love IceCreams!']").click()

# select female in the checkbox dropdown
genderBox = Select(driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1"))
genderBox.select_by_visible_text("Female")

# selecting the employed button
driver.find_element(By.CSS_SELECTOR, "#inlineRadio2").click()


# pressing submit
driver.find_element(By.XPATH, "//input[@value='Submit']").click()


# wrapping the alert
alert = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text

driver.find_element(By.TAG_NAME, "html").send_keys(Keys.HOME)

# comparing the success alert to pass the test
assert "Success!" in alert

# clicking on shop for a redirection to the shop page
driver.find_element(By.XPATH, "//a[normalize-space()='Shop']").click()

# getting all the products boxes and wrapping them into a variable
cardBoxes = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

# iterating through all the cardBoxes until I find the desired one and I add it to the cart
for card in cardBoxes:
    title = card.find_element(By.XPATH, "div/h4/a").text
    if title == "Nokia Edge":
        card.find_element(By.TAG_NAME, "button").click()

# clicking and going to the checkout cart
driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()

# clicking on checkout
driver.find_element(By.XPATH, "//button[normalize-space()='Checkout']").click()

# sending keys into the delivery location box and expliciting wait to select U.S.A
driver.find_element(By.ID, "country").send_keys("uni")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "United States of America")))
driver.find_element(By.LINK_TEXT, "United States of America").click()

# check the terms and conditions checkbox and in purchase
driver.find_element(By.CSS_SELECTOR, "label[for='checkbox2']").click()
driver.find_element(By.CSS_SELECTOR, "input[value='Purchase']").click()

final_alert = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
assert "Success!" in final_alert

#driver.find_element(By.XPATH, "(//button[contains(text(),'Add')])[4]").click()

time.sleep(3)

# we close the browser to finish the assignment
driver.close()