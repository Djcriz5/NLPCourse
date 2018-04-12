import codecs
from bs4 import BeautifulSoup

import pkg_resources


def read_raw_text(package, file):
    return codecs.open(get_path(package, file), "r", encoding='utf-8', errors='ignore')


def read_plain_text(package, file):
    return BeautifulSoup(read_raw_text(package, file), 'html.parser').get_text()


def create_raw_text(package, file):
    return codecs.open(get_path(package, file), "a", encoding='utf-8', errors='ignore')


def get_path(package, file):
    return pkg_resources.resource_filename(package, file)
