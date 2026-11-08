import os
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

# Paths to models
MODEL_PATH = os.environ.get("KOKORO_MODEL_PATH", "kokoro-v1.0.onnx")
VOICES_PATH = os.environ.get("KOKORO_VOICES_PATH", "voices-v1.0.bin")

VOICE_CONFIGS = {
    "alex_adam": {
        "description": "Masculina Principal (Cine / Épica / Creador) - Grave, profunda, cinematográfica",
        "weights": {"em_alex": 0.60, "am_adam": 0.40},
        "speed": 1.08,
    },
    "dora_sara_romance": {
        "description": "Femenina Principal (Narradora Cálida / Melódica) - Dulce, suave, humana",
        "weights": {"ef_dora": 0.55, "if_sara": 0.45},
        "speed": 1.10,
    },
    "alex_puro": {
        "description": "Masculina Explicativa (Tutorial / Directa) - Clara, sobria, técnica",
        "weights": {"em_alex": 1.0},
        "speed": 1.12,
    },
    "santa_puro": {
        "description": "Personaje Animado (Caricatura / Cómico) - Robusta, madura",
        "weights": {"em_santa": 1.0},
        "speed": 1.08,
    }
}

def generate_voiceover(text: str, voice_key: str = "alex_adam", output_path: str = "output_voice.wav"):
    """
    Sintetiza locución en español neutro / latino con mezclas de voces fluidas.
    """
    if voice_key not in VOICE_CONFIGS:
        raise ValueError(f"Voz '{voice_key}' no reconocida. Opciones: {list(VOICE_CONFIGS.keys())}")

    config = VOICE_CONFIGS[voice_key]
    print(f"Cargando Kokoro ONNX ({MODEL_PATH})...")
    kokoro = Kokoro(MODEL_PATH, VOICES_PATH)

    # Combinación ponderada de embeddings de voz
    blended_voice = None
    for voice_name, weight in config["weights"].items():
        v = kokoro.get_voice_style(voice_name)
        if blended_voice is None:
            blended_voice = v * weight
        else:
            blended_voice += v * weight

    print(f"Generando audio para ({voice_key}) con velocidad {config['speed']}x...")
    samples, sample_rate = kokoro.create(
        text,
        voice=blended_voice,
        speed=config["speed"],
        lang="es"
    )

    sf.write(output_path, samples, sample_rate)
    print(f"Audio exportado exitosamente en: {output_path}")
    return output_path

if __name__ == "__main__":
    test_text = "Bienvenidos al estudio de animación 2D. Este es un ejemplo de narración fluida en español latino."
    print("Módulo de TTS listo.")
