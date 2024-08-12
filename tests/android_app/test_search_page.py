from mobile_diplom.pages.search_page import search_page
from mobile_diplom.pages.welcome_screen_page import welcome_screen_page


def test_search_article(mobile_management):
    welcome_screen_page.welcome_screen_skip()
    search_page.search_article()


def test_click_article(mobile_management):
    welcome_screen_page.welcome_screen_skip()
    search_page.search_article().click_article()