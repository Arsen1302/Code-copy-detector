class Solution:
    def solution_1449_1_1(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph, can_make, supplies = {recipe : [] for recipe in recipes},  {}, set(supplies)
        def solution_1449_1_2(recipe : str) -> bool:
            if recipe not in can_make:
                can_make[recipe] = False
                can_make[recipe] = all([solution_1449_1_2(ingr) for ingr in graph[recipe]])
            return can_make[recipe]
        for i, recipe in enumerate(recipes):
            for ingr in ingredients[i]:
                if ingr not in supplies:
                    graph[recipe].append(ingr if ingr in graph else recipe)
        return [recipe for recipe in recipes if solution_1449_1_2(recipe)]