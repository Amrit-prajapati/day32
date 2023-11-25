import smtplib 
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")  
response.raise_for_status()

data = response.json()["iss_position"]  
iss_longi = float(data["longitude"])
iss_lati = float(data["latitude"])

def isNearMe(my_lat = 28.478333402798658, my_long =  77.5181190586513)
    if iss_lati == my_lat and iss_longi == my_long:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        my_email = "GMAIL@GMAIL.COM"
        password  = "PASSWORD"
        try:
            connection = smtplib.SMTP(smtp_server, smtp_port)
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="i.amrit.prajapati@gmail.com", msg="ISS is now over your location, you can see it ")
            connection.close()
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print (f"The location of iss is : ({iss_lati} , {iss_longi}).\nAnd your location is ({my_lat} , {my_long}). Its not over you")


mylat = float(input("Enter the latitude"))
mylong = float(input("Enter the longitude"))
isNearMe(mylat, my_long)