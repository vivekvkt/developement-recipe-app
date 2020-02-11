import time
from django.db import connections
from django.db.utils import OperationalError
from djagn.core.management.base import BaseCommand

class Command(BaseCommand):
    """ django command  to pause  excution databse util is avialable """
    def handle(self, *args, **options):
        self.stdout.write('waiting for database ...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError :
                self.stdout.write('Database unavailable , waiting 1 second ...')
                time.sleep(1)
            self.stdout.write(self.style.SUCCESS('Database is available'))