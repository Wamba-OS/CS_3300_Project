from urllib.parse import urlparse

def extract_domain(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc  # Extracts 'amazon.com' from 'https://www.amazon.com/product123'

# Example usage
product_url = "https://www.amazon.com/product123"
domain = extract_domain(product_url)
print(domain)  # Output: 'www.amazon.com'
