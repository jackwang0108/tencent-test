# NOTE: Generated By HttpRunner v4.3.5
# FROM: testcases/requests.yml
from httprunner import HttpRunner, Config, Step, RunRequest


class TestCaseRequests(HttpRunner):

    config = Config("测试API接口").base_url("http://127.0.0.1:5000").verify(False)

    teststeps = [
        Step(
            RunRequest("Test1")
            .get("/test")
            .with_params(**{"a": 1, "b": "nihao"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.error_code", "0")
            .assert_equal("body.error_message", "success")
            .assert_equal("body.reference", "111")
        ),
        Step(
            RunRequest("Test2")
            .get("/test")
            .with_params(**{"b": "nihao"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.error_code", "0")
            .assert_equal("body.error_message", "success")
            .assert_equal("body.reference", "111")
        ),
        Step(
            RunRequest("Test2")
            .get("/test")
            .with_params(**{"a": 1})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.error_code", "1")
            .assert_equal("body.error_message", "Parameter 'b' is missing")
            .assert_equal("body.reference", "None")
        ),
    ]


if __name__ == "__main__":
    TestCaseRequests().test_start()
