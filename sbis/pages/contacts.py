from .base_page import BasePage
from ..locators.locators import ContactsLocators


class ContactsPage(BasePage):
    """Методы для страницы контактов СБИС."""

    KAMCHATKA_LOCATION = "Камчатский край"
    KAMCHATKA_URL = "https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients"
    KAMCHATKA_TITLE = "СБИС Контакты — Камчатский край"

    def click_on_tensor_banner(self):
        """Кликнуть по баннеру Тензор."""
        self.find_elements(ContactsLocators.LOCATOR_TENSOR_BANNERS)[0].click()

    def find_location_element(self):
        """Найти кнопку местоположения."""
        return self.find_element(ContactsLocators.LOCATOR_CURRENT_LOCATION)

    def is_current_location(self, location):
        """Проверить соответствие местоположения."""
        return self.find_location_element().text == location

    def get_partners_list_elements(self):
        """Получить список элементов списка партнеров."""
        return self.find_elements(ContactsLocators.LOCATOR_PARTNERS_LIST)

    def is_partners_list_displayed(self):
        """Проверить отображение списка партнеров."""
        elements = self.get_partners_list_elements()
        return len(elements) != 0

    def change_location_to_kamchatka(self):
        """Изменить местоположение на Камчатский край."""
        self.find_location_element().click()
        self.wait_until_visible(ContactsLocators.LOCATOR_KAMCHATKA_BUTTON)
        self.find_element(ContactsLocators.LOCATOR_KAMCHATKA_BUTTON).click()
        self.wait_until_url_changed(self.KAMCHATKA_URL)

    def is_location_changed_to_kamchatka(self):
        """Проверить изменение местоположения на Камчатский край."""
        return self.is_current_location(self.KAMCHATKA_LOCATION)

    def is_partners_list_changed(self, partners_list_elements):
        """Проверить изменение списка партнеров."""
        return self.get_partners_list_elements != partners_list_elements

    def is_url_contains_kamchatka(self):
        """Проверить, что url содержит информацию о Камчатском крае."""
        return self.get_current_url() == self.KAMCHATKA_URL

    def is_title_contains_kamchatka(self):
        """Проверить, что заголовок содержит информацию о Камчатском крае."""
        return self.get_current_title() == self.KAMCHATKA_TITLE
