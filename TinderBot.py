from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from secrets import username, password
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TinderBot():
	def __init__(self):
		self.driver = webdriver.Chrome()

	def login(self):
		self.driver.get('https://tinder.com')

		sleep(2)

		fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
		fb_btn.click()

		self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button').click()
		# switch to login popup
		base_window = self.driver.window_handles[0]
		self.driver.switch_to_window(self.driver.window_handles[1])

		email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
		email_in.send_keys(username)

		pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
		pw_in.send_keys(password)

		login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
		login_btn.click()

		self.driver.switch_to_window(base_window)

		popup_1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')))
		popup_1.click()

		popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
		popup_2.click()

	def like(self):
		like_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')))
		like_btn.click()

	def dislike(self):
		dislike_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')))
		dislike_btn.click()

	def auto_swipe(self):
		while True:
			sleep(0.5)
			try:
				self.like()
			except Exception:
				try:
					self.close_popup()
					self.dislike()
				except Exception:
					self.close_match()
					self.dislike()


	def close_popup(self):
		popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]')
		popup_3.click()

	def close_match(self):
		match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
		match_popup.click()

bot = TinderBot()
bot.login()
bot.auto_swipe()