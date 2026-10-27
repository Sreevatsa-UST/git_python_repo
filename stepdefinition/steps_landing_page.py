
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from behave import given, then

from environment.browser_manager import (
	close_browser,
	is_page_loaded,
	launch_browser,
	maximize_browser,
)
from environment.navigation import navigate_to_url
from libraries.assertion_actions import AssertionActions
from libraries.browser_actions import BrowserActions


BASE_URL = "https://git-scm.com/"


@given("User navigates to Git website")
def step_navigate_to_git_website(context):
	context.browser = launch_browser()
	context.page = context.browser.new_page(no_viewport=True)
	maximize_browser(context.page)
	navigate_to_url(context.page)


@then("User verifies the page is loaded")
def step_verify_page_loaded(context):
	context.page.wait_for_load_state("load")
	AssertionActions.verify_true(is_page_loaded(context.page))


@then('User verifies the URL is "https://git-scm.com/"')
def step_verify_url(context):
	AssertionActions.verify_equals(
		BrowserActions.get_url(context.page),
		BASE_URL,
	)


@then('User verifies the page title contains "Git"')
def step_verify_title(context):
	AssertionActions.verify_contains(
		BrowserActions.get_title(context.page),
		"Git",
	)


@then("User closes the browser")
def step_close_browser(context):
	close_browser(context.browser)
