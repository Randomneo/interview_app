import os
import re
import wget

import zipfile

from django.core.management.base import BaseCommand, CommandError
from core.models import Locode


def _process_file(file):
    for line in file.readlines():
        print(line)
        Locode.create_from_csv(line, save=True)


class Command(BaseCommand):
    _db_folder = 'db_folder'
    help = 'test command'

    def add_arguments(self, parser):
        parser.add_argument('--url', default='http://www.unece.org/fileadmin/DAM/cefact/locode/loc201csv.zip')
        parser.add_argument('--no-download', default=False, type=bool)

    def handle(self, *args, **options):
        if not options.get('no_download'):
            url = options.get('url')
            db_zip_file = wget.download(url)
            with zipfile.ZipFile(db_zip_file, 'r') as zip_file:
                zip_file.extractall(self._db_folder)
            os.remove(db_zip_file)

        for db_file in os.listdir(self._db_folder):
            if re.match('.*UNLOCODE CodeList.*', db_file):
                with open(os.path.join(self._db_folder, db_file), 'r', encoding='cp1252') as file_data:
                    _process_file(file_data)
