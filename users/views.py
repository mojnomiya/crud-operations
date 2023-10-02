from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer
from .models import User

# Create your views here.
class UsersGetPostView(ListCreateAPIView):
    """
    /users/ - this API endpoint will return a list of all the user details if the request method is GET. By POST request to this endpoint a signle user can be created.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDetaiDeletelView(RetrieveUpdateDestroyAPIView):
    """
    /users/<id> - this API endpoint will return a  details of a single user with the id, if the request method is GET. By PUT request to this endpoint that user can be updated or deleted.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer