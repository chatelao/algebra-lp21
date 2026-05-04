import random
import os

def get_templates(topic):
    if topic == "variablen":
        return [
            (r"Schreibe ohne Malzeichen: {n} \cdot {x}", "{n}{x}"),
            (r"Schreibe ohne Malzeichen: {x} \cdot {a}", "{x}{a}"),
            ("Schreibe als Term: 'Das {n}-fache von {x}'", "{n}{x}"),
            ("Schreibe als Term: '{n} mehr als {x}'", "{x} + {n}"),
            ("Schreibe als Term: '{n} weniger als {x}'", "{x} - {n}"),
            ("Wie heisst der Koeffizient von {x} in {n}{x}?", "{n}"),
            (r"Schreibe kürzer: {x} \cdot {x} \cdot {x}", "{x}^3")
        ]
    elif topic == "vereinfachen":
        return [
            ("Vereinfache: {n}x + {m}x", "{res}x"),
            ("Vereinfache: {n}a - {m}a", "{res}a"),
            ("Vereinfache: {n}x + {m}y + {k}x", "{res}x + {m}y"),
            ("Fasse zusammen: {n} + {m}b + {k}", "{m}b + {res}"),
            ("Vereinfache: {n}x^2 + {m}x^2", "{res}x^2"),
            (r"Rechne: {n} \cdot {m}x", "{res}x"),
            (r"Vereinfache: {n}a \cdot {m}b", "{res}ab")
        ]
    elif topic == "distributiv":
        return [
            ("Multipliziere aus: {n}(x + {m})", "{n}x + {res}"),
            ("Multipliziere aus: {n}(a - {m})", "{n}a - {res}"),
            ("Multipliziere aus: {n}({m}y + 1)", "{res}y + {n}"),
            ("Klammere aus: {n}x + {res}y", "{n}(x + {m}y)"),
            ("Klammere aus: {n}a - {res}", "{n}(a - {m})")
        ]
    elif topic == "negative":
        return [
            ("Berechne: -{n} + {m}", "{res}"),
            ("Berechne: {n} - {m}", "{res}"),
            ("Berechne: -{n} - {m}", "{res}"),
            (r"Berechne: (-{n}) \cdot {m}", "{res}"),
            (r"Berechne: (-{n}) \cdot (-{m})", "{res}"),
            (r"Berechne: {n} \cdot (-{m})", "{res}"),
            ("Berechne: -{n} : {m}", "{res}")
        ]
    elif topic == "gleichungen":
        return [
            ("Löse: x + {n} = {m}", "x = {res}"),
            ("Löse: x - {n} = {m}", "x = {res}"),
            ("Löse: {n}x = {res}", "x = {m}"),
            ("Löse: {n}x + {m} = {k}", "x = {res}")
        ]
    elif topic == "auswerten":
        return [
            ("Berechne {n}x + {m} für x = {k}", "{res}"),
            ("Berechne x^2 - {n} für x = {m}", "{res}"),
            ("Berechne {n}(x - {m}) für x = {k}", "{res}")
        ]
    elif topic == "primzahlen":
        return [
            ("Ist {n} eine Primzahl?", "{res}"),
            ("Zerlege {n} in Primfaktoren.", "{res}"),
            ("Nenne die Primzahlen zwischen {n} und {m}.", "{res}"),
            ("Ist {n} durch 3 teilbar? (Quersumme!)", "{res}")
        ]
    elif topic == "brueche":
        return [
            ("Kürze den Bruch: {n}/{m}", "{res}"),
            ("Berechne: 1/{n} + 1/{m}", "{res}"),
            ("Wandle {n}/{m} in eine Dezimalzahl um.", "{res}"),
            (r"Berechne: {n}/10 \cdot 1/{m}", "{res}")
        ]
    elif topic == "prozent":
        return [
            ("Berechne {n}% von {m} CHF.", "{res} CHF"),
            ("Wie viel Prozent sind {n} von {m}?", "{res}%"),
            ("Ein Artikel kostet {n} CHF und wird um {m}% reduziert. Neuer Preis?", "{res} CHF")
        ]
    elif topic == "potenzen":
        return [
            ("Berechne: {n}^{m}", "{res}"),
            (r"Vereinfache: x^{n} \cdot x^{m}", "x^{res}"),
            ("Vereinfache: (a^{n})^{m}", "a^{res}"),
            ("Berechne: (-{n})^2", "{res}")
        ]
    elif topic == "zehnerpotenzen":
        return [
            (r"Schreibe als normale Zahl: {n} \cdot 10^{m}", "{res}"),
            (r"Schreibe in wissenschaftlicher Schreibweise: {n}0000", r"{res} \cdot 10^{m}"),
            (r"Was ist 10^{n} \cdot 10^{m}?", "10^{res}")
        ]
    elif topic == "koordinatensystem":
        return [
            ("In welchem Quadranten liegt P({n}|{m})?", "{res}"),
            ("Spiegle A({n}|{m}) an der x-Achse.", "A'({n}|{res})"),
            ("Wie gross ist der Abstand von (0|0) zu ({n}|0)?", "{n}")
        ]
    elif topic == "zuordnungen":
        return [
            ("Gehört der Punkt (2|{res}) zur Geraden y = {n}x?", "Ja"),
            ("Berechne die Steigung k für y = kx, wenn der Graph durch (2|{n}) geht.", "k = {res}"),
            ("Ist die Zuordnung 'Alter -> Grösse' proportional?", "Nein")
        ]
    elif topic == "statistik":
        return [
            ("Berechne den Durchschnitt von: {n}, {m}, {k}.", "{res}"),
            ("Finde den Median von: {n}, {m}, {k}, {p}, {q}.", "{res}"),
            ("Wie gross ist die Spannweite bei den Werten {n} und {m}?", "{res}")
        ]
    elif topic == "wahrscheinlichkeit":
        return [
            ("Wie gross ist die Chance, bei einem Würfel eine {n} zu werfen?", "1/6"),
            ("Wie gross ist die Chance, bei zwei Münzwürfen zweimal Kopf zu werfen?", "1/4"),
            ("In einer Urne sind {n} rote und {m} blaue Kugeln. P(rot)?", "{res}")
        ]
    elif topic == "prismen":
        return [
            ("Berechne das Volumen eines Quaders mit a={n}, b={m}, c={k}.", "{res}"),
            ("Ein Würfel hat die Seite s={n}. Volumen?", "{res}"),
            ("Die Grundfläche ist {n} cm^2, die Höhe {m} cm. Volumen?", "{res}")
        ]
    elif topic == "textaufgaben":
        return [
            ("Das Doppelte einer Zahl plus {n} ist {m}. Wie heisst die Zahl?", "{res}"),
            ("Drei Äpfel kosten {n} CHF. Wie viel kosten {m} Äpfel?", "{res} CHF"),
            ("Ein Vater ({n} J.) ist doppelt so alt wie sein Sohn. Alter Sohn?", "{res}")
        ]
    elif topic == "geometrie":
        return [
            ("Umfang eines Quadrats mit s={n}?", "{res}"),
            ("Fläche eines Rechtecks mit a={n}, b={m}?", "{res}"),
            ("Ein Rechteck hat U={n} und a={m}. Berechne b.", "{res}")
        ]
    else:
        return [("Aufgabe {i} zu {topic}", "Lösung {i}")]

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def generate_task(topic, i):
    templates = get_templates(topic)
    if not templates or topic == "gemischt":
        all_other_topics = ["variablen", "vereinfachen", "distributiv", "negative", "gleichungen", "auswerten", "primzahlen", "brueche", "prozent", "potenzen", "zehnerpotenzen", "koordinatensystem", "zuordnungen", "statistik", "wahrscheinlichkeit", "prismen", "textaufgaben", "geometrie"]
        templates = get_templates(random.choice(all_other_topics))

    tpl, sol_tpl = random.choice(templates)

    n = random.randint(1, 20)
    m = random.randint(1, 20)
    k = random.randint(1, 10)
    p = random.randint(1, 10)
    q = random.randint(1, 10)
    x_var = random.choice(['x', 'a', 'b', 'y'])

    # Custom logic
    if topic == "negative":
        if " : " in tpl:
            m = random.randint(1, 5)
            n = m * random.randint(1, 10)
        expr = tpl.split(": ")[1].format(n=n, m=m).replace(r"\cdot", "*").replace(":", "/")
        try:
            res = int(eval(expr))
        except:
            res = "Err"
        text = tpl.format(n=n, m=m)
        sol = sol_tpl.format(res=res)
    elif topic == "gleichungen" and "{n}x = {res}" in tpl:
        n = random.randint(2, 10)
        m = random.randint(1, 12)
        res_val = n * m
        text = tpl.format(n=n, res=res_val)
        sol = sol_tpl.format(m=m)
    elif topic == "primzahlen":
        n_val = random.randint(2, 50)
        if "Primfaktor" in tpl or "Zerlege" in tpl:
            n_val = random.choice([12, 18, 20, 24, 30, 36, 40, 42, 45, 48, 50])
            # simplified
            res = "..."
        elif "Ist {n} eine Primzahl" in tpl:
            res = "Ja" if is_prime(n_val) else "Nein"
        else:
            res = "..."
        text = tpl.format(n=n_val, m=m)
        sol = sol_tpl.format(res=res)
    else:
        # Generic
        try:
            text = tpl.format(n=n, m=m, k=k, p=p, q=q, x=x_var, a='a', b='b', y='y', i=i, topic=topic)
            sol = sol_tpl.format(n=n, m=m, k=k, p=p, q=q, x=x_var, a='a', b='b', y='y', i=i, topic=topic, res=n+m)
        except:
            text = tpl
            sol = "..."

    return text, sol

