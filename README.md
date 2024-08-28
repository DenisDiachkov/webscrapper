# WebScrapper

WebScrapper is a Python-based web scraping tool that uses Selenium and BeautifulSoup to extract data from web pages. It provides a Flask API for easy integration into other projects.

## Features

- Scrape specific elements from web pages
- Scrape entire web pages
- Configurable retry mechanism for handling network issues
- Dockerized for easy deployment

## Requirements

- Docker
- Python 3.x
- Flask
- Selenium
- BeautifulSoup
- PyVirtualDisplay

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/webscrapper.git
   cd webscrapper
   ```

2. Build the Docker image:
   ```
   docker build -t webscrapper .
   ```

## Usage

1. Start the WebScrapper service:
   ```
   docker run -p 5000:5000 -e FLASK_PORT=5000 webscrapper
   ```

2. Use the API endpoints:

   - Scrape specific elements:
     ```
     POST /scrape_elements
     Content-Type: application/json

     {
       "url": "https://example.com",
       "name": "div",
       "attrs": {"class": "example-class"},
       "except_retries": 5,
       "none_retries": 5,
       "wait_time": 3
     }
     ```

   - Scrape whole page:
     ```
     POST /scrape_whole_page
     Content-Type: application/json

     {
       "url": "https://example.com",
       "retries": 5,
       "wait_time": 3
     }
     ```

## Project Structure

- `Dockerfile`: Defines the Docker image for the project
- `webscrapepr.py`: Contains the main WebScrapper class
- `app.py`: Flask application that exposes the API endpoints
- `.gitignore`: Specifies files to be ignored by Git

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).