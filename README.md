### `listening-history`

I used to use [Last.fm](https://www.last.fm/) to generate stats based off of my listening habits. My most recent account has 2018-2021 tracked, but I also had an older account that tracked my listens from 2009-2017. Before I deleted the old account, I exported the data to `csv` files. Problem is, Last.fm doesn't let you import older data to new accounts, and manual tracking limits timestamps to the last 14 days prior to entry. So, there's no easy way to take advantage of Last.fm's web interface to display the full listening history.

Still, it felt like a waste to not to do _something_ with this data! [Libre.fm](https://libre.fm/) looked promising at first, but its stats pages aren't very useful. Then I came across [ListenBrainz](https://listenbrainz.org/). The folks at [MetaBrainz](https://metabrainz.org/) really know how to appeal to the data-hoarding, archiving, open source nerd inside me. Any new music I add to my library gets sent through [Picard](https://picard.musicbrainz.org/) first, and I've edited a few entries on [MusicBrainz](https://musicbrainz.org/) when info is missing. The devs over at ListenBrainz even have a nice little Python library ([`pylistenbrainz`](https://github.com/paramsingh/pylistenbrainz)) that interfaces with ListenBrainz's Web API.
