 ## dist to pypi
 python setup.py sdist build
 twine upload dist/*
 
 
 ###links
 https://my.oschina.net/letiantian/blog/788056
 
 
 
 ### auto update requirements.txt
 pip install pipreqs
 pipreqs --force  . 
