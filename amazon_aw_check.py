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
		assert "No delivery windows" in driver.find_element_by_tag_name('body').text
		print("No available windows")
	except Exception as e:
		print(e)
		wave_obj = sa.WaveObject.from_wave_file('modem.wav')
		play_obj = wave_obj.play()
		play_obj.wait_done()  # Wait until sound has finished playing
	time.sleep(120)
driver.close()
