from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class ActionGreet(Action):
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("Hello! I can help you add two numbers.")
        return []


class ActionCalculateSum(Action):

    def name(self) -> Text:
        return "action_calculate_sum"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        number1 = tracker.get_slot("num1")
        number2 = tracker.get_slot("num2")

        if number1 is not None and number2 is not None:
            result = int(number1) + int(number2)
            message = f"The sum of {number1} and {number2} is {result}."
        else:
            message = "I could not find both numbers. Please provide them."

        dispatcher.utter_message(text=message)
        return []

class ActionCalculateDiff(Action):

    def name(self) -> Text:
        return "action_calculate_diff"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        number1 = tracker.get_slot("num1")
        number2 = tracker.get_slot("num2")

        if number1 is not None and number2 is not None:
            result = int(number1) - int(number2)
            message = f"The difference of {number1} and {number2} is {result}."
        else:
            message = "I could not find both numbers. Please provide them."

        dispatcher.utter_message(text=message)
        return []

class ActionCalculateProd(Action):

    def name(self) -> Text:
        return "action_calculate_prod"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        number1 = tracker.get_slot("num1")
        number2 = tracker.get_slot("num2")

        if number1 is not None and number2 is not None:
            result = int(number1) * int(number2)
            message = f"The product of {number1} and {number2} is {result}."
        else:
            message = "I could not find both numbers. Please provide them."

        dispatcher.utter_message(text=message)
        return []

class ActionCalculateQuo(Action):

    def name(self) -> Text:
        return "action_calculate_quo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        number1 = tracker.get_slot("num1")
        number2 = tracker.get_slot("num2")

        if number1 is not None and number2 is not None:
            result = int(number1) / int(number2)
            message = f"The quotient of {number1} and {number2} is {result}."
        else:
            message = "I could not find both numbers. Please provide them."

        dispatcher.utter_message(text=message)
        return []
