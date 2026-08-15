import os
import re
from pathlib import Path
from typing import Any, Dict, List, NamedTuple

SKIP_ENTRIES = {
    'index.md',
    'recept_prompt.md'
}

TITLE_RE = re.compile(r'# (.*)')


class Recipe(NamedTuple):
    title: str
    duration: int
    porties: int
    categories: List[str]


def parse_frontmatter(frontmatter: str) -> Dict[str, Any]:
    output = {}
    for line in frontmatter.split('\n'):
        if not line:
            continue

        key, value = line.split(': ', 1)
        parsed_value = int(value) if value.isnumeric() else value
        output[key] = parsed_value
            
    return output


def recipe_processor(recipe_file: Path) -> Recipe:
    raw_recipe = recipe_file.read_text(encoding="utf-8")
    title_m = TITLE_RE.search(raw_recipe)
    frontmatter = raw_recipe.split('---', 2)[1]
    metadata = parse_frontmatter(frontmatter)
    
    if not title_m:
        raise ValueError(f"Recipe {recipe_file} doesn't match required format")

    return Recipe(
        title_m.group(1),
        metadata['bereidingstijd'],
        metadata['porties'],
        []
    )

def main():
    file_list = {f_name for f_name in os.listdir() if f_name.endswith('.md')}
    recipes = file_list - SKIP_ENTRIES

    index = "# Recepten\n\n"
    for recipe in sorted(recipes):
        r = recipe_processor(Path(recipe))
        
        index += f"- [{r.title}]({recipe})\n"
    
    with open('index.md', 'w') as f:
        f.write(index)
    
if __name__ == '__main__':
    main()