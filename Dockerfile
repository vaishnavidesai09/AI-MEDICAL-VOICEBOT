# Use an official Python base image
FROM python:3.10-slim

# Copy all files into the container
COPY . /ai_doctor/

#set working directory
WORKDIR /ai_doctor

# Install Python dependencies
# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libportaudio2 \
    portaudio19-dev \
    ffmpeg \
    gcc \
    libc-dev \
    make \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt


# Expose the port your Gradio app will use
EXPOSE 7860

# Command to run your Gradio app
CMD ["sh","-c","python gradio_app.py"]
