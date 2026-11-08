# Creación de Videos 2D y Estudio de Animación

Proyecto para generación de videos animados en 2D con locución ultra-natural en español neutro/latino y renderizado automatizado.

---

## 📁 Estructura del Proyecto

```text
├── skills/
│   ├── 2d-animation-studio/
│   │   └── SKILL.md          # Pipeline de 5 etapas para animación 2D modular
│   └── kokoro-latam-voices/
│       └── SKILL.md          # Catálogo oficial de voces calibradas y mezclas en español latino
├── tts_generator.py          # Script ejecutable en Python para síntesis de voz con Kokoro TTS
└── README.md
```

---

## 🎙️ Voces Disponibles (`tts_generator.py`)

Basado en **Kokoro TTS ONNX v1.0**:
- `alex_adam`: Voz masculina para cine, tono grave y épico.
- `dora_sara_romance`: Voz femenina melódica y cálida.
- `alex_puro`: Voz masculina directa y técnica.
- `santa_puro`: Voz para personajes animados y cómicos.

### Requisitos de Python:
```bash
pip install kokoro-onnx soundfile numpy
```

---

## 🎬 Animación 2D

El flujo de trabajo documentado en `skills/2d-animation-studio/SKILL.md` comprende:
1. **Guión estructurado** (`script.json`)
2. **Timing a nivel de palabra** para sincronización exacta audio-visual
3. **Modelado y rigging de personajes 2D** en Canvas2D / Remotion
4. **Mezcla de audio y efectos de sonido (SFX)**
5. **Control de calidad multimodal**
