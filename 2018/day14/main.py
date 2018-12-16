INPUT = 323081

recipes = [3, 7]

elf1 = 0
elf2 = 1

recipesToMake = INPUT + 10
count = 2
while count < recipesToMake:
    recipe1 = recipes[elf1]
    recipe2 = recipes[elf2]
    newRecipes = list(map(int, list(str(recipe1 + recipe2))))
    recipes.extend(newRecipes)

    elf1 = (elf1 + recipe1 + 1) % len(recipes)
    elf2 = (elf2 + recipe2 + 1) % len(recipes)

    count += len(newRecipes)

print('P1:', ''.join(map(str, recipes[-10:])))

recipes = [3, 7]

elf1 = 0
elf2 = 1

while str(INPUT) not in ''.join(map(str, recipes[-10:])):
# while recipes[-len(digits):] != digits and recipes[-len(digits)-1:-1] != digits: # This is faster than 'in'
    recipe1 = recipes[elf1]
    recipe2 = recipes[elf2]
    newRecipes = list(map(int, str(recipe1 + recipe2)))
    recipes.extend(newRecipes)

    elf1 = (elf1 + recipe1 + 1) % len(recipes)
    elf2 = (elf2 + recipe2 + 1) % len(recipes)

print('P2:', ''.join(map(str, recipes)).index(str(INPUT)))
