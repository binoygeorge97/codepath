'''
In a reality TV show, contestants are challenged to do the best recreation of a meal cooked by an all-star judge using limited resources. 
The meal they must recreate is represented by the string target_meal. The contestants are given a collection of ingredients represented by the string ingredients.

Help the contestants by writing a function max_attempts() that returns the maximum number of copies of target_meal they can create using the given ingredients. 
You can take some letters from ingredients and rearrange them to form new strings.
'''

"""
U: target_meal -> meal to be recreated. ingredients -> each letter represents an ingredient. Goal -> Find how many meals we can make with the ingredients.
M: dictionary.
P: keeps count of how many times a letter appears in ingredients. also check for target_meal. then divide the frequency of letter sin ingrdients by the frequency of the same letter in target_meal.
take the floor of the result of each frequency and then the minimum of that will be the number of melas we can make.
I: 
"""

from collections import Counter

def max_attempts(ingredients, target_meal):
    ingredient_count = Counter(ingredients)
    target_meal_count = Counter(target_meal)
    meal = {}
    for letter in target_meal_count:
        if letter not in ingredient_count:
            return 0
        elif letter in ingredient_count:
            meal[letter] = ingredient_count[letter] // target_meal_count[letter]
    return min(meal.values())

ingredients1 = "aabbbcccc"
target_meal1 = "abc"

ingredients2 = "ppppqqqrrr"
target_meal2 = "pqr"

ingredients3 = "ingredientsforcooking"
target_meal3 = "cooking"

print(max_attempts(ingredients1, target_meal1))
print(max_attempts(ingredients2, target_meal2))
print(max_attempts(ingredients3, target_meal3))