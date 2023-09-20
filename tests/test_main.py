from sbis.pages.main_page import MainPage
from sbis.pages.contacts import ContactsPage
from sbis.pages.tensor import TensorPage
from sbis.pages.tensor_about import TensorAboutPage


def test_first_script(driver):
    """Первый сценарий."""
    main_page = MainPage(driver)
    main_page.go_to_site()
    main_page.click_on_contact_button()

    contacts_page = ContactsPage(driver)
    contacts_page.click_on_tensor_banner()
    contacts_page.switch_to_next_window()

    tensor_page = TensorPage(driver)
    assert tensor_page.is_strength_in_people_displayed(), (
        "Блок Сила в людях отсутствует."
    )
    tensor_page.click_on_strength_in_people_more()

    tensor_about_page = TensorAboutPage(driver)
    assert tensor_about_page.is_tensor_about_page(), (
        "Не открыт раздел О компании."
    )
    assert tensor_about_page.is_same_height_and_width_photo_work(), (
        "У фото не совпадают размеры."
    )


def test_second_script(driver):
    """Второй сценарий."""
    # Ваше текущее местоположние.
    current_location = "Свердловская обл."

    main_page = MainPage(driver)
    main_page.go_to_site()
    main_page.click_on_contact_button()

    contacts_page = ContactsPage(driver)
    assert contacts_page.is_current_location(current_location), (
        "Текущее местоположение не совподает."
    )
    assert contacts_page.is_partners_list_displayed(), (
        "Отсутствует список партненов."
    )
    partners_list_elements = contacts_page.get_partners_list_elements()
    contacts_page.change_location_to_kamchatka()
    assert contacts_page.is_location_changed_to_kamchatka(), (
        "Камчатский край не является текущим местоположением."
    )
    assert contacts_page.is_partners_list_changed(partners_list_elements), (
        "Список партнеров не изменился."
    )
    assert contacts_page.is_url_contains_kamchatka(), (
        "URL не содержит информации о Камчатском крае."
    )
    assert contacts_page.is_title_contains_kamchatka(), (
        "Заголовок страницы не содержит информации о Камчатском крае."
    )
