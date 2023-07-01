from flask import Flask, Response, request
from webscrapepr import Webscrapper
import os


app = Flask(__name__)


@app.route('/scrape_elements', methods=['POST'])
def scrape_elements():
    json = request.get_json()
    url = json.get('url', '')
    name = json.get('name', '')
    attrs = json.get('attrs', {})
    except_retries = json.get('except_retries', 5)
    none_retries = json.get('none_retries', 5)
    wait_time = json.get('wait_time', 3)
    
    elems = Webscrapper.scrape_elements(
        url=url,
        name=name,
        attrs=attrs,
        except_retries=except_retries,
        none_retries=none_retries,
        wait_time=wait_time,
    )
    return Response(
        "\n".join([str(elem) for elem in elems]),
        mimetype='text/html',
    )


@app.route('/scrape_whole_page', methods=['POST'])
def scrape_whole_page():
    json = request.get_json()
    url = json.get('url', 'www.google.com')
    retries = json.get('retries', 5)
    wait_time = json.get('wait_time', 3)
    page = Webscrapper.scrape_whole_page(
        url=url,
        retries=retries,
        wait_time=wait_time,
    )
    return Response(
        str(page),
        mimetype='text/html',
    )


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=os.environ.get("FLASK_PORT"),
    )