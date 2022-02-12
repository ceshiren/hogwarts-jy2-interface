"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import allure

from test_requests.testcase.utils import Utils

'''
接口测试框架第一版
1 通过 ApiObject 模式把框架分了 3 层
2 wework 中获取 access_token，department 中描述部门操作接口的信息
3 测试用例当中通过 setup_class 实例化接口描述类，准备测试数据
4 测试用例中传入数据，完成业务拼接，完成断言
'''

from test_requests.apis.department import Department

@allure.feature("部门管理")
class TestDepartment:

    def setup_class(self):
        # 获取通讯录管理的 token 参数
        conf_data = Utils.get_yaml_data("../data/config.yaml")
        corpid = conf_data["corpid"]["hogwarts"]
        corpsecret = conf_data["secret"]["contact_secret"]
        # 实例化部门类
        self.department = Department(corpid, corpsecret)
        # 清理部门数据
        self.department.clear_departments()
        # 准备测试数据
        self.depart_id = 4
        self.create_data = {
            "name": "hogwarts111",
            "name_en": "h111",
            "parentid": 1,
            "order": 2,
            "id": self.depart_id
        }
        self.update_data = {
            "id": self.depart_id,
            "name": "hogwarts111-update"
        }

    @allure.story("部门操作场景用例")
    def test_department_scene(self):
        '''
        完成部门增删查改的场景测试
        :return:
        '''
        # 创建部门
        with allure.step("创建部门"):
            self.department.create_department(self.create_data)
        # 查询是否创建成功
        with allure.step("查询部门创建结果"):
            depart_info = self.department.get_departments()
            print(depart_info)
            # assert depart_info["department"][1]["name"] == "hogwarts111"
            # 通过 jsonpath 断言
            name_list = Utils.base_jsonpath(depart_info, "$..name")
            self.department.log_info(f"部门创建后的部门名称列表:{name_list}")
            assert "hogwarts111" in name_list
        # 更新部门
        self.department.update_department(self.update_data)
        # 查询更新是否成功
        depart_info = self.department.get_departments()
        # assert depart_info["department"][1]["name"] == "hogwarts111-update"
        name_list = Utils.base_jsonpath(depart_info, "$..name")
        assert "hogwarts111-update" in name_list
        # 删除部门
        self.department.delete_department(self.depart_id)
        # 查询是否删除成功
        depart_info = self.department.get_departments()
        # assert len(depart_info["department"]) == 1
        # 使用 jsonpath 找出所有的部门 id
        id_list = Utils.base_jsonpath(depart_info, "$..id")
        print(id_list)
        # 判断要删除的部门的 id 不在 id 列表当中
        assert self.depart_id not in id_list
