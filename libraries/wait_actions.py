# Wait Actions 

class WaitActions:
    # Wait fro Visible on Screen
    def wait_for_visibility(page, locator, timeout=5000):
        try:
            page.locator(locator).wait_for(
                state="visible",
                timeout=timeout
            )
            return True
        except Exception as e:
            raise Exception(
                f"Locator '{locator}' was not visible within {timeout} ms. Error: {e}"
            )

    # Wait for element to be Clickable 
    def wait_for_clickable(page, locator, timeout=5000):
        try:
            page.locator(locator).wait_for(
                state="visible",
                timeout=timeout
            )
            
            if not page.locator(locator).is_enabled():
                raise Exception("Element is disabled")

            return True

        except Exception as e:
            raise Exception(
                f"Locator '{locator}' was not clickable within {timeout} ms. Error: {e}"
            )

    # Wait for Page Load
    def wait_for_page_load(page, timeout=10000):
        try:
            page.wait_for_load_state(
                state="networkidle",
                timeout=timeout
            )
            return True
        except Exception as e:
            raise Exception(
                f"Page did not reach network idle state within {timeout} ms. Error: {e}"
            )

    # Static Wait
    def static_wait(page, milliseconds):
        try:
            page.wait_for_timeout(milliseconds)
            return True
        except Exception as e:
            raise Exception(
                f"Failed to wait for {milliseconds} milliseconds. Error: {e}"
            )