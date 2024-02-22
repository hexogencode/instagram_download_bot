import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start chrome in background (headless mode)
options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1920x935')
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

        # XPATH to element
        photo_xpath = "//img[@class='x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3']"
        button_xpath = "//button[@aria-label='Далее']"

        # Wait for Instagram
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, photo_xpath)))

        unique_links = []
        try:
            button_element = driver.find_element(By.XPATH, button_xpath)
            for i in range(4):
                button_element.click()
        except Exception:
            pass
        elements = driver.find_elements(By.XPATH, photo_xpath)
        for photo in elements:
            unique_links.append(photo.get_attribute('src'))
        return unique_links

    else:
        return None


# link = ""
# result_generator = post(link)
# print(len(result_generator))
# print(result_generator)
#
# # for photo_src in result_generator:
# #     print(photo_src)
# # print(post(link))
