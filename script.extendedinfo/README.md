List of possible wraith script calls.
All calls can also be done by using a plugin path.

Example:
<content>plugin://script.extendedinfo?info=discography&amp;artistname=INSERT_ARTIST_NAME_HERE</content>
- keep Attention to the parameter separators: "&amp;" some places it may need to be "&"
Make your own custom commands:
- RunScript(script.extendedinfo,argument1=value1,argument2=value2)
- RunPlugin(plugin://script.extendedinfo/?argument1=value1&argument2=value2)
- ActivateWindow(Videos,plugin://script.extendedinfo/?argument1=value1&argument2=value2,return)

### Custom

RunScript(script.extendedinfo,info=list,type=movie)     --> Starts script with movie-type
  - optional additional parameter: query=
    - set query to "qqqqq" to force keyboard
  - optional additional parameter: iquery=              --> Executes custom iSearch using movie-list (~/resources/extras/movie/favourites.xml)
    - set iquery to "qqqqq" to force keyboard
  - optional additional parameter: mode=
    - available modes:  incinemas, upcoming,            --> Loads the associated TMDB list fully paged
                        popularmovies, topratedmovies 
                        
                        userlists, genres, opensearch   --> Opens the associated dialog

RunScript(script.extendedinfo,info=list,type=tv)        --> Starts script with tv-type
  - optional additional parameter: query=
    - set query to "qqqqq" to force keyboard
  - optional additional parameter: iquery=              --> Executes custom iSearch using tv-list (~/resources/extras/tv/favourites.xml)
    - set iquery to "qqqqq" to force keyboard
  - optional additional parameter: mode=
    - available modes: populartvshows, topratedtvshows, --> Loads the associated TMDB list fully paged
                       onairtvshows, airingtodaytvshows
                       
                       userlists, genres, opensearch    --> Opens the associated dialog

RunScript(script.extendedinfo,info=list,iquery=)        --> Executes custom iSearch using total list (~/resources/extras/total/favourites.xml)
  - set iquery to "qqqqq" to force keyboard

RunScript(script.extendedinfo,info=list,type=channel)   --> Starts youtube-browser with channel-type
  - optional additional parameter: query=

RunScript(script.extendedinfo,info=list,type=playlist)  --> Starts youtube-browser with playlist-type
  - optional additional parameter: query=

RunScript(script.extendedinfo,info=list,type=video)     --> Starts youtube-browser with video-type
  - optional additional parameter: query=

RunScript(script.extendedinfo,info=list,listid=)        --> Starts script using listid
  - TMDb login required

RunScript(script.extendedinfo,info=string)              --> Sets SkinString (TotalSearch) and refreshes container
  - optional additional parameter: type=
    - if type=tv                                        --> Sets SkinString (ShowSearch) and refreshes container
    - if type=movie                                     --> Sets SkinString (MovieSearch) and refreshes container
    - if type=music                                     --> Sets SkinString (MusicSearch) and refreshes container
    - if type=youtube                                   --> Sets SkinString (YoutubeSearch) and refreshes container


RunScript(script.extendedinfo,info=zmovies)             --> All Movies in Script GUI
  - optional additional parameter: query=

### TheMovieDB Movie-Widget content:
Any of the movie-lists mentioned below can also be opened in the script interface by adding type=script argument

RunScript(script.extendedinfo,info=incinemas)           --> InCinemasMovies.%d
RunScript(script.extendedinfo,info=upcoming)            --> UpcomingMovies.%d
RunScript(script.extendedinfo,info=popularmovies)       --> PopularMovies.%d
RunScript(script.extendedinfo,info=topratedmovies)      --> TopRatedMovies.%d
RunScript(script.extendedinfo,info=similarmovies)       --> SimilarMovies.%d
  - required additional parameters: dbid=
RunScript(script.extendedinfo,info=set)                 --> MovieSetItems.%d
- fetches a list of movies from the same Set
  - required additional parameters: dbid=
RunScript(script.extendedinfo,info=directormovies)      --> DirectorMovies.%d
  - required additional parameters: director=
RunScript(script.extendedinfo,info=writermovies)        --> WriterMovies.%d
  - required additional parameters: writer=
RunScript(script.extendedinfo,info=studio)              --> StudioInfo.%d
- fetches a list of movies from the same studio
  - required additional parameters: studio=

Available Properties:
- 'Title':            Movie Title
- 'OriginalTitle':    Movie OriginalTitle
- 'ID':               TheMovieDB ID
- 'Rating':           Movie Rating (0-10)
- 'Votes':            Vote Count for Rating
- 'Year':             Release Year
- 'Premiered':        Release Date

Available Art:
- 'Fanart':      Movie Fanart
- 'Poster':      Movie Poster

RunScript(script.extendedinfo,info=ztvshows)            --> All TVShows in Script GUI
  - optional additional parameter: query=

### TheMovieDB TVShow-Widget content:
Any of the tvshow-lists mentioned below can also be opened in the script interface by adding type=script argument

RunScript(script.extendedinfo,info=populartvshows)      --> PopularTVShows.%d
RunScript(script.extendedinfo,info=topratedtvshows)     --> TopRatedTVShows.%d
RunScript(script.extendedinfo,info=onairtvshows)        --> OnAirTVShows.%d
RunScript(script.extendedinfo,info=airingtodaytvshows)  --> AiringTodayTVShows.%d

Available Properties:
- 'Title':            TVShow Title
- 'ID':               TVShow MovieDB ID
- 'OriginalTitle':    TVShow OriginalTitle
- 'Rating':           TVShow Rating
- 'Votes':            Number of Votes for Rating
- 'Premiered':        TV Show First Air Date

Available Art:
- 'Poster':      TVShow Poster
- 'Fanart':      TVShow Fanart

### Trakt.tv
RunScript(script.extendedinfo,info=trendingmovies)      --> TrendingMovies.%d
RunScript(script.extendedinfo,info=similarmoviestrakt)  --> SimilarMovies.%d
  - required additional parameters: dbid= (database id) or id= (imdb id)

Available Properties:
- 'Title'
- 'Plot'
- 'Tagline'
- 'Genre'
- 'Rating'
- 'mpaa'
- 'Year'
- 'Premiered'
- 'Runtime'
- 'Trailer'

Available Art:
- 'Poster'
- 'Fanart'

RunScript(script.extendedinfo,info=trendingshows)         --> TrendingShows.%d
RunScript(script.extendedinfo,info=similartvshowstrakt)   --> SimilarTVShows.%d
  - required additional parameters: dbid= (database id) or id= (tvdb id)

Available Properties:
- 'TVShowTitle':      TVShow Title
- 'duration':         Duration (?)
- 'Plot':             Plot
- 'ID':               ID
- 'Genre':            Genre
- 'Rating':           Rating
- 'mpaa':             mpaa
- 'Year':             Release Year
- 'Premiered':        First Air Date
- 'Status':           TVShow Status
- 'Studio':           TVShow Studio
- 'Country':          Production Country
- 'Votes':            Amount of Votes
- 'Watchers':         Amount of Watchers
- 'AirDay':           Day episode is aired
- 'AirShortTime':     Time episode is aired

Available Art:
- 'Poster':      TVShow Poster
- 'Banner':      TVShow Banner
- 'Fanart':      TVShow Fanart

RunScript(script.extendedinfo,info=airingshows)         --> AiringShows.%d
RunScript(script.extendedinfo,info=premiereshows)       --> PremiereShows.%d

Available Properties:
- 'Title':         Episode Title
- 'TVShowTitle':   TVShow Title
- 'Plot':          Episode Plot
- 'Genre':         TVShow Genre
- 'Runtime':       Episode Duration
- 'Year':          Episode Release Year
- 'Certification': TVShow Mpaa Rating
- 'Studio':        TVShow Studio
- 'Thumb':         Episode Thumb

Available Art:
- 'Poster':   TVShow Poster
- 'Banner':   TVShow Banner
- 'Fanart':   TVShow Fanart


### TheAudioDB
RunScript(script.extendedinfo,info=discography)         --> Discography.%d
- fetches the artist discography (Last.FM)
  - required additional parameters: artistname=

Available Properties:
- 'Label':           Album Title
- 'artist':          Album Artist
- 'mbid':            Album MBID
- 'id':              Album AudioDB ID
- 'Description':     Album Description
- 'Genre':           Album Genre
- 'Mood':            Album Mood
- 'Speed':           Album Speed
- 'Theme':           Album Theme
- 'Type':            Album Type
- 'thumb':           Album Thumb
- 'year':            Album Release Year
- 'Sales':           Album Sales

RunScript(script.extendedinfo,info=mostlovedtracks)         --> MostLovedTracks.%d
- fetches most loved tracks for the given artist (TheAudioDB)
  - required additional parameters: artistname=
RunScript(script.extendedinfo,info=albuminfo)               --> TrackInfo.%d
  - required additional parameters: id= ???

Available Properties:
- 'Label':       Track Name
- 'Artist':      Artist Name
- 'mbid':        Track MBID
- 'Album':       Album Title
- 'Thumb':       Album Thumb
- 'Path':        Link to Youtube Video

RunScript(script.extendedinfo,info=artistdetails) ???

### LastFM
RunScript(script.extendedinfo,info=albumshouts)
- fetches twitter shouts for given album
  - required additional parameters: artistname=, albumname=
RunScript(script.extendedinfo,info=artistshouts)
- fetches twitter shouts for given artist
  - required additional parameters: artistname=

- 'comment':  Tweet Content
- 'author':   Tweet Author
- 'date':     Tweet Date

RunScript(script.extendedinfo,info=topartists)
- fetches a lists of the most popular artists
RunScript(script.extendedinfo,info=hypedartists)

Available Properties:
- 'Title':        Artist Name
- 'mbid':         Artist MBID
- 'Thumb':        Artist Thumb
- 'Listeners':    actual Listeners

RunScript(script.extendedinfo,info=nearevents)       --> NearEvents.%d
  - optional parameters: lat=, lon=, location=, distance=, festivalsonly=, tag=

Available Properties:
- 'date':         Event Date
- 'name':         Venue Name
- 'venue_id':     Venue ID
- 'event_id':     Event ID
- 'street':       Venue Street
- 'eventname':    Event Title
- 'website':      Event Website
- 'description':  Event description
- 'postalcode':   Venue PostalCode
- 'city':         Venue city
- 'country':      Venue country
- 'lat':          Venue latitude
- 'lon':          Venue longitude
- 'artists':      Event artists
- 'headliner':    Event Headliner
- 'googlemap':    GoogleMap of venue location
- 'artist_image': Artist image
- 'venue_image':  Venue image

### YouTube
RunScript(script.extendedinfo,info=youtubesearch)           --> YoutubeSearch.%d
  - required additional parameters: id=
RunScript(script.extendedinfo,info=youtubeplaylist)         --> YoutubePlaylist.%d
  - required additional parameters: id=
RunScript(script.extendedinfo,info=youtubeusersearch)       --> YoutubeUserSearch.%d
  - required additional parameters: id=

Available Properties:
- 'Thumb':        Video Thumbnail
- 'Description':  Video Description
- 'Title':        Video Title
- 'Date':         Video Upload Date

### Misc Images
RunScript(script.extendedinfo,info=xkcd)                   --> XKCD.%d
- fetches a daily random list of XKCD webcomics
RunScript(script.extendedinfo,info=cyanide)                --> CyanideHappiness.%d
- fetches a daily random list of Cyanide & Happiness webcomics
RunScript(script.extendedinfo,info=dailybabe)              --> DailyBabe.%d
RunScript(script.extendedinfo,info=dailybabes)             --> DailyBabes.%d

Available Properties:
- 'Thumb':        Image
- 'Title':        Image Title
- 'Description':  Image Description (only XKCD)

info=similarlocal
    Property Prefix: SimilarLocalMovies
    needed parameters:
    -dbid: DBID of any movie in your library
fetches similar movies from local database

### Misc Calls:
info=artistdetails
    needed parameters:
        artistname: Artist to search for
- also fetches Discography and MusicVideos ATM
info=albuminfo ## todo
    needed parameters:
        artistname: Artist to search for
- also fetches Discography and MusicVideos ATM

### ActorInfo / MovieInfo Dialogs (script.metadata.actors replacement)
possible script call for Actor Info Dialog:
RunScript(script.extendedinfo,info=extendedactorinfo,name=ACTORNAME)
RunScript(script.extendedinfo,info=extendedactorinfo,id=ACTOR_TMDB_ID)

possible script calls for Movie Info Dialog:
RunScript(script.extendedinfo,info=wraith,name=MOVIENAME)
RunScript(script.extendedinfo,info=wraith,id=MOVIE_TMDB_ID)
RunScript(script.extendedinfo,info=wraith,dbid=MOVIE_DBID)
RunScript(script.extendedinfo,info=wraith,imdb_id=IMDB_ID)

----

## SKINNING ADD-ON DIALOGS:
Please have a look at reference implementation, too much to cover. Consider the following docs as outdated, needs some updating.

#### List of Built In Controls for add-on dialogs :
 - MOVIES, TVSHOWS, SEASONS, EPISODES: script.extendedinfo-DialogVideoInfo.xml
 - ACTORS: script.extendedinfo-DialogInfo.xml

| IDS     | MOVIES    | TVSHOWS   | SEASONS   | EPISODES | ACTORS      |
|---------|-----------|-----------|-----------|----------|-------------|
| 150     | Similar   | Similar   | ---       | ---      | Movie Roles |
| 250     | Sets      | Seasons   | ---       | ---      | TV Roles    |
| 350     | Youtube   | Youtube   | Youtube   | Youtube  | Youtube     |
| 450     | Lists     | ---       | ---       | ---      | Images      |
| 550     | Studios   | Studios   | ---       | ---      | Movie Crew  |
| 650     | Releases  | Certific  | ---       | ---      | TV Crew     |
| 750     | Crew      | Crew      | Crew      | Crew     | Tagged Img  |
| 850     | Genres    | Genres    | ---       | ---      | ---         |
| 950     | Keywords  | Keywords  | ---       | ---      | ---         |
| 1000    | Actors    | Actors    | Actors    | Actors   | ---         |
| 1050    | Reviews   | ---       | ---       | ---      | ---         |
| 1150    | Videos    | Videos    | Videos    | Videos   | ---         |
| 1250    | Images    | Images    | Images    | ---      | ---         |
| 1350    | Backdrops | Backdrops | Backdrops | Images   | ---         |
| 1450    | ---       | Networks  | ---       | ---      | ---         |
| 2000    | ---       | ---       | Episodes  | ---      | ---         |

#### Labels Available In script.extendedinfo-DialogInfo.xml:

Labels of the currently selected actor / director / writer / artist.
- Window(home).Property(Title) ----------------------> Name
- Window(home).Property(Label) ----------------------> Same as Title
- Window(home).Property(Poster)----------------------> Poster
- Window(home).Property(Plot)------------------------> Biography
- Window(home).Property(Biography) ------------------> Same as Plot
- Window(home).Property(TotalMovies) ----------------> Total of Known Movies (acting / directing / writing)
- Window(home).Property(Birthday) -------------------> Date of Birthday
- Window(home).Property(HappyBirthday) --------------> return true or empty
- Window(home).Property(Age) ------------------------> Age (30)
- Window(home).Property(AgeLong) --------------------> Age long format (age 30)
- Window(home).Property(Deathday) -------------------> Date of Deathday
- Window(home).Property(PlaceOfBirth) ---------------> Place of birth
- Window(home).Property(AlsoKnownAs) ----------------> Also Known Name
- Window(home).Property(Homepage) -------------------> Link of homepage
- Window(home).Property(Adult) ----------------------> Is Adult Actor (no / yes)
- Window(home).Property(fanart) ---------------------> Fanart

Labels of Known Movies list
- Container(150).ListItem.Label ---------------------> Title of movie
- Container(150).ListItem.Title ---------------------> same as label
- Container(150).ListItem.originaltitle -------------> originaltitle
- Container(150).ListItem.Year ----------------------> year
- Container(150).Listitem.Icon ----------------------> icon of movie
- Container(150).ListItem.Property(role) ------------> role in currently slected movie
- Container(150).ListItem.Property(job) -------------> job in currently slected movie (director / writer / etc)
- Container(150).ListItem.Property(release_date) ----> release date of movie
- Container(150).ListItem.Property(year) ------------> same as year, but not return empty
- Container(150).ListItem.Property(DBID) ------------> return 1 or empty, if movie exists in library
- Container(150).ListItem.Property(Playcount) -------> Playcount of movie (default is 0)
- Container(150).ListItem.Property(file) ------------> media to play

Labels of thumbs list
- Container(250).ListItem.Label ---------------------> Image résolution (512x720)
- Container(250).Listitem.Icon ----------------------> Image
- Container(250).ListItem.Property(aspect_ratio) ----> Aspect Ratio (0.66)

[...](WIP)

#### Labels Available In script.extendedinfo-DialogVideoInfo.xml:

[...](WIP)
