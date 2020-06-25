fileNameStr = "bootstrap.min.css style.css style-responsive.css animate.min.css vertical-rhythm.min.css owl.carousel.css magnific-popup.css rev-slider.css"
filenames = fileNameStr.split(' ')
print(filenames)

text_file = open("common_merged.css", "w")

for f in filenames:
    #deal with import in files
    #print(f)
    fileContent = open(f).read()
    for line in fileContent.splitlines():
        if line.startswith("@import"):
            importFile = line.split("\"")[1]
            print("import",importFile)
            text_file.write(open(importFile).read())
            text_file.write("\n\r")
    
    text_file.write(fileContent)
    text_file.write("\n\r")

text_file.close()