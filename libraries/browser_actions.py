# Browser action 

class BrowserActions:
    # Refresh Page
    def refresh_page(page):
        page.reload()
        page.wait_for_load_state("load")

    # # Get Current URL 
    # def get_current_url(page):
    #     return page.url

    # Get Current Page URL
    def get_url(page):
        try:
            return page.url
        except Exception as e:
            raise Exception(
                f"Failed to get current URL. Error: {e}"
            )

    # Get Title Of Current Page
    def get_title(page):
        try:
            return page.title()
        except Exception as e:
            raise Exception(
                f"Failed to get page title. Error: {e}"
            )

    # Nagigate back to previous page
    def navigate_back(page):
        try:
            page.go_back()
            return True
        except Exception as e:
            raise Exception(
                f"Failed to navigate back. Error: {e}"
            )

    # Navigate forward to next page
    def navigate_forward(page):
        try:
            page.go_forward()
            return True
        except Exception as e:
            raise Exception(
                f"Failed to navigate forward. Error: {e}"
            )