def main():
    topics = [
        ("variablen", "docs/uebungen/01_variablen.md"),
        ("vereinfachen", "docs/uebungen/02_vereinfachen.md"),
        ("distributiv", "docs/uebungen/03_distributiv.md"),
        ("negative", "docs/uebungen/04_negative_zahlen.md"),
        ("gleichungen", "docs/uebungen/05_gleichungen.md"),
        ("auswerten", "docs/uebungen/07_auswerten.md"),
        ("textaufgaben", "docs/uebungen/08_textaufgaben.md"),
        ("proportionalitaet", "docs/uebungen/09_proportionalitaet.md"),
        ("geometrie", "docs/uebungen/10_geometrie.md"),
        ("primzahlen", "docs/uebungen/11_primzahlen.md"),
        ("brueche", "docs/uebungen/12_brueche.md"),
        ("prozent", "docs/uebungen/13_prozent.md"),
        ("potenzen", "docs/uebungen/14_potenzen.md"),
        ("zehnerpotenzen", "docs/uebungen/15_zehnerpotenzen.md"),
        ("koordinatensystem", "docs/uebungen/16_koordinatensystem.md"),
        ("zuordnungen", "docs/uebungen/17_zuordnungen.md"),
        ("statistik", "docs/uebungen/18_statistik.md"),
        ("wahrscheinlichkeit", "docs/uebungen/19_wahrscheinlichkeit.md"),
        ("prismen", "docs/uebungen/20_prismen.md"),
        ("gemischt", "docs/uebungen/06_gemischt.md")
    ]

    all_solutions = {}

    for topic_key, filepath in topics:
        topic_name = topic_key.replace("_", " ").capitalize()
        solutions = []
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# Übungen: {topic_name}\n\n")
            f.write("## Aufgaben\n")
            for i in range(1, 101):
                text, sol = generate_task(topic_key, i)
                f.write(f"{i}. {text}\n")
                solutions.append(f"{i}) {sol}")

        all_solutions[topic_name] = solutions

    with open("docs/uebungen/loesungen.md", 'w', encoding='utf-8') as f:
        f.write("# Lösungen zu den Übungen\n\n")
        for topic_name, solutions in sorted(all_solutions.items()):
            f.write(f"### {topic_name}\n")
            f.write(" | ".join(solutions[:15]) + " ...\n\n")

if __name__ == "__main__":
    main()
