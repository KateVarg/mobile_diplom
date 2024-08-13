import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class MainPage:

    def search_article_success(self):
        with allure.step('Ввод запроса в поле поиска'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Selene')

        with allure.step('Проверка результатов поиска'):
            results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
            results.should(have.size_greater_than(0))
            results.first.should(have.text('Selene'))

        return self

    def click_article(self):
        with allure.step('Проверка нажатия на статью в результате поиска'):
            elements = browser.all((AppiumBy.CLASS_NAME, 'android.view.ViewGroup'))
            desired_element = elements[2]
            desired_element.click()

        return self

    def search_article_fail(self):
        with allure.step('Ввод запроса в поле поиска'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('!@#$%')

        with allure.step('Проверка результатов поиска'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/results_text')).should(have.text('No results'))

        return self


main_page = MainPage()
