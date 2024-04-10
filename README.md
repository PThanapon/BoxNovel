# BoxNovel Downloader

## Description
This Flask web application allows users to download chapters from BoxNovel. Users can specify the title of the novel, starting and ending chapter numbers, and the application will generate a downloadable ZIP file containing HTML files for each chapter.

## Installation
1. Clone this repository to your local machine:

    ```
    git clone <[repository-url](https://github.com/PThanapon/BoxNovel)>
    ```

2. Navigate to the project directory:

    ```
    cd BoxNovel
    ```

3. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage
1. Run the Flask application:

    ```
    python app.py
    ```

2. Open your web browser and go to `http://localhost:5000`.

3. Enter the title of the novel, starting and ending chapter numbers, then click the "Download" button.

4. Once the download is complete, click the provided download link to get the ZIP file containing the chapters.

### Alternative Usage
Alternatively, you can access the site hosted at [https://boxnovel.onrender.com](https://boxnovel.onrender.com) and follow the same steps as described above.

## Files
- `app.py`: This file contains the Flask application code which handles the routing and downloading of chapters.
- `requirements.txt`: This file lists all the dependencies required by the application.
- `templates`: This directory contains HTML templates.
  - `index.html`: HTML template for the main page where users input the details of the novel and chapters they want to download.
  - `download.html`: HTML template for the download page which displays the download link for the generated ZIP file.

## Dependencies
- Flask: A micro web framework for Python.
- BeautifulSoup: A library for parsing HTML and XML documents.
- Requests: An HTTP library for making requests to web servers.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Landing Page
<img src="https://raw.githubusercontent.com/PThanapon/BoxNovel/main/demo/landing-page.jpg" alt="Landing/Form Page" width="200">

## Download Page
<img src="https://raw.githubusercontent.com/PThanapon/BoxNovel/main/demo/download-page.jpg" alt="Download Page" width="200">

## Video Demo
[Download Video Demo](https://raw.githubusercontent.com/PThanapon/BoxNovel/main/demo/demo.mp4)



