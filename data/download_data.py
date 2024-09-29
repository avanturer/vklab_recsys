import gdown

url = 'https://drive.google.com/uc?id=1wK6Z1_Nld00tIwKgwZmN2hhN9FSIOdza'
output = 'data/data.csv'  # Укажите имя выходного файла
# Скачивание файла
gdown.download(url, output, quiet=False)

url = 'https://drive.google.com/uc?id=17OhQM6PJvUtWQ5Mt-r8ACmisZ-x3S2oK'
output = 'data/post2ctr_dataset_2000.csv'  # Укажите имя выходного файла
# Скачивание файла
gdown.download(url, output, quiet=False)

url = 'https://drive.google.com/uc?id=1U2DhtkNLysxqiU2kELyM7QIvgjfisKPp'
output = 'data/post2ctr_dataset_7000.csv'  # Укажите имя выходного файла
# Скачивание файла
gdown.download(url, output, quiet=False)

url = 'https://drive.google.com/uc?id=1rDNY4tWT2g7Bzf_2ULdyRFD6FEDe2VWA'
output = 'data/post2ctr_dataset.csv'  # Укажите имя выходного файла
# Скачивание файла
gdown.download(url, output, quiet=False)