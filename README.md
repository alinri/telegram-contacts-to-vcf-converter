# Telegram contacts to vcf converter
A useful script to convert telegram contacts to vcf for import to your phone.

# Getting started

### Prerequisites
1. Open telegram desktop then go to:
Settings -> Advanced -> Export Telegram data
2. Uncheck all items except Contact list
3. Check Machine-readable JSON radio button.
4. Click EXPORT button.
5. Click SHOW MY DATA button to open result.json location and remember this location.

## Run

###### You must have Python installed on your system.
### Windows
```bash
git clone https://github.com/alinri/telegram-contacts-to-vcf-converter.git
cd .\telegram-contacts-to-vcf-converter.git\
python .\telegram_to_vcf.py
Please enter your telegram json location:
\path\to\result.json\file
done
Your vcf file Stored in in \path\to\result.vcf
```

### Linux
```bash
git clone https://github.com/alinri/telegram-contacts-to-vcf-converter.git
cd telegram-contacts-to-vcf-converter/
python3 telegram_to_vcf.py
Please enter your telegram json location:
/path/to/result.json/file
done
Your vcf file Stored in in /path/to/result.vcf
```


## Contributing
Pull requests are welcome.

