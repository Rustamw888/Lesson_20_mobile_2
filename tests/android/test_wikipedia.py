from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from selene.support.by import text
from selene.support.shared import browser
from allure import step

from mobile_tests_lesson_20.model import app


def test_search():
    app.given_opened()

    with step('Search for content'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type(
            'BrowserStack'
        )

    with step('Content should be found'):
        browser.all(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
        ).should(have.size_greater_than(0))


def test_the_four_screens():
    app.given_opened()

    with step('First page checking'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/secondaryTextView')).should_have(text(
            'We’ve found the following on your device:'))
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step('Second page checking'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should_have(text(
            'New ways to explore'))
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step('Third page checking'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should_have(text(
            'Reading lists with sync'))
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/imageViewCentered')).should(be.visible)
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step('Fourth page checking'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/switchView')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_done_button')).should_have(text(
            'GET STARTED'))
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_container')).should(be.visible)
