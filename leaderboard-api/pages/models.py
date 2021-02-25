""" ### MODELS ### """

""" IMPORTS """
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Count
from django_countries.fields import CountryField
import uuid

""" TABLES

Table: User
- user_gui: uuid
- user_name: varchar
- user_rank: foreignkey
- user_score: int
- user_country: django-countries.Country

#TODO
Table: Ranks

"""

""" USER TABLE """
class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user_name = models.CharField(blank=True, null=True, max_length=50, default=None)
    user_rank = models.PositiveBigIntegerField(default=0, validators=[MinValueValidator(1)])
    user_score = models.PositiveBigIntegerField(db_index=True, default=0, blank=True, validators=[MinValueValidator(0)])
    user_country = CountryField()

    """ Default value returned """
    def __str__(self):
        return str(self.user_id)

    """ Get ranking based on user_score """
    def ranking(self):
        aggregate = User.objects.filter(user_score__gt=self.user_score).aggregate(ranking=Count('user_score'))
        self.user_rank = aggregate['ranking'] + 1
        return self.user_rank

    """ Model meta """
    class Meta:
        verbose_name_plural = 'Users'
        
        # Keep table sorted for user_score
        ordering = ['-user_score']
        
        # Index table for user_score
        indexes = [
            models.Index(fields=['user_score'])
        ]

    """ On model save """
    def save(self, *args, **kwargs):
        # Generate ID if no username is given ('user_' + user Mac Address from UUID)
        if self.user_name == '' or self.user_name is None:
            self.user_name = 'user_' + str(self.user_id)[-12:] # Last 12 digits
        super(User, self).save(*args, **kwargs)
