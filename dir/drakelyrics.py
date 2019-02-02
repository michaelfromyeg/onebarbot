from time import sleep
from credentials import * # API shtuffs
import lyricsgenius as genius
import hashlib

# Variables
num_songs = 5
completed_lines_hash = set()

# APIs
api2 = genius.Genius(genius_client_token)
drake = api2.search_artist('Drake', sort='popularity', max_songs=num_songs)

for i in range(num_songs):
	print(drake.songs[i])

drake.save_lyrics(format_='txt')

# Clean text file
def clean_text():
	print('File cleaned and saved to CleanLyrics_Drake.txt.')
	removes = ['[']
	with open('Lyrics_Drake.txt') as oldfile, open('CleanLyrics_Drake.txt', 'w') as newfile:
		for line in oldfile:
			hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
			if (not any(remove in line for remove in removes)) and (len(line) >= 20) and (hashValue not in completed_lines_hash):
				newfile.write(line)
				completed_lines_hash.add(hashValue)
		newfile.close()


	
clean_text()