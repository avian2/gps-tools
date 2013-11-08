from math import pi
from StringIO import StringIO
import unittest

from gps_tools.log import load

class TestLog(unittest.TestCase):
	
	def _open(self):
		return StringIO("""# started at 2013-11-07 09:47:11.468649 (1383814031.468649)
1.657601        $GPGGA,084713,4555.8813,N,01414.2587,E,0,00,,,M,,M,,*5F
2.656886        $GPGGA,084714,4555.8823,N,01414.2597,E,0,00,,,M,,M,,*58
3.655318        $GPGGA,084715,4555.8833,N,01414.2607,E,0,00,,,M,,M,,*59
""")

	def test_basic(self):
		l = load(self._open())

		self.assertEqual(l.time_off, 1383814031.468649)

		self.assertEqual(len(l.time), 3)

		self.assertEqual(len(l.lat), 3)
		self.assertEqual(len(l.lon), 3)

		self.assertEqual(l.time[0], 1.657601)
		self.assertEqual(l.lat[0], 45.931355)
		self.assertEqual(l.lon[0], 14.237645)

	def test_get_point(self):
		l = load(self._open())

		lat, lon = l.get_point((l.time[0] + l.time[1]) * .5)

		self.assertAlmostEqual(lat, (l.lat[0] + l.lat[1]) * .5)
		self.assertAlmostEqual(lon, (l.lon[0] + l.lon[1]) * .5)

from gps_tools import bearing

class TestUtils(unittest.TestCase):
	def test_bearing(self):
		self.assertAlmostEqual(bearing(46.0, 14.0, 46.1, 14.0), 0., places=3)
		self.assertAlmostEqual(bearing(46.0, 14.0, 46.0, 14.01), pi/2., places=3)
		self.assertAlmostEqual(bearing(46.0, 14.0, 45.9, 14.0), pi, places=3)
		self.assertAlmostEqual(bearing(46.0, 14.0, 46.0, 13.99), -pi/2., places=3)
