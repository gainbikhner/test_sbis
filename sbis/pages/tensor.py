from .base_page import BasePage
from ..locators.locators import TensorLocators


class TensorPage(BasePage):
    """Методы для главной страницы Тензор."""

    def is_strength_in_people_displayed(self):
        """Проверить видимость блока Сила в людях."""
        element = self.find_element(TensorLocators.LOCATOR_STRENGTH_IN_PEOPLE)
        return element.is_displayed()

    def click_on_strength_in_people_more(self):
        """Кликнуть на Подробнее в блоке Сила в людях."""
        element = self.find_element(
            TensorLocators.LOCATOR_STRENGTH_IN_PEOPLE_MORE
        )
        self.click_on_hidden_element(element)
