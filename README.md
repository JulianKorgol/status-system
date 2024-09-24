# Open-Source Status System

Software that allow anyone to create a status page for their services.

---

**Documentation**: <a href="https://status-system.juliankorgol.com/" target="_blank">https://status-system.juliankorgol.com/</a> <br>
**GitHub Repository**: <a href="https://github.com/JulianKorgol/status-system" target="_blank">https://github.com/JulianKorgol/status-system</a>

---

## How to run
### Mariadb
Just run in the repo/app root folder:
```bash
docker compose up -d
```

### Backend (FastAPI)
Go to `backend` folder, then:
1. Install `requirements.txt`. You can use this command:
```bash
pip install -r  requirements.txt
```

2. Create `.env.local` and enter values from `env.example`

3. Run the app. You can use this command:
```bash
uvicorn main:app --env-file .env.local --reload
```

## Future frontend
![Future frontend image](https://status-system.juliankorgol.com/img/2024-09-24_future_frontend.png)

## Features:

* **TODO**: That section will be in the future
