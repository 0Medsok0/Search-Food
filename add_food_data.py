from index import app, db, Food, Store


# Добавляем первый магазин
def add_food_data():
    with app.app_context():
        db.create_all()
        db.session.query(Food).delete()
        db.session.query(Store).delete()
        db.session.commit()

        store = Store(name="Вкусняшкин", description="Лучший магазин еды в городе", image_path="images/store_1.jpg")
        db.session.add(store)
        db.session.commit()

        foods = [
            Food(name="Пицца", description="Томатный соус, моцарелла, пепперони", delivery_time="30 минут",
                 image_path="images/pizza.jpg", store_id=store.id, category='fast_food'),
            Food(name="Бургер", description="Котлета из говядины, листья салата, помидор, сыр",
                 delivery_time="20 минут", image_path="images/burger.jpg", store_id=store.id, category='fast_food'),
            Food(name="Суши", description="Рис, сырая рыба, нори", delivery_time="45 минут",
                 image_path="images/sushi.jpg", store_id=store.id, category='fast_food'),
            Food(name="Салат", description="Смесь зелени, помидоров черри, огурцов, сыра фета",
                 delivery_time="15 минут", image_path="images/salad.jpg", store_id=store.id, category='fruits_vegetables'),
            Food(name="Паста", description="Спагетти, томатный соус, фрикадельки", delivery_time="25 минут",
                 image_path="images/pasta.jpg", store_id=store.id, category='fast_food')
        ]

        for food in foods:
            db.session.add(food)

        db.session.commit()
        print("Данные добавлены успешно!")

# Добавляем второй магазин
def add_food_data_2():
    with app.app_context():
        db.create_all()

        store = Store(name="Лавка вкуса", description="Мы специализируемся на продаже эксклюзивных "
                                                      "продуктов, таких как авторские сыры, редкие специи, "
                                                      "необычные десерты и напитки", image_path="images/store_2.jpg")
        db.session.add(store)
        db.session.commit()

        foods = [
            Food(name="Сыр с плесенью", description="Изысканный продукт с благородной голубой плесенью, который "
                                                    "обладает насыщенным вкусом и ароматом. Идеально подходит для "
                                                    "гурманов и любителей необычных сыров", delivery_time="30-45 "
                                                                                                          "минут",
                 image_path="images/cheese_with_mold.jpg", store_id=store.id, category='dairy'),
            Food(name="Десерт шотландский", description="Традиционный шотландский десерт, состоящий из песочного "
                                                        "теста, свежих ягод и нежного сливочного крема. Обладает "
                                                        "ярким вкусом и неповторимым ароматом", delivery_time="20-35 "
                                                                                                              "минут",
                 image_path="images/Dessert_is_Scottish.jpg", store_id=store.id, category='dairy'),
            Food(name="Горный Мохито", description="Освежающий напиток, приготовленный на основе горного чая с "
                                                   "добавлением мяты, лайма и сахара. Отлично утоляет жажду и "
                                                   "бодрит", delivery_time="45-1 час",
                 image_path="images/Mountain_Mojito.jpg",
                 store_id=store.id, category='drinks'),
            Food(name="Сыр голландский", description="Твёрдый голландский сыр, известный своим насыщенным вкусом и "
                                                     "ароматом. Идеально подходит для приготовления различных блюд и "
                                                     "закусок", delivery_time="25 минут",
                 image_path="images/Dutch_cheese.jpg", store_id=store.id, category='dairy'),
            Food(name="Копченая паприка", description="Ароматная копчёная приправа, изготовленная из красного перца и "
                                                      "других специй. Обладает ярким вкусом и ароматом, "
                                                      "идеально подходит для мясных и овощных блюд",
                 delivery_time="35 минут", image_path="images/Smoked_paprika.jpg", store_id=store.id, category='groceries')
        ]

        for food in foods:
            db.session.add(food)

        db.session.commit()
        print("Данные добавлены успешно!")

