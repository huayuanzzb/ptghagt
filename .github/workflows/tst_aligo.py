from aligo import Aligo

if __name__ == '__main__':
  ali = Aligo(refresh_token='123456')
  user = ali.get_user()  # 获取用户信息
    ll = ali.get_file_list()  # 获取网盘根目录文件列表
    # 遍历文件列表
    for file in ll:
        print(file.file_id, file.name, file.type)
