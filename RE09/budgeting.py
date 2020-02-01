#budgeting.py
"""
- checks if the budget is not exceeded, making the appropriate adjustments, 
if needed.
- calculate what products should have their desired quantity
lowered (or even be removed) in order to reduce the total amount to fit the budget
- Examine products with lower price first. 

"""
def budgeting(budget, products, wishlist):
    result={}
    sortedproducts = sorted(products.items(), key=lambda kv: kv[1])
    sortedproducts = sortedproducts[::-1]
    print(sortedproducts)
    for i in sortedproducts:
        """Por cada produto ordenado maior preço para menor"""
        product = i[0]
        price = i[1]
        for a in wishlist:
            "por cada a = key"
            if a == product:
                """se produto está na wishlist"""
                numberofitem = wishlist[product]
                for _ in range(int(numberofitem)):
                    """se tiver mais que 1 produto"""
                    if budget >= price:
                        """"verifica se pode adicionar ou se passa o budget"""
                        if product not in result:
                            """Verifica se o produto ja está no result, se não estiver adiciona"""
                            result[product] = 1
                        else:
                            result[product] += 1
                        budget = budget - price
    return result    
    
print(budgeting(1500, {'xbox': 250, 'smartphone': 500, 'jeans': 50,
'pc': 600, 'glasses': 100}, {'glasses': 3, 'jeans': 2, 'pc': 1,
'xbox':1})
)