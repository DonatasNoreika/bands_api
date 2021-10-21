from django.db import models
from django.contrib.auth.models import User


class Band(models.Model):
    name = models.CharField(verbose_name="Name", max_length=150)


class Album(models.Model):
    name = models.CharField(verbose_name="Name", max_length=150)
    band = models.ForeignKey('Band', on_delete=models.CASCADE)


class Song(models.Model):
    name = models.CharField(verbose_name="Name", max_length=150)
    duration = models.IntegerField(verbose_name="Duration")
    album = models.ForeignKey('Album', on_delete=models.CASCADE)


class AlbumReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Content", max_length=150)

    SCORE = (
        ('1', '1/10'),
        ('2', '2/10'),
        ('3', '3/10'),
        ('4', '4/10'),
        ('5', '5/10'),
        ('6', '6/10'),
        ('7', '7/10'),
        ('8', '8/10'),
        ('9', '9/10'),
        ('10', '10/10'),
    )

    score = models.IntegerField(
        choices=SCORE,
        blank=True,
        default='10',
        help_text='Score',
    )


class AlbumReviewComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_review = models.ForeignKey('AlbumReview', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(verbose_name="Content", max_length=150)


class AlbumReviewLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_review = models.ForeignKey('AlbumReview', on_delete=models.CASCADE, related_name='likes')
