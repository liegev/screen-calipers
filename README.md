# screen-calipers

A terminal tool that reads mouse positions and measures distances on screen, in pixels.

Useful for checking a UI mockup, a scanned drawing or a front-panel layout against
the real thing without opening an image editor.

## Use

```sh
pip install pyautogui
python3 screen_calipers.py
```

| Key | Mode |
|---|---|
| `l`  | live pointer position |
| `lc` | live position from an origin you pick with the mouse |
| `lo` | live position from an origin you type in |
| `d`  | distance between two points: dx, dy and diagonal |
| `q`  | quit |

Ctrl+C returns to the menu. On macOS, give the terminal Accessibility permission
so it can read the pointer.

## License

MIT. See [LICENSE](LICENSE).
