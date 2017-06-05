from selenium import webdriver
from selenium.webdriver.common.by import By

class IndeedLogin():


    def loginTest(self):
        '''
        This will test the failed login message. 
        :return: 
        '''

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

        if submit is not None:
            try:
                submit.click()
                driver.implicitly_wait(3)
                errorMessage = driver.find_element(By.XPATH, "//*[@id='signin_password_grp']/div")
                print("Element found after submit was clicked")
                driver.quit()
            except:
                print("Error message did not appear after submission")
            finally:
                driver.quit()




test = IndeedLogin()
test.loginTest()
