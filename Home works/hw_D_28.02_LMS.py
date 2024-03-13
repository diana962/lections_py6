# Написать платформу для прослушивания музыки
# 1) Класс Пользователь с юзернеймом, возраст, эл. почтой и подпиской(по дефолту - Без подписки, если подписка не оформлена, то с каждым прослушиванием появялется реклама, спам), плейлист(по дефолту - пустой список). Можно дополнительно еще пароль сделать, с валидацией, вся информация должна быть приватной.
# Нужно провалидировать все данные(почту на наличие @, пароль, возраст)

# - Метод для оформления подписки, для добавления в пейлист песни, 
# - метод для прослушивания песни, 
# - метод который прослушивает весь плейлист по очередно

# 2) Класс жанр в названием

# 3) Класс музыка с названием, автором, жанром, длительностью

# 4) Класс работник, который наследуется от Пользователя, но у него есть доп атрибут - роль (например админ), и платформа где он работает

# 5) Класс платформа для прослушивания музыки, например - Spotify, у которого должны быть списки песен, жанры, список пользователей с полпиской и без

# - методы для  просмотра всех песен,
# - методы для просмотра песен по определенному жанру,
# - метод для оформления подписки у пользователя, если
# - метод для поиска песни по названию
# - метод для добавления определенной песни в плейлист пользователя
# - метод удаления, добавления песни, жанра из списка Платформы, которую может сделать только админ этой платформы
# - метод блокировки, удаления пользователя, если это потребуется


class Username:
    def __init__(self, username, age, email, password):
        if self.check_username(username):
            self.username = username
        if self.check_age(age):
            self.age = age
        if self.check_email(email):
            self.email = email
        if self.check_password(password):
            self.password = password
        self.__subscribe = False
        self.__playlist = []

        # print(f'Invalid value for name' if not isinstance(username, str) else self.username)
        # print(f'Invalid value for age' if not isinstance(age, int) else self.age)
        # print('Invalid value for email' if not isinstance(email, str) else self.email) #isinstance(email, email.endswith('@gmail.com')
        # print('Invalid value for subscribe' if not isinstance(subscribe, True) else self.subscribe)

    def check_username(self, username):
        if not isinstance(username, str):
            print('Invalid')   
        else:
            self.__username = username

    def check_age(self, age):
        if isinstance(age, int):
            return age
        else:   
            raise ValueError('Invalid Value for age')
    
    def check_email(self, email):
        for i in email:
            if i == '@':
                return email
        else:
            raise ValueError('Invalid Value for email')
    
    from string import ascii_letters, digits
    symbols = '!@#$%^&*()_-+=<>?/,. '
    def check_password(self, password):
        if len(password) in range(8, 16) and [i for i in password if i in self.symbols] and [i for i in password if i in self.ascii_letters] and [i for i in password if i in self.digits]:
                print('Ваш пароль успешен') 
                return True
        else: 
                raise ValueError('Неправильный пароль')
    
    def subscribe(self):
        self.__subscribe = True

    def add_to_playlist(self, song):
        self.__playlist.append(song)

    def listen_to_song(self, song):
        print(f"Now listening to: {song}")

    def listen_to_playlist(self):
        if not self.__playlist:
            print("Playlist is empty")
        else:
            print("Listening to playlist:")
            for song in self.__playlist:
                print(song)
    def __str__(self):
        return self
    
class  Genre:
    def __init__(self, genre_name):
        self.genre_name = genre_name

class Music:
    def __init__(self, autor, name, genre, duration):
        self.autor = autor
        self.name = name
        self.duration = duration
        self.genre = genre

class Employee(Username):
    def __init__(self, user, email, password, role, platform):
        super().__init__(user, email,  password)
        self.role = role
        self.platform = platform

class Platform:
    def __init__(self,genres_songs,list_users) -> None:
        self.__genres_songs = genres_songs
        self.__list_users = list_users
    
    @property
    def genres_songs(self):
        return self.__genres_songs
    
    @property
    def list_users(self):
        return self.__list_users
    
    def view_all_songs(self):
        for genre, songs in self.__genres_songs.items():
            print(f"{genre} Songs:")
            for song in songs:
                print(f" - {song}")

    def view_songs_by_genre(self, genre_name):
        if genre_name in self.__genres_songs:
            print(f"{genre_name} Songs:")
            for song in self.__genres_songs[genre_name]:
                print(f" - {song}")
        else:
            print(f"No songs found for genre '{genre_name}'.")

    def subscribe_user(self, user):
        user.subs_premium()
        print(f"{user.name} has successfully subscribed.")

    def add_song(self, genre_name, song_name):
        if genre_name in self.__genres_songs and song_name not in self.__genres_songs[genre_name]:
            self.__genres_songs[genre_name].append(song_name)
            print(f"Song '{song_name}' added to genre '{genre_name}' on the platform.")
        else:
            print(f"Song '{song_name}' already exists in genre '{genre_name}' on the platform.")

    def remove_song(self, genre_name, song_name):
        if genre_name in self.__genres_songs and song_name in self.__genres_songs[genre_name]:
            self.__genres_songs[genre_name].remove(song_name)
            print(f"Song '{song_name}' removed from genre '{genre_name}' on the platform.")
        else:
            print(f"Song '{song_name}' not found in genre '{genre_name}' on the platform.")

    def add_genre(self, genre_name):
        if genre_name not in self.__genres_songs:
            self.__genres_songs[genre_name] = []
            print(f"Genre '{genre_name}' added to the platform.")
        else:
            print(f"Genre '{genre_name}' already exists on the platform.")

    def remove_genre(self, genre_name):
        if genre_name in self.__genres_songs:
            del self.__genres_songs[genre_name]
            print(f"Genre '{genre_name}' removed from the platform.")
        else:
            print(f"Genre '{genre_name}' not found on the platform.")
    def search_song(self, song_name):
        for genre, songs in self.__genres_songs.items():
            if song_name in songs:
                print(f"Song '{song_name}' found in genre '{genre}'.")
                return
        print(f"No results found for song '{song_name}'.")

    def add_song_to_user_playlist(self, user, genre_name, song_name):
        if genre_name in self.__genres_songs and song_name in self.__genres_songs[genre_name]:
            user.add_to_playlist(song_name)
            print(f"Song '{song_name}' added to {user.name}'s playlist.")
        else:
            print(f"No results found for song '{song_name}' in genre '{genre_name}'.")


me = Username('Diana', 21, 'i@gmail.com', '123qweASD!')
me.subscribe

spotify = Platform({'Pop': ['Love on', 'Drown', 'little vice', 'Swing fever', 'Training Season'],
                    'Rock': ['Real Estate', 'Catfish and the Bottlemen', 'The Mysterines', 'Linkin Park'],
                    'Hip-Hop': ['Prinz', 'Luciano', 'Skepta', 'PLK', 'Kaaris', 'Nemzzz'],
                    'Indie': ['Gemini Rights', 'who cares', 'glimpse of us', 'Crushing']},
                   ['suxxxida', 'jame', 'donk'])

spotify.view_all_songs()
spotify.view_songs_by_genre('Pop')
spotify.add_song('Pop', 'New Song')
spotify.remove_song('Pop', 'Drown')


spotify.add_genre('R&B')
spotify.remove_genre('R&B')
spotify.search_song('Drown')