# Добавляем третий магазин
def add_food_data_3():
    with app.app_context():
        db.create_all()

        store = Store(name="Гастровкус", description="Мы предлагаем широкий ассортимент товаров, включая свежие овощи "
                                                     "и фрукты, мясные и молочные продукты, бакалею и кондитерские "
                                                     "изделия", image_path="images/store_3.jpg")
        db.session.add(store)
        db.session.commit()
        print(f"Магазин добавлен: {store.name}")

        foods = [
            Food(name="Помидоры тепличные", description="Эти помидоры выращиваются в специальных теплицах, "
                                                        "где создаются оптимальные условия для роста и развития "
                                                        "растений. Плоды имеют насыщенный красный цвет, "
                                                        "плотную мякоть и сладкий вкус. Они идеально подходят для "
                                                        "употребления в свежем виде, а также для приготовления "
                                                        "различных блюд и консервации",
                 delivery_time="50 минут",
                 image_path="images/Greenhouse_tomatoes.jpg",
                 store_id=store.id, category='fruits_vegetables'),
            Food(name="Дыня абхазкая", description="Абхазская дыня известна своими крупными размерами, сладким вкусом "
                                                   "и ароматом. Она выращивается в Абхазии и считается одной из "
                                                   "лучших дынь в мире. Плоды имеют жёлтую кожуру и белую мякоть, "
                                                   "наполненную множеством мелких семян. Дыню употребляют в свежем "
                                                   "виде, а также используют для приготовления десертов и напитков",
                 delivery_time="50 минут",
                 image_path="images/The_Abkhazian_melon.jpg",
                 store_id=store.id, category='fruits_vegetables'),
            Food(name="Молоко фермерское", description="Фермерское молоко производится из молока коров, которые "
                                                       "питаются свежей травой и сеном. Оно имеет приятный вкус и "
                                                       "запах, а также богато витаминами и минералами. Фермерское "
                                                       "молоко идеально подходит для приготовления молочных "
                                                       "продуктов, таких как йогурт, творог и сметана",
                 delivery_time="50 минут",
                 image_path="images/Farm_milk.jpg",
                 store_id=store.id, category='dairy'),
            Food(name="Гречка", description="Гречка — это полезный и питательный злак, который выращивается во многих "
                                            "странах мира. Она богата железом, магнием и другими полезными "
                                            "веществами. Гречку используют для приготовления каш, гарниров и других "
                                            "блюд",
                 delivery_time="50 минут",
                 image_path="images/Buckwheat.jpg",
                 store_id=store.id, category='groceries'),
            Food(name="Печенье из песочного теста",
                 description="Песочное печенье изготавливается из муки, масла, сахара и яиц. Оно имеет рассыпчатую "
                             "структуру и нежный вкус. Песочное печенье часто посыпают сахарной пудрой или украшают "
                             "глазурью",
                 delivery_time="50 минут",
                 image_path="images/Shortbread_cookies.jpg",
                 store_id=store.id, category='groceries')
        ]

        for food in foods:
            db.session.add(food)
            print(f"Товар добавлен: {food.name}")

        db.session.commit()
        print("Данные добавлены успешно!")

# Добавляем четвертый магазин
def add_food_data_4():
    with app.app_context():
        db.create_all()

        store = Store(name="Хочу Пури", description="Вкус традиций в каждом кусочке!", image_path="images/store_4.jpg")
        db.session.add(store)
        db.session.commit()
        print(f"Магазин добавлен: {store.name}")

        foods = [
            Food(name="Хинкали", description="Традиционные грузинские пельмени с сочной начинкой из мяса и специями",
                 delivery_time="50 минут",
                 image_path="images/Khinkali.jpg",
                 store_id=store.id, category='georgian_cuisine'),
            Food(name="Лобио", description="Грузинское блюдо из фасоли, приготовленное с овощами, специями и зеленью",
                 delivery_time="50 минут",
                 image_path="images/Lobio.jpg",
                 store_id=store.id, category='georgian_cuisine'),
            Food(name="Чахохбили", description="Тушеное мясо (обычно курица) с помидорами, луком, чесноком и грузинскими специями",
                 delivery_time="50 минут",
                 image_path="images/Chakhokhbili.jpg",
                 store_id=store.id, category='georgian_cuisine'),
            Food(name="Манты", description="Традиционные центральноазиатские пельмени с сочной начинкой из мяса, лука и специй, приготовленные на пару",
                 delivery_time="50 минут",
                 image_path="images/Mantas.jpg",
                 store_id=store.id, category='georgian_cuisine'),
            Food(name="Хочапури",
                 description="Грузинские лепешки с начинкой из сыра, яйца и масла, выпекаемые до золотистой корочки",
                 delivery_time="50 минут",
                 image_path="images/Khachapuri.jpg",
                 store_id=store.id, category='georgian_cuisine')
        ]

        for food in foods:
            db.session.add(food)
            print(f"Товар добавлен: {food.name}")

        db.session.commit()
        print("Данные добавлены успешно!")

# Добавляем пятый магазин
def add_food_data_5():
    with app.app_context():
        db.create_all()

        store = Store(name="Лента", description="Качество и свежесть в каждом продукте", image_path="images/store_5.jpg")
        db.session.add(store)
        db.session.commit()
        print(f"Магазин добавлен: {store.name}")

        foods = [
            Food(name="Свежие овощи и фрукты", description="Всегда свежие и сезонные овощи и фрукты, выращенные с любовью",
                 delivery_time="50 минут",
                 image_path="images/Fresh_vegetables_and_fruits.jpg",
                 store_id=store.id, category='fruits_vegetables'),
            Food(name="Молочные продукты", description="Широкий ассортимент молока, йогуртов, сыров и других молочных продуктов высокого качества",
                 delivery_time="50 минут",
                 image_path="images/Dairy_products.jpg",
                 store_id=store.id, category='dairy'),
            Food(name="Мясные деликатесы", description="Выбор свежего мяса и колбасных изделий для любого вкуса и бюджета",
                 delivery_time="50 минут",
                 image_path="images/Meat_delicacies.jpg",
                 store_id=store.id, category='groceries'),
            Food(name="Хлебобулочные изделия", description="Свежеиспеченный хлеб, булочки и выпечка, приготовленные по традиционным рецептам",
                 delivery_time="50 минут",
                 image_path="images/Bakery_products.jpg",
                 store_id=store.id, category='groceries'),
            Food(name="Натуральные соки",
                 description="Соки без добавок и консервантов, идеальные для здорового питания",
                 delivery_time="50 минут",
                 image_path="images/Natural_juices.jpg",
                 store_id=store.id, category='drinks')
        ]

        for food in foods:
            db.session.add(food)
            print(f"Товар добавлен: {food.name}")

        db.session.commit()
        print("Данные добавлены успешно!")

if __name__ == '__main__':
    add_food_data()
    add_food_data_2()
    add_food_data_3()
    add_food_data_4()
    add_food_data_5()
