import mysql.connector
import json

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Mueems_Hotel_DB"
)

def search(title, bedroom, bathroom, sleep, price, location):

    # city = 'North Carolina'

    jsonData = []

    mycursor = mydb.cursor()

    sql = ("SELECT * FROM Hotel_details WHERE Name="+f"'{title}' AND Sleeps ="+f"'Sleeps {sleep}' AND Bedroom ="+f"'{bedroom} Bedroom' AND Bathroom ="+f"'{bathroom} Bathroom' AND Location ="+f"'{location}' ")

    print(sql)

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        data = {
            "Title": x[0],
            "Sleeps": x[1],
            "Bedrooms": x[2],
            "Bathrooms": x[3],
            "Picture": {
                "Picture_1": x[4],
                "Picture_2": x[5],
                "Picture_3": x[6],
            },
            "Price": x[7],
            "Location": x[8],
        }
        jsonData.append(data)


    json_object = json.dumps(jsonData, indent = 4)
    # print(json_object)
    return json_object
