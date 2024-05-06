import pytest

@pytest.fixture(autouse=True)
def my_fixture():
    with open("Home_Work_6\\Test1.txt", "w") as f:
        f.write("first")
    with open("Home_Work_6\\Test2.txt", "w") as f:
        f.write("second")
    with open("Home_Work_6\\Test3.txt", "r") as f:
        pass
