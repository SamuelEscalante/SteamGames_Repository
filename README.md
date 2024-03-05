# ETL ~ Steam Game Dataset ~ Data Engineer Project <img align="center" src="https://static.vecteezy.com/system/resources/previews/020/975/555/non_2x/steam-logo-steam-icon-transparent-free-png.png" alt="Steam logo" height="150px" width="150px">

*Presented by :*  
- Samuel Escalante Gutierrez - [@SamuelEscalante](https://github.com/SamuelEscalante)
- Manuela Mayorga Rojas - [@ManuelaMayorga](https://github.com/ManuelaMayorga)
- Mariana Mera Gutierrez - [@MarianaMera12](https://github.com/MarianaMera12)

## Welcome


### Tools used

- *Python* <img src="https://cdn-icons-png.flaticon.com/128/3098/3098090.png" alt="Python" width="21px" height="21px">
- *Jupyter Notebooks* <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/883px-Jupyter_logo.svg.png" alt="Jupyer" width="21px" height="21px">
- *PostgreSQL* <img src="https://cdn-icons-png.flaticon.com/128/5968/5968342.png" alt="Postgres" width="21px" height="21px">
- *Power BI* <img src="https://1000logos.net/wp-content/uploads/2022/08/Microsoft-Power-BI-Logo.png" alt="PowerBI" width="30px" height="21px">
- *SQLAlchemy* <img src="https://quintagroup.com/cms/python/images/sqlalchemy-logo.png/@@images/eca35254-a2db-47a8-850b-2678f7f8bc09.png" alt="SQLalchemy" width="50px" height="21px">

### Requirements for this project
1. Install Python : [Python Downloads](https://www.python.org/downloads/)
2. Install PostgreSQL : [PostgreSQL Downloads](https://www.postgresql.org/download/)
3. Install Power BI : [Install Power BI Desktop](https://www.microsoft.com/en-us/download/details.aspx?id=58494) 

## Dataset Description

The data used in this project was obtained from [Steam Games Dataset](https://www.kaggle.com/datasets/fronkongames/steam-games-dataset/data). Be sure to review and comply with the terms and conditions of use of the original source before using this data for any purpose.

Information of more than 85,000 games published on Steam

- *appID*: Unique identifier for each app (string).
- *name*: Game name (string).
- *releaseDate*: Release date (string).
- *estimatedOwners*: Estimated owners (string, e.g.: "0 - 20000").
- *peakCCU*: Number of concurrent users, yesterday (int).
- *required_age*: Age required to play, 0 if it is for all audiences (int).
- *price*: Price in USD, 0.0 if it's free (float).
- *dlcCount*: Number of DLCs, 0 if you have none (int).
- *longDesc*: Detailed description of the game (string).
- *shortDesc*: Brief description of the game, does not contain HTML tags (string).
- *languages*: Comma-separated enumeration of supporting languages.
- *fullAudioLanguages*: Comma-separated enumeration of languages with audio support.
- *reviews*: Game reviews.
- *headerImage*: Header image URL in the store (string).
- *website*: Game website (string).
- *supportWeb*: Game support URL (string).
- *supportEmail*: Game support email (string).
- *supportWindows*: Does it support Windows? (bool).
- *supportMac*: Does it support Mac? (bool).
- *supportLinux*: Does it support Linux? (bool).
- *metacriticScore*: Metacritic score, 0 if it has none (int).
- *metacriticURL*: Metacritic review URL (string).
- *userScore*: Users score, 0 if it has none (int).
- *positive*: Positive votes (int).
- *negative*: Negative votes (int).
- *scoreRank*: Score rank of the game based on user reviews (string).
- *achievements*: Number of achievements, 0 if it has none (int).
- *recommendations*: User recommendations, 0 if it has none (int).
- *notes*: Extra information about the game content (string).
- *averagePlaytime*: Average playtime since March 2009, in minutes (int).
- *averageplaytime2W*: Average playtime in the last two weeks, in minutes (int).
- *medianPlaytime*: Median playtime since March 2009, in minutes (int).
- *medianPlaytime2W*: Median playtime in the last two weeks, in minutes (int).
- *developers*: Developer name (string).
- *publishers*: Publisher name (string).
- *categories*: Category name (string).
- *gender*: Gender name (string).
- *scrennshots*: Game screenshot URL (string).
- *movie*: Game movie URL (string).
- *tags*: Tag key (string, int).

## ¿How to run this project?

1. Clone this reposiory
```bash
  git clone https://github.com/SamuelEscalante/SteamGames_Repository.git
```

2. Go to the project directory
```bash
  cd SteamGames_Repository
```

3. Create virtual environment for Python
```bash
  python -m venv venv
```

4. Start the virtual environment
```bash
  ./venv/Scripts/activate
```

5. Install libreries
```bash
  pip install -r requirements.txt
```

6. Create a configuration file named `credentials.json` in the project's root directory and add the following keys to the file:
```json
{
  "DIALECT": "The database dialect or type. In this case, it is set to 'postgres' for PostgreSQL.",
  "PGUSER": "Your PostgreSQL database username.",
  "PGPASSWD": "Your PostgreSQL database password.",
  "PGHOST": "The host address or IP where your PostgreSQL database is running.",
  "PGPORT": "The port on which PostgreSQL is listening.",
  "PGDB": "The name of your PostgreSQL database."
}

```

7. Create a `.env` file and add this variable:  
   `WORK_DIR` <- Sets the working directory for the application, indicating the base path for performing operations and managing files.
   
8. Create a database in PostgreSQL (Make sure it has the same name as your file `credentials.json`)}

9. Explore the project, you shoul start by folder **notebooks** :
   - _001_load_data:_  this notebook focused on initial data insertion into database
   - _EDA/002_raw_eda:_ this notebook is the Exploratory Data Analysis
   - _003_adicional_csvs:_ the output of this notebook is additional CSV files that are explained in the notebook and will be saved inside the `data` folder
## Farewell and Thanks

Thank you for visiting our repository! We hope you find this project useful. If it has been helpful or you simply liked it, consider giving the repository a star! 🌟

We would love to hear your feedback, suggestions, or contributions.

Thanks for your support! 👋
