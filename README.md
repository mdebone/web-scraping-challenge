# web-scraping-challenge

Didn't realize that I needed to change the name of the local repository differntly from the remote on Git hub, we never have used specified names for the locals before 
but I guess that its probably a good idea to have a signifier that is different for local/remote, would make my life a lot easier. 

So this went a whole lot better after I had a chance to revisit after completing most html homework. So took a bit to get my bearings, but I basically started from scratch. 
I had, and have all of the data pulled from the scapping previously, so no need to revisit that just yet. Instead, I started working from the bootstrap template forward, found a bootswatch template that I liked. 
Got a jumbotron header going, using the css file to specifcy things that I had only previously been doing in the html, but after a thurough read of the MDN web docs, basically the readme of CSS,
and going thru the w3 bootstrap index rather than the html index this was a lot easier.

Since the jumpbtron acts like a header above a header, I was able to create an actual 'header' since none had been created before, I don't think it would stop me if I tried to create two headers, a question
that I am only know giving voice to what I had taken as a given. I have no idea if you can declare two headers in one html file, I just assumed you couldnt. Anyway, from there it was relatively simple to just make 
a col-9, col-3 container for what will be the table on the right and the featured image on the left. I hadn't realized that I had not pulled the Earth data, so the table currently is sort of a wreck.
But that doesn't matter really, its formatted into its space and doesn't seem to be misbehaving. The featured image on the right I thought would happily fill to occupy more of the screen, since I gave it 3/4 of the page. 

Need to see what the resolution on it is, and if messing around with the pixel count in the image will do anything. Important thing is that both headers, seperate from their respective image and table are formated on top in a h4,
that looks pretty good. The real success of the evening was diving deep into card decks, card images and card groups. I thought that I would be able to get the four images of Mars to fill the respective space, 
I did what w3 said and just defined a card deck, and then I realized that I didn't want the image to be nested underneath the card body, there are card images that naturally fill the card space alloated to them.
Okay, progress, but rather than populating left to right across the bottom, the were doing it vertically. Naturally, I thought that maybe the image size had something to do with it,
so I messed around with the px count, 4 images and they were 256 to begin with, seemed kinda large, so I halved it to 128, and nothing. Still vertical. I halved them again down to 64 and still nothing, they remained vertical.

So I took a step back and realized that even as their own thing, cards still need a container, even if they don't use the rows and columns spacing formatting. Still nothing, so I tried making them image colums, w3 has a nifty image of what look like,
well profile pics, but the idea is that you call the card-img-top before the div class card body and I thought for sure I had it, again nope. So on a whim, I tried card-group, rather than card deck and BLAM, 
on load they moved from vertical to horizontal and filled up most of the space alloated to them. Looks good, gave the class a h2, and calling that container done. did the same thing with the col-9, and col-3, and both the featured image and
the table that is in chaos have a header. Will need to scape some Earth facts to go along with the Mars facts, but most of the way thru this.