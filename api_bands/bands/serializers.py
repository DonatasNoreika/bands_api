from rest_framework import serializers
from .models import Band, Album, Song, AlbumReview, AlbumReviewComment, AlbumReviewLike


class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = ['id', 'name']


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'name', 'band']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'name', 'duration', 'album']


class AlbumReviewCommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = AlbumReviewComment
        fields = ['id', 'user', 'user_id', 'album_review', 'content']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumReviewLikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = AlbumReviewLike
        fields = ['id', 'user', 'user_id', 'album_review']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    comments = AlbumReviewCommentSerializer(many=True)
    comment_count = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    def get_comment_count(self, obj):
        return AlbumReviewComment.objects.filter(album_review=obj).count()

    def get_likes_count(self, obj):
        return AlbumReviewLike.objects.filter(album_review=obj).count()

    class Meta:
        model = AlbumReview
        fields = ['id', 'user', 'user_id', 'album', 'content', 'score', 'comment_count', 'comments', 'likes_count']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
