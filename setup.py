Importieren von Codecs
Import-os
Import

Von Setuptools importieren Setup, find_packages


################################################################################################### #################

NAME = "Pygflib"
PAKETE = Find_packages (Wobei "Src" =)
META_PATH = os.path.join ("Src", "Pygflib", "__init__.py")
KEYWORDS = ["Gutefrage", "api", "Rest", "Gfapi"]
KLASSIFIKATOREN =]
"Entwicklungsstatus:: 3 - Alpha",
"Zielgruppe: Entwickler",
"Lizenzgebern:: OSI Genehmigt:: MIT Lizenzgebern",
"Natürliche Sprache:: Englisch",
"Betriebssystem: OS Unabhängig",
"Programmiersprache:: Python",
"Programmiersprache:: Python:: 3",
"Programmiersprache:: Python:: 3,5",
"Programmiersprache:: Python:: 3:: Nur",
"Thema:: Software-Entwicklung:: Bibliotheken:: Python-Modul",
]
INSTALL_REQUIRES = ["Anfragen", "Lxml"]

################################################################################################### #################

HIER = os.path.abspath (os.path.dirname (__ File__))


DEF Lesen (* Teile):
Aufrechtzuerhalten.
Erstellen Sie Einen Absoluten Biodiesel aus * Teile * Und Geben Sie Den Inhalt der
Resultierende Datei. Nehmen Wir UTF-8-Codierung ein.
Aufrechtzuerhalten.
Mit codecs.open (os.path.join (HIER * Teile), "Rb", "Utf-8") als f:
Rückkehr f.read)


META_FILE = Read (META_PATH)


DEF Find_meta (Meta):
Aufrechtzuerhalten.
Aus __ * Meta * __ aus META_FILE Extrahieren.
Aufrechtzuerhalten.
Meta_match = Suche (
(Meta = Meta), Wobei Das Format (Meta Meta =)
META_FILE, Re. M
)
Wenn Meta_match:
Return meta_match.group (1)
RuntimeError ("Unable to __ __ {Meta} Zeichenfolge zu finden." Formatieren (Meta Meta =))


Wenn __name__ == "__main__":
Konfiguration)
Name = NAME,
Beschreibung = Find_meta ("Beschreibung"),
Lizenzgebern = Find_meta ("nun"),
Version = Find_meta ("Version")
Autor = Find_meta ("Autor"),
Betreuer = Find_meta ("Autor"),
Keywords = SCHLÜSSELWÖRTER,
URL = "https://github.com/waz4bb/pygflib"
Long_description = Lesen ("README.md"),
Verwöhnpaketes = VERWÖHNPAKETES,
Package_dir = {"": "Src"},
Zip_safe = False,
Klassifikatoren = KLASSIFIKATOREN,
Install_requires = INSTALL_REQUIRES,
)
