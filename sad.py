url = "https://groups.roblox.com/v2/groups/11846881/wall/posts?sortOrder=Desc&limit=10"

import urllib
from bs4 import BeautifulSoup

url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

dict = {
  "previousPageCursor": "null",
  "nextPageCursor": "2478653499_1_aa5ae34096d2d5ace96ca9b68bfad38c",
  "data": [
    {
      "id": 2500595125,
      "poster": {
        "user": {
          "buildersClubMembershipType": "None",
          "userId": 2204331759,
          "username": "SANTYx_xLOL",
          "displayName": "Santiago_Windsorley"
        },
        "role": {
          "id": 69335564,
          "name": "Ciudadano",
          "rank": 246
        }
      },
      "body": "Hola",
      "created": "2021-10-17T01:59:13.537Z",
      "updated": "2021-10-17T01:59:13.537Z"
    },
    {
      "id": 2499915819,
      "poster": {
        "user": {
          "buildersClubMembershipType": "None",
          "userId": 1643649441,
          "username": "losto95",
          "displayName": "Korai"
        },
        "role": {
          "id": 69335652,
          "name": "Inmigrante",
          "rank": 244
        }
      },
      "body": "vamos bolivia pe webon",
      "created": "2021-10-16T00:36:25.437Z",
      "updated": "2021-10-16T00:36:25.437Z"
    },
    {
      "id": 2499270763,
      "poster": {
        "user": {
          "buildersClubMembershipType": "None",
          "userId": 435344088,
          "username": "Joshuagar1",
          "displayName": "joshuaXd"
        },
        "role": {
          "id": 69215748,
          "name": "Guest",
          "rank": 0
        }
      },
      "body": "creer Bolivia ##### mar",
      "created": "2021-10-14T20:15:33.587Z",
      "updated": "2021-10-14T20:15:33.587Z"
    },
    {
      "id": 2489462316,
      "poster": {
        "user": {
          "buildersClubMembershipType": "None",
          "userId": 1432530075,
          "username": "urkfsl3",
          "displayName": "Purple_Guy"
        },
        "role": {
          "id": 69215748,
          "name": "Guest",
          "rank": 0
        }
      },
      "body": "####################",
      "created": "2021-09-27T20:37:36.94Z",
      "updated": "2021-09-27T20:37:36.94Z"
    },
    {
      "id": 2484975350,
      "poster": {
        "user": {
          "buildersClubMembershipType": "None",
          "userId": 2665674772,
          "username": "CarlosDiegoMesa",
          "displayName": "CarlosDiegoMesa"
        },
        "role": {
          "id": 69215747,
          "name": "Presidente del Estado",
          "rank": 253
        }
      },
      "body": "ya esta el nuevo link de disk",
      "created": "2021-09-20T18:14:40.777Z",
      "updated": "2021-09-20T18:14:40.777Z"
    },
    {
      "id": 2482123542,
      "poster": {
        "user": {
          "buildersClubMembershipType": "None",
          "userId": 1154962398,
          "username": "jorgefur498",
          "displayName": "Alex"
        },
        "role": {
          "id": 69335652,
          "name": "Inmigrante",
          "rank": 244
        }
      },
      "body": "Oigan, el link de disk expiró.",
      "created": "2021-09-16T03:30:03.207Z",
      "updated": "2021-09-16T03:30:03.207Z"
    },
    {
      "id": 2481262614,
      "poster": {
        "user": {
          "buildersClubMembershipType": "None",
          "userId": 1621543148,
          "username": "kamelhmadou",
          "displayName": "Kyllian_Baratieu"
        },
        "role": {
          "id": 69215748,
          "name": "Guest",
          "rank": 0
        }
      },
      "body": "kamelhmadou",
      "created": "2021-09-14T16:01:02.907Z",
      "updated": "2021-09-14T16:01:02.907Z"
    },
    {
      "id": 2480729624,
      "poster": {
        "user": {
          "buildersClubMembershipType": "None",
          "userId": 1958447246,
          "username": "rosaj7mari",
          "displayName": "Melinamiku"
        },
        "role": {
          "id": 69215748,
          "name": "Guest",
          "rank": 0
        }
      },
      "body": "Yo boliviano xd",
      "created": "2021-09-13T16:08:54.453Z",
      "updated": "2021-09-13T16:08:54.453Z"
    },
    {
      "id": 2479204119,
      "poster": {
        "user": {
          "buildersClubMembershipType": "None",
          "userId": 1937387627,
          "username": "ItzFlaviuZRoBlox",
          "displayName": "MrDou"
        },
        "role": {
          "id": 69215748,
          "name": "Guest",
          "rank": 0
        }
      },
      "body": "soy de peru y quiero verificarme en su grupo  de dis",
      "created": "2021-09-11T13:30:04.94Z",
      "updated": "2021-09-11T13:30:04.94Z"
    },
    {
      "id": 2478653499,
      "poster": {
        "user": {
          "buildersClubMembershipType": "None",
          "userId": 1726507832,
          "username": "seyopipe2cuenta",
          "displayName": "nubsudo"
        },
        "role": {
          "id": 69215748,
          "name": "Guest",
          "rank": 0
        }
      },
      "body": "🌊🌊🌊🌊🌊🌊",
      "created": "2021-09-10T17:20:17.917Z",
      "updated": "2021-09-10T17:20:17.917Z"
    }
  ]
}
name = "Santiago_Windsorley"
message = "Hola"

if (name == dict["data"][0]["poster"]["user"]["username"] or name == dict["data"][0]["poster"]["user"]["displayName"]) and message == dict["data"][0]["body"]:
  print(dict["data"][0]["poster"]["user"]["username"], dict["data"][0]["body"])