import media
import fresh_tomatoes
toy_story = media.Movie("Toy Story","A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=JcpWXaA2qeg")
print(toy_story.storyline)

avatar = media.Movie("Avatar"," A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
print(avatar.storyline)

guardians = media.Movie("Guardians of the Galaxy","Aliensss",
                        "https://upload.wikimedia.org/wikipedia/en/9/95/GotG_Vol2_poster.jpg",
                        "https://www.youtube.com/watch?v=2cv2ueYnKjg")
#avatar.show_trailer()
#guardians.show_trailer()
ratatouille = media.Movie("Ratatouille"," A rat is a chef in Paris",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=3YG4h5GbTqU")

tfios = media.Movie("The Fault in our Stars","A love story of cancer patients",
                    "https://upload.wikimedia.org/wikipedia/en/4/41/The_Fault_in_Our_Stars_%28Official_Film_Poster%29.png",
                    "https://www.youtube.com/watch?v=9ItBvH5J6ss")

defenders= media.Movie("Marvel's The Defenders"," A Netfix Marvel Superhero venture",
                       "https://upload.wikimedia.org/wikipedia/en/7/7d/Defenders_Netflix.jpg",
                       "https://www.youtube.com/watch?v=4h3m7B4v6Zc")

movies =  [toy_story,avatar,guardians,ratatouille,tfios,defenders]
fresh_tomatoes.open_movies_page(movies)
