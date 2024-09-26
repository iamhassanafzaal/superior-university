film_collection = [
    ("The Grand Adventure", 25000000),
    ("Shadows of the Past", 12000000),
    ("A Dream Unraveled", 5500000),
    ("Voyage Across the Seas", 400000000),
    ("Heroes Assemble", 380000000),
    ("The Final Battle", 340000000),
    ("Family Matters", 220000000)
]

def compute_average_budget(films):
    total_budget = sum(budget for _, budget in films)
    return total_budget / len(films) if films else 0

def identify_over_budget_films(films, average_budget):
    expensive_films = []
    for title, budget in films:
        if budget > average_budget:
            extra_cost = budget - average_budget
            expensive_films.append(title)
            print(f"{title} costs: ${budget} (over by: ${extra_cost:.2f}) compared to the average budget of ${average_budget:.2f}")
    print(f"{len(expensive_films)} films are over the average budget.")

def add_new_films(films):
    count = int(input("How many films would you like to add? "))
    for _ in range(count):
        title = input("Enter the title of the film: ")
        budget = int(input("Enter the budget for the film: "))
        films.append((title, budget))
    return films

def main():
    updated_films = add_new_films(film_collection)
    average_budget = compute_average_budget(updated_films)
    print(f"\nThe average budget for the films is: ${average_budget:.2f}")
    identify_over_budget_films(updated_films, average_budget)

if __name__ == "__main__":
    main()
