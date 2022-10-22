import openai
import os


class Recipe:
    def __init__(self, api_key=None):
        # list of ingredients extracted
        self.ingredients = self.extractIngredients
        self.num = self.__num
        self.api_key = api_key

    def generateRecipe(self):
        openai.api_key = self.api_key

        if self.num == 1:
            fullPrompt = "give me a recipe that uses either"
        else:
            fullPrompt = "give me " + self.num + " recipes uses either "

        for ing in self.ingredients:
            fullPrompt += ing + " and "

        recipe = openai.Completion.create(
            engine="text-davinci-002",
            prompt=fullPrompt,
            temperature=0.7,
            max_tokens=1200,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        # name = index 0, ingredients = index 1, directions = index 2
        recipeParts = recipe.split('Ingredients:')
        recipe = recipeParts[1]
        recipeLeftover = recipe.split('Directions:')
        recipeParts[1] = recipeLeftover[0]
        recipeParts[2] = recipeLeftover[1]

        return (recipeParts)
