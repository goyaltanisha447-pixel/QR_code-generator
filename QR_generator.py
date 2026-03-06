import qrcode
def generate_qr_code(data, filename="qr_code.png"):
    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,#size of the QR code, 1 is the smallest
        box_size=10,#size of each box in pixels
        border=4,#size of the border in boxes
    )
    #add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
#create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR code generated and saved as {filename}")