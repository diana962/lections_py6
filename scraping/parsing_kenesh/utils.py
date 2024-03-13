from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


chrome_options = webdriver.ChromeOptions()

def get_deps_html_selenium(url):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'card-title')))
    html = driver.page_source
    driver.quit() 
    return html


# chrome_options.add_argument("--disable-javascript")
# service = Service('path')

# def get_html_selenium(url):
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.get(url)
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_all_elements_located(
#             (By.CLASS_NAME, 'stretched-link'))
#     )
    
#     html = driver.page_source
#     driver.quit() 
#     return html


# url = "https://kenesh.kg/deputies"
# html_content = get_html_selenium(url)
# print(html_content)

def get_page_html_selenium(url): 
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'section-footer')))
    sleep(3)

    i = 1
    res = {}
    while i <= 8:
        sleep(1.5)
        html = driver.page_source
        res[i] = html
        ### if i == 8:
        ###     break
        page_button = driver.find_elements(By.CSS_SELECTOR, '.page-link')
        # print(list(x.text for x in page_button))
# создание клика
        element = page_button[-1]
        if page_button:
            ActionChains(driver).move_to_element(element).perform()
            sleep(0.5)
            element.click()
        sleep(1)
        i +=1
    
    driver.quit() 
    return res

# get_page_html_selenium('https://kenesh.kg/deputies')
