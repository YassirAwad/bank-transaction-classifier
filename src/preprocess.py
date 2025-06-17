import re

# Known vendors (case-normalized)
GROCERS = ["woolworths", "checkers", "pnp", "spar", "superspar"]
RESTAURANTS = ["kfc", "steers", "uber eats", "marble pantry", "zapper", "fournos", "nice on 4th"]
GARAGE = ["engen", "shell", "sasol"]


def replace_tokens(text: str, label: str) -> str:
    """
    Replace specific merchant names, locations, and embedded patterns
    with general class tokens to improve model generalization.
    """

    # --- Step 1: Normalize the text ---
    text = text.lower().strip()

    # --- Step 2: Replace known merchants ---
    grocer_pattern = '|'.join([fr'\b{re.escape(v)}\b' for v in GROCERS])
    text = re.sub(grocer_pattern, '[grocers]', text)

    restaurant_pattern = '|'.join([fr'\b{re.escape(v)}\b' for v in RESTAURANTS])
    text = re.sub(restaurant_pattern, '[restaurant]', text)

    garage_pattern = '|'.join([fr'\b{re.escape(v)}\b' for v in GARAGE])
    text = re.sub(garage_pattern, '[garage]', text)

    # --- Step 3: Replace embedded date patterns ---
    date_pattern = r"\*\s*\d{1,2}\s+[a-zA-Z]{3}"
    text = re.sub(date_pattern, '[date]', text)

    # --- Step 4: Inferred restaurant token for Eating Out ---
    if label == 'Eating Out' and 'pos purchase' in text and '[restaurant]' not in text and '[date]' in text:
        text = re.sub(r"(pos purchase)\s+(.+?)\s+(\[date\])", r"\1 [restaurant] \3", text)

    # --- Step 5: Location insertion for Eating Out ---
    if label == 'Eating Out' and '[restaurant]' in text and '[date]' in text:
        text = re.sub(r"(\[restaurant\])\s+(.+?)\s+(\[date\])", r"\1 [location] \3", text)

    # --- Step 6: Location insertion for Fuel ---
    if label == 'Fuel' and '[garage]' in text and '[date]' in text:
        text = re.sub(r"(\[garage\])\s+(.+?)\s+(\[date\])", r"\1 [location] \3", text)

    return text
