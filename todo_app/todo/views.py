from rest_framework import viewsets
from rest_framework.response import Response
from todo_app.todo.models import Task
from todo_app.todo.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class RequiredBankDocuments(APIView):
    def get(self, request):
        return Response({'result': 'fail', 'message': 'Something went wrong'})