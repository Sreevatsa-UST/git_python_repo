Feature: Git Landing Page Validation

@Smoke @LandingPage
Scenario: Verify Git landing page loads successfully
  Given User navigates to Git website
  Then User verifies the page is loaded
  And User verifies the URL is "https://git-scm.com/"
  And User verifies the page title contains "Git"
  And User closes the browser

@Smoke
Scenario: Verify Download Git is visible
  Given User navigates to Git website
  Then User verifies Download Git is displayed

@Smoke
Scenario: Verify About menu is visible
  Given User navigates to Git website
  Then User verifies About menu is displayed

@Smoke
Scenario: Verify Search textbox is available
  Given User navigates to Git website
  Then User verifies Search field is displayed

