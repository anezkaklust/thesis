 gs -dCompatibilityLevel=1.4 \
    -dPDFSETTINGS=/prepress \
    -dCompressFonts=true \
    -dSubsetFonts=true \
    -dNOPAUSE \
    -dBATCH \
    -sDEVICE=pdfwrite \
    -sOutputFile=Klustova-A-2024-PhD-Thesis.pdf \
    -c ".setpdfwrite <</NeverEmbed [ ]>> setdistillerparams" \
    -f thesis.pdf
