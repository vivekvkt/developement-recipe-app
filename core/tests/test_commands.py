from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandTests(TestCase):
    
    def test_wait_for_db_ready(self):
        """ test waiting for db when  db is availbable """
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_test,1)
        
    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, tst):
        """ test waiting for db """
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError] *5 + True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count,6)