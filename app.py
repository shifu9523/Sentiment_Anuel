```python
from textblob import TextBlob
import streamlit as st
from PIL import Image
from deep_translator import GoogleTranslator

st.title('Análisis de Sentimiento')

# Imagen
image = Image.open('emoticones.jpg')
st.image(image)

st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")

# Sidebar
with st.sidebar:
    st.subheader("Polaridad y Subjetividad")
    st.write("""
    Polaridad: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
    Va de -1 (muy negativo) a 1 (muy positivo), siendo 0 neutral.

    Subjetividad: Mide cuánto del contenido es subjetivo u objetivo.
    Va de 0 (objetivo) a 1 (subjetivo).
    """)

# Input
with st.expander('Analizar texto'):
    text = st.text_input('Escribe por favor: ')
    
    if text:
        # Traducción
        trans_text = GoogleTranslator(source='es', target='en').translate(text)
        
        # Análisis
        blob = TextBlob(trans_text)
        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        st.write('Polarity:', polarity)
        st.write('Subjectivity:', subjectivity)

        # Clasificación correcta
        if polarity > 0:
            st.write('Es un sentimiento Positivo 😊')
        elif polarity < 0:
            st.write('Es un sentimiento Negativo 😔')
        else:
            st.write('Es un sentimiento Neutral 😐')
```
