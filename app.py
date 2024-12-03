from flask import Flask, render_template, request, jsonify
import openai

# Initialize Flask app
app = Flask(__name__)

# OpenAI API Key
import os
openai_api_key = os.getenv("OPENAI_API_KEY")

# Function to adapt email
def adaptar_email_gpt(email, cultura, formalidad, idioma):
    prompt = f"""
    Quiero que actúes como un experto en comunicación intercultural. 
    Reformula el siguiente email teniendo en cuenta:
    1. La cultura del lector: {cultura}.
    2. El nivel de formalidad: {formalidad}.
    3. Traduce el email al idioma: {idioma}.
    4. Mantén un tono respetuoso y profesional según las indicaciones.

    Email original:
    {email}

    Reformula el email:
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un experto en comunicación intercultural y redacción profesional."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Error al conectarse con GPT-3.5: {str(e)}"

# Flask routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adapt', methods=['POST'])
def adapt_email():
    data = request.json
    email = data.get("email")
    cultura = data.get("cultura")
    formalidad = data.get("formalidad")
    idioma = data.get("idioma")
    if not email:
        return jsonify({"error": "No email provided"}), 400

    adapted_email = adaptar_email_gpt(email, cultura, formalidad, idioma)
    return jsonify({"adapted_email": adapted_email})

if __name__ == '__main__':
    app.run(debug=True)

