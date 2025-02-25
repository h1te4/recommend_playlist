import json


def load(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def recommend(ontology, жанр, настроение=None, время_суток=None, популярность=None):
    результаты = []
    if жанр in ontology:
        варианты = ontology[жанр]
        if настроение:
            варианты = [вариант for вариант in варианты if вариант["mood"].lower() == настроение.lower()]
        if время_суток:
            варианты = [вариант for вариант in варианты if вариант["time_of_day"].lower() == время_суток.lower()]
        if популярность:
            варианты = [вариант for вариант in варианты if вариант["popularity"].lower() == популярность.lower()]
        результаты.extend(варианты)

    if настроение and len(результаты) < 2:
        for другой_жанр, варианты in ontology.items():
            if другой_жанр == жанр:
                continue
            фильтрованные = [вариант for вариант in варианты if вариант["mood"].lower() == настроение.lower()]
            if время_суток:
                фильтрованные = [вариант for вариант in фильтрованные if
                                 вариант["time_of_day"].lower() == время_суток.lower()]
            if популярность:
                фильтрованные = [вариант for вариант in фильтрованные if
                                 вариант["popularity"].lower() == популярность.lower()]
            результаты.extend(фильтрованные)

    if not результаты:
        return "не найдено подходящих вариантов"
    вывод = "Рекомендованные песни:\n"
    for вариант in результаты:
        вывод += "- " + ", ".join(вариант["songs"]) + "\n"
    return вывод
ontology = load("playlists.json")
жанр = input("Введите жанр плейлиста (рок, поп, электронная и т.д.): ").strip().lower()
настроение = input("Введите настроение (энергичное, спокойное, веселое и т.д.): ").strip().lower() or None
время_суток = input("Введите время суток (утро, день, вечер, ночь): ").strip().lower() or None
популярность = input("Введите популярность (хиты, альтернативное): ").strip().lower() or None

print(recommend(ontology, жанр, настроение, время_суток, популярность))
