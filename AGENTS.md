# Repository Guidelines

## Project Structure & Module Organization
The frontend lives entirely in `index.html`, which bundles HTML, CSS, and vanilla JS for playlist merging and UI behavior (`index.html:1`). The Flask proxy in `server.py` (`server.py:1`) serves the static file and relays calls to the Deezer API to bypass CORS limits. Python metadata (`pyproject.toml`, `uv.lock`) defines dependencies; no separate `/src` or `/tests` folders exist yet. Keep new assets (images, data files) alongside `index.html` unless they become numerous enough to justify a dedicated directory.

## Build, Test, and Development Commands
- `uv sync` — install the Flask/CORS/requests stack declared in `pyproject.toml`.
- `uv run python server.py` — start the proxy plus static host on http://localhost:5000; auto-reloads are disabled, so restart after backend edits.
- `python -m http.server` (optional) serves the static UI only when you do not need API access.

## Coding Style & Naming Conventions
Frontend JS sticks to camelCase for variables/functions (`index.html:332`) and leans on const/let for immutability; keep indentation at two spaces to match the existing markup. Prefer descriptive helpers (e.g., `mergePlaylists`, `renderTable`) and keep inline comments focused on intent, not mechanics. Python code follows PEP 8 with 4-space indents; add type hints when expanding `server.py`.

## Testing Guidelines
There is no automated suite yet. Before opening a PR, exercise the happy-path flow: fetch both configured playlists, run several searches, toggle processed checkboxes, and confirm Deezer links open correctly. When introducing Python logic, add `pytest`-style tests under a new `tests/` directory and gate new features behind them; naming should mirror `test_<module>_<behavior>.py`.

## Commit & Pull Request Guidelines
Recent commits favor short, imperative summaries such as “Make search bar sticky and add navigation to search results” (`git log`). Keep messages under 72 characters and describe the user-facing effect in the body if needed. Pull requests should explain the motivation, outline UI/API impacts, list any manual testing performed, and attach screenshots/GIFs for visible changes. Reference related issues or Deezer tickets so maintainers can trace context quickly.

## Security & Configuration Tips
Playlist IDs are hard-coded in `index.html:332`; swap them for public IDs before pushing or load sensitive values from environment variables injected into the page. Avoid logging API tokens or full Deezer responses in the proxy. Remember that the proxy trusts all callers—add rate limiting or auth if exposing beyond local demos.
