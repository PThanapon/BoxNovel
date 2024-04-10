from flask import Flask, request, send_file, render_template, redirect, url_for, jsonify
from bs4 import BeautifulSoup
import requests
import os
import re
import zipfile

app = Flask(__name__)

# Your existing functions and routes
def download(title, chapter):
    valid_title = re.sub(r'[\\/:*?"\'\’\%<>|]', '', title)
    link_title = "-".join(word for word in valid_title.split())

    abv = "".join(word[0].upper() for word in valid_title.split())
    url = f"https://boxnovel.com/novel/{link_title}/chapter-{chapter}"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    lst = []

    paragraphs = soup.find_all('p')

    if paragraphs == BeautifulSoup(requests.get(f"https://boxnovel.com/novel/{link_title}/").content, 'html.parser').find_all('p'):
        print("Invalid Chapter number")
        return False

    for paragraph in paragraphs:
        lst.append(paragraph.get_text())

    #text = '\n\n'.join(l for l in lst[:-21])
    text = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text Wrapping Example</title>
    <style>
        /* Apply CSS to ensure text wraps within a specific width */
        p {
            line-height: 1.15;
            width: 90%; /* Adjust width as needed */
            margin: 0 auto 30px; /* Center the paragraph on the page */
            text-align: justify; /* Justify the text for better readability */
            font-family: sans-serif; /* Apply sans-serif font */
            font-size: 20px; /* Specify font size */
        }
    </style>
    </head>
    <body>

    '''
    for l in lst[:-21]:
        text += f"<p>{l}</p>"

    text += '''
    </body>
    </html>
    '''

    # Determine the previous chapter
    prev_chapter_link = f"{abv} chapter {chapter - 1}.html" if chapter > 1 else None

    # Determine the next chapter
    next_chapter_link = f"{abv} chapter {chapter + 1}.html"

    # Create navigation buttons HTML with inline styles
    nav_buttons_html = f"""
    <div class="navigation" style="text-align: center; margin-top: 30px; padding-bottom: 20px;">
        {'<button style="padding: 10px 20px; background-color: red; color: white; border: none; border-radius: 5px; cursor: pointer; width: 150px;" onclick="location.href=/'' + {prev_chapter_link} + ''">Previous Chapter</button>' if prev_chapter_link else ''}
        <button style="padding: 10px 20px; background-color: red; color: white; border: none; border-radius: 5px; cursor: pointer; width: 150px;" onclick="location.href='{next_chapter_link}'">Next Chapter</button>
    </div>
    """
    
    # Insert navigation buttons HTML into the generated text
    text = text.replace('</body>', f'{nav_buttons_html}</body>')

    # Create the folder if it doesn't exist
    folder_path = os.path.join(app.root_path, 'static', 'downloads', valid_title)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Write the text to a text file inside the folder
    file_path = os.path.join(folder_path, f'{abv} chapter {chapter}.html')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

    return file_path

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_chapter():
    title = request.form['title']
    start = int(request.form['start'])
    end = int(request.form['end'])
    
    file_paths = []
    for i in range(start, end+1):
        file_path = download(title, i)
        if file_path:
            file_paths.append(file_path)
        else:
            # If download fails, return JSON response to trigger pop-up alert in JavaScript
            return jsonify({'error': 'Failed to download any chapter. Novel cannot be found.'}), 404
    
    if file_paths:
        zip_filename = f"{title}_chapters_{start}_to_{end}.zip"
        zip_path = os.path.join(app.root_path, 'static', 'downloads', zip_filename)
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for file_path in file_paths:
                zipf.write(file_path, os.path.basename(file_path))
        
        # Redirect to the download page
        return redirect(url_for('download_page', filename=zip_filename))
    else:
        # If download fails, return JSON response to trigger pop-up alert in JavaScript
        return jsonify({'error': 'Failed to download any chapter. Novel cannot be found.'}), 404

@app.route('/download_page/<filename>')
def download_page(filename):
    # Construct the download link
    download_link = url_for('static', filename=f'downloads/{filename}')
    return render_template('download.html', download_link=download_link)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
















