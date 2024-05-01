# SHA-512 for files integrity

This repository is a Python executable to verify the integrity of two files that pretends to be the same.
The importance of this verification could be transported to another complex scenario in wich we
want to verify if some data has suffered any changes after some process.

## Get Started

**⚠️You should have Python installed.⚠️**  
**⚠️This tutorial works on Linux⚠️**  
If you are not on Linux, try to look for the equivalences in your OS.

## Run executable

Make the file executable:

```
sudo chmod +x ./AES
```

Run the .txt example:
```
./check -i tests/text1.txt tests/text2.txt
./check -i tests/text1.txt tests/text1.copy.txt
```
Note that the difference between `text1.txt` and `text2.txt` is that `text2.txt` does not have the
final space that `text1.txt` have on the end of the first line.
**Text 1:**
![alt text](https://github.com/jesus2801/AES-for-file-encryption/blob/master/imgs/text1.png?raw=true)
**Text 2:**
![alt text](https://github.com/jesus2801/AES-for-file-encryption/blob/master/imgs/text2.png?raw=true)

## Authors

- [@jesus2801](https://github.com/jesus2801)

## License

[MIT](https://choosealicense.com/licenses/mit/)
