import qrcode

# Replace the URL with link
gk="https://www.linkedin.com/in/gauravkumar2111/"
data = "https://www.cricbuzz.com/profiles/576/rohit-sharma"

# Generate QR code
img = qrcode.make(data)
img = qrcode.make(gk)

# Save the QR code image
img.save("Gaurav.png")
