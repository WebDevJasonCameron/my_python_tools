from selenium import webdriver
from selenium.webdriver.chrome.service import service

service = Service(executable_path = "")
driver = webdriver.Chrome(service = service)