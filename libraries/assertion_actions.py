# Assertion Actions

class AssertionActions: 
    def verify_equals(actual, expected):
        try:
            if actual == expected:
                return True

            raise Exception(
                f"Verification failed. Expected: '{expected}', Actual: '{actual}'"
            )

        except Exception as e:
            raise Exception(str(e))

    # Verify Not Equals 
    def verify_not_equals(actual, expected):
        if actual == expected:
            raise Exception(
                f"Verification failed. Values should not be equal. Actual: '{actual}', Expected: '{expected}'"
            )
        return True
    
    # Verify Consian 
    def verify_contains(actual, expected):
        if expected not in actual:
            raise Exception(
                f"Verification failed. '{expected}' was not found in '{actual}'"
            )
        return True

    #Verify is True
    def verify_true(condition):
        if not condition:
            raise Exception(
                f"Verification failed. Expected True, but got {condition}"
            )
        return True

    # Verify is False
    def verify_false(condition):
        if condition:
            raise Exception(
                f"Verification failed. Expected False, but got {condition}"
            )
        return True