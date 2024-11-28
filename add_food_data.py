from index import app, db, Food, Store


# Добавляем первый магазин
def add_food_data():
    with app.app_context():
        # Создаем таблицы, если они не существуют
        db.create_all()

        # Удаляем все существующие записи (если нужно)
        db.session.query(Food).delete()
        db.session.query(Store).delete()
        db.session.commit()

        # Создаем магазин
        store = Store(name="Вкусняшкин", description="Лучший магазин еды в городе", image_path="images/store_1.jpg")
        db.session.add(store)
        db.session.commit()

        # Добавляем товары в магазин
        foods = [
            Food(name="Пицца", description="Томатный соус, моцарелла, пепперони", delivery_time="30 минут",
                 image_path="images/pizza.jpg", store_id=store.id),
            Food(name="Бургер", description="Котлета из говядины, листья салата, помидор, сыр",
                 delivery_time="20 минут", image_path="images/burger.jpg", store_id=store.id),
            Food(name="Суши", description="Рис, сырая рыба, нори", delivery_time="45 минут",
                 image_path="images/sushi.jpg", store_id=store.id),
            Food(name="Салат", description="Смесь зелени, помидоров черри, огурцов, сыра фета",
                 delivery_time="15 минут", image_path="images/salad.jpg", store_id=store.id),
            Food(name="Паста", description="Спагетти, томатный соус, фрикадельки", delivery_time="25 минут",
                 image_path="images/pasta.jpg", store_id=store.id)
        ]

        for food in foods:
            db.session.add(food)

        db.session.commit()
        print("Данные добавлены успешно!")


# Добавляем второй магазин
def add_food_data_2():
    with app.app_context():
        # Создаем таблицы, если они не существуют
        db.create_all()

        # Удаляем все существующие записи (если нужно)
        # db.session.query(Food).delete()
        # db.session.query(Store).delete()
        # db.session.commit()

        # Создаем магазин
        store = Store(name="Лавка вкуса", description="Мы специализируемся на продаже эксклюзивных "
                                                      "продуктов, таких как авторские сыры, редкие специи, "
                                                      "необычные десерты и напитки", image_path="images/store_2.jpg")
        db.session.add(store)
        db.session.commit()

        # Добавляем товары в магазин
        foods = [
            Food(name="Сыр с плесенью", description="Изысканный продукт с благородной голубой плесенью, который "
                                                    "обладает насыщенным вкусом и ароматом. Идеально подходит для "
                                                    "гурманов и любителей необычных сыров", delivery_time="30-45 "
                                                                                                          "минут",
                 image_path="images/cheese_with_mold.jpg", store_id=store.id),
            Food(name="Десерт шотландский", description="Традиционный шотландский десерт, состоящий из песочного "
                                                        "теста, свежих ягод и нежного сливочного крема. Обладает "
                                                        "ярким вкусом и неповторимым ароматом", delivery_time="20-35 "
                                                                                                              "минут",
                 image_path="images/Dessert_is_Scottish.jpg", store_id=store.id),
            Food(name="Горный Мохито", description="Освежающий напиток, приготовленный на основе горного чая с "
                                                   "добавлением мяты, лайма и сахара. Отлично утоляет жажду и "
                                                   "бодрит", delivery_time="45-1 час",
                 image_path="images/Mountain_Mojito.jpg",
                 store_id=store.id),
            Food(name="Сыр голландский", description="Твёрдый голландский сыр, известный своим насыщенным вкусом и "
                                                     "ароматом. Идеально подходит для приготовления различных блюд и "
                                                     "закусок", delivery_time="25 минут",
                 image_path="images/Dutch_cheese.jpg", store_id=store.id),
            Food(name="Копченая паприка", description="Ароматная копчёная приправа, изготовленная из красного перца и "
                                                      "других специй. Обладает ярким вкусом и ароматом, "
                                                      "идеально подходит для мясных и овощных блюд",
                 delivery_time="35 минут", image_path="images/Smoked_paprika.jpg", store_id=store.id)
        ]

        for food in foods:
            db.session.add(food)

        db.session.commit()
        print("Данные добавлены успешно!")


# Добавляем третий магазин
def add_food_data_3():
    with app.app_context():
        # Создаем таблицы, если они не существуют
        db.create_all()

        # Удаляем все существующие записи (если нужно)
        # db.session.query(Food).delete()
        # db.session.query(Store).delete()
        # db.session.commit()

        # Создаем магазин
        store = Store(name="Гастровкус", description="Мы предлагаем широкий ассортимент товаров, включая свежие овощи "
                                                     "и фрукты, мясные и молочные продукты, бакалею и кондитерские "
                                                     "изделия", image_path="images/store_2.jpg")
        db.session.add(store)
        db.session.commit()

        # Добавляем товары в магазин
        foods = [
            Food(name="Помидоры тепличные", description="Эти помидоры выращиваются в специальных теплицах, "
                                                        "где создаются оптимальные условия для роста и развития "
                                                        "растений. Плоды имеют насыщенный красный цвет, "
                                                        "плотную мякоть и сладкий вкус. Они идеально подходят для "
                                                        "употребления в свежем виде, а также для приготовления "
                                                        "различных блюд и консервации",
                 delivery_time="50 минут",
                 image_path="images/Greenhouse_tomatoes.jpg",
                 store_id=store.id),
            Food(name="Дыня абхазкая", description="Абхазская дыня известна своими крупными размерами, сладким вкусом "
                                                   "и ароматом. Она выращивается в Абхазии и считается одной из "
                                                   "лучших дынь в мире. Плоды имеют жёлтую кожуру и белую мякоть, "
                                                   "наполненную множеством мелких семян. Дыню употребляют в свежем "
                                                   "виде, а также используют для приготовления десертов и напитков",
                 delivery_time="50 минут",
                 image_path="images/The_Abkhazian_melon.jpg",
                 store_id=store.id),
            Food(name="Молоко фермерское", description="Фермерское молоко производится из молока коров, которые "
                                                       "питаются свежей травой и сеном. Оно имеет приятный вкус и "
                                                       "запах, а также богато витаминами и минералами. Фермерское "
                                                       "молоко идеально подходит для приготовления молочных "
                                                       "продуктов, таких как йогурт, творог и сметана",
                 delivery_time="50 минут",
                 image_path="images/Farm_milk.jpg",
                 store_id=store.id),
            Food(name="Гречка", description="Гречка — это полезный и питательный злак, который выращивается во многих "
                                            "странах мира. Она богата железом, магнием и другими полезными "
                                            "веществами. Гречку используют для приготовления каш, гарниров и других "
                                            "блюд",
                 delivery_time="50 минут",
                 image_path="images/Buckwheat.jpg",
                 store_id=store.id),
            Food(name="Печенье из песочного теста",
                 description="Песочное печенье изготавливается из муки, масла, сахара и яиц. Оно имеет рассыпчатую "
                             "структуру и нежный вкус. Песочное печенье часто посыпают сахарной пудрой или украшают "
                             "глазурью",
                 delivery_time="50 минут",
                 image_path="images/Shortbread_cookies.jpg",
                 store_id=store.id)
        ]

        for food in foods:
            db.session.add(food)

        db.session.commit()
        print("Данные добавлены успешно!")




if __name__ == '__main__':
    add_food_data_3()
