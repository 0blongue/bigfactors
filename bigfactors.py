from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from math import *

driver = webdriver.Chrome()
driver.get('https://www.calculator.net/big-number-calculator.html?')
x = driver.find_element_by_name('cx')
y = driver.find_element_by_name('cy')
mod = driver.find_element_by_xpath("//button[@name='co'][@value='mod']")
div = driver.find_element_by_xpath("//button[@name='co'][@value='divide']")
n = 99983822328771741915661664084210270492316661686065226187943726935927708098627133761115200633753782266657227051992984282266909248764614872208244524523644140765911124633192107172800292859463975078535453799144782333189152913945549375961009819542163328481805815228294057160911379202715558861783600702052502938725873989346037196766450398638158342797
m = 9999191083721309799282959470256012468984116020376325978703334253725952909163785640752619969835246881690742369819095071255449544964244476023848775957831652902563923134479964
factors = [1]

n = 315
m = int(sqrt(n))+1

x.send_keys(n)
y.send_keys('2')
mod.click()
output = driver.find_element_by_xpath("//p[@class='bigtext']")

def bigmod(a,b):
	x = driver.find_element_by_name('cx')
	y = driver.find_element_by_name('cy')
	mod = driver.find_element_by_xpath("//button[@name='co'][@value='mod']")
	output = driver.find_element_by_xpath("//p[@class='bigtext']")
	x.send_keys(a)
	y.send_keys(b)
	mod.click()
	return output.text

def bigdiv(a,b):
	x = driver.find_element_by_name('cx')
	y = driver.find_element_by_name('cy')
	div = driver.find_element_by_xpath("//button[@name='co'][@value='divide']")
	output = driver.find_element_by_xpath("//p[@class='bigtext']")
	x.send_keys(a)
	y.send_keys(b)
	div.click()
	return output.text



# while reduce((lambda a, b: a * b), factors) is not n:
for i in range (3,m,2):
	while bigmod(n,i) == 0:
		factors.append(i)
		n = bigdiv(n,i)
	
print(factors)