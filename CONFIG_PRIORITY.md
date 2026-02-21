# 配置目录优先级说明

## 修改说明

原项目硬编码使用系统用户配置目录，不便于开发和调试。现已修改为**优先使用项目目录**的策略。

## 配置目录优先级

程序现在按以下优先级查找配置和字典：

### 1. 项目目录（优先）✅
```
E:\Workspace\tools\anki_packager/
├── config/
│   ├── config.toml         # 如果这个文件存在，则使用项目目录
│   ├── vocabulary.txt
│   └── failed.txt
└── dicts/
    ├── stardict.7z
    ├── stardict.csv
    ├── stardict.db
    ├── 单词释义比例词典-带词性.mdx
    └── 有道词语辨析.mdx
```

### 2. 用户配置目录（备用）
如果项目目录中没有 `config/config.toml`，则使用系统用户配置目录：

**Windows:**
```
C:\Users\<用户名>\AppData\Roaming\anki_packager/
├── config/
│   ├── config.toml
│   ├── vocabulary.txt
│   └── failed.txt
└── dicts/
    └── ...
```

**Linux/macOS:**
```
~/.config/anki_packager/
├── config/
│   ├── config.toml
│   ├── vocabulary.txt
│   └── failed.txt
└── dicts/
    └── ...
```

## 使用建议

### 开发/调试场景
直接在项目目录下编辑配置文件：
```bash
# 编辑配置
notepad E:\Workspace\tools\anki_packager\config\config.toml

# 编辑生词本
notepad E:\Workspace\tools\anki_packager\config\vocabulary.txt

# 运行程序
python -m anki_packager
```

### 生产环境使用
通过 pip 安装后，配置文件会自动在用户配置目录中创建：
```bash
pip install apkger

# Windows 下快速打开配置目录
explorer %APPDATA%\anki_packager\config

# 或直接编辑
notepad %APPDATA%\anki_packager\config\vocabulary.txt

# 运行
apkger
```

## 修改的文件

1. `anki_packager/utils.py`
   - 新增 `get_project_root()` - 获取项目根目录
   - 新增 `get_config_dir()` - 智能选择配置目录
   - 修改 `initialize_config()` - 支持两种目录

2. `anki_packager/cli.py`
   - 修改导入，使用 `get_config_dir()` 替代 `get_user_config_dir()`

3. `anki_packager/dict/ecdict.py`
   - 修改所有字典路径获取，使用 `get_config_dir()`

## 判断逻辑

程序通过以下逻辑判断使用哪个目录：

```python
project_config_file = os.path.join(project_root, "config", "config.toml")

if os.path.exists(project_config_file):
    使用项目目录  # ✅ 推荐用于开发
else:
    使用用户配置目录  # 推荐用于安装后使用
```

## 好处

✅ **开发更便捷** - 直接在项目目录修改配置和单词列表  
✅ **调试更简单** - 配置文件和代码在同一个目录  
✅ **向后兼容** - 已安装的用户不受影响，继续使用用户配置目录  
✅ **版本控制友好** - 可以将项目配置加入 git（注意不要提交敏感信息如 API key）  
✅ **多环境支持** - 可以为不同项目/环境使用不同配置

