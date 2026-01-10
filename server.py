from flask import Flask, request, jsonify, send_from_directory
import os
import json

app = Flask(__name__, static_folder='.', static_url_path='')

BLOG_FILE = 'blog.html'

@app.route('/')
def serve_index():
    return send_from_directory('.', 'blog-admin.html')

@app.route('/<path:filename>')
def serve_files(filename):
    return send_from_directory('.', filename)

@app.route('/api/save-blog', methods=['POST'])
def save_blog():
    try:
        data = request.get_json()
        html_content = data.get('html')
        
        if not html_content:
            return jsonify({'success': False, 'error': 'No HTML provided'}), 400
        
        with open(BLOG_FILE, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return jsonify({'success': True, 'message': 'Blog updated successfully!'})
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    print("Blog server running at http://localhost:5000")
    print("Open http://localhost:5000 to create posts")
    app.run(debug=False, port=5000)
