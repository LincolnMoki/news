import unittest
from app.models import Articles


class TestArticles(unittest.TestCase):
    '''
    Test class to test the behavior of the articles class
    '''

    def setUp(self):
        '''
        Test class to run before other tests
        '''
        self.new_article = Articles('Gary Davenport', 'Loss to Cardinals Exposes 49ers in Bid to Repeat as NFC Champions', 'Sunday at Levis Stadium, the San Francisco 49ers began a difficult task. The list of teams that have made it back to the Super Bowl after losing it the preceding year is not a long one...',
                                    'https://bleacherreport.com/articles/2909005-loss-to-cardinals-exposes-49ers-in-bid-to-repeat-as-nfc-champions', 'https://img.bleacherreport.net/img/images/photos/003/884/173/hi-res-c636598412b064ab00c3de9b59941dd7_crop_exact.jpg?w=1200&h=1200&q=75')
