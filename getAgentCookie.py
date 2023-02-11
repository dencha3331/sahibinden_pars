from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
from fake_useragent import UserAgent


def get_cookies_for_requests():
    try:
        exit_func = True

        print("start, set options")
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("window-size=1400,600")
        user = UserAgent()
        useragent = user.random
        options.set_preference("general.useragent.override", useragent)

        browser = webdriver.Firefox(options=options)
        print("download link")

        browser.implicitly_wait(10)
        browser.get("https://www.sahibinden.com")
        print("authorized")

        try:
            browser.find_element(By.CSS_SELECTOR, ".error-page-logo").click()
        except NoSuchElementException:
            pass
        browser.find_element(By.ID, "onetrust-accept-btn-handler").click()
        print("authorized complete, get cookies")

        selenium_userAgent = browser.execute_script("return navigator.userAgent;")
        print("get cookie complete, save data")

        with open("cookiesForRequests.py", 'w') as file2write:
            file2write.write(f"userAgent = '{selenium_userAgent}'\n")
            file2write.write("cookies_for_requests = [")
            for cookie in browser.get_cookies():
                file2write.write("\n\t{" + f"\n\t\t'name': '{cookie['name']}',")
                file2write.write(f"\n\t\t'value': '{cookie['value']}',")
                file2write.write(f"\n\t\t'domain': '{cookie['domain']}'\n\t" + "},")
            file2write.write("]\n")

        print("complete")

    except (ElementNotInteractableException, NoSuchElementException):
        print("disconnect")
        exit_func = False
    finally:
        print("out browser")
        browser.quit()
    return exit_func


if __name__ == "__main__":
    get_cookies_for_requests()
