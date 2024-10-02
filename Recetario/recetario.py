from pathlib import Path

# Inicio del programa
print("--------------------------")
print("Bienvenido/a al recetario!")
print("--------------------------")
home = Path.home() / 'Recetas'
files_count = len(list(Path(home).glob("**/*.txt")))
print(f"La ruta donde se encuentran las recetas en tu ordenador es la siguiente:\n\n{home}, donde se encuentran {files_count} recetas!") # Indica ruta de acceso

# Opciones para elegir
def get_option():
    while True:
        try:
            option = int(input(""" 
            Por favor ingresa una de las siguientes opciones:
            [1] - Leer receta
            [2] - Crear receta
            [3] - Crear categoría
            [4] - Eliminar receta
            [5] - Eliminar categoría
            [6] - Finalizar programa
            ------------------------\t
            
            """))

            if option in range(1, 7):
                print(f"Has seleccionado la opción {option}!")
                return option
            else:
                print("Error: Sólo debes ingresar un número entre 1 y 6!")

        except ValueError:
            print("Error: Por favor, debes ingresar un número válido!")


# ELegir categoría
category_paths = {
    1: 'Carnes',
    2: 'Ensaladas',
    3: 'Pastas',
    4: 'Postres'
}
def chose_category():
    try:
        category = int(input("¿Qué categoría eliges?\n" + "\n".join(f"[{key}] - {value}" for key, value in category_paths.items()) + "\n" + "--------------------\n"))

        if category in range(len(category_paths) + 1):
            print(f"Has seleccionado la categoría {category}!")
            return category
        else:
            print(f"Error: Sólo debes ingresar un número entre 1 y {len(category_paths)}.")

    except ValueError:
        print("Error: Por favor, debes ingresar un número válido!")


# Crear categoría
def create_category():
    category = input("Ingresa el nombre de la categoría que quieres crear: ").capitalize()
    if category in category_paths.values():
        print(f"La categoría {category} ya existe")
        return category_paths

    # Crear nueva carpeta
    category_path = Path(home, f"{category}")
    category_path.mkdir(parents=True, exist_ok=True)

    # Añadir al diccionario
    category_paths[len(category_paths) + 1] = f"{category}"
    print(f"La categoría '{category_path.stem}' ha sido creada exitosamente!")
    print(category_paths)

    return category_paths


# Eliminar categoría
def delete_category():
    category = input("Ingresa el nombre de la categoría que quieres eliminar: ").capitalize()
    if category in category_paths.values():
        print(f"La categoría {category} ya existe")
        return category_paths

    # Obtener la clave de la categoría a eliminar
    category_key = [key for key, value in category_paths.items() if value == category][0]

    # Eliminar la carpeta de la categoía
    category_path = Path(home, f"{category}")
    try:
        for recipe in category_path.glob("*.txt"): # Eliminar todas las recetas de la categoría eliminada
            recipe.unlink() # Método para eliminar categoría
        category_path.mkdir() # Eliminar carpeta
        del category_paths[category_key] # Eliminar del diccionario

        print(f"La categoría '{category}' y todas sus recetas (en caso de que las hubiera) han sido eliminadas exitosamente")
        print(category_paths)

    except Exception as e:
        print(f"Error al eliminar la categoría: {e}")

    return category_paths


# 1 -> Leer receta
def read_recipe(cat):
    if cat not in category_paths:
        print("Error: Categoría no válida")
        return

    # Obtener categoría correspondiente
    category_name = category_paths[cat]
    category_path = Path(home, category_name)

    print(f"Has seleccionado la categoría {category_name}!, la cual contiene las siguientes recetas:\n ")

    # Lista de recetas
    recipes = list(category_path.glob("*.txt"))
    for recipe in recipes:
        print(f"{recipe.stem}\n")

    try:
        recipe_name = input("Selecciona la receta que quieres leer: ")
        found = False

        for recipe in recipes:
            if recipe.stem == recipe_name:
                with open(recipe, "r") as file:
                    print("\nContenido de la receta:\n")
                    print(file.read())
                found = True
                break

        if not found:
            print("Error: No se encontró la receta que estás intentando buscar!")

    except ValueError:
        print("Error: Por favor ingresa un valor correcto!")


# 2 --> Crear archivo
def create_recipe(cat):

    if cat not in category_paths:
        print("Error: Categoría no válida")
        return

    # Obtener categoría correspondiente
    category_name = category_paths[cat]
    category_path = Path(home, category_name)

    print(f"Has seleccionado la categoría {category_name}!")

    # Nombre y contenido del archivo
    name = input("Elige la receta que quieres crear: ")
    content = input("Ahora escribe el contenido del archivo: ")
    with open(f"{category_path}/{name}.txt", "w") as file:
        file.write(f"{content}")

    print(f"Se ha creado el archivo {name}.txt exitosamente!")

    file.close()


# 3 --> Eliminar archivo
def delete_recipe(cat):
    if cat not in category_paths:
        print("Error: Categoría no válida")
        return

    # Obtener categoría correspondiente
    category_name = category_paths[cat]
    category_path = Path(home, category_name)

    print(f"Has seleccionado la categoría {category_name}!, la cual contiene las siguientes recetas:\n ")

    # Lista de recetas
    recipes = list(category_path.glob("*.txt"))
    if not recipes:
        print("No hay recetas disponibles para esta categoría en este momento.")
        return

    for recipe in recipes:
        print(f"{recipe.stem}\n")

    try:
        recipe_name = input("Selecciona la receta que quieres eleiminar: ")
        found = False

        for recipe in recipes:
            if recipe.stem == recipe_name:
                recipe.unlink()
                print(f"La receta '{recipe_name}' ha sido eliminada exitosamente.")
                found = True
                break

        if not found:
            print("Error: No se encontró la receta que estás intentando eliminar!")

    except ValueError:
        print("Error: Por favor ingresa un valor correcto!")


### Buble de ejecución del programa ###

while True:
    options = get_option()
    if options == 1:
        print("Has elegido la opción 1: Leer receta\n")
        print("Ahora por favor elige la categoría de la receta que quieres leer:\n")
        categories = chose_category()
        read_recipe(categories)
    elif options == 2:
        print("Has elegido la opción 2: Crear receta\n")
        print("Ahora por favor elige ula categoría de la receta que quieres crear:\n")
        categories = chose_category()
        create_recipe(categories)
    elif options == 3:
        print("Has elegido la opción 3: Crear categoría\n")
        create_category()
    elif options == 4:
        print("Has elegido la opción 4: Eliminar receta\n")
        print("Ahora por favor elige la categoría de la receta que deseas eliminar:\n")
        categories = chose_category()
        delete_recipe(categories)
    elif options == 5:
        print("Has elegido la opción 5: Eliminar categoría\n")
        delete_category()
    else:
        print("Has elegido apagar el programa")
        break





