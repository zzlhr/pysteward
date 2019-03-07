# django还原数据结构到model
```bash
python manage.py inspectdb > steward/models.py
```

# 创建虚拟环境
```bash
python3 -m venv env

# windows 
venv\Scripts\activate.bat

# mac/Unix
source env/bin/activate
```