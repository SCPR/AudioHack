from django.utils import unittest
from player.models import Track, Annotation

class TrackTestCase(unittest.TestCase):
    def setUp(self):
        self.boo = Track.objects.create(url="/this/path/boo.mp3", 
                                        title="Ghost Sound",
                                        length=1000,
                                        recorded_date="1/1/1000",
                                        soundcloud_id=21597662,
                                        )
        self.poo = Animal.objects.create(url="/this/path/poo.mp3", 
                                        title="Polite way of saying Cr#!p",
                                        length=2000,
                                        recorded_date="2/2/2000",
                                        soundcloud_id=21597662,
                                        )





<object height="81" width="100%"> <param name="movie" value="http://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F21597662"></param> <param name="allowscriptaccess" value="always"></param> <embed allowscriptaccess="always" height="81" src="http://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F21597662" type="application/x-shockwave-flash" width="100%"></embed> </object>  <span><a href="http://soundcloud.com/user979634/la-public-safety-08-08-11">LA Public Safety 08/08/11</a> by <a href="http://soundcloud.com/user979634">user979634</a></span> 