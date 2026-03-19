from django.db import models

class Product(models.Model):
    # Основная информация
    title = models.CharField(max_length=255, verbose_name="Название продукта")

    # Общие параметры (Макронутриенты)
    water = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    calories = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    proteins = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    fats = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    carbs = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    fiber = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Клетчатка")
    sugars = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Сахара")
    ash = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Зола")

    # Аминокислоты
    tryptophan = models.DecimalField(max_digits=8, decimal_places=4, default=0)
    threonine = models.DecimalField(max_digits=8, decimal_places=4, default=0)
    isoleucine = models.DecimalField(max_digits=8, decimal_places=4, default=0)
    leucine = models.DecimalField(max_digits=8, decimal_places=4, default=0)
    lysine = models.DecimalField(max_digits=8, decimal_places=4, default=0)
    methionine = models.DecimalField(max_digits=8, decimal_places=4, default=0)
    cystine = models.DecimalField(max_digits=8, decimal_places=4, default=0)
    phenylalanine = models.DecimalField(max_digits=8, decimal_places=4, default=0)
    tyrosine = models.DecimalField(max_digits=8, decimal_places=4, default=0)
    valine = models.DecimalField(max_digits=8, decimal_places=4, default=0)
    arginine = models.DecimalField(max_digits=8, decimal_places=4, default=0)
    histidine = models.DecimalField(max_digits=8, decimal_places=4, default=0)
    glycine = models.DecimalField(max_digits=8, decimal_places=4, default=0)

    # Жиры и холестерин
    saturated_fats = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    monounsaturated_fats = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    omega_3 = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    omega_6 = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    trans_fats = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    cholesterol = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    # Индексы (ГИ, ГН, ИИ)
    gi = models.DecimalField(max_digits=5, decimal_places=1, default=0, verbose_name="Гликемический индекс")
    gl = models.DecimalField(max_digits=5, decimal_places=1, default=0, verbose_name="Гликемическая нагрузка")
    ii = models.DecimalField(max_digits=5, decimal_places=1, default=0, verbose_name="Инсулиновый индекс")
    pral = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="PRAL (кислотная нагрузка)")

    # Витамины
    vit_c = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    vit_b1 = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    vit_b2 = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    vit_b3 = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    vit_b5 = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    vit_b6 = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    vit_b7 = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    vit_b9 = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    vit_b12 = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    vit_a = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    vit_e = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    vit_d = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    vit_k = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    choline = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    betaine = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    beta_carotene = models.DecimalField(max_digits=8, decimal_places=3, default=0)

    # Минералы и микроэлементы
    calcium = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    iron = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    magnesium = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    phosphorus = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    potassium = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    sodium = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    zinc = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    copper = models.DecimalField(max_digits=8, decimal_places=4, default=0)
    manganese = models.DecimalField(max_digits=8, decimal_places=4, default=0)
    selenium = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    fluoride = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    iodine = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    molybdenum = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    boron = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    lithium = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    cobalt = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    sulfur = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    silicon = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    chromium = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    chlorine = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    # Служебные данные
    # Список полей, рассчитанных ИИ
    predicted_data = models.TextField(blank=True, null=True, verbose_name="Рассчитано ИИ")
    # Строка источников
    source = models.TextField(blank=True, null=True, verbose_name="Источники данных")
    # JSON-поле для лайфхаков и маркеров
    advice = models.JSONField(blank=True, null=True, verbose_name="Лайфхаки и маркеры")
    # внешний ключ для связки с таблицей категорий
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True)
    # контроль времени добавленияи изменения
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children')
    def __str__(self):
        return self.name

class Recipes(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название рецепта")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, null=True, verbose_name="Рецепт")