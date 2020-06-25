fileNameStr = "jquery-1.11.1.min.js jquery.easing.1.3.js bootstrap.min.js SmoothScroll.js jquery.scrollTo.min.js jquery.localScroll.min.js jquery.viewport.mini.js jquery.countTo.js jquery.appear.js jquery.sticky.js jquery.parallax-1.1.3.js jquery.fitvids.js owl.carousel.min.js isotope.pkgd.min.js imagesloaded.pkgd.min.js jquery.magnific-popup.min.js gmap3.min.js wow.min.js masonry.pkgd.min.js jquery.simple-text-rotator.min.js rev-slider.js all.js contact-form.js"
filenames = fileNameStr.split(' ')
print(filenames)


text_file = open("common_merged.js", "w")

for f in filenames:
    text_file.write(open(f).read())
    text_file.write(";\n\r")

text_file.close()