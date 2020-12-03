from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

DRIVER_PATH = 'Driver/chromedriver.exe'
options = Options()
options.add_argument("--window-size=1920,1200")
options.headless = True
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://github.com/login")
# print(driver.page_source)
login_user=driver.find_element_by_xpath("//*[@id=\"login_field\"]")
login_user.send_keys("your-username")
login_pass=driver.find_element_by_xpath("//*[@id=\"password\"]")
login_pass.send_keys("your-pass")
driver.find_element_by_xpath("//*[@id=\"login\"]/form/div[4]/input[12]").click()
# driver.save_screenshot("screen.png")

# driver.get("https://github.com/login")
# print(driver.page_source)

try:
    driver.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/summary/img")
    print("Success login")
    # driver.save_screenshot("login_page.png")
    driver.get("https://github.com/user?tab=repositories")
    repo=driver.find_element_by_xpath("//*[@id=\"user-repositories-list\"]/ul")
    # print(repo.text)
    li=repo.find_elements_by_tag_name("li")
    ans=[]
    for i in li:
        a=i.find_element_by_tag_name('h3')
        ans.append(a.text)
    total_repos=len(ans)
    print("Your total repos: "+str(total_repos))
    print(ans)

except NoSuchElementException:
    print("Unsuccessful login")

driver.quit()
