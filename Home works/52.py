# Написать платформу для прослушивания музыки
# 1) Класс Пользователь с юзернеймом, возраст, эл. почтой и подпиской(по дефолту - Без подписки, если подписка не 
# оформлена, то с каждым прослушиванием появялется реклама, спам), плейлист(по дефолту - пустой список). 
# Можно дополнительно еще пароль сделать, с валидацией, вся информация должна быть приватной.
# Метод для оформления подписки, для добавления в пейлист песни, 
# метод для прослушивания песни, 
# метод который прослушивает весь плейлист по очередно

# 2) Класс жанр в названием

# 3) Класс музыка с названием, автором, жанром, длительностью

# 4) Класс работник, который наследуется от Пользователя, но у него есть доп атрибут - роль (например админ), и платформа где он работает

# 5) Класс платформа для прослушивания музыки, например - Spotify, у которого должны быть списки песен, жанры, список пользователей с полпиской и без
# методы для  просмотра всех песен,
# методы для просмотра песен по определенному жанру,
# метод для оформления подписки у пользователя, если
# метод для поиска песни по названию
# метод для добавления определенной песни в плейлист пользователя
# метод удаления, добавления песни, жанра из списка Платформы, которую может сделать только админ этой платформы
import random

class MusicPlayerMixin:
    def playing_playlist(self):
        def listening_one_by_one():
            for song in self.playlist:
                print(f"Now we are listening to the {song}")
        
        def random_song():
            playlist_copy = self.playlist
            while playlist_copy:
                selected_song = random.choice(playlist_copy)
                self.play_song_with_ads(selected_song)
                print(f"Now we are listening to the {selected_song}")
                playlist_copy.remove(selected_song)
            
        listen = input("Do you want to listen all songs one by one or just random? (OneByOne/Random)").lower().strip()
        if 'one' in listen:
            listening_one_by_one()
        elif 'random' in listen:
            random_song() 


class Username(MusicPlayerMixin):
    def __init__(self,name,year,email,password):
        self.__name = name
        self.__year = year
        self.__email = email
        self.__password = password
        self.__playlist=['GOSE']
        self.__subscription= False

    @property
    def name(self):
        return self.__name

    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self,value):
        if value >= 18:
            self.year = value
        else:
            print("User is too young")
    
    @property
    def email(self):
        return self.__email
    
    @property
    def password(self):
        return self.__password
    
    @property
    def playlist(self):
        return self.__playlist
    
      
    
    @property
    def subs(self):
        return self.__subscription
    
    @subs.setter
    def subs(self,value):
        #print("Setting subscription to ",value)
        self.__subscription = value
    
    def subscribe_premium(self):
        if not self.subs:
            self.subs = True
            print(f"{self.name} has successfully subscribed to premium.")
        else:
            print(f"{self.name} is already subscribed to premium.")


    def play_song_with_ads(self, song):
        if self.subs:
            self.listen_song(song)
        else:
            print(f"Playing song '{song}' with ads. Subscribe to premium to remove ads.")

    def __check_password(self):
        if len(self.password)<6:
            return "Password should be at least  6 symbols"
        elif not any(char.isdigit() for char in self.password):
            return "Password should contains digit"
        elif not any(char.islower() for char in self.password):
            return "Password should contains lowercase letter"
        elif not any(char.isupper() for char in self.password):
            return "Password should contains uppercase letter"
        else:
            return "Password strength is strong enough"
    
    def __str__(self):
        return self.__check_password() + f'\nName: {self.name}, Year: {self.year} Email: {self.email} Password: {self.password}'
    
    def add_to_playlist(self, song):
        self.playlist.append(song)
        print(f"Song '{song}' added to the playlist.")

    def listen_song(self, song):
        print(f"Now we are listening to the {song}")

    
    
    

class Genre:
    def __init__(self, genre_name):
        self.genre_name = genre_name
        self.music_library = []

    def add_music(self, music):
        if isinstance(music, Music):
            self.music_library.append(music)
class Music:
    def __init__(self, name, author, duration,genre):
        self.name = name
        self.author = author
        self.duration = duration
        self.genre = genre
    

class Employeel(Username):
    def __init__(self, name, password,platform):
        super(Employeel,self).__init__(name,password)
        self.role = 'Admin'
        self.platform = platform

    
    def show_info(self):
        return f'''
        Name :{self.name}
        Password:{self.password}
        Role :{self.role}
        Platform :{self.platform}
        '''
    
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

    
    
    




user_1 = Username('raychel',18,'raychel@gmail.com','passworD2')

print(user_1)

user_1.add_to_playlist('Ded')
user_1.add_to_playlist('Jmsl')

# user_1.playing_playlist()
print('---------------------------------')
# Создаем экземпляр платформы
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
spotify.add_song_to_user_playlist(user_1, 'Pop', 'Love on')
user_1.playing_playlist()
user_1.subscribe_premium()
user_1.play_song_with_ads('Ded')