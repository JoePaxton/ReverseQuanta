# Problem
Is it possible to create a musically appealing song reversing one attribute (bars, beats, tatums, sections, and segments) at a time?

# Question
1. What attributes from [EchoNest Remix] in the audio file will be reversed? Do any of them seem musically appealing?
2. Can we use [reverse.py] from [EchoNest Remix] to compare a hip-hop song with lyrics to its instrumental? If so, how do they compare? 
3. If you reverse the beats on [rewind.mp3], will it produce a lyrical story in forward time? [Nas Rewind Explained]

# Resources
1. [EchoNest Remix]
2. [reverse.py]
3. [Nas - Rewind]
4. [Nas Rewind Explained]

# Question 1
The attributes that I inserted into the [reverse.py] included: tatums, bars, and sections. These are properties that come from the
[EchoNest Remix] AudioAnalysis object. The argument needs to be a valid path to an audio file or a track ID in order for the track to be uploaded
to the Echo Nest Analyze API. When you reverse the bars on a hip-hop tracks with lyrics, it almost seems like you are listening to a "remix" version
of the original. It seems this way because lyricists tend to have rhyme-schemes and melodies that match throughout the instrumental loop. Most hip-
hop songs have the same loop during the standard three verses (not including interludes, bridges, hooks, and etc.). With that being said,
the lyrics tend to seem perfectly normal to the human ear, unless you are breaking down the lyrics. In my opinion, I find that reversing the bars
in the standard hip-hop song is still musically appealing as long as if you are not analyzing the lyrical content.

# Question 2
I modified [reverse.py] inherited from the [EchoNest Remix] examples and added functions so you can reverse the tatums, bars, and sections. 
When you reverse the sections on a traditional hip-hop track, the new audio file sounds like a new song with a few bad transitions, due to a "lag"
at runtime with the reverse() function in the main method in [reverse.py]. When I reversed the sections on the instrumental, the modified track I 
analyzed sounded around the same as the original. When you reverse bars, beats, and tatums the transition tends to stick out more, since these
attributes have a shorter duration than sections and segments.

# Question 3
When I discovered the [reverse.py] script, I quickly thought of a track I am familiar with where the lyrical story during the song is backwards;
hence, the title [Nas - Rewind] (explicit content). The sentences and the lyrics are not backwards until he quotes someone during the story. The story 
is the only thing that is backwards, making the listener have to listen to the whole song in order to understand the story. When I reversed the bars on 
[Nas - Rewind], I went to [Nas Rewind Explained] in order to listen to the story "in order" with the lyrics. As stated before, the transition (appx. 
tenth of a second) is a little "choppy", but I could still listen to the story forwards by looking at the lyrics on [Nas Rewind Explained]. The lyrics
tend to be so confusing, but it is still musically appealing as far as the instruments go.


[EchoNest Remix]: http://echonest.github.io/remix/apidocs/
[reverse.py]: https://github.com/echonest/remix/blob/master/examples/reverse/reverse.py
[Nas - Rewind]: https://www.youtube.com/watch?v=J3Sd2gDkSV8
[Nas Rewind Explained]: http://genius.com/Nas-rewind-lyrics
