from api.card_validation import CardValidator
from api.payment_api import PaymentAPI

class CardHandler:
    def __init__(self):
        self.validator = CardValidator()
        self.payment_api = PaymentAPI()

    def validate_card(self, card_number: str) -> dict:
        """
        Validate the credit card number.

        Args:
            card_number (str): The credit card number as a string.

        Returns:
            dict: A dictionary containing the validation results.
        """
        return self.validator.validate_card(card_number)

    def process_payment(self, card_number: str, amount: float) -> dict:
        """
        Process payment using the credit card.

        Args:
            card_number (str): The credit card number as a string.
            amount (float): The amount to be charged.

        Returns:
            dict: A dictionary containing the payment processing results.
        """
        # Validate the card first
        validation_result = self.validate_card(card_number)
        
        if not validation_result['is_valid']:
            return {
                "success": False,
                "message": "Invalid card details.",
                "validation_result": validation_result
            }

        # If the card is valid, process the payment
        payment_result = self.payment_api.process_payment(card_number, amount)
        return payment_result

# Example usage
if __name__ == "__main__":
    card_handler = CardHandler()
    
    # Example card number and amount
    card_number = "4111 1111 1111 1111"  # Example Visa card number
    amount = 100.00  # Amount to charge

    # Validate card
    validation_result = card_handler.validate_card(card_number)
    print("Validation Result:", validation_result)

    # Process payment
    payment_result = card_handler.process_payment(card_number, amount)
    print("Payment Result:", payment_result)
