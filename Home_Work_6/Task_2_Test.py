import pytest
from Task_2 import merge_and_write
#
def test_merge_and_write():
    assert merge_and_write("Home_Work_6\\Test1.txt", "Home_Work_6\\Test2.txt", "Home_Work_6\\Test3.txt") == "first second"
def test_merge_and_write_warnings():
    assert merge_and_write("Home_Work_6\\Test12.txt", "Home_Work_6\\Test2.txt", "Home_Work_6\\Test3.txt") == "Один из файлов не найден"
#
@pytest.mark.parametrize("first_path, second_path, third_path",[
    ("Home_Work_6\\Test1.txt", "Home_Work_6\\Test2.txt", "Home_Work_6\\Test3.txt"),  
    ("Home_Work_6\\Test1.txt", "Home_Work_6\\Test3.txt", "Home_Work_6\\Test3.txt"),
    ("Home_Work_6\\Test2.txt", "Home_Work_6\\Test1.txt", "Home_Work_6\\Test3.txt"),
    ("Home_Work_6\\Test2.txt", "Home_Work_6\\Test3.txt", "Home_Work_6\\Test2.txt"),
    ("Home_Work_6\\Test3.txt", "Home_Work_6\\Test1.txt", "Home_Work_6\\Test2.txt"),
    ("Home_Work_6\\Test3.txt", "Home_Work_6\\Test2.txt", "Home_Work_6\\Test1.txt")
])
#
def test_with_no_files_merge_and_write(first_path, second_path, third_path):
    assert merge_and_write(first_path, second_path, third_path) != "Один из файлов не найден"
