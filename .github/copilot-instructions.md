# Copilot Instructions for OpenVoicePacks

## Project Overview
- **OpenVoicePacks** is a sound pack generator for EdgeTX/OpenTX radios, focused on generating comprehensive, consistent voice packs using both self-hosted and cloud TTS engines.
- Audio output: 16kHz mono `.wav` files for maximum radio compatibility.
- Major TTS providers: Amazon Polly and Piper (see `src/openvoicepacks/providers.py`).
- The project is a WIP; low-level components are mostly complete, but the client/CLI is not fully functional yet.

## Key Components & Structure
- `src/openvoicepacks/` — Main package. Contains:
  - `audio.py`: Audio file generation and processing.
  - `providers.py`: TTS provider abstraction and implementations.
  - `voicepacks.py`: Voice pack configuration and build logic.
  - `client.py`, `__main__.py`: CLI entry points (planned/partial).
- `packs/` — Example/configuration YAMLs for voice packs.
- `resources/piper/` — Piper model files for local TTS.

## Developer Workflows
- **Unit tests:**
  - Run with `inv unit` (uses `tasks.py`/Invoke).
  - Tests are in `tests/`.
- **Build/Run:**
  - No full build pipeline yet; main entry is `main.py` (WIP).
  - CLI usage is planned as `openvoicepacks ...` (see README for examples).
- **Dependencies:**
  - Managed with `uv` (`pyproject.toml`).
  - Use `uv` for lockfile (`uv.lock`).
  - Requires Python 3.14 and `ffmpeg` installed.

## Project Conventions & Patterns
- **Provider abstraction:** Add new TTS providers by extending `TTSProvider` in `providers.py`.
- **Audio processing:** Always output 16kHz mono WAV.
- **Testing:** New code should have tests in `tests/`.
- **Legacy code:** Avoid changes to `legacy/` unless fixing regressions.

## Integration Points
- **Amazon Polly:** Requires AWS credentials (see `src/openvoicepacks/providers.py`).
- **Piper:** Uses local ONNX models in `resources/piper/`.
- **ffmpeg:** Used for audio conversion; must be available in PATH.

## Examples
- To add a new TTS provider, subclass `TTSProvider` in `src/openvoicepacks/providers.py` and register it.
- To add a new voicepack, create a YAML config in `packs/` and reference it in CLI commands.

---
For more details, see `README.md` and code comments in `src/openvoicepacks/`.
