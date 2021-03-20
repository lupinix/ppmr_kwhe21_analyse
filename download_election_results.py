import requests

# We have to define our own download function using requests, as simple
# urlretrieve is blocked by server :(
def urlretrieve(url, filename):
    r = requests.get(url)
    with open(filename, "wb") as f:
        f.write(r.content)

def download_election_results():
    # Kreiswahl
    urlretrieve("https://votemanager-gi.ekom21cdn.de/2021-03-14/06534000/html5/Open-Data-Kreiswahl-Hessen3021.csv",
        "data/kreiswahl_gesamt.csv")
    urlretrieve("https://votemanager-gi.ekom21cdn.de/2021-03-14/06534000/html5/Open-Data-Kreiswahl-Hessen3023.csv",
        "data/kreiswahl_gemeinden.csv")
    urlretrieve("https://votemanager-gi.ekom21cdn.de/2021-03-14/06534000/html5/OpenDataInfo.html",
        "data/beschreibung_kreiswahl.html")
    # Stadtverordnetenwahl Marburg
    urlretrieve("https://votemanager-gi.ekom21cdn.de/2021-03-14/06534014/html5/Open-Data-Gemeindewahl-Hessen3033.csv",
        "data/stv_marburg_gesamt.csv")
    urlretrieve("https://votemanager-gi.ekom21cdn.de/2021-03-14/06534014/html5/Open-Data-Gemeindewahl-Hessen3038.csv",
        "data/stv_marburg_ortsbezirke.csv")
    urlretrieve("https://votemanager-gi.ekom21cdn.de/2021-03-14/06534014/html5/Open-Data-Gemeindewahl-Hessen3036.csv",
        "data/stv_marburg_wahlbezirke.csv")
    urlretrieve("https://votemanager-gi.ekom21cdn.de/2021-03-14/06534014/html5/OpenDataInfo.html",
        "data/beschreibung_stv_marburg.html")

if __name__ == "__main__":
    download_election_results()