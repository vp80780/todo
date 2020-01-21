from rest_framework import viewsets
from rest_framework.response import Response
from todo_app.todo.models import Task
from todo_app.todo.serializers import TaskSerializer
from rest_framework.views import APIView


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class RequiredBankDocuments(APIView):
    def get(self, request):
        return Response({'result': 'success', 'message': 'application successfully deployed on Openshift with Postgres database'})