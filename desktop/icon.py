"""Generate a macOS .iconset directory with the FrameWeaver placeholder icon.

Usage: python3 desktop/icon.py <path/to/FrameWeaver.iconset>
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

SIZES = [16, 32, 128, 256, 512]
FONT_CANDIDATES = [
    '/System/Library/Fonts/Supplemental/Arial Bold.ttf',
    '/System/Library/Fonts/Supplemental/Arial.ttf',
    '/Library/Fonts/Arial Bold.ttf',
]


def render(size):
    image = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    margin = round(size * 0.04)
    draw.rounded_rectangle((margin, margin, size - margin, size - margin),
                            radius=round(size * 0.18), fill='#8255EE')
    font = None
    for candidate in FONT_CANDIDATES:
        if Path(candidate).exists():
            font = ImageFont.truetype(candidate, round(size * 0.34))
            break
    if font:
        draw.text((size / 2, size / 2), 'FW', font=font, anchor='mm', fill='white')
    return image


def main():
    target = Path(sys.argv[1])
    target.mkdir(parents=True, exist_ok=True)
    base = render(1024)
    for size in SIZES:
        base.resize((size, size), Image.LANCZOS).save(target / f'icon_{size}x{size}.png')
        base.resize((size * 2, size * 2), Image.LANCZOS).save(target / f'icon_{size}x{size}@2x.png')


if __name__ == '__main__':
    main()
