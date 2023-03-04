"""Katseta, kas ka sõnesid saab võrrelda märkide
<, <=, >= ja > abil. Kuidas tulemust kommenteerida?"""

hoster1 = 'Cloud'
hoster2 = 'cloud'
print(hoster1 > hoster2)

hoster1 = 'Cloud'
hoster2 = 'cloud'
print(hoster1 < hoster2)

hoster1 = '20'
hoster2 = '10'
print(hoster1 < hoster2)

hoster1 = '20'
hoster2 = '10'
print(hoster1 > hoster2)

""" Tagastab väärtuse Väär,kuna tähe 'C' Unicode'i väärtus on
väiksem kui tähe "c" väärtus – 67 vs 99.
Kui muudate operaatorit:see tuleb tagasi Tõsi.
Nii töötab Pythonis leksikograafiline stringide võrdlus –
iga tähemärki ühes stringis võrreldakse omakorda mõne teise stringi märgiga.
"""