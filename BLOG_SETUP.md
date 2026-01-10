# Blog Admin Setup

The blog-admin.html now automatically updates blog.html when you click "Save to blog.html". Here's how to set it up:

## Quick Start (Windows)

1. **Install Flask** (if you haven't already):
   ```
   pip install flask
   ```

2. **Start the server** by running:
   ```
   start-server.bat
   ```
   Or from PowerShell:
   ```
   python server.py
   ```

3. **Open your blog editor**:
   - Go to `http://localhost:5000` in your browser
   - This opens the blog-admin.html interface

4. **Create and save posts**:
   - Fill in the title, content, and optionally a custom date
   - Click "Add Post to Blog" to add it to the preview
   - Click "Save to blog.html" to automatically update your blog!

## How It Works

- `server.py` runs a local Python Flask server that listens for POST requests
- `blog-admin.html` sends the blog content to the server when you click save
- The server writes the updated HTML directly to `blog.html`
- Your blog updates instantly without needing to download files

## Troubleshooting

- **"Flask not found"**: Install it with `pip install flask`
- **"Address already in use"**: Another app is using port 5000. Close it or edit `server.py` to use a different port
- **Server won't start**: Make sure you're in the junoweb directory and have Python installed

## Manual Stop

Press `Ctrl+C` in the server window to stop it.

Enjoy your automated blog posting! 🎉
