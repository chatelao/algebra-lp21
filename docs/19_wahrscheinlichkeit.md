## 19. Wahrscheinlichkeit

Wahrscheinlichkeit gibt an, wie sicher ein Ereignis eintreten wird. Wir messen sie mit Zahlen zwischen **0** (unmöglich) und **1** (sicher) – oder in Prozent von $0\%$ bis $100\%$.

### Das Laplace-Experiment
Wenn alle Ergebnisse gleich wahrscheinlich sind (wie bei einem fairen Würfel), gilt die Formel:
$P(E) = \frac{\text{Anzahl der günstigen Ergebnisse}}{\text{Anzahl der möglichen Ergebnisse}}$

*Beispiel:* Eine "6" würfeln.
- Günstig: $\{6\}$ (1 Ergebnis)
- Möglich: $\{1, 2, 3, 4, 5, 6\}$ (6 Ergebnisse)
- $P = \frac{1}{6} \approx 16.7\%$.

---

## Vertiefung: Mehrstufige Experimente

Wenn du mehrmals hintereinander würfelst oder ziehst, hilft ein **Baumdiagramm**.
- **Pfadregel 1 (Produktregel):** Entlang eines Pfades werden die Wahrscheinlichkeiten multipliziert.
- **Pfadregel 2 (Summenregel):** Wenn mehrere Pfade zum Ziel führen, werden deren Ergebnisse addiert.

### Ziehen mit/ohne Zurücklegen
- **Mit Zurücklegen:** Die Wahrscheinlichkeit bleibt bei jedem Zug gleich.
- **Ohne Zurücklegen:** Der Nenner wird kleiner, weil eine Kugel weniger im Topf ist!

---

## Beispielaufgaben mit Lösungsweg

### Beispiel 1: Münzwurf
**Aufgabe:** Wie gross ist die Wahrscheinlichkeit, bei zwei Münzwürfen zweimal "Kopf" zu erhalten?
**Lösungsweg:**
1. Erster Wurf: $P(K) = \frac{1}{2}$.
2. Zweiter Wurf: $P(K) = \frac{1}{2}$.
3. Kombiniert: $\frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4} = 25\%$.
- **Ergebnis:** $25\%$.

### Beispiel 2: Kugeln ziehen (mit Zurücklegen)
**Aufgabe:** In einer Urne sind 3 rote und 7 blaue Kugeln. Wie gross ist die Chance, eine rote zu ziehen?
**Lösungsweg:**
- Günstig: 3 (rot).
- Gesamt: $3 + 7 = 10$.
- $P = \frac{3}{10} = 30\%$.
- **Ergebnis:** $30\%$.

### Beispiel 3: Das Gegenereignis
**Aufgabe:** Wie gross ist die Chance, bei einem Würfel *keine* 6 zu würfeln?
**Lösungsweg:**
- "Nicht 6" ist das Gegenereignis zu "6".
- $1 - P(6) = 1 - \frac{1}{6} = \frac{5}{6}$.
- **Ergebnis:** $\frac{5}{6} \approx 83.3\%$.

---

## Checkpoint: Teste dein Wissen

*   **Frage 1:** Kann eine Wahrscheinlichkeit $1.5$ oder $150\%$ sein? Warum nicht?
*   **Frage 2:** Wenn du 5-mal "Zahl" beim Münzwurf hattest, ist es dann beim 6. Mal wahrscheinlicher, dass "Kopf" kommt?

---

## Sokratische Begleitung

**Tutor-Frage:** Wenn du in einem Kartenspiel (32 Karten) ein Ass ziehen willst... wie viele Karten sind "günstig" für dich? Und wie ändert sich deine Chance, wenn schon ein Ass auf dem Tisch liegt?

**Tutor-Frage:** Stell dir vor, ein Wetterbericht sagt: "Regenwahrscheinlichkeit 50% für Samstag und 50% für Sonntag". Bedeutet das, dass es am Wochenende sicher regnet ($50\% + 50\% = 100\%$)? Wo liegt der Denkfehler?
