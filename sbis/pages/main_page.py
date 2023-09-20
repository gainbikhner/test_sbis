from .base_page import BasePage
from ..locators.locators import MainPageLocators


class MainPage(BasePage):
    """Методы для главной страницы СБИС."""

    def click_on_contact_button(self):
        """Кликнуть по разделу Контакты."""
        self.find_element(MainPageLocators.LOCATOR_CONTACT_BUTTON).click()
