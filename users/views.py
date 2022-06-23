import json

from rest_framework.views import APIView
from rest_framework.response import Response


class UsersListCreateView(APIView):
    def get(self, *args, **kwargs):
        try:
            with open('users.json') as file:
                return Response(json.loads(file.read()))
        except Exception as err:
            print(err)
        finally:
            file.close()

    def post(self, *args, **kwargs):
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


class RetrieveUser(APIView):
    def get(self, *args, **kwargs):
        user_id = kwargs.get('id')
        try:
            with open('users.json') as file:
                users_list = json.loads(file.read())
                for user in users_list:
                    if user['id'] == user_id:
                        return Response(user)
        except Exception as err:
            print(err)
        finally:
            file.close()

    def put(self, *args, **kwargs):
        user_id = kwargs.get('id')
        data = self.request.data
        try:
            with open('users.json') as file:
                users_list = json.loads(file.read())
                upd_user_list = []
                for user in users_list:
                    if user['id'] == user_id:
                        upd_user_list.append(data)
                    else:
                        upd_user_list.append(user)
                print(upd_user_list)
                with open('users.json', 'w') as file2:
                    file2.write(json.dumps(upd_user_list))
        except Exception as err:
            print(err)
        finally:
            file.close()
            file2.close()
        return Response('put')

    def delete(self, *args, **kwargs):
        user_id = kwargs.get('id')
        try:
            with open('users.json') as file:
                users_list = json.loads(file.read())
                upd_user_list = []
                for user in users_list:
                    if user['id'] == user_id:
                        pass
                    else:
                        upd_user_list.append(user)
                print(upd_user_list)
                with open('users.json', 'w') as file2:
                    file2.write(json.dumps(upd_user_list))
        except Exception as err:
            print(err)
        finally:
            file.close()
            file2.close()
        return Response('delete')

    def patch(self, *args, **kwargs):
        user_id = kwargs.get('id')
        data = self.request.data
        try:
            with open('users.json') as file:
                users_list = json.loads(file.read())
                upd_user_list = []
                for user in users_list:
                    if user['id'] == user_id:
                        user.update(data)
                        upd_user_list.append(user)
                    else:
                        upd_user_list.append(user)
                print(upd_user_list)
                with open('users.json', 'w') as file2:
                    file2.write(json.dumps(upd_user_list))
        except Exception as err:
            print(err)
        finally:
            file.close()
            file2.close()
        return Response('patch')

