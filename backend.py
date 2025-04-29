from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Tes fonctions existantes :
def extract_digits_from_file(filename: str) -> str:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    return content

def find_sequence_position(digits: str, sequence: str) -> int:
    return digits.find(sequence)

def get_next_digits(digits, position, length):
    start: int = position + length
    return digits[start:start + length]

def analyze_sequence(filename, sequence) -> tuple:
    position: int = -1
    next_digits: str = ''
    if not sequence.isdigit() or len(sequence) > 10:
        return (position, next_digits)
    digits = extract_digits_from_file(filename)
    position = find_sequence_position(digits, sequence)
    if position != -1:
        next_digits = get_next_digits(digits, position, len(sequence))
    return (position, next_digits)

# =======================
# Route HTML principal :
# =======================
@app.route('/',methods=['GET', 'POST'])
def index():
    # Je te laisse ici un exemple très simple d'HTML intégré
    # (tu peux le remplacer par render_template si tu préfères un fichier .html)
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Number Finder</title>
    </head>
    <body>
        <h2>Number finder</h2>
        <p>Ce petit programme permet de chercher une suite de chiffres dans les décimales.</p>
        
        <form action="/analyze" method="post">
            <input type="radio" id="pi" name="nombre" value="pi" checked>
            <label for="pi">Pi</label><br>

            <input type="radio" id="e" name="nombre" value="e">
            <label for="e">Nombre d'Euler</label><br>

            <input type="radio" id="phi" name="nombre" value="phi">
            <label for="phi">Nombre d'or</label><br>

            <br>
            <label for="sequence">Entrez votre séquence de chiffres :</label><br>
            <input type="text" id="sequence" name="sequence" pattern="\\d{1,10}" maxlength="10" required><br><br>

            <button type="submit">Envoyer</button>
        </form>
    </body>
    </html>
    '''

# =======================
# Route backend pour traiter l'analyse
# =======================
@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    nombre = request.form.get('nombre')  # pi, e ou phi
    sequence = request.form.get('sequence')

    # Déterminer quel fichier utiliser
    if nombre == 'pi':
        filename = 'pi.txt'
    elif nombre == 'e':
        filename = 'e.txt'
    elif nombre == 'phi':
        filename = 'phi.txt'
    else:
        return "Nombre non valide", 400

    # Analyse
    position, next_digits = analyze_sequence(filename, sequence)

    if position == -1:
        return f"""Séquence {sequence} non trouvée.
        <form action="/" method="get">
            <button type="submit">Retour</button>
        </form>
        """
    else:
        return f"""Séquence {sequence} trouvée à la position {position}. Chiffres suivants : {next_digits}
<form action="/" method="post">
            <button type="submit">Retour</button>
        </form>
"""

if __name__ == "__main__":
    app.run(debug=True)
