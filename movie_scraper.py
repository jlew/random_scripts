from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

def getMoviesAtTheater(id):
    soup = BeautifulSoup(urlopen("http://www.google.com/movies?tid=%s" % id))
    movie_list = []

    for movie in soup.findAll("div",{"class":"movie"}):
        movieData = {}
        try:
            movieData['name'] = movie.find("div", {"class":"name"}).contents[0].string
        except:
            movieData['name'] = "BORKED"

        try:
            movieData['info'] = movie.find("span", {"class":"info"}).contents[0].string
        except:
            movieData['info'] = "BORKED"
        try:
            movieData['time'] = movie.find("div",{"class":"times"}).contents[0].string.split("&nbsp; ")
        except:
            movieData['time'] = ["BORKED"]
        movie_list.append(movieData)

    return movie_list

movie_theaters = {
    "Movies 10":"4b1e850b4dc5d28",
    "Regal":"461d4c09947de2f2"
    }

for theater in movie_theaters:
    mlist = getMoviesAtTheater(movie_theaters[theater])
    print
    print
    print theater
    for movie in mlist:
        print "\t",movie['name'],":\t",", ".join(movie['time'])

