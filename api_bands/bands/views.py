from django.shortcuts import render
from rest_framework import generics
from .models import (Band,
                     Album,
                     Song,
                     AlbumReview,
                     AlbumReviewComment,
                     AlbumReviewLike)
from .serializers import (BandSerializer,
                          AlbumSerializer,
                          SongSerializer,
                          AlbumReviewSerializer,
                          AlbumReviewCommentSerializer,
                          AlbumReviewLikeSerializer)


class BandList(generics.ListCreateAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer


class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class AlbumReviewList(generics.ListCreateAPIView):
    queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer


class AlbumReviewCommentList(generics.ListCreateAPIView):
    queryset = AlbumReviewComment.objects.all()
    serializer_class = AlbumReviewCommentSerializer


class AlbumReviewLikeList(generics.ListCreateAPIView):
    queryset = AlbumReviewLike.objects.all()
    serializer_class = AlbumReviewLikeSerializer
