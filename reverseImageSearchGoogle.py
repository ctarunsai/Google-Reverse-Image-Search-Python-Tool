#python3 searchImage.py <ImageFile Path> <OutputFile Path>
import time,random,sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def automate(driver,output):	
	count = 1
	links = getPageLinks(driver,output)
	link = getNextPageLink(driver)
	print(count)
	while link != -1:
		navigate(driver,link,-1)
		links = getPageLinks(driver,output)
		link = getNextPageLink(driver)
		count += 1
		print(count)

def navigate(driver,link,upload):
	if upload == -1:
		driver.get(link)
		sleepProcess()
	else:
		driver.get(link)
		sleepProcess()
		uploadImage(driver,upload)

def getNextPageLink(driver):
	try:
		nplelem = driver.find_element_by_xpath('//*[@id="pnnext"]')
		link = nplelem.get_attribute("href")
		return link
	except:
		return -1

def getPageLinks(driver,output):
	links = []
	links_elem = driver.find_elements_by_xpath('//div[@class="r"]/a')
	for obj in links_elem:
		link = obj.get_attribute("href")
		links.append(link)
	writeToFile(links,output)
	return links

def uploadImage(driver,file_path):
	image_pic = driver.find_element_by_xpath('//div[@class="LM8x9c"]').click()
	select_by_image = driver.find_element_by_xpath('//a[@class="qbtbha qbtbtxt qbclr"]').click()
	choose_file = driver.find_element_by_xpath('//input[@id="qbfile"]')
	choose_file.send_keys(file_path)
	sleepProcess()

def sleepProcess():
	time.sleep(random.randint(1,10))

def writeToFile(links,output):
	out = open(output,"a")
	for link in links:
		out.write(link + "\n")
	out.close()

input_path = sys.argv[1]
output_path = sys.argv[2]

chrome_options = Options()
chrome_options.add_argument("--headless")


driver = webdriver.Chrome(options=chrome_options)
link = "https://images.google.com/"
navigate(driver,link,input_path)
automate(driver,output_path)

driver.quit()
