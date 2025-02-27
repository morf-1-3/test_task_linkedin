from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os
import logging
import urllib.request


load_dotenv()
# logging.basicConfig(level=logging.INFO)
logging.basicConfig(
    # filename="out.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

LOGIN = os.getenv("LOGIN")
PASS = os.getenv("PASS")



options = webdriver.ChromeOptions()

prefs = {
    "profile.default_content_setting_values.notifications": 2,  # Вимкнути push-сповіщення
    "profile.default_content_setting_values.geolocation": 2,  # Заборонити визначення локації
    "webrtc.ip_handling_policy": "disable_non_proxied_udp"  # Вимкнути WebRTC IP
}
options.add_experimental_option("prefs", prefs)
options.add_argument("--headless")
options.add_argument("--user-data-dir=/tmp/chrome-user-data-----")
options.add_argument("--disable-webrtc")

options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-features=OptimizationGuideModelDownloading")
user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.6943.141 Safari/537.36"
options.add_argument(f"user-agent={user_agent}")

options.add_argument("--disable-blink-features=AutomationControlled")


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
        Object.defineProperty(navigator, 'language', {get: () => 'en-US'});
        Object.defineProperty(navigator, 'platform', {get: () => 'Linux x86_64'});
        Object.defineProperty(navigator, 'deviceMemory', {get: () => 8});
    """
})
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3, 4, 5]});
    """
})

try:
   
    # driver.get("https://www.linkedin.com")
    # driver.get("https://www.linkedin.com/login/ru?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
    driver.get("https://www.linkedin.com/login")
    logging.info("Open linkedin")
    time.sleep(1)
    # driver.save_screenshot("screenshot.png")
    # time.sleep(10)
    driver.find_element(By.ID, "username").send_keys(LOGIN)
    logging.info("write username")

    time.sleep(0.5)
    driver.find_element(By.ID, "password").send_keys(PASS)
    logging.info("write pass")
    time.sleep(0.8)
    driver.find_element(By.CLASS_NAME, "btn__primary--large").click()
    logging.info("clicked login")
    time.sleep(3)
    driver.save_screenshot("screenshot.png")
    time.sleep(5)
    # share-box-feed-entry__avatar


    driver.find_element(By.CLASS_NAME, "share-box-feed-entry__avatar").click()
    logging.info("clicked button")

    time.sleep(3)

    driver.find_element(By.CLASS_NAME, "profile-photo-edit__edit-btn").click()
    time.sleep(2)
    logging.info("clicked button")


    img_element = driver.find_element(By.CSS_SELECTOR, "div.imgedit-profile-photo-frame-viewer__image-container img")
    img_url = img_element.get_attribute("src")
    urllib.request.urlretrieve(img_url, f"media/{LOGIN}_profile_picture.jpg")

    logging.info("success button")
    time.sleep(2)

finally:
    time.sleep(60)
    driver.quit()