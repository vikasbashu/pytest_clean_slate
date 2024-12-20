from pages.rest_user_profile import UserProfile
from utils import random_test_data as GenericFunctions
import random
import pytest
import allure

@pytest.mark.api
@pytest.mark.xdist_group(name="Suit3")
class Test_Go_Rest_API_Test_004:
    goRestUser = UserProfile()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.hookimpl(tryfirst=True)
    def test_create_user_request(self):
        payload = {
            "name": GenericFunctions.get_test_username(),
            "gender": ["male", "female"][random.randrange(0, 2)],
            "email": GenericFunctions.get_test_email(),
            "status": ["active", "inactive"][random.randrange(0, 2)]
        }
        response = self.goRestUser.createUser(payload)
        assert 201 == response.status_code
        self.goRestUser.resp = response.json()

    def test_get_user_request(self):
        response = self.goRestUser.getUser(self.goRestUser.resp["id"])
        assert 200 == response.status_code
        response = response.json()
        assert self.goRestUser.resp["name"] == response["name"]
        assert self.goRestUser.resp["email"] == response["email"]
        assert self.goRestUser.resp["gender"] == response["gender"]
        assert self.goRestUser.resp["status"] == response["status"]
        self.goRestUser.resp = response

    def test_update_user_patch_request(self):
        payload = {
            "name": GenericFunctions.get_test_username(),
            "email": GenericFunctions.get_test_email(),
        }
        response = self.goRestUser.updateUserPatch(self.goRestUser.resp["id"], payload)
        assert 200 == response.status_code
        response = response.json()
        assert self.goRestUser.resp["name"] != response["name"]
        assert self.goRestUser.resp["email"] != response["email"]
        self.goRestUser.resp = response
        self.test_get_user_request()

    def test_update_user_put_request(self):
        payload = {
            "name": GenericFunctions.get_test_username(),
            "gender": ["male", "female"][random.randrange(0, 2)],
            "email": GenericFunctions.get_test_email(),
            "status": ["active", "inactive"][random.randrange(0, 2)]
        }
        response = self.goRestUser.updateUserPut(self.goRestUser.resp["id"], payload)
        assert 200 == response.status_code
        response = response.json()
        assert self.goRestUser.resp["email"] != response["email"]
        assert self.goRestUser.resp["name"] != response["name"]
        self.goRestUser.resp = response
        self.test_get_user_request()

    @pytest.hookimpl(trylast=True)
    def test_update_user_delete_request(self):
        response = self.goRestUser.deleteUser(self.goRestUser.resp["id"])
        assert response.status_code == 204
