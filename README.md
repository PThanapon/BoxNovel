# BoxNovel Downloader

This Flask application allows users to download chapters from BoxNovel in HTML format. It scrapes the content from the BoxNovel website and provides users with downloadable HTML files for the specified range of chapters.

## Requirements

To run this application, you need to have Python installed on your system. Additionally, you need to install the required Python packages listed below. You can install them using the following command:

```bash
pip install Flask requests beautifulsoup4
```

## Directory Structure

```
flask.py
template/
    - index.html
    - download.html
```

## Usage

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install the required packages as mentioned above.
4. Run the Flask application by executing the following command:

```bash
python flask.py
```

5. Open your web browser and go to `http://127.0.0.1:5000/`.
6. Enter the title of the novel, start and end chapter numbers, then click the "Download" button.
7. Once the download is complete, you will be redirected to a page where you can download the ZIP file containing all the chapters.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.

## Credits

This application was created by [Your Name] and is based on [Your Source/Inspiration].

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

