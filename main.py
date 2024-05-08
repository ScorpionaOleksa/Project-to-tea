import time
import random

def generate_motivational_quote():
    quotes = [
        "The only way to do great work is to love what you do. – Steve Jobs",
        "Believe you can and you're halfway there. – Theodore Roosevelt",
        "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
        "In the middle of every difficulty lies opportunity. – Albert Einstein"
    ]
    return random.choice(quotes)

if __name__ == "__main__":
    while True:
        print(generate_motivational_quote())
        time.sleep(3)  # 7 minutes = 7 * 60 seconds = 420 seconds
