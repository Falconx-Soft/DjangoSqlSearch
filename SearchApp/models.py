from django.contrib.auth.models import User
from django.db import models
from django.db.models import query

# Create your models here.

class Reviews(models.Model):
	class Pillar(models.TextChoices):
		Pillar1 = "Pillar1"
		Pillar2 = "Pillar2"
		Pillar3 = "Pillar3"
	pillar = models.CharField(max_length=200, choices=Pillar.choices, default=Pillar.Pillar1)

	class sourceType(models.TextChoices):
		sourceType1 = "sourceType1"
		sourceType2 = "sourceType2"
		sourceType3 = "sourceType3"
	sourceType = models.CharField(max_length=200, choices=sourceType.choices, default=sourceType.sourceType1)

	class market(models.TextChoices):
		market1 = "market1"
		market2 = "market2"
		market3 = "market3"
	market = models.CharField(max_length=200, choices=market.choices, default=market.market1)

	class brandSource(models.TextChoices):
		brandSource1 = "brandSource1"
		brandSource2 = "brandSource2"
		brandSource3 = "brandSource3"
	brandSource = models.CharField(max_length=200, choices=brandSource.choices, default=brandSource.brandSource1)
	review = models.CharField(max_length=1000)
	created_at = models.DateField(auto_now_add=True, null=True, blank=True)

class Quries(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	query = models.CharField(max_length=150)
	name = models.CharField(max_length=150, null=True, blank=True)