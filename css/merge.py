fileNameStr = "bootstrap.min.css style.css style-responsive.css animate.min.css vertical-rhythm.min.css owl.carousel.css magnific-popup.css rev-slider.css"
filenames = fileNameStr.split(' ')
print(filenames)


text_file = open("common_merged.css", "w")

for f in filenames:
    text_file.write(open(f).read())
    text_file.write(";\n\r")

text_file.close()