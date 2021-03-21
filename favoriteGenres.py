from collections import defaultdict
def favoGenre(userSongs, songGenres):

    if not userSongs or not songGenres:
        d = {}
        for u in userSongs:
            d[u] = []
        return d
    
    # reverse the genre map:
    s_g = {}
    for gen in songGenres:
        for song in songGenres[gen]:
            s_g[song] = gen
    # GOAL --> s_g = { song123 : Rock }

    u_gens = defaultdict(list)
    for u in userSongs:
        for s in userSongs[u]:
            gen = s_g[s]
            u_gens[u].append(gen)
    # GOAL --> u_gens = {david : [rock, rock, jazz, jazz, pop]}

    final = {}
    for u in u_gens:
        fav_gens = []
        temp = {}
        for s in u_gens[u]:
            if s in temp:
                temp[s] += 1
            else:
                temp[s] = 1
        maxVal = max(temp.values())
        for k in temp:
            if temp[k] == maxVal:
                fav_gens.append(k)
        final[u] = fav_gens
    return final
    # GOAL --> final = {david : {[rock, jazz]}



# TEST 1 #
userSongs, songGenres = {"David": ["song1", "song2", "song3", "song4", "song8"], 
"Emma": ["song5", "song6", "song7"]}, {"Rock":["song1", "song3"], "Dubstep": ["song7"], "Techno":  ["song2", "song4"], "Pop": ["song5", "song6"], "Jazz": ["song8", "song9"]}

# Output: {  
#    "David": ["Rock", "Techno"],
#    "Emma":  ["Pop"]
# }

# TEST 2 #
#userSongs, songGenres = {"David": ["song1", "song2"],"Emma":  ["song3", "song4"]},{}

# Output: {  
#    "David": [],
#    "Emma":  []
# }

print(' -- Favourite Genre --')
print(favoGenre(userSongs, songGenres))