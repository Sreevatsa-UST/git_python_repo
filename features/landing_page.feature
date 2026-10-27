Feature: Git Landing Page Validation

Scenario: Verify Git landing page loads successfully
  Given User navigates to Git website
  Then User verifies the page is loaded
  And User verifies the URL is "https://git-scm.com/"
  And User verifies the page title contains "Git"
  And User closes the browser