# setup
# 1. open terminal and put in the commands
# 2. ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
# 3. brew install python3
# 4. brew cask install chromedriver
# 5. pip3 install selenium
# 6. pip3 install simpleaudio
#
# 7. download some sound file and replace "modem.wav" with the sound wave file name, put the file in same directory as this script
# 8. in terminal - python3 amazon_aw_check.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import simpleaudio as sa
import time

print("Make sure you have your amazon cart ready to go")
driver = webdriver.Chrome()
driver.get("https://www.amazon.com/gp/navigation/redirector.html/ref=sign-in-redirect?ie=UTF8&associationHandle=usflex&currentPageURL=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&pageType=Gateway&switchAccount=&yshURL=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26ref_%3Dnav_signin")
print("Sign in on the page and leave it at amazon.com, you have 100 seconds...")
time.sleep(100)
while(True):
	print("Refreshing amazon checkout")
	try:
		driver.get('https://www.amazon.com/gp/cart/desktop/go-to-checkout.html/ref=alm_cx_byg_proceed?proceedToCheckout=1&ie=UTF8&isFresh=1&useDefaultCart=1')
		today = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[1]/div[3]/div[2]/div/ul/li[1]/span/span/span/button/div/div[3]').text
		tomorrow = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[1]/div[3]/div[2]/div/ul/li[2]/span/span/span/button/div/div[3]').text
		cloverfield = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[1]/div[3]/div[2]/div/ul/li[3]/span/span/span/button/div/div[3]').text
		assert today == "Not available"
		assert tomorrow == "Not available"
		assert cloverfield == "Not available"
		print("No available windows")
	except Exception as e:
		print(e)
		wave_obj = sa.WaveObject.from_wave_file('modem.wav')
		play_obj = wave_obj.play()
		play_obj.wait_done()  # Wait until sound has finished playing
	time.sleep(120)
driver.close()
