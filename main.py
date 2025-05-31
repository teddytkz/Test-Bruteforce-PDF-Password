import PyPDF2
from datetime import datetime, timedelta

def generate_dates(start_year=1950, end_year=2025):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = timedelta(days=1)

    while start_date <= end_date:
        yield start_date.strftime("%d%m%y")
        start_date += delta

def brute_force_pdf(pdf_path, start_year=1950, end_year=2025):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        for password in generate_dates(start_year, end_year):
            try:
                if reader.decrypt(password):
                    print(f"[✓] Password ditemukan: {password}")
                    return password
            except Exception:
                pass
        print("[-] Password tidak ditemukan.")
        return None

pdf_path = "bill.pdf"
brute_force_pdf(pdf_path)
