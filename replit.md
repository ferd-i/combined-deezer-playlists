# Playlists Deezer Combinées

## Overview
A static web application that merges and displays tracks from two Deezer playlists. The app shows which playlist(s) each track belongs to, with search functionality to filter by title, artist, album, or playlist name.

## Project Structure
- `index.html` - Single-page application containing HTML, CSS, and JavaScript
- Pure vanilla JavaScript (no framework)
- No build process required
- Static hosting only

## Technical Details
- **Language**: HTML/CSS/JavaScript
- **API**: Deezer Public API
- **Features**:
  - Fetches two Deezer playlists by ID (up to 10,000 tracks each)
  - Merges and deduplicates tracks
  - Shows which playlist(s) contain each track with color-coded pills:
    - Yellow pill (AM1) for Library AM1
    - Red pill (AM2) for Library AM2
  - Clickable titles that link directly to Deezer tracks (ID shown in tooltip)
  - Sortable columns: click headers to sort by title, artist, album, or playlists
  - Checkbox system to mark tracks as "processed" (state saved in localStorage)
  - Sticky search bar with keyboard shortcut (Cmd+K on Mac, Ctrl+K on Windows)
  - Client-side search/filter across titles, artists, albums, and playlists
  - "Voir dans la liste" button in search results to jump back to track position in full list
  - Responsive design

## Configuration
- Playlist IDs are configured in the JavaScript section (lines 233-236)
- Currently set to playlists: "14516675863" and "14516679663"

## Deployment
- Flask backend server acts as CORS proxy for Deezer API
- Frontend makes API calls through `/api/deezer/` endpoint
- Configured for autoscale deployment on port 5000

## Setup Notes
The playlists configured in the app (14516675863 and 14516679663) require Deezer authentication. To use this app:
- Replace the playlist IDs in `index.html` (lines 236-237) with public Deezer playlist IDs, OR
- Implement Deezer OAuth authentication to access private playlists

To find public playlists, visit deezer.com and get the playlist ID from the URL.

## Recent Changes
- 2025-11-07: Initial import from GitHub
- 2025-11-07: Set up Flask proxy server to handle CORS issues with Deezer API
- 2025-11-07: Configured workflow for port 5000 with cache control headers
- 2025-11-07: Added color-coded pills for playlists (yellow for AM1, red for AM2)
- 2025-11-07: Added sortable columns (click headers to sort)
- 2025-11-07: Added checkbox system to mark processed tracks (saved in localStorage)
- 2025-11-07: Made titles clickable with direct links to Deezer tracks
- 2025-11-07: Increased API timeout to 120 seconds for large playlists
- 2025-11-08: Made search bar sticky for easier access while scrolling
- 2025-11-08: Added keyboard shortcut (Cmd+K / Ctrl+K) to focus search bar
- 2025-11-08: Added "Voir dans la liste" button in search results to navigate back to track position
- 2025-11-08: Made playlist pills clickable to open playlists on Deezer
- 2025-11-08: Added automatic retry logic (3 attempts) for failed API requests to reduce CORS/timeout errors
- 2025-11-08: Added debouncing (200ms) to search input for smoother performance with large playlists
- 2025-11-08: Implemented optimized localStorage cache system (24h duration) to save playlist data and avoid repeated API calls
  - Cache stores only essential fields to reduce size
  - Handles quota exceeded errors gracefully with fallback
- 2025-11-08: Added "Actualiser" button to manually force refresh from API
- 2025-11-08: Added "Playlists" button with modal interface to manage source playlists (add/remove)
- 2025-11-08: Made playlist IDs configurable and persistent in localStorage
