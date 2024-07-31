from rest_framework import routers, viewsets
from store.models import Book
from store.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

router = routers.DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = router.urls