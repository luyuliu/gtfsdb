try:
    from ConfigParser import ConfigParser
except ImportError:
    from configparser import ConfigParser
import logging.config
import os
from pkg_resources import resource_filename  # @UnresolvedImport


'''Parse configuration file and setup logging'''
config = ConfigParser()
ini_file = os.path.join(resource_filename('gtfsdb', 'configs'), 'app.ini')
config.read(ini_file)
if config.has_section('loggers'):
    logging.config.fileConfig(ini_file, disable_existing_loggers=False)


'''Application defaults'''
DEFAULT_BATCH_SIZE = 10000
DEFAULT_DATABASE_URL = 'sqlite://'
DEFAULT_IS_GEOSPATIAL = False
DEFAULT_SCHEMA = None

'''Data source constants'''
DATASOURCE_GTFS = 1
DATASOURCE_LOOKUP = 2
DATASOURCE_DERIVED = 3

'''Geometry constants'''
SRID = 4326

'''Order list of class names, used for creating & populating tables'''
SORTED_CLASS_NAMES = [
    'RouteType',
    'RouteFilter',
    'FeedInfo',
    'Agency',
    'Block',
    'Calendar',
    'CalendarDate',
    'Route',
    'RouteDirection',
    'Stop',
    'StopFeature',
    'Transfer',
    'Shape',
    'Pattern',
    'Trip',
    'StopTime',
    'RouteStop',
    'Frequency',
    'FareAttribute',
    'FareRule',
    'UniversalCalendar',
]
