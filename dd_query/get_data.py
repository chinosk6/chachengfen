from . import api, models, errors
import time
import json


class GetUserFollowingVTB:
    def __init__(self, username: str):
        self.username = username
        self.userdata = self.get_userinfo()
        self.userid = self.userdata.mid
        self.follow_list, self.total_following = self.get_user_following()
        self.follow_list, self.total_vtb_count = self.check_vtb_list()
        self.user_mainpage_data = self.get_user_mainpage_data()

    def get_userinfo(self):
        try:
            data = json.loads(api.user_search(self.username))
            if "result" not in data["data"]:
                raise errors.UserNotFound(f"没有找到相关用户: {self.username}")
            result = data["data"]["result"]
            self.username = data["data"]["result"][0]["uname"]
            return models.SerachBiliUserResult(**result[0])

        except json.JSONDecodeError:
            raise errors.APIError("用户信息拉取失败")
        except IndexError:
            raise errors.UserNotFound(f"没有找到用户: {self.username}")

    def get_user_mainpage_data(self):
        data = json.loads(api.get_biliuser_info(self.userid))
        return models.UserMainPageInfo(**data["data"])

    def get_user_following(self) -> models.t.Tuple[models.t.List[models.FollowingUserInfo], int]:
        following = []
        total_following = 0
        for i in range(5):
            data = json.loads(api.get_user_following_list(self.userid, ps=50, pn=i + 1))
            if data["code"] not in [0, "0"]:
                raise errors.APIError(data["message"])

            get_list = data["data"]["list"]
            total_following = data["data"]["total"]
            if not get_list:
                break
            else:
                following += [models.FollowingUserInfo(**u) for u in get_list]
            time.sleep(0.5)
        return following, total_following

    def check_vtb_list(self) -> models.t.Tuple[models.t.List[models.VTBInfo], int]:
        vtb_list = []
        vtb_data = json.loads(api.get_all_vtb_info())
        for v in vtb_data:
            vtb_list.append(v["mid"])
        vtb_total_count = len(vtb_list)
        vtb_following = []
        for u in self.follow_list:
            if u.mid in vtb_list:
                vdata = vtb_data[vtb_list.index(u.mid)]
                vtb_following.append(models.VTBInfo(u.mtime, **vdata))
        return vtb_following, vtb_total_count
