import re

class CardValidator:
    def __init__(self):
        pass

    @staticmethod
    def is_valid_length(card_number: str) -> bool:
        """
        Check if the card number length is valid.

        Args:
            card_number (str): The credit card number as a string.

        Returns:
            bool: True if the length is valid, otherwise False.
        """
        return len(card_number) in [13, 15, 16]

    @staticmethod
    def passes_luhn_algorithm(card_number: str) -> bool:
        """
        Check if the card number passes the Luhn algorithm.

        Args:
            card_number (str): The credit card number as a string.

        Returns:
            bool: True if the card number is valid according to the Luhn algorithm, otherwise False.
        """
        digits = [int(d) for d in card_number if d.isdigit()]
        checksum = 0

        # Double every second digit from the right
        for i in range(len(digits) - 2, -1, -2):
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9

        checksum = sum(digits)

        return checksum % 10 == 0

    @staticmethod
    def is_valid_format(card_number: str) -> bool:
        """
        Check if the card number has a valid format.

        Args:
            card_number (str): The credit card number as a string.

        Returns:
            bool: True if the format is valid, otherwise False.
        """
        return bool(re.match(r'^\d{13,16}$', card_number.replace(" ", "")))

    def validate_card(self, card_number: str) -> dict:
        """
        Validate the credit card number.

        Args:
            card_number (str): The credit card number as a string.

        Returns:
            dict: A dictionary containing the validation results.
        """
        card_number = card_number.replace(" ", "")  # Remove spaces
        results = {
            "valid_length": self.is_valid_length(card_number),
            "valid_format": self.is_valid_format(card_number),
            "passes_luhn": self.passes_luhn_algorithm(card_number),
        }

        results["is_valid"] = all(results.values())
        return results

# Example usage
if __name__ == "__main__":
    validator = CardValidator()
    
    # Example card number
    card_number = "4111 1111 1111 1111"  # Example Visa card number
    validation_result = validator.validate_card(card_number)
    
    print("Validation Result:", validation_result)
