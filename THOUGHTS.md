# Project thoughts

## Order of development

- Core library → abstracting TTS and normalizing outputs (the “engine room”).
- CLI tool → practical utility for power users who want to generate packs quickly.
- Templating/localisation → lowers the barrier for non-technical users and makes it global.
- Repository/community hub → turns it from a tool into an ecosystem.

## Improvements

🗂 Config flexibility: If you allow configs to be modular (e.g., “warning phrases,” “telemetry phrases”), people could swap out just parts of a pack instead of regenerating everything.

🔊 Audio consistency: Different TTS services can vary in volume and tone. A normalization step (RMS or LUFS leveling) would make packs feel more polished.

⚡ Caching: If someone regenerates the same phrase with the same voice, caching the WAV avoids unnecessary API calls and costs.

🌐 Future repo idea: You could even let people “fork” configs—like GitHub but for soundpacks—so someone could take a base English pack and tweak it into “English with sci-fi flair.”

### More immediate
- CLI tool for building voicepacks.
- Packaging as docker container.
- Remove ffmpeg requirement and use native Python method for wave conversion.
- Web repository of existing sound packs.
- Generate default 'system' data from EdgeTX repository automatically.
- Cache provider responses, speeding up generation where sound data already exists locally.
- Multiprocessing.
- Support for more TTS services.
- Multilingual support.

## Strategies

🏷 Branding & positioning: Give the tool a clear, memorable name and logo. If it looks official, people will treat it that way.

📖 Documentation first: A clean README, examples, and a quick-start guide go a long way. If someone can generate a pack in 5 minutes, they’ll spread the word.

🔄 Versioning & changelog: Even small updates show the project is alive. A visible release cadence (even if modest) reassures users.

🤝 Upstream collaboration: If you can get OpenTX/EdgeTX maintainers to link to your tool in their docs or forums, that’s basically a stamp of approval.

🌱 Community contributions: Set clear contribution guidelines so others can help maintain it. That way, it doesn’t live or die on your free time alone.

🛡 Sustainability mindset: Even if you step back one day, having a structure for others to pick it up (tests, modular code, clear roadmap) keeps it from fading.

## Tagline

> Generate and customize complete voice packs for OpenTX and EdgeTX radios.

## UX ideas

```bash
openvoicepacks init --template en_default
openvoicepacks build --config mypack.yaml
openvoicepacks list-voices --service polly
```

## Branding

🎨 Color Palette
| Color Name     | Hex       | Usage                          |
|----------------|-----------|--------------------------------|
| Coral Red      | #F04E4E | Primary accent (logo, buttons) |
| Navy           | #1E293B | Backgrounds, headers           | 
| Sky Blue       | #60A5FA | Highlights, links              | 
| Light Gray     | #F3F4F6 | Backgrounds, borders           | 
| Charcoal Black | #111827 | Text, outlines                 |


🔤 Typography
| Font face     | Usage                       |
|---------------|-----------------------------|
| Inter Bold    | Logo, headers               |
| Inter Regular | Body text                   |
| Inter Medium  | Subheadings                 |
| Monospace     | CLI examples, code snippets |

## Notes

https://pypi.org/project/diff-cover/

https://docs.astral.sh/ruff/integrations/

https://docs.astral.sh/uv/guides/integration/pre-commit/

https://github.com/EdgeTX/edgetx-sdcard-sounds

https://github.com/apps/renovate
