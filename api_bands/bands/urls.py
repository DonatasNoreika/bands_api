from django.contrib import admin
from django.urls import path, include
from .views import (BandList,
                    SongList,
                    AlbumList,
                    AlbumReviewList,
                    AlbumReviewCommentList,
                    AlbumReviewLikeList,
                    AlbumReviewDetail,
                    AlbumReviewCommentDetail)

urlpatterns = [
    path('bands', BandList.as_view()),
    path('songs', SongList.as_view()),
    path('albums', AlbumList.as_view()),
    path('albumreviews', AlbumReviewList.as_view()),
    path('albumreviews/<int:pk>', AlbumReviewDetail.as_view()),
    path('albumreviewscomments', AlbumReviewCommentList.as_view()),
    path('albumreviewscomments/<int:pk>', AlbumReviewCommentDetail.as_view()),
    path('albumreviewslikes', AlbumReviewLikeList.as_view()),
]
