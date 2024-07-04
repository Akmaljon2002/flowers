from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    # about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Category2(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategory")
    category2 = models.ForeignKey(Category2, on_delete=models.CASCADE, related_name="subcategory", blank=True, null=True)
    name = models.CharField(max_length=255)
    about = models.TextField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    narx = models.FloatField(default=0)
    kod = models.IntegerField(default=0)
    miqdor = models.PositiveIntegerField(default=0)
    miqdor_paket = models.PositiveIntegerField(default=1)
    ekish_material_olcham = models.CharField(max_length=100, blank=True, null=True)
    ekish_chuqurligi = models.CharField(max_length=100, blank=True, null=True)
    masofa = models.CharField(max_length=100, blank=True, null=True)
    balandlik = models.CharField(max_length=100, blank=True, null=True)
    mahsulot_turi = models.CharField(max_length=255, blank=True, null=True)
    mamlakat = models.CharField(max_length=100, blank=True, null=True)
    sovuqqa_chiqamlilik = models.CharField(max_length=255, blank=True, null=True)
    kesish = models.BooleanField(default=True)
    gullash_davri = models.CharField(max_length=50, blank=True, null=True)
    gullash_davri_tugashi = models.CharField(max_length=50, blank=True, null=True)
    qonish_joyi = models.CharField(max_length=255, blank=True, null=True)
    sotib_olish_turi = models.CharField(max_length=255, blank=True, null=True)
    rangi = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Banner(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ImageField()

    def __str__(self):
        return self.name


class ProductPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_photo")
    name = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.product.name


class AbouteProduct(models.Model):
    title = models.CharField(max_length=255)
    aboute = models.TextField()
    photo = models.ImageField()

    def __str__(self):
        return self.title


class Links(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=255)
    photo = models.ImageField()

    def __str__(self):
        return self.name


class YoutubeVideo(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.link







