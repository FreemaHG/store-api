from sqladmin import ModelView

from src.models.category import Category
from src.models.product import Product


class CategoryAdmin(ModelView, model=Category):
    name = "Категория"
    name_plural = "Категории"
    icon = "fa-bars"  # Иконка

    column_list = [Category.id, Category.name, Category.image]
    column_searchable_list = [Category.name]
    column_sortable_list = [Category.id, Category.name]

    column_labels = {
        Category.name: "Название",
        Category.image: "Изображения",
        Category.products: "Товары",
    }


class ProductAdmin(ModelView, model=Product):
    name = "Товар"
    name_plural = "Товары"
    # Иконка слева от названия
    icon = "fa-automobile"

    column_list = [
        Product.id, "category.name", Product.title, Product.description, Product.price, Product.images
    ]
    column_searchable_list = [Product.title]
    column_sortable_list = [Product.id, Product.title, Product.price, Product.category_id,]
    # Короткий вывод названия и описания товара
    column_formatters = {
        Product.title: lambda m, a: m.title[:50],
        Product.description: lambda m, a: m.description[:100],
    }

    # Кол-во записей на странице и варианты пагинации
    page_size = 10
    page_size_options = [10, 20, 40]

    # Наименования столбцов
    column_labels = {
        Product.title: "Название",
        Product.description: "Описание",
        Product.price: "Цена, $",
        Product.category_id: "id категории",
        Product.images: "Изображения",
        "category": "Категория",
        "category.name": "Категория",
    }



