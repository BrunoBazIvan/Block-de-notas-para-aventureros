# Mostrar proceso que escucha en 8080 (recomendado)
sudo lsof -iTCP:8080 -sTCP:LISTEN -P -n


# Levantar mi servidor 
uvicorn blocknote.app.main:app --host 0.0.0.0 --port 8080 --reload