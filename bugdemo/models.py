from __future__ import unicode_literals
import random

from django.db import models

# Create your models here.

class SideB(models.Model):
    name = models.CharField(max_length=2000)

    def __str__(self):
        return "SideB(%s)" % (self.name)

class SideA(models.Model):
    name = models.CharField(max_length=2000)
    class Meta:
        ordering = ['id']

    def populate_sideb_links(self):
        links = []
        for sideb in SideB.objects.all():
            score = int(random.random() * 50)
            rank = 0
            link = ABLink(
                side_a=self,
                side_b=sideb,
                score=score)

            links.append(link)
        rank = 0
        sorted_links = sorted(links, key=lambda x: x.score)[::-1]
        for slink in sorted_links:
            slink.ranking = rank
            slink.save()
            rank += 1
            print slink

    def __str__(self):
        return "SideA(%s)" % (self.name)

class ABLink(models.Model):
    side_a = models.ForeignKey(SideA)
    side_b =  models.ForeignKey(SideB)
    ranking = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    score = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['ranking']
        index_together = ['side_a', 'ranking', 'side_b']
        unique_together = [
            ['side_a', 'ranking', 'side_b'],
            ['side_a', 'side_b'],
            #['ranking', 'CP']
        ]

    def __str__(self):
        return "AB(%d, %d, %s, %s)" % (
            self.score, self.ranking, self.side_a.name, self.side_b.name)

    __repr__ = __str__
