from selenium import webdriver


class DriverFactory:
    DRIVER_CHROME = 'chrome'
    DRIVER_FIREFOX = 'firefox'

    @staticmethod
    def create_driver(browser_name: str, visible: bool = True) -> webdriver:
        if browser_name.lower() == DriverFactory.DRIVER_CHROME:
            options = webdriver.chrome.options.Options()
            options.headless = not visible
            return webdriver.Chrome(options=options)
        elif browser_name.lower() == DriverFactory.DRIVER_FIREFOX:
            options = webdriver.firefox.options.Options()
            options.headless = not visible
            return webdriver.Firefox(options=options)
        else:
            raise Exception('No webdriver installed.')
