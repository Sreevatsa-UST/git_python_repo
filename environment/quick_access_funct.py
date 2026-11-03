
import sys
from pathlib import Path

# To access folders from other paths
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from browser_manager import launch_browser
from navigation import navigate_to_url
from browser_manager import maximize_browser
from browser_manager import is_page_loaded
from browser_manager import close_browser

from object_repository.landing_page import HomeObjects

from environment.data_read import get_test_data
from environment.element_actions import ElementActions

from libraries.browser_actions import BrowserActions

from libraries.wait_actions import WaitActions

from libraries.assertion_actions import AssertionActions

from libraries.screenshot_actions import ScreenshotActios

browser = launch_browser()

page = browser.new_page(no_viewport=True)

navigate_to_url(page)

maximize_browser(page)

pageLoad = is_page_loaded(page)

#### Element Actions ####
# ElementActions.click(page, HomeObjects.landingPageAbout) #Click Functionality
# ElementActions.enter_text(page, HomeObjects.landingSearchTab, get_test_data("search_text")) #Fetch text from json and enter
# ElementActions.clear_text(page, HomeObjects.landingSearchTab) #Clearing Text
# ElementActions.double_click(page, HomeObjects.landingDayNightIcon) #Double Click
# ElementActions.right_click(page, HomeObjects.landingDayNightIcon) #Right Click
# ElementActions.hover(page, HomeObjects.landingGitTextLnk) #Hover
# ElementActions.get_text(page, HomeObjects.landingPageAbout) #Get Text 
# ElementActions.exists(page, HomeObjects.landingPageAbout) #Exists
# ElementActions.not_exists(page, HomeObjects.landingPageAbout) #NotExists
# ElementActions.send_keys(page, HomeObjects.landingSearchTab, "Enter") #Send HotKeys

#### Browser Actions ####
# BrowserActions.current_url = BrowserActions.get_url(page) #Get Current Page URL
# BrowserActions.title = BrowserActions.get_title(page) #Get Current Page URL
# BrowserActions.navigate_back(page)
# BrowserActions.navigate_forward(page)

#### Wait Actions ####
# WaitActions.wait_for_visibility(page, HomeObjects.landingPageAbout) #Wait for Visible on Screen
# WaitActions.wait_for_clickable(page, HomeObjects.landingPageAbout) #Wait for Object to be Clickable
# WaitActions.wait_for_page_load(page, 15000) #Custom Wait Page Load 
# WaitActions.static_wait(page, 5000) #Static Wait

#### Assertion Actions ####
# AssertionActions.verify_equals((BrowserActions.get_url(page)), "https://git-scm.com/") #Verify Equals by calling a function as args
# AssertionActions.verify_not_equals(BrowserActions.get_url(page), "https://git.com/") #Not Equals
# AssertionActions.verify_contains(BrowserActions.get_url(page), "git") #Verify Contains

#### Screenshot Actions ####
# ScreenshotActios.capture_failure_screenshot(page, "/screenshots/git_homepage.png") #Capture Screenshot
# ScreenshotActios.capture_screenshot(page, "/screenshots/git_homepage.png")

input("Press Enter to close...")

close_browser(browser)