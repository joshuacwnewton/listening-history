### `listening-history`

This repo stores my music listening history (in file form) and keeps track of what I do with those files. 

----

I used to use [Last.fm](https://www.last.fm/) to generate stats based off of my listening habits. My most recent account has 2018-2021 tracked, but I also had an older account that tracked my listens from 2009-2017. Before I deleted the old account, I exported the data to `csv` files. Problem is, Last.fm doesn't let you import older data to new accounts, and manual tracking limits timestamps to the last 14 days prior to entry. So, there's no easy way to take advantage of Last.fm's web interface to show how my tastes have evolved over time.

Still, I wanted to do _something_ with this data, so I started looking for alternatives. [Libre.fm](https://libre.fm/) looked promising at first, but its stats pages aren't very useful. Then I came across [ListenBrainz](https://listenbrainz.org/). The folks at [MetaBrainz](https://metabrainz.org/) really know how to appeal to the data-hoarding, archiving, open source nerd inside me. Any new music I download gets sent through [Picard](https://picard.musicbrainz.org/) before hitting my library, and I've edited a few entries on [MusicBrainz](https://musicbrainz.org/) when info is missing, so ListenBrainz seemed like a natural fit. The devs over at ListenBrainz even have a nice little Python library ([`pylistenbrainz`](https://github.com/paramsingh/pylistenbrainz)) that interfaces with ListenBrainz's Web API. 

I've got the tools and the data, and now I just need to massage everything into a nice enough form that I can migrate everything over to my account. (Famous last words.)