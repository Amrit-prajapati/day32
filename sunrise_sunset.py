import requests 


def showtime(lat = float(28.644800) , lng = float(77.216721)):
    request = requests.get(url = f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}")
    request.raise_for_status()
    data = request.json()
    print(f"The timing of sunrise at your location is {data["results"]["sunrise"]}")
    print(f"The timing of sunset at your location is {data["results"]["sunset"]}")

lati = float(input("Enter desired latitude"))
longi  = float(input ("Enter desired longitude"))
showtime(lati , longi)