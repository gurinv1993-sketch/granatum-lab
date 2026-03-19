def main_menu(request):
    # Возвращаем словарь с меню, который будет доступен во всех шаблонах
    return {
        'main_menu': [
            {'name': 'home', 'label': 'Главная', 'namespace': None},
            {'name': 'about', 'label': 'О проекте', 'namespace': None},
            {'name': 'eat:hub', 'label': 'Сгенерировать блюдо', 'namespace': 'eat'},
            {'name': 'profile:index', 'label': 'Личный кабинет', 'namespace': 'profile'},
        ]}
def main_menu_lk(request):
    return {
        'main_menu_lk': [
            {'name': 'profile:fridge', 'label': 'Холодильник', 'namespace': 'profile'},
            {'name': 'profile:info', 'label': 'Обо мне', 'namespace': 'profile'},
            {'name': 'profile:shops', 'label': 'Мои магазины', 'namespace': 'profile'},

        ]
    }