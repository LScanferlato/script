# script
conda install gcc_linux-64 gxx_linux-64
sudo zypper install libwebp-tools

for x in *.html; do mv "$x" "${x%.html}.php"; done
