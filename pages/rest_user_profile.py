from utils.apiHelper import API_Helper

class UserProfile(API_Helper):

    url = "https://gorest.co.in"
    post_end_point = "/public/v2/users"
    get_end_point = "/public/v2/users/{}"
    put_patch_end_point = "/public/v2/users/{}"
    delete_end_point = "/public/v2/users/{}"
    access_token = "Bearer {}".format('ac683ac93cb5d079a79b34ea7febfb2e9f1c9bd7aba7160a8ed15a7898f79293')
    request_header = {
        "Authorization": access_token
    }
    resp = {}

    def __init__(self):
        super().__init__(self.url, self.request_header)

    def createUser(self, payload):
        return self.post(self.post_end_point, payload)

    def getUser(self, user_id):
        return self.get(self.get_end_point.format(str(user_id)))

    def updateUserPatch(self, user_id, payload):
        return self.patch(self.put_patch_end_point.format(str(user_id)), payload)

    def updateUserPut(self, user_id, payload):
        return self.put(self.put_patch_end_point.format(str(user_id)), payload)

    def deleteUser(self, user_id):
        return self.delete(self.get_end_point.format(str(user_id)))