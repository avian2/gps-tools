import numpy
import re

class GPSLog:
	def __init__(self):
		self.time = []
		self.time_off = None

		self.lat = []
		self.lon = []

	def get_point(self, time):
		if time < self.time[0]:
			return None
		if time > self.time[-1]:
			return None

		lat = numpy.interp(time, self.time, self.lat)
		lon = numpy.interp(time, self.time, self.lon)

		return lat, lon

def _nmea_to_degrees(s):
	s = s.strip("0")
	deg = float(s[0:2])
	min = float(s[2:])

	return deg + min/60.0

def load(f):
	log = GPSLog()

	for line in f:
		if line.startswith('#'):
			g = re.match("# started at .* \(([0-9.]+)\)", line)
			if g:
				log.time_off = float(g.group(1))
		else:
			time, nmea = line.split()

			nmea_f = nmea.split(",")
			if nmea_f[0] == '$GPGGA':
				log.time.append(float(time))
				log.lat.append(_nmea_to_degrees(nmea_f[2]))
				log.lon.append(_nmea_to_degrees(nmea_f[4]))

	log.time = numpy.array(log.time)
	log.lat = numpy.array(log.lat)
	log.lon = numpy.array(log.lon)

	return log
