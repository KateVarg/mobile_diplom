from wikipedia_app_tests.pages.welcome_screen_page import welcome_screen_page
import allure


@allure.feature("Приветственный экран")
@allure.story("Проверка приветственного экрана")
@allure.title("Переход по кнопке Continue")
def test_welcome_screen(mobile_management):

    welcome_screen_page.welcome_screen()

