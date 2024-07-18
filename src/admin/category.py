from sqladmin import ModelView

from src.posts.models.category import Category


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
