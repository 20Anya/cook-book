with open('cook_book.txt', encoding="utf-8") as file:
  cook_book = {}
  for line in file:
    name_dish = line.strip()
    number_ingredients = int(file.readline())
    products = []
    for i in range(number_ingredients):
      product = file.readline().strip()
      ingredient_name, quantity, measure = product.split(' | ')
      products.append({'ingredient': ingredient_name,
                       'quantity': quantity,
                       'measure': measure})
    file.readline()
    cook_book[name_dish] = products

def get_shop_list_by_dishes(dishes, person_count):
    new_book = {}
    for dish in dishes:
        if dish in cook_book:
          for ingredients in cook_book[dish]:
            ingredient_name1 = ingredients.get('ingredient')
            quantity1 = int(ingredients.get('quantity')) * person_count
            measure1 = ingredients.get('measure')
            if ingredient_name1 in new_book:
                quantity1 += new_book[ingredient_name1]['quantity']
            new_book[ingredient_name1] = {'quantity': quantity1, 'measure': measure1}
        else:
            print(f'Блюда {dish} нет в книге рецептов')
    print(new_book)

get_shop_list_by_dishes(['Омлет', 'Омлет'], 2)











