import re

recipes = [
    {
        "name": "Stir-fry",
        "pattern": re.compile(r"(chicken|beef|tofu).*(rice).*(broccoli|carrot|pepper|onion)", re.IGNORECASE),
        "response": "Based on what you have, a **Stir-fry** sounds perfect! Just cook your protein (chicken/beef/tofu), add veggies, and serve with rice. A little soy sauce will bring it all together."
    },
    {
        "name": "Simple Pasta",
        "pattern": re.compile(r"(pasta|spaghetti|penne).*(tomato|marinara|pesto).*(cheese|parmesan)?", re.IGNORECASE),
        "response": "You've got the makings of a classic **Simple Pasta** dish! Cook the pasta, heat the sauce, and top with cheese if you have some. An easy and delicious meal!"
    },
    {
        "name": "Omelette / Scrambled Eggs",
        "pattern": re.compile(r"(egg|eggs).*(cheese|milk|ham|pepper|onion)", re.IGNORECASE),
        "response": "An **Omelette** or **Scrambled Eggs** would be a great choice. Whisk the eggs (with milk for fluffiness), cook them in a pan, and add your cheese, ham, or veggies."
    },
    {
        "name": "Quesadilla",
        "pattern": re.compile(r"(tortilla).*(cheese).*(chicken|bean)?", re.IGNORECASE),
        "response": "A **Quesadilla** is a fantastic and quick option. Just sprinkle cheese and your filling (chicken/beans) on a tortilla, fold it, and heat it in a pan until the cheese is melted."
    },
    {
        "name": "Basic Salad",
        "pattern": re.compile(r"(lettuce|spinach).*(tomato|cucumber).*(chicken|tuna)?", re.IGNORECASE),
        "response": "It sounds like you can make a fresh **Salad**. Combine your greens and veggies, add a protein like chicken or tuna if you have it, and top with your favorite dressing."
    },
    {
        "name": "Grilled Cheese",
        "pattern": re.compile(r"(bread|toast).*(cheese|cheddar|mozzarella).*(butter)?", re.IGNORECASE),
        "response": "A **Grilled Cheese** sandwich is the way to go! Butter two slices of bread, place cheese in between, and cook in a pan on medium heat until the bread is golden and the cheese is melty."
    },
    {
        "name": "Fried Rice",
        "pattern": re.compile(r"(rice).*(egg|eggs).*(onion|garlic|soy sauce)", re.IGNORECASE),
        "response": "With those ingredients, you're set to make a delicious **Fried Rice**! Sauté your veggies and scrambled egg, then add the rice and a splash of soy sauce. It's a great way to use up leftovers."
    },
    {
        "name": "Chicken and Veggie Soup",
        "pattern": re.compile(r"(chicken|stock|broth).*(carrot|celery|onion).*(noodle|rice)?", re.IGNORECASE),
        "response": "A hearty bowl of **Chicken and Veggie Soup** is exactly what you need. Boil the chicken and vegetables in stock, and add some noodles or rice if you'd like to make it more filling."
    },
    {
        "name": "Tuna Salad",
        "pattern": re.compile(r"(tuna).*(mayonnaise|mayo).*(bread|lettuce)", re.IGNORECASE),
        "response": "It sounds like you have everything for a classic **Tuna Salad Sandwich**! Just mix the tuna with mayonnaise and serve it on bread or over a bed of lettuce for a quick lunch."
    },
    {
        "name": "Black Bean Burgers",
        "pattern": re.compile(r"(black bean|black beans).*(bread|bun).*(onion|garlic|spice|pepper)", re.IGNORECASE),
        "response": "You can make delicious homemade **Black Bean Burgers**! Mash the beans with your spices and onion, form them into patties, and cook them in a pan. Serve on a bun with your favorite toppings."
    },
    {
        "name": "Pancakes",
        "pattern": re.compile(r"(flour|pancake mix).*(egg|eggs).*(milk|butter)", re.IGNORECASE),
        "response": "It sounds like you have everything you need for **Pancakes**! Just whisk the flour or mix with an egg and milk until a smooth batter forms, then cook on a griddle or pan until golden brown."
    },
    {
        "name": "Chili",
        "pattern": re.compile(r"(ground beef|turkey|bean|beans).*(tomato|onion|chili powder)", re.IGNORECASE),
        "response": "You can make a great pot of **Chili**! Brown your meat or beans, then add diced tomatoes, onions, and plenty of chili powder. Let it simmer until the flavors have combined."
    },
    {
        "name": "Baked Potato",
        "pattern": re.compile(r"(potato|potatoes).*(cheese|sour cream|chive|bacon)", re.IGNORECASE),
        "response": "A **Baked Potato** is a fantastic choice. Poke holes in the potato, bake it until tender, then load it up with your favorite toppings like cheese, sour cream, and chives."
    },
    {
        "name": "Basic Tomato Soup",
        "pattern": re.compile(r"(tomato|tomatoes|tomato paste).*(onion|garlic|broth|stock)", re.IGNORECASE),
        "response": "A simple **Tomato Soup** would be delicious. Sauté the onion and garlic, then add the tomatoes and broth. Simmer for a while, and you can blend it for a creamy consistency."
    },
    {
        "name": "Chicken Noodle Soup",
        "pattern": re.compile(r"(chicken|stock|broth).*(noodle|noodles).*(carrot|celery|onion)", re.IGNORECASE),
        "response": "A classic bowl of **Chicken Noodle Soup** is perfect. Combine the chicken, noodles, and vegetables in a pot of broth and simmer until everything is cooked through."
    },
]
