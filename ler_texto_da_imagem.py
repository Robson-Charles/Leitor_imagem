import os

import pytesseract
import cv2




def iniciar():

    image = cv2.imread("Captcha.jpg")

    pytesseract.pytesseract.tesseract_cmd = "Tesseract-OCR/tesseract.exe"

    texto = pytesseract.image_to_string(image)
    try:
        os.remove('Captcha.txt')
    except:
        pass

    
    os.remove('Captcha.jpg')
    return texto
#text = iniciar()




'''from playwright.async_api import Playwright, async_playwright
import asyncio
from tkinter.messagebox import showinfo
async def iniciar():
    async with async_playwright() as playwright:
        browser = await playwright.webkit.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://api.products.aspose.app/ocr/pt/scan-image")
        await page.locator("#UploadFileInput").set_input_files("Captcha.jpg")
        await page.locator("#lngselect").click()
        await asyncio.sleep(1)
        await page.locator("#dropdownmenu1").get_by_text("Português").click()
        await asyncio.sleep(1)
        await page.locator('#rbtxt').click()
        await page.get_by_text("Got it!").wait_for(timeout=10000)

        texto = await page.locator("#textBoxResult").inner_text()
        while texto == 'Processing...':
            print('carregando')
            await asyncio.sleep(2)
            texto = await page.locator("#textBoxResult").inner_text()

        showinfo('texto', texto)
        await asyncio.sleep(100)
        # ---------------------
        await context.close()
        await browser.close()
        print(texto)
        return texto

    async with async_playwright() as playwright:
        texto_obtido = await run(playwright)

    return texto_obtido
if __name__ == "__main__":
    asyncio.run(iniciar())
# Chamando a função iniciar e obtendo o texto retornado

'''
