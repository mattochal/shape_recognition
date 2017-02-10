!#/bin/bash

echo "zipping"
zip -r images.zip images/
echo "emailing"
mpack -s "Images" images.zip mateusz.ochal8@outlook.com