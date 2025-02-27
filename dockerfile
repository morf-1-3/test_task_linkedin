FROM python:3.9  

WORKDIR /app  

COPY . .  

# Встановлення залежностей для Chrome і ChromeDriver
RUN apt update && apt install -y wget curl unzip \
    libnss3 libatk1.0-0 libx11-xcb1 libxcomposite1 libxcursor1 \
    libxdamage1 libxfixes3 libxi6 libxrandr2 libxrender1 \
    libxss1 libxtst6 fonts-liberation libappindicator3-1 \
    libasound2 libgbm1 libgtk-3-0 libxcb1 xdg-utils

# Встановлення Google Chrome
RUN wget -qO- https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb > chrome.deb \
    && apt install -y ./chrome.deb \
    && rm chrome.deb

# Встановлення ChromeDriver (переконайся, що версія збігається з Chrome)
RUN wget -O /tmp/chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/133.0.6943.141/linux64/chromedriver-linux64.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip



# Додаємо chromedriver у PATH
ENV PATH="/usr/local/bin:${PATH}"

# Встановлення залежностей Python
RUN pip install --no-cache-dir -r requirements.txt  

CMD ["python", "main.py"]  
