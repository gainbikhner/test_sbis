from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Общие методы для всех страниц."""

    TIMEOUT = 15

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://sbis.ru/"

    def find_element(self, locator):
        """Найти элемент."""
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        """Найти несколько элементов."""
        return self.driver.find_elements(*locator)

    def go_to_site(self):
        """Перейти на сайт СБИС."""
        return self.driver.get(self.base_url)

    def switch_to_next_window(self):
        """Переключиться на следующую вкладку."""
        self.driver.switch_to.window(self.driver.window_handles[1])

    def get_current_url(self):
        """Получить текущий url страницы."""
        return self.driver.current_url

    def click_on_hidden_element(self, element):
        """Кликнуть по элементу за пределами экрана."""
        self.driver.execute_script("arguments[0].click();", element)

    def wait_until_visible(self, locator):
        """Подождать пока элемент не станет видимым."""
        WebDriverWait(self.driver, self.TIMEOUT, 1).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_until_url_changed(self, url):
        """Подождать пока url не изменится до заданного."""
        WebDriverWait(self.driver, self.TIMEOUT, 1).until(EC.url_to_be(url))

    def get_current_title(self):
        """Получить текущий заголовок страницы."""
        return self.driver.title
