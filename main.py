from selenium import webdriver
from selenium.webdriver.common.by import By

from mongo import Mongo

db_client = Mongo().client
db = db_client.get_database('EXAMENFINAL')
col = db.get_collection('autos')

driver = webdriver.Chrome()
driver.get("https://www.es.kayak.com/cars/Quito%2CEcuador-c35586/2023-10-02/2023-10-09?fs=carclass=SMALL&sort=rank_a")
autos = driver.find_elements(By.CLASS_NAME, "QYm5-CardContent")
for f in autos:

    marca = f.find_element(by=By.CLASS_NAME, value="fzHt-Header").text
    precio = f.find_element(by=By.CLASS_NAME, value="EuxN-price").text
    caracteristicas = f.find_element(by=By.CLASS_NAME, value="iTHr-result-list").text

    document = {

        "marca": marca,
        "precio": precio,
        "caracteristicas": caracteristicas,
    }
    col.insert_one(document=document)


    print(marca)
    print(precio)
    print(caracteristicas)
    print("-------------------------------")

driver.close()
