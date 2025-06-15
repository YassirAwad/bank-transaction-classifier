from src.preprocess import replace_tokens

def test_basic_replacement():
    example = "POS Purchase Col Cacchio Bryanston"
    result = replace_tokens(example)
    assert "[Restaurant]" in result
    assert "[Location]" in result
