
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "environment"))

from behave import given, then, when

from browser_manager import (
	close_browser,
	is_page_loaded,
	launch_browser,
	maximize_browser,
)

from libraries.wait_actions import WaitActions
from object_repository.landing_page import HomeObjects
from data_read import get_test_data
from navigation import navigate_to_url
from libraries.assertion_actions import AssertionActions
from libraries.browser_actions import BrowserActions
from element_actions import ElementActions

BASE_URL = get_test_data("website_URL")


def cleanup_browser(context):
	if context.browser is not None:
		close_browser(context.browser)
		context.browser = None
		context.page = None


@given("User navigates to Git website")
def step_navigate_to_git_website(context):
	context.browser = launch_browser()
	context.add_cleanup(cleanup_browser, context)
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
	cleanup_browser(context)


@then("User verifies Download Git is displayed")
def step_verify_download_git_is_displayed(context):
	AssertionActions.verify_true(
		ElementActions.exists(context.page, HomeObjects.landingDownloadBtn)
	)


@then("User verifies About menu is displayed")
def step_verify_about_menu_is_displayed(context):
	AssertionActions.verify_true(
		ElementActions.exists(context.page, HomeObjects.landingPageAbout)
	)


@then("User verifies Search field is displayed")
def step_verify_search_field_is_displayed(context):
	AssertionActions.verify_true(
		ElementActions.exists(context.page, HomeObjects.landingSearchTab)
	)

@when("User clicks Download Button")
def step_clicks_download_button(context):
	ElementActions.click(context.page, HomeObjects.landingDownloadBtn)

@then("User should navigate to Download Page")
def step_navigate_to_download_page(context):
	AssertionActions.verify_equals(
		BrowserActions.get_url(context.page), get_test_data("download_page_URL")
	)

@when("User clicks About Menu")
def step_click_about_menu(context):
	ElementActions.click(context.page, HomeObjects.landingPageAbout)

@then("User should navigate to About Page")
def step_navigate_to_about_page(context):
	AssertionActions.verify_equals(
		BrowserActions.get_url(context.page), get_test_data("about_page_URL")
	)

@when("User clicks Learn Menu")
def step_click_learn_menu(context):
	ElementActions.click(context.page, HomeObjects.landingLearnBtn)

@then("User should navigate to Git Learn Page")
def step_navigate_to_learn_page(context):
	AssertionActions.verify_equals(
		BrowserActions.get_url(context.page), get_test_data("learn_page_URL")
	)

@when("User clicks Tools Menu")
def step_click_tool_menu(context):
	ElementActions.click(context.page, HomeObjects.landingToolsBtn)

@then("User should navigate to Tools Page")
def step_navigate_to_Tools_Page(context):
	AssertionActions.verify_equals(
		BrowserActions.get_url(context.page), get_test_data("tools_page_URL")
	)

@when("User searches for '{search_text}'")
def step_search(context, search_text):
	ElementActions.enter_text(context.page, HomeObjects.landingSearchTab, search_text)
	ElementActions.send_keys(context.page, HomeObjects.landingSearchTab, "Enter")


@then("Relevant search results should be displayed")
def step_results_displayed(context):
	results = context.page.locator(HomeObjects.searchPageResults)
	results.wait_for(state="visible", timeout=10000)
	AssertionActions.verify_true(results.count() > 0)

@then("Search results should be displayed")
def step_results_displayed(context):
	results = context.page.locator(HomeObjects.searchPageResults)
	results.wait_for(state="visible", timeout=10000)
	AssertionActions.verify_true(results.count() > 0)

@then("No relevant results should be displayed")
def step_no_search_results(context):
	results = context.page.locator(HomeObjects.searchPageResults)
	results.wait_for(state="visible", timeout=10000)
	AssertionActions.verify_equals(results.locator("li").count(), 0)

