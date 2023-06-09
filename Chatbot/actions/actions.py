from typing import Any, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# A small dictionary simulating the database
database = {
    "1234567890": {
        "name": "Michael Prasad",
        "balance": 59000
    },
    "0987654321": {
        "name": "Jenny Kumari",
        "balance": 5000
    }
}

class ActionCheckBalance(Action):
    def name(self) -> Text:
        return "action_check_balance"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        account_number = tracker.get_slot("account_number")

        if account_number in database:
            account_info = database[account_number]
            name = account_info["name"]
            balance = account_info["balance"]

            response = f"Dear {name}, your account {account_number} has a balance of Rs. {balance}."
        else:
            response = "Sorry, the provided account number is not valid."

        dispatcher.utter_message(text=response)

        return []

class ActionCheckTransactionHistory(Action):
    def name(self) -> Text:
        return "action_check_transaction_history"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Sorry, transaction history is not available at the moment.")

        return []
