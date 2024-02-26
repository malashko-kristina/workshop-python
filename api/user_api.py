from http import HTTPStatus
from custom_requester.custom_requester import CustomRequester

class UserAPI(CustomRequester):

    #Метод для отправки запроса по созданию юзера
    def create_user(self, user_data):
        return self.send_request("POST", "/app/rest/users", data=user_data)

    #Метод для отправки запроса по удалению юзера
    def delete_user(self, user_locator):
        return self.send_request("DELETE", f"/app/rest/users/{user_locator}", expected_status=HTTPStatus.NO_CONTENT)

    #Метод для отправки запроса по получению информации по юзеру
    def get_user_data(self, user_locator):
        return self.send_request("GET", f"/app/rest/users/{user_locator}")