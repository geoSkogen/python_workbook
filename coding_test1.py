class Catalog(object):

    def __init__(self, songs):
        self.songs = songs

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics


def begin_entry():
    playlist = []
    catalog = Catalog(playlist)
    prompt = "> "
    #these are nested methods; flow control begins below
    def enter_lines():
        lines = []
        print("enter title")
        lines.append(input(prompt))
        print("enter line by line")
        i = 1
        lines.append(input(prompt))
        while lines[i] != "end":
            i += 1
            lines.append(input(prompt))
        if lines[i] == "end":
            print(lines)
            next_song = Song(lines)
            catalog.songs.append(lines)
            begin_entry()

    def search_by_title(thistitle):
        titlefound = False
        for i in catalog.songs:
            if i[0] == thistitle:
                titlefound = True
                print(i)
                begin_entry()
        if titlefound == False:
            print("no matches found for %s" % thistitle)
            begin_entry()

    def get_title():
        serchtitle = input(prompt)
        search_by_title(searchtitle)        

    def make_selection(char):
        if char == "N":
            enter_lines()
        elif char == "V":
            print(catalog.songs)
            begin_entry()
        elif char == "D":
            print("delete coming soon")
            begin_entry()
        else:
            print("whatup python?")
            begin_entry()

    #flow control begins here
    print ("N = new song || V = view song || D = delete song")
    selector =  input(prompt)
    if selector == "N" or selector == "V" or selector == "D":
        make_selection(selector)
    else:
        print("unrecognized character")
        being_entry()

begin_entry()
