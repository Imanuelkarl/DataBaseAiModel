from google_images_download import google_images_download

# Define search query
search_query = "cute puppies"

# Create downloader object
downloader = google_images_download.googleimagesdownload()  # Do not change format

# Define arguments for downloader
arguments = {"keywords": search_query, "limit": 2, "output_directory": "downloads"}

# Download image
downloader.download(arguments)

# Access downloaded image (modify path as needed)
image_link = f"downloads/{search_query}.jpg"

print(f"Downloaded image link: {image_link}")
