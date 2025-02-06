#登陆注册

class User:
    def __init__(self, name, password):
        self.username = name
        self.password = password

    def __repr__(self):
        return f"{self.username}|{self.password}"

    def __eq__(self, other):
        if isinstance(other,User):
            return self.username == other.username and self.password == other.password
        return False


class UserManager:

    def register(self, user):
        try :
            with open("users.txt", "a", encoding="utf-8") as f:
                print(user, file=f, flush=True)
                return True
        except FileExistsError as e:
            return False

    def login(self, user):
        #加载文件中的所有用户信息
        with open("users.txt", "r", encoding="utf-8") as f:
            for line in f:
                s = line.strip().split("|")
                username, password = s
                db_user = User(username, password)
                if user == db_user:
                    return True
            return False












if __name__=="__main__":

    usermanager = UserManager()
    user = User("张三","123456789")
    usermanager.register(user)


