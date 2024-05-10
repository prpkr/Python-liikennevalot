# Python-liikennevalot

Rauta:
Raspberry Pi 3
Pi kamera moduuli 2
Ledejä, vastuksia ja piuhoja


Koodi:

Ohjelma ohjaa liikennevaloja, jossa siis vihreä, keltainen ja punainen valo. Siirtyessä vihreästä punaiseen välissä palaa keltainen. Ja siirtyessä punaisesta vihreään välissä palaa punainen ja keltainen yhdessä.

Siirto punaisesta vihreään tapahtuu kameran tunnistaessa “jotain”. Nyt sillä pystyy tunnistamaan kasvot, mutta tarkoitus olisi saada monipuolisempi “object detection” käyttöön tensor flow liten avulla.

Datasetti ja malli:
Coco dataset
yolo v5
