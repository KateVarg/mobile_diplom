from wikipedia_app_tests.pages.search_page import search_page
from wikipedia_app_tests.pages.welcome_screen_page import welcome_screen_page
import allure


@allure.feature("Главный экран")
@allure.story("Поиск статьи")
@allure.title("Успешный поиск статьи")
def test_search_article_success(mobile_management):
    welcome_screen_page.welcome_screen_skip()
    search_page.search_article_success()


@allure.feature("Главный экран")
@allure.story("Поиск статьи")
@allure.title("Неуспешный поиск статьи")
def test_search_article_fail(mobile_management):
    welcome_screen_page.welcome_screen_skip()
    search_page.search_article_fail()


@allure.feature("Главный экран")
@allure.story("Поиск статьи")
@allure.title("Переход на страницу со статьей")
def test_click_article(mobile_management):
    welcome_screen_page.welcome_screen_skip()
    search_page.search_article_success().click_article()
