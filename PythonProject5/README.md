# Sentiment-Analyse von Restaurantbewertungen

## Projektübersicht

Dieses Projekt untersucht Kundenbewertungen eines Restaurants mithilfe von Natural Language Processing und Machine Learning.

Ziel ist es, englischsprachige Bewertungen automatisch als positiv oder negativ zu klassifizieren. Dadurch kann ein Restaurant kritisches Feedback schneller erkennen, wiederkehrende Probleme analysieren und gezielte Verbesserungen ableiten.

## Datensatz

Der Datensatz enthält 1000 Restaurantbewertungen:

| Spalte | Beschreibung |
|---|---|
| `Review` | Text der Kundenbewertung |
| `Liked` | Sentiment: `0` = negativ, `1` = positiv |

Die Klassen sind vollständig ausgeglichen:

- 500 positive Bewertungen
- 500 negative Bewertungen
- keine fehlenden Werte

## Projektablauf

1. Laden und Prüfen des Datensatzes
2. Explorative Datenanalyse
3. Analyse der Bewertungslängen
4. Untersuchung häufiger Wörter nach Sentiment
5. Textbereinigung
6. Feature Engineering mit TF-IDF
7. Training und Vergleich mehrerer Modelle
8. Bewertung anhand von Accuracy, Precision, Recall und F1-Score
9. Test mit neuen Beispielbewertungen
10. Ableitung geschäftlicher Empfehlungen

## Textvorverarbeitung

Die Bewertungen werden vor dem Modelltraining bereinigt:

- Umwandlung in Kleinbuchstaben
- Entfernen von Zahlen und Sonderzeichen
- Tokenisierung
- Entfernen englischer Stoppwörter
- Zusammenführen der bereinigten Wörter

Anschließend werden die Texte mithilfe von TF-IDF in numerische Merkmale umgewandelt.

## Modellergebnisse

| Modell | Accuracy | Recall negativ | Recall positiv |
|---|---:|---:|---:|
| Logistic Regression | 79,5 % | 77 % | 82 % |
| Naive Bayes | 77,0 % | 71 % | 83 % |
| Logistic Regression mit N-Grammen | 79,5 % | 76 % | 83 % |

Die ursprüngliche logistische Regression wurde als finales Modell ausgewählt. Sie erzielt die beste Gesamtleistung und erkennt negative Bewertungen zuverlässiger als die getesteten Alternativen.

## Geschäftlicher Nutzen

Das Modell kann eingehende Bewertungen automatisch vorsortieren. Negative Rückmeldungen lassen sich dadurch schneller prüfen und priorisieren.


Mögliche Anwendungsfälle:

- Erkennen wiederkehrender Serviceprobleme
- Analyse von Beschwerden zu Wartezeiten oder Speisenqualität
- Identifikation von Verbesserungspotenzial
- Unterstützung bei der Priorisierung kritischer Bewertungen

Das Modell soll die persönliche Prüfung nicht ersetzen, sondern als unterstützendes Werkzeug dienen.

## Einschränkungen

- Der Datensatz ist mit 1000 Bewertungen relativ klein.
- Das Modell wurde nur mit englischen Texten trainiert.
- Ironische oder gemischte Aussagen sind schwieriger zu klassifizieren.
- Das Modell unterscheidet nur zwischen positiv und negativ, nicht zwischen Themen wie Service, Preis oder Speisenqualität.

## Mögliche Erweiterungen

- Training mit einem größeren Datensatz
- Optimierung der Modellparameter
- Vergleich mit weiteren Modellen
- Unterstützung mehrerer Sprachen
- Automatische Zuordnung negativer Bewertungen zu Themenbereichen
- Entwicklung einer kleinen Benutzeroberfläche für neue Bewertungen

## Projektstruktur

```text
restaurant_sentiment_project/
├── data/
│   └── Restaurant_Reviews.tsv
├── restaurant_sentiment_analysis.ipynb
├── main.py
└── README.md

## Verwendete Technologien

- Python
- pandas
- matplotlib
- seaborn
- NLTK
- scikit-learn
- Jupyter Notebook

## Ausführung
Installiere zunächst die benötigten Bibliotheken:

pip install pandas matplotlib seaborn nltk scikit-learn notebook
Starte anschließend Jupyter Notebook:

jupyter notebook
Öffne das Analyse-Notebook und führe die Zellen der Reihe nach aus.

## Fazit
Das Projekt zeigt, wie Restaurantbewertungen mithilfe von Natural Language Processing automatisiert ausgewertet werden können.

Die logistische Regression erreicht eine Accuracy von 79,5 % und bildet eine solide Grundlage, um Kundenfeedback effizienter zu analysieren und Verbesserungsmaßnahmen abzuleiten.




Kleine Anpassung: Falls dein Notebook anders heißt, ersetze `restaurant_sentiment_analysis.ipynb` im Abschnitt `Projektstruktur` durch deinen tatsächlichen Dateinamen.