@when("User searches with empty value")
def step_search_with_empty_value(context):
	ElementActions.clear_text(context.page, HomeObjects.landingSearchTab)
	ElementActions.send_keys(context.page, HomeObjects.landingSearchTab, "Enter")

@then("User should remain on current page")
def step_remain_current_page(context):
	AssertionActions.verify_equals(
		BrowserActions.get_url(context.page), get_test_data("website_URL")
	)

@then("Git logo should be displayed")
def step_git_logo(context):
	ElementActions.exists(context.page, HomeObjects.landingGitLogo)

@then("Header section should be displayed")
def step_header_displayed(context):
	ElementActions.exists(context.page, HomeObjects.landingGitHeader)

@then("Footer section should be displayed")
def step_footer_displayed(context):
	ElementActions.exists(context.page, HomeObjects.landingFooter)

@then("User should see all navigation menus")
def step_navigation_menus(context):
	ElementActions.exists(context.page, HomeObjects.landingNavMenus)

@when("User clicks '{search_text}'")
def step_click_on_menus(context, search_text):
	locator = f"//nav[@id='front-nav']//a[.//h3[normalize-space()='{search_text}']]"
	ElementActions.click(context.page, locator)

@then("User should navigate to '{destination_page}'")
def step_user_navigate_page(context, destination_page):
	AssertionActions.verify_equals(
		BrowserActions.get_url(context.page), get_test_data(destination_page)
	)

@given("User navigates to invalid Git URL")
def step_navigate_to_invalid_git_url(context):
	invalid_url = get_test_data("invalid_website_URL")
	context.browser = launch_browser()
	context.add_cleanup(cleanup_browser, context)
	context.page = context.browser.new_page(no_viewport=True)
	maximize_browser(context.page)
	context.page.goto(invalid_url)

@then("Error page should be displayed")
def step_error_page_displayed(context):
	ElementActions.exists(context.page, HomeObjects.landingErrorPage)

@when("User refreshes page")
def step_user_refreshes_page(context):
	BrowserActions.refresh_page(context.page)
	WaitActions.wait_for_page_load(context.page, 15000)

@then("Landing page should remain functional")
def step_landing_page_functional(context):
	ElementActions.click(context.page, HomeObjects.landingPageAbout)
	AssertionActions.verify_equals(
		BrowserActions.get_url(context.page), get_test_data("about_page_URL")
	)

@when("User opens Downloads page")
def step_user_opens_downloads_page(context):
	ElementActions.click(context.page, HomeObjects.landingDownloadBtn)
	WaitActions.wait_for_page_load(context.page, 15000)
	AssertionActions.verify_equals(
		BrowserActions.get_url(context.page), get_test_data("download_page_URL")
	)

@when("User navigates back")
def step_user_navigates_back(context):
	BrowserActions.navigate_back(context.page)
	WaitActions.wait_for_page_load(context.page, 15000)

@then("Git landing page should be visible")
def step_git_landing_page_visible(context):
	AssertionActions.verify_equals(
		BrowserActions.get_url(context.page), get_test_data("website_URL")
	)

@then("Page should load successfully")
def step_page_load_successfully(context):
	AssertionActions.verify_equals(
		BrowserActions.get_url(context.page), get_test_data("website_URL")
	)

@given("User navigates to Downloads page")
def steps_navigate_Download_Page(context):
	context.browser = launch_browser()
	context.add_cleanup(cleanup_browser, context)
	context.page = context.browser.new_page(no_viewport=True)
	maximize_browser(context.page)
	navigate_to_url(context.page)

	ElementActions.click(context.page, HomeObjects.landingDownloadBtn)
	WaitActions.wait_for_page_load(context.page, 15000)
	AssertionActions.verify_equals(
		BrowserActions.get_url(context.page), get_test_data("download_page_URL")
	)

@then("User should be able to retrieve current URL")
def step_retrieve_current_url(context):
	AssertionActions.verify_equals(
		BrowserActions.get_url(context.page), get_test_data("website_URL")
	)
