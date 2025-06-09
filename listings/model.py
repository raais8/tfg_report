class Product(models.Model):
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
    )
    name = models.CharField(
        max_length=250,
    )
    sku = models.CharField(
        max_length=50,
    )
    reference = models.CharField(
        max_length=50,
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )
    stock = models.PositiveIntegerField()
    image = models.URLField(
        null=True,
    )