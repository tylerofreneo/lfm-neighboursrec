# lfm-neighboursrec
An alternative song recommender for Last.fm users using Last.fm's Neighbours feature.
# Requirements
A significant amount of recent scrobbles tied to your Last.fm account.
# Prerequisites
`pip install joblib requests beautifulsoup4 python-dotenv scikit-learn`
# Installation
- Get an api key at https://www.last.fm/api/account/create 
- Clone the repo\
`git clone https://github.com/tylerofreneo/lfm-neighboursrec.git`
- Create a file in the main directory named `.env`
- Enter your API key in `.env`\
`LFM_API_KEY = "...................."`
# Usage
`python main.py <your_lastfm_username>`
# Example
`python main.py tyronejafari`
```Screaming - Loathe
Rosemary - Deftones
Gnaw - Alex G
The Razor's Apple - Fleshwater
Backstairs Breathing - Fleshwater
Entombed - Deftones
Ghost Town - Kanye West
Please Please Please Let Me Get What I Want - 2005 Remaster - Deftones
Mimi - 
...
```
Note: Recommendations take ~1min to produce