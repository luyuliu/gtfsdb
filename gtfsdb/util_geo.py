"""
this is how to add more postgis ST_ functions to geoalchemy2
:see:
"""

from geoalchemy2 import Geometry
from geoalchemy2.functions import GenericFunction


class ST_ExteriorRing(GenericFunction):
    name = 'ST_ExteriorRing'
    type = Geometry


class ST_MakePolygon(GenericFunction):
    name = 'ST_MakePolygon'
    type = Geometry


class ST_Collect(GenericFunction):
    name = 'ST_Collect'
    type = Geometry



def make_point(lon, lat):
    point = 'POINT({0} {1})'.format(lon, lat)
    return point


def make_point_srid(lon, lat, srid='4326'):
    ret_val = 'SRID={0};{1}'.format(srid, make_point(lon, lat))
    return ret_val


def does_point_intersect_geom(point, geom, buffer=0.0):
    """
    return true or false whether point is in / out of the geom
    """
    log.debug('does point intersect this geom')
    ret_val = False
    return ret_val


def point_to_geom_distance(point, geom):
    """
    return true or false whether point is in / out of the geom
    """
    log.debug("distance between point and a geom (assuming they don't intersect")
    ret_val = False
    return ret_val