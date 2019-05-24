import random

def remove_floating_point(value: float) -> int:
    value = int(value*100)
    return value

def add_floating_point(value: int) -> float:
    value = float(value/100)
    return value

def equally_divided_price_and_rest(price: int, divisions: int) -> tuple:
    value, rest = divmod(price, divisions)
    return value, rest

def select_random_users_to_pay_difference(user_ids: list, rest_of_division: int) -> list:
    available_users = user_ids.copy()
    result = list()

    for value in range(rest_of_division):
        user_id = random.choice(available_users)
        result.append(user_id)
        available_users.remove(user_id)

    return result

def calculate_price_for_each_user(price: int, user_ids: list) -> dict:
    price = remove_floating_point(price)
    value_per_person, rest_of_division= equally_divided_price_and_rest(price, len(user_ids))
    price_for_each_user = dict()
    
    # calculate the base value for each user
    for id in user_ids:
        price_for_each_user[id] = value_per_person
    
    # add the extra values to random users
    payers_of_the_difference = select_random_users_to_pay_difference(user_ids, rest_of_division)
    for payer in payers_of_the_difference:
        price_for_each_user[payer] += 1

    return price_for_each_user

def show_values(values: dict) -> None:
    for k, v in values.items():
        print(f"user: {k}, value: {add_floating_point(v)}")
    print(f"sum: {add_floating_point(sum(values.values()))}")
