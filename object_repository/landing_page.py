#Object Repository 

class HomeObjects:

    landingGitLogo = "//a[@id='logo']"
    landingGitHeader = "//div[@id='masthead']"
    landingNavMenus = "//section[@id='front-navigation']"
    landingPageAbout = "//nav[@id='front-nav']//h3[contains(text(), 'About')]"
    landingSearchTab = "//form//input[@id='search-text']"
    landingDayNightIcon = "//img[@id='dark-mode-button']"
    landingGitTextLnk = "//p//a[contains(text(), 'free and open source')]"
    landingDownloadBtn = "//div//a[@id='download-link']"
    landingLearnBtn = "//h3[contains(text(), 'Learn')]"
    landingToolsBtn = "//h3[contains(text(), 'Tools')]"
    landingFooter = "//footer//a[contains(text(), 'About this site')]"
    landingErrorPage = "//div//h1[contains(text(), ('That page does'))]"

    searchPageResults = "//p[contains(text(), 'results for')]//..//ol"