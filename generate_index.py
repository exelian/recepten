import os

SKIP_ENTRIES = {
    __file__,
    '.git',
    'index.md',
    'recept_prompt.md',
    'CNAME'
}

def main():
    file_list = set(os.listdir())
    recipes = file_list - SKIP_ENTRIES

    index = "# Recepten\n\n"
    for recipe in sorted(recipes):
        f_recipe = open(recipe)
        header = f_recipe.read().split('\n', 1)[0][2:]
        index += f"- [{header}]({recipe})\n"
    
    with open('index.md', 'w') as f:
        f.write(index)
    
if __name__ == '__main__':
    main()