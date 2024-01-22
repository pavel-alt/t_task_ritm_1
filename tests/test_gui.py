def test_open_home_page(home_page):
    home_page.open_page()
    assert home_page.check_open_page(), 'Домашняя страница не открыта'


def test_open_elements_page(home_page, elements_page):
    home_page.elements.click_on_element()
    assert elements_page.check_open_page(), 'Страница элементов не открыта'


def test_open_check_box_page(elements_page, check_box_page):
    elements_page.check_box.click_on_element()
    assert check_box_page.check_open_page(), 'Страница чекбоксов не открыта'


def test_expand_home_dir(check_box_page):
    check_box_page.expand_home_dir.click_on_element()
    assert check_box_page.check_home_dir_expanded.check_visibility(), ('Проверка на открытие экспандера '
                                                                       'домашней страницы не пройдена')


def test_expand_downloads_dir(check_box_page):
    check_box_page.expand_download_dir.click_on_element()
    assert check_box_page.check_download_dir_expanded.check_visibility(), ('Проверка на открытие экспандера '
                                                                           'страницы загрузок не пройдена')


def test_selected_word_file(check_box_page):
    check_box_page.word_file_check_box_unchecked.click_on_element()
    assert (check_box_page.word_file_check_box_checked.check_visibility() and
            check_box_page.get_actual_result() == 'You have selected :wordFile', ('Проверка на выделение чекбокса и '
                                                                                  'соответствие результирующего '
                                                                                  'ожиданиям текста не пройдена'))
