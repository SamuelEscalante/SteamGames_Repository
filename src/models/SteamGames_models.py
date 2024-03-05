
""" 
SQLAlchemy Table Definition 

This script defines two model classes to represent tables in a database using SQLAlchemy.

Defined Classes:
- Games: Represents the 'raw_games' table with fields related to video game information.
- SteamGames: Represents the 'steam_games' table with additional fields specific to Steam games.

Common Attributes:
- AppID: Unique identifier for each record.
- Name: Name of the game.
- ReleaseDate: Date of the game's release.
- EstimatedOwners: Estimated number of game owners.
- PeakCCU: Peak concurrent players.
- RequiredAge: Minimum age required to play the game.
- Price: Price of the game.
- DLCCount: Number of downloadable content (DLC).
- SupportedLanguages: Languages supported by the game.
- FullAudioLanguages: Languages with full audio support.
- Windows, Mac, Linux: Compatibility information for different operating systems.
- MetacriticScore: Metacritic score of the game.
- UserScore: User score of the game.
- Positive: Number of positive reviews.
- Negative: Number of negative reviews.
- Achievements: Number of in-game achievements.
- Recommendations: Number of user recommendations.
- AveragePlaytimeForever: Average playtime per player (lifetime).
- AveragePlaytimeTwoWeeks: Average playtime per player (last two weeks).
- MedianPlaytimeForever: Median playtime per player (lifetime).
- MedianPlaytimeTwoWeeks: Median playtime per player (last two weeks).
- Developers: Game developers.
- Publishers: Game publishers.
- Categories: Game categories.
- Genres: Game genres.
- Tags: Game tags.
- Screenshots: URLs to game screenshots.
- Movies: URLs to game movies.

Additional Attributes (Only in SteamGames):
- OwnersClean: Cleaned and formatted number of game owners.
- OS: Supported operating systems.
- FreeOrPaid: Indicator of whether the game is free or paid ('paid' for paid, 'free' for free).

Additionally, both classes have a special _str_ method that provides a string representation of the associated table.
""" 
from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.orm import declarative_base

BASE = declarative_base()

class Games(BASE):
    __tablename__ = 'raw_games'
    AppID = Column(Integer, primary_key=True, nullable=False)
    Name = Column(String(), nullable=False)
    ReleaseDate = Column(Date, nullable=False)
    EstimatedOwners = Column(String(), nullable=False)
    PeakCCU = Column(Integer, nullable=False)
    RequiredAge = Column(Integer, nullable=False)
    Price = Column(Float, nullable=False)
    DLCCount = Column(Integer, nullable=False)
    AboutTheGame = Column(String(), nullable=True)
    SupportedLanguages = Column(String(), nullable=False)
    FullAudioLanguages = Column(String(), nullable=False)
    Reviews = Column(String(), nullable=True)
    HeaderImage = Column(String(), nullable=False)
    Website = Column(String(), nullable=True)
    SupportUrl = Column(String(), nullable=True)
    SupportEmail = Column(String(), nullable=True)
    Windows = Column(String(15), nullable=False)
    Mac = Column(String(15), nullable=False)
    Linux = Column(String(15), nullable=False)
    MetacriticScore = Column(Integer, nullable=False)
    MetacriticUrl = Column(String(), nullable=True)
    UserScore = Column(Integer, nullable=False)
    Positive = Column(Integer, nullable=False)
    Negative = Column(Integer, nullable=False)
    ScoreRank = Column(Integer, nullable=True)
    Achievements = Column(Integer, nullable=False)
    Recommendations = Column(Integer, nullable=False)
    Notes = Column(String(), nullable=True)
    AveragePlaytimeForever = Column(Integer, nullable=False)
    AveragePlaytimeTwoWeeks = Column(Integer, nullable=False)
    MedianPlaytimeForever = Column(Integer, nullable=False)
    MedianPlaytimeTwoWeeks = Column(Integer, nullable=False)
    Developers = Column(String(), nullable=True)
    Publishers = Column(String(), nullable=True)
    Categories = Column(String(), nullable=True)
    Genres = Column(String(), nullable=True)
    Tags = Column(String(), nullable=True)
    Screenshots = Column(String(), nullable=True)
    Movies = Column(String(), nullable=True)

class SteamGames(BASE):
    __tablename__ = 'steam_games'
    AppID = Column(Integer, primary_key=True, nullable=False)
    Name = Column(String(), nullable=False)
    ReleaseDate = Column(Date, nullable=False)
    EstimatedOwners = Column(String(), nullable=False)
    PeakCCU = Column(Integer, nullable=False)
    RequiredAge = Column(Integer, nullable=False)
    Price = Column(Float, nullable=False)
    DLCCount = Column(Integer, nullable=False)
    SupportedLanguages = Column(String(), nullable=False)
    FullAudioLanguages = Column(String(), nullable=False)
    Windows = Column(String(15), nullable=False)
    Mac = Column(String(15), nullable=False)
    Linux = Column(String(15), nullable=False)
    MetacriticScore = Column(Integer, nullable=False)
    UserScore = Column(Integer, nullable=False)
    Positive = Column(Integer, nullable=False)
    Negative = Column(Integer, nullable=False)
    Achievements = Column(Integer, nullable=False)
    Recommendations =  Column(Integer, nullable=False)
    AveragePlaytimeForever = Column(Integer, nullable=False)
    AveragePlaytimeTwoWeeks = Column(Integer, nullable=False)
    MedianPlaytimeForever = Column(Integer, nullable=False)
    MedianPlaytimeTwoWeeks = Column(String(), nullable=False)
    Developers = Column(Integer, nullable=False)
    Publishers = Column(String(), nullable=True)
    Categories = Column(String(), nullable=True)
    Genres = Column(String(), nullable=True)
    Tags = Column(String(), nullable=True)
    OwnersClean = Column(Integer, nullable=False)
    OS = Column(String(), nullable=False)
    FreeOrPaid = Column(Integer, nullable=False)