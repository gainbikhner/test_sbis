from selenium.webdriver.common.by import By


class MainPageLocators:
    "Локаторы для главной страницы СБИС."
    LOCATOR_CONTACT_BUTTON = (
        By.XPATH,
        (
            "//a[text()='Контакты' and "
            "contains(@class, 'sbisru-Header__menu-link')]"
        ),
    )


class ContactsLocators:
    "Локаторы для страницы контактов СБИС."
    LOCATOR_TENSOR_BANNERS = (
        By.XPATH,
        "//img[@alt='Разработчик системы СБИС — компания «Тензор»']",
    )
    LOCATOR_CURRENT_LOCATION = (By.CLASS_NAME, "sbis_ru-Region-Chooser__text")
    LOCATOR_PARTNERS_LIST = (By.CLASS_NAME, "controls-Tree__item")
    LOCATOR_KAMCHATKA_BUTTON = (By.XPATH, "//span[@title='Камчатский край']")


class TensorLocators:
    "Локаторы для главной страницы Тензор."
    LOCATOR_STRENGTH_IN_PEOPLE = (By.XPATH, "//p[text()='Сила в людях']")
    LOCATOR_STRENGTH_IN_PEOPLE_MORE = (
        By.XPATH,
        "//a[text()='Подробнее' and @href='/about']",
    )


class TensorAboutLocators:
    "Локаторы для страницы о компании Тензор."
    LOCATOR_PHOTOS_WORK = (
        By.XPATH,
        "//img[@class='tensor_ru-About__block3-image new_lazy']",
    )
