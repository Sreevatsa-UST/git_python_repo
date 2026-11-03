Feature: Git UI Validation

@UI
Scenario: Verify Git logo visibility
    Given User navigates to Git website
    Then Git logo should be displayed

@UI
Scenario: Verify page header section
    Given User navigates to Git website
    Then Header section should be displayed

@UI
Scenario: Verify footer section
    Given User navigates to Git website
    Then Footer section should be displayed

@UI
Scenario: Verify all navigation menus are visible
    Given User navigates to Git website
    Then User should see all navigation menus