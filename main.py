cities_be = input('Введіть через пробіл міста в яких Ви були останні 10 років >>>').title().split()
cities_want_be = input('Введіть через прбіл міста в яких Ви хочите побувати наступні 10 років >>>').title().split()

cities_be_2 = set(cities_be)
cities_want_be_2 = set(cities_want_be)
# print(cities_be_2)
# print(cities_want_be_2)
cities = (cities_be_2.intersection(cities_want_be_2))
print(cities)

if not cities:
    print('У вас все попереду')
else:
    print(f"неймовірні міста {', '.join(cities)}")
