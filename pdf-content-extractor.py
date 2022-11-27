# def main():
#  print("OSR Sample program")
#  name = input ("what is your name?")
#  print ("Nice to meet you", name)

# if __name__ == "__main__" :
#   main()
import PyPDF2
pdf = open("project-resource\pdf-sample.pdf", "rb")
reader = PyPDF2.PdfFileReader(pdf)
page = reader.getPage(0)
print(page.extractText())