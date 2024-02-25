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


def reels(link: str):
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


def post(link: str):
    if link.startswith('https://www.instagram.com/') and '/p/' in link:
        # Open link
        driver.get(link)

        # XPATH to photo url
        photo_xpath = "//img[@class='x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3']"
        # XPATH to button
        button_xpath = "//button[@aria-label='Далее']"

        # Wait for Instagram
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, photo_xpath)))

        photo_links = []

        try:
            # If webdriver can find next button in post = post have few photos
            button_element = driver.find_element(By.XPATH, button_xpath)
            for i in range(4):
                # By clicking 4 times post is loading completely
                button_element.click()
        # If there are no button found, pass
        except Exception:
            pass

        elements = driver.find_elements(By.XPATH, photo_xpath)
        # Because find_elementS used, we need to store photo links in list
        for photo in elements:
            photo_links.append(photo.get_attribute('src'))

        return photo_links

    else:
        return None
