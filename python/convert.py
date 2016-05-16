import re

fn_bold = lambda x: "<b>" + x.group() + "</b>"
fn_asterisk = lambda x: "***" + x.group() + "***"

MEASUREMENT_WORDS = set(['tsp','tbsp','cup','ml','gram','g'])
PERMANENT_INGREDIENT_WORDS = set(['salt','pepper'])

RE_WORDS = "[a-zA-Z]+"
RE_INGREDIENTS = "[Ii]ngredients:?.*\n"
RE_DIRECTIONS = "[Dd]irections:?.*\n"

if __name__ == "__main__":
    with open( "pork_chop.txt", 'rb') as fin:
        raw = fin.read()
    parsed = re.split( RE_DIRECTIONS, re.split(RE_INGREDIENTS, raw )[1] )
    ingredients, directions = parsed[:2]
    ingredients_list = [ x.strip() for x in ingredients.split('\n') if x.strip() ]
    ingredients_list = [ x.strip() for x in directions.split('\n') if x.strip() ]
    ingredient_words = set( [ x.lower() for x in re.findall(RE_WORDS, ingredients)]) - MEASUREMENT_WORDS
    ingredient_words = ingredient_words.union(PERMANENT_INGREDIENT_WORDS)
    re_any_ingredient = '|'.join( [ x + "[a-zA-Z\-]*" for x in ingredient_words ])
    bolded_directions = re.sub( re_any_ingredient, fn_asterisk, directions, flags=re.IGNORECASE )
