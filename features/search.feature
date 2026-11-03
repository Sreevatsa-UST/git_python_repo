Feature: Git Search

@Smoke @Search
Scenario: Search valid keyword
    Given User navigates to Git website
    When User searches for 'git clone'
    Then Relevant search results should be displayed

@Regression @Search
Scenario: Search with another valid keyword
    Given User navigates to Git website
    When User searches for 'git branch'
    Then Relevant search results should be displayed

@Chrome @Search
Scenario: Search using single character
    Given User navigates to Git website
    When User searches for 'a'
    Then Search results should be displayed

@Chrome @Search
Scenario: Search using special characters
    Given User navigates to Git website
    When User searches for '@#$%^'
    Then No relevant results should be displayed

@Chrome @Search
Scenario: Search with empty text
    Given User navigates to Git website
    When User searches with empty value
    Then User should remain on current page