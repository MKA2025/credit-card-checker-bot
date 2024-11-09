import requests
from config import Config

class PaymentAPI:
    def __init__(self):
        self.api_url = Config.PAYMENT_API_URL
        self.api_key = Config.PAYMENT_API_KEY

    def check_card_status(self, card_number: str) -> dict:
        """
        Check the status of the credit card by making a request to the payment API.

        Args:
            card_number (str): The credit card number as a string.

        Returns:
            dict: A dictionary containing the status of the credit card.
        """
        payload = {
            'card_number': card_number,
            'api_key': self.api_key
        }

        try:
            response = requests.post(self.api_url, json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response

        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def process_payment(self, card_number: str, amount: float) -> dict:
        """
        Process a payment using the credit card.

        Args:
            card_number (str): The credit card number as a string.
            amount (float): The amount to charge.

        Returns:
            dict: A dictionary containing the result of the payment processing.
        """
        payload = {
            'card_number': card_number,
            'amount': amount,
            'api_key': self.api_key
        }

        try:
            response = requests.post(f"{self.api_url}/process_payment", json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response

        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    payment_api = PaymentAPI()
    
    # Check card status
    card_number = "4111 1111 1111 1111"  # Example Visa card number
    status_response = payment_api.check_card_status(card_number)
    print("Card Status Response:", status_response)

    # Process a payment
    payment_response = payment_api.process_payment(card_number, 100.00)
    print("Payment Response:", payment_response)
