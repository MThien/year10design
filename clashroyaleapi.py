import requests
import webbrowser
import tkinter
myfile = open("apisite.html", "w")
tag = input("Enter Your Clash Royale Player Tag: #")
headers = {
    'Accept': 'application/json',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjQ3NzBlZTc4LWRiNDItNDJiNy04NTU2LTFiNDkyY2I4YzBiNSIsImlhdCI6MTU2OTM2ODQ0MCwic3ViIjoiZGV2ZWxvcGVyL2MyYjY1NmYzLWE4MGMtOWU4Mi03MTdmLTcwY2I2YWYwZjY3YSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI5OS4yNDEuMzUuMTYwIl0sInR5cGUiOiJjbGllbnQifV19.0Cro4Pg33ZR44fJILziuD_JtX1YXcnFjXalLDeLhrR2XtPA4_RSwApEsWYs6ZGhx_Cr5MnfpBiQgenNTSp5rSg'
}
response = requests.get("https://api.clashroyale.com/v1/players/%23" + tag.upper(), headers=headers)
#Retrieving Data From API
userdata = response.json()
king_tower = str(userdata['expLevel'])
player_name = str(userdata['name'])
player_trophies = str(userdata['trophies'])
player_best_trophies = str(userdata['bestTrophies'])
player_wins = str(userdata['wins'])
player_losses = str(userdata['losses'])
#Write on website
myfile.write("<h1>Clash Royale Statistics</h1>")
myfile.write("<p>"+ player_name + ": " + tag.upper() +"</p>")
myfile.write("<p> King Tower Level: "+ king_tower + "</p>")
myfile.write("<p> Trophies: "+ player_trophies + "</p>")
myfile.write("<p> Best Trophies: "+ player_best_trophies + "</p>")
myfile.write("<p> Wins: "+ player_wins + "</p>")
myfile.write("<p> Losses: "+ player_losses + "</p>")
myfile.close()
filename = 'file:///Users/mikey.thien/Desktop/Year-10/Design/apisite.html'
webbrowser.open_new_tab(filename)