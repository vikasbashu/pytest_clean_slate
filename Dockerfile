
FROM ubuntu:latest

# Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3 \
    python3.10-venv \
    git \
    nano \
    default-jdk \
    allure \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Download the allure package
RUN wget https://github.com/allure-framework/allure2/releases/download/2.27.0/allure_2.27.0-1_all.deb

# Install allure package
RUN dpkg -i allure_2.27.0-1_all.deb

# Clone the repository
RUN git clone https://github.com/vikasbashu/pytest_clean_slate.git

# Set the working directory
WORKDIR /pytest_clean_slate

# Create and activate virtual environment
RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Run tests and generate test report
CMD ["sh", "-c", "\
    . venv/bin/activate && \
    pytest -v -m api or smoke tests/ && \
    allure serve output/allure --port 8081 \
"]



