Feature: Git functional navigation

# Functional navigation scenarios for Git landing page
@Functional
Scenario: Verify Download Page navigation
    Given User navigates to Git website
    When User clicks Download Button
    Then User should navigate to Download Page

@Functional
Scenario: Verify About Page navigation
    Given User navigates to Git website
    When User clicks About Menu
    Then User should navigate to About Page

@Functional
Scenario: Verify Learn page navigation
    Given User navigates to Git website
    When User clicks Learn Menu
    Then User should navigate to Git Learn Page

@Functional
Scenario: Verify Tools Page navigation
    Given User navigates to Git website
    When User clicks Tools Menu
    Then User should navigate to Tools Page

@Functional @Regression 
Scenario Outline: Verify menu navigation
    Given User navigates to Git website 
    When User clicks '<MenuName>'
    Then User should navigate to '<DestinationPage>'

    Examples:
    | MenuName      | DestinationPage       |
    | About         | about_page_URL        |
    | Learn         | learn_page_URL        |
    | Tools         | tools_page_URL        |
    | Reference     | referance_page_URL    |
    | Install       | install_page_URL      |
    | Community     | community_page_URL    |

# Edge cases for Git landing page
@Negative
Scenario: Verify invalid URL handling
    Given User navigates to invalid Git URL
    Then Error page should be displayed

@Negative
Scenario: Verify browser refresh behavior
    Given User navigates to Git website
    When User refreshes page
    Then Landing page should remain functional

@Negative
Scenario: Verify Back navigation
    Given User navigates to Git website
    When User opens Downloads page
    And User navigates back
    Then Git landing page should be visible

@Framework
Scenario: Verify browser refresh action
    Given User navigates to Git website
    When User refreshes page
    Then Page should load successfully

@Framework
Scenario: Verify browser back functionality
    Given User navigates to Downloads page
    When User navigates back
    Then Git landing page should be visible

@Framework
Scenario: Verify current URL retrieval
Given User navigates to Git website
Then User should be able to retrieve current URL