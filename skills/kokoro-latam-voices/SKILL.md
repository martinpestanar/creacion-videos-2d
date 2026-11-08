---
name: kokoro-latam-voices
description: Generates ultra-natural Latin American Spanish voice narration using Kokoro TTS (v1.0 ONNX) with custom voice blending recipes and fluid pacing parameters. Use whenever synthesizing Spanish voiceovers, character dialogues, or narrations for 2D animation and videos.
---
# Kokoro TTS: Guía de Voces en Español Latino & Fluidez

Esta skill define el catálogo oficial de voces calibradas en español latino y los parámetros de síntesis continua (habla corrida y natural) para proyectos de animación 2D y videos.

---

## 1. Elenco Oficial de Voces (Voice Blends)

| Clave de Voz | Rol / Carácter | Fórmula de Mezcla (Kokoro) | Velocidad | Sensación Vocal |
| :--- | :--- | :--- | :--- | :--- |
| **`alex_adam`** | **Masculina Principal (Cine / Épica / Creador)** | `0.60 * em_alex + 0.40 * am_adam` | `1.08x` | Grave, profunda, cinematográfica y con autoridad. |
| **`dora_sara_romance`** | **Femenina Principal (Narradora Cálida / Melódica)** | `0.55 * ef_dora + 0.45 * if_sara` | `1.10x` | Dulce, suave, cadencia melódica y humana, sin agudos estridentes. |
| **`alex_puro`** | **Masculina Explicativa (Tutorial / Directa)** | `1.00 * em_alex` | `1.12x` | Clara, sobria, ágil y directa para explicaciones técnicas. |
| **`santa_puro`** | **Personaje Animado (Caricatura / Cómico)** | `1.00 * em_santa` | `1.08x` | Robusta, madura y cómica para personajes secundarios animados. |

---

## 2. Parámetros Críticos de Fluidez (Habla Corrida)

Para evitar la sensación de "robot entrecortado" o pausas artificiales largas:

- **`sentence_pause = 0.08`**: Reduce el silencio entre oraciones de 250ms a solo 80ms.
- **`clause_pause = 0.04`**: Reduce las pausas por comas de 100ms a 40ms.
- **Redacción de guión**: Usar conectores naturales (*"y", "donde", "mientras", "así que"*) en vez de puntos seguidos excesivos o signos de admiración repetidos.

---

## 3. Implementación en Código (Python)

```python
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

MODEL_PATH = "/home/antigravity/kokoro_models/kokoro-v1.0.onnx"
VOICES_PATH = "/home/antigravity/kokoro_models/voices-v1.0.bin"

VOICE_CONFIGS = {
    "alex_adam": {
        "weights": {"em_alex": 0.60, "am_adam": 0.40},
        "speed": 1.08,
    },
    "dora_sara_romance": {
        "weights": {"ef_dora": 0.55, "if_sara": 0.45},
        "speed": 1.10,
    },
    "alex_puro": {
        "weights": {"em_alex": 1.0},
        "speed": 1.12,
    },
    "santa_puro": {
        "weights": {"em_santa": 1.0},
        "speed": 1.08,
    }
}

def generate_voiceover(k: Kokoro, text: str, voice_name: str = "alex_adam", out_path: str = "voice.wav"):
    cfg = VOICE_CONFIGS[voice_name]
    
    # Calcular vector de estilo ponderado
    style = sum(w * k.get_voice_style(v_id) for v_id, w in cfg["weights"].items())
    
    # Generar con pausas reducidas
    samples, sr = k.create(
        text=text,
        voice=style,
        speed=cfg["speed"],
        lang="es",
        sentence_pause=0.08,
        clause_pause=0.04
    )
    sf.write(out_path, samples, sr)
    return out_path, len(samples) / sr
```

---

## 4. Integración con el Pipeline de Animación 2D

1. Escribir el guión en escenas y asignar a cada personaje o narrador una de las 4 claves de voz.
2. Generar el archivo `voice.wav` usando esta receta.
3. Extraer marcas de tiempo por palabra (`words.json`) para sincronizar cortes de cámara, gesticulación de bocas y reacciones 2D exactamente al compás del habla.