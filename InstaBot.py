from selenium import webdriver
import time

class InstaBot:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.driver=webdriver.Chrome(executable_path="LOCATION OF chromedriver.exe file location)
    
    def login(self):
        driver=self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(3)
        driver.find_element_by_name("username").send_keys(self.username)
        password=driver.find_element_by_name("password")
        password.send_keys(self.password)
        password.submit()
        time.sleep(3)
    
    def searchHashtags(self,hashtag):
        driver=self.driver
        driver.get("https://www.instagram.com/explore/tags/"+hashtag)
    
    def likePhotos(self,num):
        driver=self.driver
        driver.find_element_by_class_name("v1Nh3").click()

        i=1
        while i<=num:
            time.sleep(1)
            driver.find_element_by_class_name("fr66n").click() #like a posts
            driver.find_element_by_class_name("coreSpriteRightPaginationArrow").click() #Go to next post
            time.sleep(1)
            i=i+1 

        driver.get("https://www.instagram.com/") #Back to Insta main page
        time.sleep(2)
        # if you like this code then please follow me Instagram using below line... 
		    # If you don't want ? then remove below line..
		    driver.get('https://www.instagram.com/_dev_z0.1')
		    time.sleep(2)
		    driver.find_element_by_xpath('//button[text()="Follow"]').click()
        

instaBot=InstaBot("YOUR_USERNAME","YOUR_PASSWORD") #write your username and password
instaBot.login()
instaBot.searchHashtags("programming")
num=6 #Num of posts you want to like
instaBot.likePhotos(num)
