import json

from rest_framework.views import APIView
from rest_framework.response import Response


class UsersListCreateView(APIView):
    def get(self, request):
        try:
            with open('users.json') as file:
                return Response(json.loads(file.read()))
        except Exception as err:
            print(err)
        finally:
            file.close()

    def post(self, request):
        try:
            with open('users.json', 'r') as file:
                file_read = json.loads(file.read())
                file_read.append(self.request.data)
                with open('users.json', 'w') as file2:
                    file2.write(json.dumps(file_read))
        except Exception as err:
            print(err)
        finally:
            file.close()
            file2.close()
            return Response('Created')


