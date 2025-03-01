"""
Cтворити асинхронний веб-додаток за допомогою FastAPI,
який дозволяє користувачам відправляти URL веб-сторінки для парсингу.
Додаток буде отримувати HTML-код сторінки і витягати з нього певну інформацію, наприклад заголовки або всі посилання.

Example: https://en.wikipedia.org/wiki/Python_(programming_language)

title: span class='mw-page-title-main
"""
import httpx
import ngrok
import uvicorn
from fastapi import FastAPI, Query
from bs4 import BeautifulSoup

listener = ngrok.forward(8000, authtoken='Your ngrok token(But please store the token in a YML file, for example)')


app = FastAPI()


async def get_http(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.text


async def get_class_info(
    html_code: str,
    class_name: str
):
    soup = BeautifulSoup(html_code, 'html.parser')
    class_content = soup.find(class_=class_name)
    return class_content


async def collect_info_from_wiki(url: str):
    url = 'https://' + url
    html_code = await get_http(url=url)
    result_title = await get_class_info(html_code=html_code, class_name='mw-page-title-main')

    result_paradigm = await get_class_info(html_code=html_code, class_name='infobox vevent')
    th_paradigm = result_paradigm.find('th', string='Paradigm')
    paradigm_info = th_paradigm.find_next_sibling('td')

    website_th = result_paradigm.find('th', string='Website')
    website_info = website_th.find_next_sibling('td')

    th_influenced = result_paradigm.find('th', string="Influenced")
    tr_influenced = th_influenced.find_parent('tr').find_next_sibling('tr')

    return {
        "title": result_title.text,
        "paradigm_info": paradigm_info.text,
        "website_info": website_info.text,
        "influenced_info": tr_influenced.text,
    }


@app.get("/info")
async def get_info_from_wiki(
    url: str = Query(
        title='url link',
        description='url link without http(s)://',
    )
):
    return await collect_info_from_wiki(url=url)

if __name__ == "__main__":
    print(listener.url())
    uvicorn.run(
        app=app,
        port=8000
    )
