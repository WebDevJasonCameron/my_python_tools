import os
import hashlib
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(filename='file_hash_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')


def calculate_hash(file_path, buffer_size=65536):
    """Calculate SHA-256 hash for a given file."""
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(buffer_size):
            sha256.update(chunk)
    return sha256.hexdigest()


def split_file(file_path, chunk_size=1024 * 1024):  # Default chunk size: 1MB
    """Split file into smaller chunks and return the paths of the chunks."""
    file_chunks = []
    file_size = os.path.getsize(file_path)
    with open(file_path, 'rb') as f:
        for i in range(0, file_size, chunk_size):
            chunk_filename = f"{file_path}.part{i // chunk_size}"
            with open(chunk_filename, 'wb') as chunk_file:
                chunk_file.write(f.read(chunk_size))
                file_chunks.append(chunk_filename)
    return file_chunks


def process_files(directory):
    """Process each file in the directory."""
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)

            # Calculate and log hash of the original file
            file_hash = calculate_hash(file_path)
            logging.info(f"File: {file_path} - Hash: {file_hash}")

            # Split the file into smaller chunks
            chunks = split_file(file_path)

            # Calculate and log hash for each chunk
            for chunk in chunks:
                chunk_hash = calculate_hash(chunk)
                logging.info(f"Chunk: {chunk} - Hash: {chunk_hash}")


if __name__ == "__main__":
    directory_to_process = "path/to/your/directory"  # Set the path to the directory you want to process
    process_files(directory_to_process)
