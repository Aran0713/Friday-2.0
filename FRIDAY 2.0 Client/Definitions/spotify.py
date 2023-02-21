from lib2to3.pgen2 import driver
from time import sleep
import spotipy
import json
import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
# username = 'arantt3'
# clientID = 'bce81e38be294ed28e98f065dd4dd0a3'
# clientSecret = '30433ef4614844c7a3f942233483436d'

# Note: private.json is not uploaded on to github so you will not be able to use spotify without inputting your own keys
import json
with open('.././Information/private.json') as private:
    privateData = json.load(private)
username = privateData["spotifyUsername"]
clientID = privateData["spotifyClientID"]
clientSecret = privateData["spotifyClientSecret"]
redirectURI = 'http://google.com/'

print("In hereeee")
# Create OAuth Object
oauth_object = spotipy.SpotifyOAuth(clientID,clientSecret,redirectURI)
# Create token
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
# Create Spotify Object
spotifyObject = spotipy.Spotify(auth=token)
user = spotifyObject.current_user()
        
### Set up ###        
def setUpPlaylist():
    print("In playlist")
    print("Welcome, "+ user['display_name'])
    path = "../Definitions/chromedriver.exe"
    print("past driver")
    chromeService = Service(executable_path=path)
    driver = webdriver.Chrome(service=chromeService)
    driver.get('https://open.spotify.com/collection/tracks')
    print("opened window")
    driver.maximize_window()
    print("1")
    sleep(2)
    xButton = driver.find_element(by="xpath", value='//button[@class="onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button ot-close-icon"]')
    xButton.click()
    print("2")
    loginButton = driver.find_element(by="xpath", value='//button[@class="Button-sc-qlcn5g-0 jsmWVV"]')
    loginButton.click()
    print("3")
    sleep(2)
    usernameInput = driver.find_element(by="xpath", value='//input[@id="login-username"]')
    usernameInput.click()
    print("4")
    usernameInput.send_keys("aran0713@hotmail.com")
    passwordInput = driver.find_element(by="xpath", value='//input[@id="login-password"]')
    passwordInput.click()
    print("5")
    passwordInput.send_keys("sangeethkeke")
    passwordInput.send_keys(Keys.RETURN)
    print("6")
    return driver
      
        
### Playlists ###
def playLikedSongs():
    driver = setUpPlaylist()
    print("Back in function")
    sleep(5)
    likedSongsButton = driver.find_element(by="xpath", value='//div[@class="g3f_cI5usQX7ZOQyDtA9"]')
    likedSongsButton.click()
        
    sleep(2)
    playButton = driver.find_element(by="xpath", value='//button[@class="Button-sc-qlcn5g-0 futnNt"]')
    playButton.click()
    sleep(2)
    try:
        shuffleButton = driver.find_element(by="xpath", value='//button[@class="KVKoQ3u4JpKTvSSFtd6J"]')
    except NoSuchElementException:
        print("skipped")
    else:
        shuffleButton.click()
        
    return driver

def vibe():
    driver = setUpPlaylist()
            
    sleep(5)
    vibeButton = driver.find_element(by="xpath", value='//div[@class="GlueDropTarget GlueDropTarget--albums GlueDropTarget--tracks GlueDropTarget--local-tracks GlueDropTarget--episodes GlueDropTarget--playlists GlueDropTarget--folders"][1]')
    vibeButton.click()
        
    sleep(2)
    playButton = driver.find_element(by="xpath", value='//button[@class="Button-sc-qlcn5g-0 futnNt"]')
    playButton.click()
    sleep(2)
    try:
        shuffleButton = driver.find_element(by="xpath", value='//button[@class="KVKoQ3u4JpKTvSSFtd6J"]')
    except NoSuchElementException:
        print("skipped")
    else:
        shuffleButton.click()
        
    return driver

def slowSongs():
    driver = setUpPlaylist()
            
    sleep(5)
    slowButton = driver.find_element(by="xpath", value='//div[@class="GlueDropTarget GlueDropTarget--albums GlueDropTarget--tracks GlueDropTarget--local-tracks GlueDropTarget--episodes GlueDropTarget--playlists GlueDropTarget--folders"][2]')
    slowButton.click()
        
    sleep(2)
    playButton = driver.find_element(by="xpath", value='//button[@class="Button-sc-qlcn5g-0 futnNt"]')
    playButton.click()
    sleep(2)
    try:
        shuffleButton = driver.find_element(by="xpath", value='//button[@class="KVKoQ3u4JpKTvSSFtd6J"]')
    except NoSuchElementException:
        print("skipped")
    else:
        shuffleButton.click()
        
    return driver

def tunes():
    driver = setUpPlaylist()
            
    sleep(5)
    tunesButton = driver.find_element(by="xpath", value='//div[@class="GlueDropTarget GlueDropTarget--albums GlueDropTarget--tracks GlueDropTarget--local-tracks GlueDropTarget--episodes GlueDropTarget--playlists GlueDropTarget--folders"][3]')
    tunesButton.click()
        
    sleep(2)
    playButton = driver.find_element(by="xpath", value='//button[@class="Button-sc-qlcn5g-0 futnNt"]')
    playButton.click()
    sleep(2)
    try:
        shuffleButton = driver.find_element(by="xpath", value='//button[@class="KVKoQ3u4JpKTvSSFtd6J"]')
    except NoSuchElementException:
        print("skipped")
    else:
        shuffleButton.click()
        
    return driver
        
        
        
### Close the driver ###
def closeDriver(driver):
    driver.close()



#### Not Implemented ####
def playSong():
    print("Welcome, "+ user['display_name'])
    # Get the Song Name.
    searchQuery = input("Enter Song Name: ")
    # Search for the Song.
    searchResults = spotifyObject.search(searchQuery,1,0,"track")
    # Get required data from JSON response.
    tracks_dict = searchResults['tracks']
    tracks_items = tracks_dict['items']
    song = tracks_items[0]['external_urls']['spotify']
    # Open the Song in Web Browser
    path = "../Definitions/chromedriver.exe"
    chromeService = Service(executable_path=path)
    driver = webdriver.Chrome(service=chromeService)
    driver.get(song)
    driver.maximize_window()
            
    sleep(2)
    xButton = driver.find_element(by="xpath", value='//button[@class="onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button ot-close-icon"]')
    xButton.click()
    loginButton = driver.find_element(by="xpath", value='//button[@class="Button-qlcn5g-0 gPMZVP"]')
    loginButton.click()
    sleep(2)
    usernameInput = driver.find_element(by="xpath", value='//input[@id="login-username"]')
    usernameInput.click()
    usernameInput.send_keys("aran0713@hotmail.com")
    passwordInput = driver.find_element(by="xpath", value='//input[@id="login-password"]')
    passwordInput.click()
    passwordInput.send_keys("sangeethkeke")
    passwordInput.send_keys(Keys.RETURN)
        
    sleep(5)
    playButton = driver.find_element(by="xpath", value='//button[@class="Button-sc-qlcn5g-0 futnNt"]')
    playButton.click()
    
    return driver