# vhxclient
A Python client for the VHX (Vimeo OTT) API

```
from vhxclient import VHXClient
from vhxclient.video import Video

vhx = VHXClient(<api key>)

# create a new video
new_vid = Video(vhx)
new_vid.title = 'A Video'
new_vid.source_url = <publicly-accessable url of source>
new_vid.save()  # loads the response back into the object

old_vid = Video(vhx, <video id>)
old_vid.title
>>> "A Video"
old_vid.description = 'This is the descriptiong of the old vid'
old_vid.save()  # loads the response back into the object

# collections work the same way

# list videos and collections like this
vhx.list('collections')
vhx.list('videos')
```

More features and docs coming.  For more usage examples, look at the tests.
