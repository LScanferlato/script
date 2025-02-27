#!/bin/bash

# Configurazione
CONTAINER_NAME="stirling-pdf"
IMAGE_NAME="frooodle/s-pdf:latest"

echo "Aggiornamento ed esecuzione del container $CONTAINER_NAME..."

# Ferma e rimuovi il container esistente se presente
if [ "$(podman ps -aq -f name=$CONTAINER_NAME)" ]; then
    echo "Arresto il container esistente..."
    podman stop $CONTAINER_NAME
    podman rm $CONTAINER_NAME
fi

# Pull dell'ultima versione dell'immagine
echo "Download dell'ultima versione dell'immagine..."
podman pull $IMAGE_NAME

# Avvia il nuovo container
echo "Avvio il nuovo container..."
podman run -d \
    --name $CONTAINER_NAME \
    --restart unless-stopped \
    -v ./trainingData:/usr/share/tesseract-ocr/5/tessdata \
    -v ./extraConfigs:/configs \
    -v ./logs:/logs \
    -e DOCKER_ENABLE_SECURITY=false \
    -p 9008:8080 \
    $IMAGE_NAME

# Verifica lo stato del container
echo -e "\nStato del container:"
podman ps -f name=$CONTAINER_NAME

# Mostra i log iniziali
echo -e "\nLog del container:"
podman logs --tail 10 $CONTAINER_NAME
