from django.shortcuts import render
from rest_framework import generics, permissions, mixins, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django.contrib.auth.models import User

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
                          AlbumReviewLikeSerializer,
                          AlbumReviewAlternativeLikeSerializer,
                          UserSerializer)


class BandList(generics.ListCreateAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AlbumReviewList(generics.ListCreateAPIView):
    queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        post = AlbumReview.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if post.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('Negalima trinti svetimų albumų apžvalgų!')

    def put(self, request, *args, **kwargs):
        post = AlbumReview.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if post.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError('Negalima koreguoti svetimų albumų apžvalgų!')


class AlbumReviewCommentList(generics.ListCreateAPIView):
    queryset = AlbumReviewComment.objects.all()
    serializer_class = AlbumReviewCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumReviewCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AlbumReviewComment.objects.all()
    serializer_class = AlbumReviewCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        post = AlbumReviewComment.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if post.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('Negalima trinti svetimų komentarų!')

    def put(self, request, *args, **kwargs):
        post = AlbumReviewComment.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if post.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError('Negalima koreguoti svetimų komentarų!')


class AlbumReviewLikeList(generics.ListCreateAPIView):
    queryset = AlbumReviewLike.objects.all()
    serializer_class = AlbumReviewLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumReviewLikeCreate(generics.CreateAPIView, mixins.DestroyModelMixin):
    serializer_class = AlbumReviewAlternativeLikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        review = AlbumReview.objects.get(pk=self.kwargs['pk'])
        return AlbumReviewLike.objects.filter(album_review=review, user=user)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('Jūs jau palikote patiktuką šiai apžvalgai!')
        review = AlbumReview.objects.get(pk=self.kwargs['pk'])
        serializer.save(user=self.request.user, album_review=review)

    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('Jūs nepalikote patiktuko po šia apžvalga!')


class AlbumReviewLikeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AlbumReviewLike.objects.all()
    serializer_class = AlbumReviewLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        post = AlbumReviewLike.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if post.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('Negalima trinti svetimų laikų!')

    def put(self, request, *args, **kwargs):
        post = AlbumReviewLike.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if post.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError('Negalima koreguoti svetimų laikų!')


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)
