import os
import re
from typing import NamedTuple, List

SKIP_ENTRIES = {
    'index.md',
    'recept_prompt.md'
}

TITLE_RE = re.compile(r'# (.*)')


class Recipe(NamedTuple):
    title: str
    categories: List[str]


def recipe_processor(recipe_file: str) -> Recipe:
    f_recipe = open(recipe_file)
    raw_recipe = f_recipe.read()
    f_recipe.close()
    title_m = TITLE_RE.search(raw_recipe)
    if not title_m:
        raise ValueError(f"Recipe {recipe_file} doesn't match required format")

    return Recipe(
        title_m.group(1),
        []
        
    )

def main():
    file_list = {f_name for f_name in os.listdir() if f_name.endswith('.md')}
    recipes = file_list - SKIP_ENTRIES

    index = "# Recepten\n\n"
    for recipe in sorted(recipes):
        r = recipe_processor(recipe)
        
        index += f"- [{r.title}]({recipe})\n"
    
    with open('index.md', 'w') as f:
        f.write(index)
    
if __name__ == '__main__':
    main()