!pip install transformers gradio

import gradio as gr
from transformers import pipeline

# Initialize the translation pipeline with the M2M100 model
translator = pipeline("translation", model="facebook/m2m100_418M")

# Supported languages dictionary
languages = {
    'Afrikaans': 'af',
    'Albanian': 'sq',
    'Amharic': 'am',
    'Arabic': 'ar',
    'Armenian': 'hy',
    'Basque': 'eu',
    'Belarusian': 'be',
    'Bengali': 'bn',
    'Bosnian': 'bs',
    'Bulgarian': 'bg',
    'Catalan': 'ca',
    'Chinese (Simplified)': 'zh',
    'Chinese (Traditional)': 'zh-TW',
    'Croatian': 'hr',
    'Czech': 'cs',
    'Danish': 'da',
    'Dutch': 'nl',
    'English': 'en',
    'Estonian': 'et',
    'Finnish': 'fi',
    'French': 'fr',
    'Galician': 'gl',
    'Georgian': 'ka',
    'German': 'de',
    'Greek': 'el',
    'Gujarati': 'gu',
    'Haitian Creole': 'ht',
    'Hausa': 'ha',
    'Hebrew': 'he',
    'Hindi': 'hi',
    'Hungarian': 'hu',
    'Icelandic': 'is',
    'Indonesian': 'id',
    'Irish': 'ga',
    'Italian': 'it',
    'Japanese': 'ja',
    'Javanese': 'jv',
    'Kannada': 'kn',
    'Kazakh': 'kk',
    'Khmer': 'km',
    'Korean': 'ko',
    'Kurdish': 'ku',
    'Latvian': 'lv',
    'Lithuanian': 'lt',
    'Macedonian': 'mk',
    'Malagasy': 'mg',
    'Malay': 'ms',
    'Maltese': 'mt',
    'Marathi': 'mr',
    'Mongolian': 'mn',
    'Nepali': 'ne',
    'Norwegian': 'no',
    'Pashto': 'ps',
    'Persian': 'fa',
    'Polish': 'pl',
    'Portuguese': 'pt',
    'Punjabi': 'pa',
    'Romanian': 'ro',
    'Russian': 'ru',
    'Serbian': 'sr',
    'Sinhala': 'si',
    'Slovak': 'sk',
    'Slovenian': 'sl',
    'Spanish': 'es',
    'Swahili': 'sw',
    'Swedish': 'sv',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Thai': 'th',
    'Turkish': 'tr',
    'Ukrainian': 'uk',
    'Urdu': 'ur',
    'Uzbek': 'uz',
    'Vietnamese': 'vi',
    'Welsh': 'cy',
    'Xhosa': 'xh',
    'Yiddish': 'yi',
    'Yoruba': 'yo',
    'Zulu': 'zu',
    'Azerbaijani': 'az',
    'Bengali (Bangladesh)': 'bn-BD',
    'Bosnian (Latin)': 'bs-Latn',
    'Catalan (Valencia)': 'ca-VALENCIA',
    'Central Kurdish': 'ckb',
    'Cebuano': 'ceb',
    'Chichewa': 'ny',
    'Corsican': 'co',
    'Croatian (Latin)': 'hr-Latn',
    'Czech (cs)': 'cs',
    'Esperanto': 'eo',
    'Filipino': 'tl',
    'Finnish (fi)': 'fi',
    'Georgian (ka)': 'ka',
    'Greek (el)': 'el',
    'Haitian Creole (ht)': 'ht',
    'Hebrew (he)': 'he',
    'Hindi (hi)': 'hi',
    'Somali (so)': 'so',
    'Tajik (tg)': 'tg'
}

# Translation function
def translate_text(input_text, source_language, target_language):
    if not input_text.strip():
        return "Error: Please enter text to translate."

    # Retrieve language codes
    src_lang = languages[source_language]
    tgt_lang = languages[target_language]

    # Configure model for the selected languages
    translator.model.config.src_lang = src_lang
    translator.model.config.tgt_lang = tgt_lang

    # Perform translation
    result = translator(input_text, src_lang=src_lang, tgt_lang=tgt_lang)
    return result[0]['translation_text']

# Define Gradio interface
interface = gr.Interface(
    fn=translate_text,
    inputs=[
        gr.Textbox(label="Enter text to translate:"),
        gr.Dropdown(label="Select source language:", choices=list(languages.keys())),
        gr.Dropdown(label="Select target language:", choices=list(languages.keys()))
    ],
    outputs=gr.Textbox(label="Translated Text"),
    title="Multilingual Translation App",
    description="Select a source and target language, then enter text to translate!"
)

# Launch the Gradio interface
interface.launch()
