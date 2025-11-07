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
  - Fetches two Deezer playlists by ID
  - Merges and deduplicates tracks
  - Shows which playlist(s) contain each track
  - Client-side search/filter
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
