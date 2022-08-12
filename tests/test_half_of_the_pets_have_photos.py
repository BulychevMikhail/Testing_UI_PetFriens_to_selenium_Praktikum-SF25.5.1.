from conftest import *


# def test_half_of_the_pets_have_photos(go_to_my_pets):
#     """Поверяем что на странице со списком моих питомцев хотя бы у половины питомцев есть фото"""
#
#     # Сохраняем в переменную statistic элементы статистики
#     statistic = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")
#
#     # Сохраняем в переменную images элементы с атрибутом img
#     images = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')
#
#     # Получаем количество питомцев из данных статистики
#     number = statistic[0].text.split('\n')
#     number = number[1].split(' ')
#     number = int(number[1])
#
#     # Находим половину от количества питомцев
#     half = number // 2
#
#     # Находим количество питомцев с фотографией
#     number_photos = 0
#     for i in range(len(images)):
#         if images[i].get_attribute('src') != '':
#             number_photos += 1
#
#     # Проверяем что количество питомцев с фотографией больше или равно половине количества питомцев
#     assert number_photos >= half
#     print(f'\nКоличество фото: {number_photos}')
#     print(f'\nПоловина от числа питомцев: {half}')




def test_half_of_the_pets_have_photos(go_to_my_pets):
    """Поверяем, что на странице со списком моих питомцев хотя бы у половины питомцев есть фото"""
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//tbody")))
    pets_list = pytest.driver.find_element(By.XPATH, "//tbody")
    # Вычленяем список питомцев по тегу img
    pets_list_photo = pets_list.find_elements(By.TAG_NAME, 'img')
    # Считаем кол-во тех питомцев, у которых значение абрибута scr в теге img не равно нулю, то есть есть ссылка на фото
    counter = 0
    for i in pets_list_photo:
        if i.get_attribute('src') != "":
            counter += 1
    # Проверяем, что питомцев с фото больше либо равно половине всего списка питомцев с тегом img
    assert counter >= len(pets_list_photo) / 2


# python -m pytest -v --driver Chrome --driver-path C:\\chromedriver\\chromedriver.exe test_half_of_the_pets_have_photos.py
# Статистика на момент запуска теста: 1 вариант: Всего питомцев 19, с фото 9: ОР: FAILED  ФР: FAILED
#                                     2 вариант: Всего питомцев 10, с фото 9: ОР: PASSED  ФР: PASSED


