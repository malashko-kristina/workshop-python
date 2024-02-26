from http import HTTPStatus
from custom_requester.custom_requester import CustomRequester

class RunBuildConfAPI(CustomRequester):

    #Метод по отправки запроса для запуска билд конфигурации
    def run_build_conf(self, run_build_data, expected_status=HTTPStatus.OK):
        return self.send_request("POST", "/app/rest/buildQueue", data=run_build_data, expected_status=expected_status)

    #Метод для отправки запроса списка билд конфигураций в очереди
    def check_status_build_conf(self, build_conf_id, expected_status=HTTPStatus.OK):
        return self.send_request("GET", f"/app/rest/buildQueue?locator=buildType(id:{build_conf_id})", expected_status=expected_status)

    #Метод для отправки запроса отмены билда в очереди
    def cancel_run_build_conf(self, build_conf_data, build_conf_in_id, expected_status=HTTPStatus.OK):
        return self.send_request("POST", f"/app/rest/buildQueue/id:{build_conf_in_id}", data=build_conf_data, expected_status=expected_status)

    #Метод для отправки запроса списка билд конфигураций в очереди
    def check_query_with_build_conf(self, expected_status=HTTPStatus.OK):
        return self.send_request("GET", f"/app/rest/buildQueue", expected_status=expected_status)








