from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=120)


class Author(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        unique_together = ("name", "lastname")

    def __unicode__(self):
        return("{} {} {}".format(self.name, self.lastname, self.nickname))


class Book(models.Model):
    authors = models.ManyToManyField(Author)
    title = models.CharField(max_length=120)
    isbn = models.CharField(max_length=24, null=True, blank=True)
    publisher = models.ForeignKey(Publisher, null=True, blank=True)

    def __unicode__(self):
        return("{} {}".format(self.title, self.authors))
