from langchain.tools import Tool
import requests


def parse_card_data(card_data):
    result = {}
    for key in ["name", "oracle_text", "type_line", "power", "toughness", "color_identity", "cmc"]:
        value = card_data.get(key)
        if value not in (None, "", []):
            # Remove decimals for numbers (e.g., cmc)
            if key == "cmc" and isinstance(value, float):
                value = int(value)
            result[key] = value
    return result

def call_to_scryfall(data: str):
    headers = {"User-Agent": "MtgJudgeApp/1.0", "Accept": "application/json"}
    response = requests.get(
        "https://api.scryfall.com/cards/search",
        params={"q": data},
        headers=headers,
    )
    if response.status_code == 200:
        cards = response.json().get("data", [])
        if not cards:
            print("No cards found for the given query.")
        formatted_text = parse_card_data(cards[0] if cards else {})
        return formatted_text
    else:
        print(f"Error fetching card data: {response.status_code} - {response.text}")
        return "Error: Unable to fetch card data from Scryfall. Please check your query or try again later."


card_lookup_tool = Tool(
    name="card_lookup",
    func=call_to_scryfall,
    description="Lookup a Magic the gathering card for oracle text, type, power, toughness, color identity and cmc",
)
