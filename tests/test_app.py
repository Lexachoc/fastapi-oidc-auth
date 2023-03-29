import json

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_successfull_login(browser_driver: webdriver):
    """Try to login to the system."""
    browser_driver.delete_all_cookies()
    browser_driver.get("http://localhost:5000")
    browser_driver.find_element(By.ID, "username").send_keys("myuser")
    browser_driver.find_element(By.ID, "password").send_keys("myuser")
    browser_driver.find_element(By.ID, "kc-login").click()
    content = browser_driver.find_element(By.TAG_NAME, "pre").text
    parsed_json = json.loads(content)
    assert parsed_json["message"] == "success"