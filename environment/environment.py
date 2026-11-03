import allure

from libraries.screenshot_actions import ScreenshotActions
from core.browser_manager import BrowserManager


def after_scenario(context, scenario):

    if scenario.status == "failed":

        screenshot_path = (
            ScreenshotActions.capture_failure_screenshot()
        )

        allure.attach.file(
            screenshot_path,
            name="Failure Screenshot",
            attachment_type=
            allure.attachment_type.PNG
        )

    BrowserManager.close_browser()