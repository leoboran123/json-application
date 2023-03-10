import json
import os

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        # load users from .json file
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists("json_uygulama/users.json"):
            with open("json_uygulama/users.json","r",encoding="utf-8") as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username = user['username'], password = user['password'], email = user['email'])
                    self.users.append(newUser)
            print(self.users)

    def register(self, user: User):
        self.users.append(user)
        self.savetoFile()
        print("Kullanıcı oluşturuldu.")

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password==password:
                self.isLoggedIn = True
                self.currentUser = user
                print("Giriş yapıldı.")
                break
    def Logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print("Çıkış yapıldı")
    def identity(self):
        if self.isLoggedIn:
            print(f"username: {self.currentUser.username}")
        else:
            print("Giriş yapılmadı")
    def savetoFile(self):
        list = []

        for user in self.users:
            list.append(json.dumps(user.__dict__))

        with open("json_uygulama/users.json","w") as file:
            json.dump(list, file)

repository = UserRepository()

while True:
    print("Menü".center(50,"*"))
    secim = input("1-Register\n2-Login\n3-Logout\n4-Identity\n5-Exit\nSeçiminiz: ")
    if secim == "5":
        break
    else:
        if secim == "1":
            #register
            username = input("username: ")
            password = input("password: ")
            email = input("email: ")
            
            user = User(username = username, password = password, email= email)
            repository.register(user)

            print(repository.users)
        elif secim == "2":
            if repository.isLoggedIn:
                print("Zaten giriş yaptınız.")
            else:
                username = input("username: ")
                password = input("password: ")
                repository.login(username, password)
        elif secim == "3":
            repository.Logout()
        elif secim == "4":
            repository.identity()
        else:
            print("Yanlış bir değer girdiniz.")











