from model import main as pegasus
import pytesseract
import PIL.Image

def processor(fname):
    # Process image
    myconfig = r"--psm 6 --oem 3"
    input_text = pytesseract.image_to_string(PIL.Image.open(fname), config=myconfig)

    # Summarization
    summary = pegasus(input_text)
    return summary