import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Start chrome in background (headless mode)
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x935')
driver = webdriver.Chrome(options=options)
driver.get('about:blank')


def reels(link):
    if link.startswith('https://www.instagram.com/') and 'reel' in link:

        # Open link
        driver.get(link)

        # XPATH to element
        xpath = "//video[contains(@class, 'x1lliihq') and contains(@class, 'x5yr21d') and contains(@class, 'xh8yej3')]"

        # Wait for Instagram
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))

        # Find element by XPATH
        video_link = driver.find_element(By.XPATH, xpath).get_attribute('src')

        return video_link

    else:
        return None