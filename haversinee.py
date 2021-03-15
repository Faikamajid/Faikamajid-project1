from math import radians, cos, sin, asin, sqrt
def haver_sine(lon1, lat1, lon2, lat2):
    # converting Decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2]) #radians funtion is being applied to these 4 values
    # Applying haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2      # 2**3= mnz 2*2*2
    c = 2 * asin(sqrt(a))
    r = 6371  # calculating Radius of earth in kilometers. we can Use 3956 for miles
    return c * r
x1 = float(input("Enter longitude FOR location 1:"))
y1 = float(input("Enter latitude FOR location  1:"))
x2 = float(input("Enter longitude FOR location 2:"))
y2 = float(input("Enter latitude FOR location  2:"))
km=(haver_sine(x1, y1, x2, y2))
#print("Distance in kilometers is :",km)
if km<=1:
    print("YES distance is within range of 1km")
else:
    print("NO distance is'nt within range of 1km")