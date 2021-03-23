from django.db import models
from django.utils.translation import gettext as _


class Product(models.Model):
  name = models.CharField(_("Feature Name"), max_length=50, unique=True)
  price = models.IntegerField(_("Price"))
  category = models.ManyToManyField("Category", verbose_name=_("Product categories"), blank=True)
  in_stock = models.BooleanField(_("In Stock?"), default=True)
  date_created = models.DateTimeField(_("Date created"), auto_now=False, auto_now_add=False, blank=True, null=True)

  def __str__(self):
    return self.name

  def get_category(self):
      return "\n".join([p.name for p in self.category.all()])

class Category(models.Model):
  name = models.CharField(_("Category"), max_length=50, unique=True)

  def __str__(self):
    return self.name