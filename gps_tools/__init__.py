from math import acos, atan2, cos, sin, radians

def distance(lat1, lon1, lat2, lon2):
	if lat1 == lat2 and lon1 == lon2:
		return 0.0
	else:
		return acos(
				sin(radians(lat1)) * sin(radians(lat2)) +
				cos(radians(lat1)) * cos(radians(lat2)) * 
				cos(radians(lon1 - lon2))
		) * 6372.8 * 1e3

def bearing(lat1, lon1, lat2, lon2):
	y = sin(radians(lon2 - lon1)) * cos(radians(lat2))
	x = cos(radians(lat1)) * sin(radians(lat2)) - sin(radians(lat1)) * cos(radians(lat2)) * cos(radians(lon2 - lon1))

	return atan2(y, x)
