import requests
import webbrowser
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from requests.exceptions import ConnectionError
myfile1 = open("apipage1.html", "w")
myfile2 = open("apipage2.html", "w")
myfile3 = open("apipage3.html", "w")
myfile4 = open("apipage4.html", "w")
try:
    x = requests.get("http://google.com")
except ConnectionError as e:
    messagebox.showinfo("WiFi Error", "Please Connect with WiFi to continue")
def processBtn():
        headers = {
    'Accept': 'application/json',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6Ijk2ZjY3ZWEyLWFjYzYtNDgzMC05ODZlLTg4ZjllNzQ5MjI1ZSIsImlhdCI6MTU3MTgwMDY4Mywic3ViIjoiZGV2ZWxvcGVyL2MyYjY1NmYzLWE4MGMtOWU4Mi03MTdmLTcwY2I2YWYwZjY3YSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI5OS4yNDAuMTUyLjEzMyJdLCJ0eXBlIjoiY2xpZW50In1dfQ.Zpy-Sl_qmAsEcTQh5lqI8EIJox6G7TF6DhT1-SK6zwl1uPSK46JYpgZCEzcFsHvKi3nIv1-6Ae5H6ieIrl4vFQ'
}
        response = requests.get("https://api.clashroyale.com/v1/players/%23" + str(enterTag.get().upper()), headers = headers)
        response2 = requests.get("https://api.clashroyale.com/v1/players/%23" + str(enterTag.get().upper()) + "/upcomingchests", headers = headers)
        userdata = response.json()
        userdata2 = response2.json()
        try: 
            clan = str(userdata['clan']['name'])
            role = str(userdata['role'])
        except:
            clan = "No Clan"
            role = "No Role"
        if (response.status_code == 200):
            winrate = str(((userdata['wins'])/((userdata['wins']) + (userdata['losses']))*100))
            #Write on website
            filename1 = 'file:///Users/mikey.thien/Desktop/Year-10/Design/apipage1.html'
            filename2 = 'file:///Users/mikey.thien/Desktop/Year-10/Design/apipage2.html'
            filename3 = 'file:///Users/mikey.thien/Desktop/Year-10/Design/apipage3.html'
            webbrowser.open_new_tab(filename1)
            myfile1.write("""
            <head> <link rel = "stylesheet" type = "text/css" href = "clashroyale.css" /></head>
            <body>
            <div class="topnav">
                <a  class = "active" href="apipage1.html">Personal Statistics</a>
                <a href="apipage2.html">Cards & Decks</a>
                <a href="apipage3.html">Achievements</a>
                <a href = "apipage4.html">Upcoming Chests</a>
            </div>
            <img src = """"banner.jpg"""" width = 100%>
            <h1>"""+str(userdata['name'])+ """'s Clash Royale Statistics</h1>

            <table>
              <tr>
                <th>Individual Information:  - """+str(userdata['name'])+"""</th>
                <th></th>
              </tr>
              <tr>
                <td>Player Tag</td>
                <td>""" + enterTag.get().upper() + """</td>
              </tr>
              <tr>
                <td>King Tower Level</td>
                <td>Level """ + str(userdata['expLevel']) + """</td>
              </tr>
              <tr>
                <td>Player Trophies</td>
                <td>"""+ str(userdata['trophies']) +""" trophies</td>
              </tr>
              <tr>
                <td>Best Trophies</td>
                <td>"""+ str(userdata['bestTrophies']) + """ trophies</td>
              </tr>
              <tr>
                <td>Player Wins</td>
                <td>"""+str(userdata['wins'])+""" games won</td>
              </tr>
              <tr>
                <td>Player Losses</td>
                <td>"""+str(userdata['losses'])+""" games lost</td>
              </tr>
              <tr>
                <td>Win %</td>
                <td>""" + str(winrate) +"""%</td>
              </tr>
              <tr>
                <td>Clan Name</td>
                <td>""" + clan + """ - """+role+"""</td>
              </tr>
            </table>
            """)
            myfile1.write("</table></body>")
            myfile1.close()
            myfile2.write("""
            <head> <link rel = "stylesheet" type = "text/css" href = "clashroyale.css" /></head>
            <body>
            <div class="topnav">
                <a href="apipage1.html">Personal Statistics</a>
                <a class = "active" href="apipage2.html">Cards & Decks</a>
                <a href="apipage3.html">Achievements</a>
                <a href = "apipage4.html">Upcoming Chests</a>
            </div>
            <img src = """"banner.jpg"""" width = 100%>
            <h1>"""+str(userdata['name'])+ """'s Cards and Decks</h1>
            <h2>Cards and Deck Information - """+str(userdata['name'])+"""</h2>
            <h3>The last 8 cards form your deck!</h3>
            <table>
              <tr>
                <th>Card Name</th>
                <th>Card Level</th>
                <th>Card Icon</th>
                <th>Number of Cards</th>
              </tr>
            """)
            for i in range(len(userdata['cards'])):
                myfile2.write("""
                <tr>
                  <th>Card Name: """+ str(userdata['cards'][i]['name']) + """</th>
                  <th>Lvl """+ str(userdata['cards'][i]['level'])+ """</th>
                  <th><img src = """+ userdata['cards'][i]['iconUrls']['medium'] +""" width = "100"></th>
                  <th>Number of Cards: """+ str(userdata['cards'][i]['count']) + """</th>
                </tr>
                """)
            myfile2.write("""
            </table></body>
            """)
            myfile2.close()
            myfile3.write("""
            <head> <link rel = "stylesheet" type = "text/css" href = "clashroyale.css" /></head>
            <body>
            <div class="topnav">
                <a href="apipage1.html">Personal Statistics</a>
                <a href="apipage2.html">Cards & Decks</a>
                <a class = "active" href="apipage3.html">Achievements</a>
                <a href = "apipage4.html">Upcoming Chests</a>
            </div>
            <img src = """"banner.jpg"""" width = 100%>
            <h1>"""+str(userdata['name'])+ """'s Clash Royale Achievements & Badges </h1>
            <h2>Achievements & Badges - """+str(userdata['name'])+"""</h2>
            <h3>Congratulations on all of these amazing badges!</h3>
            <table>
              <tr>
                <th>Badges</th>
                <th>Progress</th>
              </tr>
            """)
            for i in range(len(userdata['badges'])):
                myfile3.write("""
                <tr>
                  <th>Badge: """+ str(userdata['badges'][i]['name']) + """</th>
                  <th>Progress: """+ str(userdata['badges'][i]['progress'])+ """</th>
                </tr>
                """) 
            myfile3.write(
            """
            </table>
            <h3>Congratulations! These are all of the achievements you have unlocked.</h3>
            <table>
              <tr>
                <th>Achievement</th>
                <th>Description</th>
                <th>Value</th>
                <th>Stars</th>
              </tr>
            """)
            for i in range(len(userdata['achievements'])):
                myfile3.write("""
                <tr>
                  <th>Name: """+ str(userdata['achievements'][i]['name']) + """</th>
                  <th>Info: """+ str(userdata['achievements'][i]['info'])+ """</th>
                  <th>Value: """+ str(userdata['achievements'][i]['value']) + """</th>
                  <th>Stars: """+ str(userdata['achievements'][i]['stars']) + """</th>
                </tr>
                """)
            myfile3.write("</table></body>")
            myfile3.close()
            myfile4.write("""
            <head> <link rel = "stylesheet" type = "text/css" href = "clashroyale.css" /></head>
            <body>
            <div class="topnav">
                <a href="apipage1.html">Personal Statistics</a>
                <a href="apipage2.html">Cards & Decks</a>
                <a href="apipage3.html">Achievements</a>
                <a class = "active" href = "apipage4.html">Upcoming Chests</a>
            </div>
            <img src = """"banner.jpg"""" width = 100%>
            <h3>Here are your upcoming chests. Chest ranking: Silver, Gold, Magical, Giant, Mega Lightning, Epic, Legendary Chest.</h3>
            <table>
              <tr>
                <th>Order Number</th>
                <th>Type</th>
                <th>Image</th>
              </tr>
            """)
            for i in range(len(userdata2['items'])):
                chest_name = userdata2['items'][i]['name']
                image_file = chest_name + ".png"
                image_url = "Users/mikey.thien/Desktop/Year-10/Design/"+chest_name
                myfile4.write("""
                <tr>
                  <th>Upcoming Chest Placement:  """+ str(userdata2['items'][i]['index']) + """</th>
                  <th>"""+ str(userdata2['items'][i]['name'])+ """</th>
                  <th><img src = """+ image_url +""" width = "100"></th>
                </tr>
                """)
            myfile4.write("</table></body>")
            myfile4.close()
        elif (response.status_code == 400):
            messagebox.showinfo("Error 400", "Error 400 has occured. Client provided incorrect parameters for the request.")
        elif (response.status_code == 403):
            messagebox.showinfo("Error 403", "Error 403 has occured. Access denied, either because of missing/incorrect credentials or used API token does not grant access to the requested resource.")
        elif (response.status_code == 404):
            messagebox.showinfo("Error 404", "Error 404 has occured. Resource was not found.")
        elif (response.status_code == 429):
            messagebox.showinfo("Error 429", "Error 429 has occured. Request was throttled, because amount of requests was above the threshold defined for the used API token.")
        elif (response.status_code == 500):
            messagebox.showinfo("Error 500", "Error 500 has occured. Unknown error happened when handeling the requests.")
        elif (reponse.status_code == 503):
            messagebox.showinfo("Error 503", "Error 503 has occured. Service is temporarily unavailable because of maintenance.")
root = Tk()
root.title("Clash Royale Statistics")
root.geometry("540x200")
label = Label(root, text = "Find out your clash royale statistics!")
enterTag = Entry(root)
btnName = Button(text = "Find My Stats", command = processBtn)
label.grid(row = 0, column = 0)
enterTag.grid(row = 0, column = 1)
btnName.grid(row = 0, column = 2)
root.mainloop()