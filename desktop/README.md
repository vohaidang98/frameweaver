# FrameWeaver desktop media sources (macOS)

This archive accompanies a macOS preview build produced by `desktop/build-macos.py`.
It contains the exact FFmpeg/x264 source tarballs (pinned by SHA256 in
`runtime-lock.json`) and the `media-build.py` script used to compile the
static `ffmpeg`/`ffprobe` binaries bundled inside the app, with no Homebrew
libraries linked. Rebuild them yourself with:

```
python3 media-build.py
```

See the top-level `THIRD_PARTY_NOTICES.md` for licensing of the media sources
and other bundled runtimes (Electron, CPython, fonts).
