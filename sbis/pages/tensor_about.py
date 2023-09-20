from .base_page import BasePage
from ..locators.locators import TensorAboutLocators


class TensorAboutPage(BasePage):
    """Методы для страницы о компании Тензор."""

    URL_TENSOR_ABOUT = "https://tensor.ru/about"

    def is_tensor_about_page(self):
        """Проверить, что открыт раздел О компании."""
        return self.get_current_url() == self.URL_TENSOR_ABOUT

    def is_same_height_and_width_photo_work(self):
        """
        Проверить, что у фото в блоке Работаем одинаковые высота и ширина.
        """
        photos = self.find_elements(TensorAboutLocators.LOCATOR_PHOTOS_WORK)
        last_photo = photos.pop()
        height = last_photo.get_attribute("height")
        width = last_photo.get_attribute("width")
        for photo in photos:
            if (
                photo.get_attribute("height") != height
                or photo.get_attribute("width") != width
            ):
                return False
        return True
