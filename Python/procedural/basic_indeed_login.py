from selenium import webdriver
from selenium.webdriver.common.by import By

class IndeedLogin():


    def loginTest(self):

        #Starting up browser and going to URL
        url = "http://www.indeed.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)

        #At destination, clicking on signing in button
        signIn = driver.find_element(By.ID, "userOptionsLabel")

        if signIn is not None:
            signIn.click()

        driver.implicitly_wait(5)

        #Make a sign-in attempt

        #Locate email input and enter info
        emailInput = driver.find_element(By.ID, "signin_email")
        emailInput.send_keys("someemail@gmail.com")

        #locate Password input and enter info
        passwordInput = driver.find_element(By.ID, "signin_password")
        passwordInput.send_keys("12345")

        #Locate submit button and click
        submit = driver.find_element(By.XPATH, "//*[@id='loginform']/button")

        driver.implicitly_wait(3)

        errorMessage = driver.find_element(By.LINK_TEXT, "Incorrect password or email address")

        if errorMessage is not None:
            print("Verified that sign in error functions properly")
        else:
            print("Sign in error has not appeared as expected")

        quit()

test = IndeedLogin()
test.loginTest()
