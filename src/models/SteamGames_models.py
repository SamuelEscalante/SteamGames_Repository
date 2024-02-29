from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.orm import declarative_base

BASE = declarative_base()

class Games(BASE):
    __tablename__ = 'raw_games1'
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

