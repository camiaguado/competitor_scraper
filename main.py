from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/scrape")
def scrape():
    # Ejecuta el spider de Scrapy
    result = subprocess.run(["scrapy", "crawl", "competitor", "-o", "output.json"], capture_output=True, text=True)
    
    if result.returncode == 0:
        return {"status": "Success", "data": "output.json has been created"}
    else:
        return {"status": "Error", "details": result.stderr}
