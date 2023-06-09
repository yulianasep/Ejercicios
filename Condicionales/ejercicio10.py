"""La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus 
clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o 
no, y en función de su respuesta le muestre un menú con los ingredientes 
disponibles para que elija. Solo se puede eligir un ingrediente además de la 
mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar 
por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes 
que lleva
"""

print("Hello! Pizzeria Bella Napoli welcomes you. we are here to assist you,"
      "please enter the number that corresponds to the type of pizza you wish,"
      "to order or enter 0 in any time to exit.")
print("1. Veggie pizza")
print("2. Non-veggie pizza")


order_completed = False

while not order_completed:

    pizza = int(input("\nEnter the number of the pizza you want to order: "))
    error_message = "You have to choose one of the options above"
    sentence_end = "tomato and mozzarella"
    order_completed_message = "\nYour order is complete."

    if pizza == 0:
        print("Thank you for your visit, we hope to see you soon.")
        break

    elif pizza == 1:
        print("You have chosen a veggie pizza, please choose the ingredients"
              "you want to add to your pizza.")
        print("1. Pepper")
        print("2. Tofu")

        while True:
            ingredient = int(
                input("Enter the number of the ingredient you want to add: "))

            if ingredient == 1:
                print(
                    f"You have chosen a veggie pizza with pepper, {sentence_end}")
                order_completed = True
                print(order_completed_message)
                break
            elif ingredient == 2:
                print(
                    f"You have chosen a veggie pizza with tofu, {sentence_end}")
                order_completed = True
                print(order_completed_message)
                break
            else:
                print(error_message)

    elif pizza == 2:
        print("You have chosen a no veggie pizza, please choose the ingredients you want to add to your pizza.")
        print("1. Pepperoni")
        print("2. Ham")
        print("3. Salmon")

        while True:
            ingredient = int(
                input("Enter the number of the ingredient you want to add: "))
            if ingredient == 1:
                print(
                    f"You have chosen a no veggie pizza with pepperoni, {sentence_end}")
                order_completed = True
                print(order_completed_message)
                break
            elif ingredient == 2:
                print(
                    f"You have chosen a no veggie pizza with ham, {sentence_end}")
                order_completed = True
                print(order_completed_message)
                break
            elif ingredient == 3:
                print(
                    f"You have chosen a no veggie pizza with salmon, {sentence_end}")
                order_completed = True
                print(order_completed_message)
                break
            else:
                print(error_message)

    else:
        print(error_message)
