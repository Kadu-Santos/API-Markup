from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from backend.views import PerguntaViewsets, PuzzleViewsets

router = routers.DefaultRouter()
router.register(r'perguntas', PerguntaViewsets)
router.register(r'puzzles', PuzzleViewsets)

urlpatterns = [
    path('MarkupSettings/', admin.site.urls),
    path('', include(router.urls)),
]

