import re
import requests
from config import Config

def validate_card(card_number: str) -> bool:
    """
    Validate the credit card number using the Luhn algorithm.
    
    Args:
        card_number (str): The credit card number as a string.
    
    Returns:
        bool: True if the card number is valid, False otherwise.
    """
    # Remove spaces and hyphens
    card_number = re.sub(r'\D', '', card_number)
    
    if not card_number.isdigit() or len(card_number) < 13 or len(card_number) > 19:
        return False

    total = 0
    reverse_digits = card_number[::-1]

    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:  # Double every second digit
            n *= 2
            if n > 9:  # If the result is greater than 9, subtract 9
                n -= 9
        total += n

    return total % 10 == 0

def check_card_status(card_number: str) -> str:
    """
    Check the status of the credit card by making a request to the payment API.
    
    Args:
        card_number (str): The credit card number as a string.
    
    Returns:
        str: The status of the credit card.
    """
    # Example payload for the API request
    payload = {
        'card_number': card_number,
        'api_key': Config.PAYMENT_API_KEY  # Add your API key here
    }

    try:
        response = requests.post(Config.PAYMENT_API_URL, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        
        # Assuming the API returns a JSON with a 'status' field
        if 'status' in data:
            return f"Card Status: {data['status']}"
        else:
            return "Status information not available from the API."
    
    except requests.exceptions.RequestException as e:
        return f"Error checking card status: {str(e)}"

# Example usage
if __name__ == "__main__":
    test_card = "4111 1111 1111 1111"  # Example Visa card number
    if validate_card(test_card):
        print("Valid card number.")
        status = check_card_status(test_card)
        print(status)
    else:
        print("Invalid card number.")
