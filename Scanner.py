from PIL import Image
import zxing
image_path = 'path_to_your_image.jpg'
reader = zxing.BarCodeReader()
barcode = reader.decode(image_path)
decoded_text = barcode.parsed if barcode else "No Data Matrix code found."
print(decoded_text)
