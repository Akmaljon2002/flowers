from django.contrib import admin
from product.models import Category, SubCategory, Product, Banner, Category2, ProductPhoto, AbouteProduct, Links, \
    YoutubeVideo

admin.site.register(Category)
admin.site.register(Category2)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(ProductPhoto)
admin.site.register(Banner)
admin.site.register(AbouteProduct)
admin.site.register(YoutubeVideo)
admin.site.register(Links)