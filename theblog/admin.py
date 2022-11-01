from django.contrib import admin
from .models import Post, Category, Profile, Comment, SubCategory, Product, WinningProduct


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'post_date', 'category','sub_category', 'winning_product',)
    ordering = ('-post_date',)
    search_fields = ('title','author__first_name','category', 'sub_category', 'winning_product__product_name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    search_fields = ('name',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', )
    ordering = ('user',)
    search_fields = ('user__first_name',)

class CommentAdmin(admin.ModelAdmin):
     list_display = ('post', 'name', 'date_added',)
     ordering = ('-date_added',)
     search_fields = ('title','post__first_name',)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'sub_category', )
    ordering = ('name',)
    search_fields = ('name','sub_category__name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_seller_1', 'product_seller_2', 'product_seller_3',)
    ordering = ('product_name',)
    search_fields = ('product_name', 'product_seller_1', 'product_seller_2', 'product_seller_3',)

class WinningProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_seller_1', 'product_seller_2', 'product_seller_3',)
    ordering = ('product_name',)
    search_fields = ('product_name', 'product_seller_1', 'product_seller_2', 'product_seller_3',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(WinningProduct, WinningProductAdmin)





