# 📚 项目文档索引

本项目的完整文档指南，帮助你快速找到需要的信息。

---

## 📑 文档列表

### 🎯 快速开始

#### **README.md** - 项目主文档
- 项目介绍和特性
- 安装和配置指南
- 基本使用方法
- 字典下载链接

👉 **适合**：首次使用的用户

---

### 🔧 配置相关

#### **CONFIG_PRIORITY.md** - 配置目录优先级说明
- ✅ 项目目录 vs 用户配置目录
- 配置文件查找逻辑
- 开发和生产环境配置建议
- 修改的技术细节

📍 **关键点**：
- 项目目录优先（开发便利）
- 用户配置目录备用（生产环境）
- 判断依据：`config/config.toml` 是否存在

👉 **适合**：想了解配置目录逻辑的开发者

---

### 🤖 AI/LLM 相关

#### **LLM_USAGE_SUMMARY.md** - LLM 功能总览 ⭐推荐⭐
- **核心问题解答**：
  - LLM 用来做什么？
  - 是否支持 Ollama？
- 4 大功能详解（词源/助记/词形/故事）
- 技术实现原理
- 支持的 100+ LLM 服务
- 实际效果对比
- 推荐配置方案

👉 **适合**：想全面了解 LLM 功能的用户

---

#### **LLM_ANALYSIS.md** - LLM 技术深度分析
- 详细代码实现
- Pydantic 数据模型
- Prompt 设计
- LiteLLM Router 机制
- 性能和并发控制
- 卡片展示效果

👉 **适合**：开发者和技术深入研究

---

#### **OLLAMA_SETUP_GUIDE.md** - Ollama 本地服务指南
- 安装和启动 Ollama
- 模型下载和管理
- 服务验证方法
- 常见问题排查
- 推荐模型选择
- 性能对比

👉 **适合**：使用本地 Ollama 的用户

---

## 🗂️ 目录结构

```
anki_packager/
│
├── README.md                    # 项目主文档
├── CONFIG_PRIORITY.md           # 配置目录说明
├── LLM_USAGE_SUMMARY.md        # ⭐ LLM 功能总览
├── LLM_ANALYSIS.md             # LLM 技术分析
├── OLLAMA_SETUP_GUIDE.md       # Ollama 配置指南
├── DOCUMENTATION_INDEX.md      # 本文档
│
├── config/
│   ├── config.toml             # 主配置文件
│   ├── vocabulary.txt          # 生词本
│   └── failed.txt              # 失败记录
│
├── dicts/                       # 字典文件目录
├── anki_packager/              # 源代码
└── anki_packager.log           # 运行日志
```

---

## 🔍 按场景查找文档

### 场景 1️⃣：我刚克隆项目，不知道怎么用
📖 阅读顺序：
1. **README.md** - 了解项目和基本安装
2. **CONFIG_PRIORITY.md** - 理解配置文件位置
3. **LLM_USAGE_SUMMARY.md** - 了解 AI 功能

---

### 场景 2️⃣：我想使用本地 Ollama
📖 阅读顺序：
1. **OLLAMA_SETUP_GUIDE.md** - 完整的 Ollama 配置流程
2. **LLM_USAGE_SUMMARY.md** - 推荐配置方案
3. 编辑 `config/config.toml`

快速命令：
```bash
# 1. 启动 Ollama
ollama serve

# 2. 下载模型
ollama pull qwen2.5:14b

# 3. 运行程序
python -m anki_packager
```

---

### 场景 3️⃣：我想知道 AI 具体生成什么内容
📖 直接阅读：
- **LLM_USAGE_SUMMARY.md** - 查看"核心答案"部分

关键内容：
- ✅ 词源分析
- ✅ 联想助记
- ✅ 谐音助记
- ✅ 词形变化
- ✅ 双语故事

---

### 场景 4️⃣：程序读不到我的配置文件
📖 直接阅读：
- **CONFIG_PRIORITY.md**

快速诊断：
```bash
# 检查项目配置是否存在
ls config/config.toml

# 如果存在，程序会优先使用项目目录
# 如果不存在，程序会使用用户配置目录
```

---

### 场景 5️⃣：Ollama 连接失败
📖 直接阅读：
- **OLLAMA_SETUP_GUIDE.md** - 查看"常见问题"部分

快速解决：
```bash
# 1. 检查服务
ollama serve

# 2. 验证端口
curl http://localhost:11434

# 3. 检查模型
ollama list
```

---

### 场景 6️⃣：我想了解技术实现细节
📖 阅读顺序：
1. **LLM_ANALYSIS.md** - 代码实现
2. 源代码：`anki_packager/ai.py`
3. 源代码：`anki_packager/prompt.py`

---

### 场景 7️⃣：我想切换到其他 LLM 服务
📖 直接阅读：
- **LLM_USAGE_SUMMARY.md** - 查看"支持的 LLM 服务"

配置示例都在文档中，包括：
- OpenAI
- Google Gemini
- Claude
- 国内大模型

---

### 场景 8️⃣：程序运行出错
📖 诊断步骤：
1. 查看 `anki_packager.log` 日志
2. 根据错误类型查阅相应文档：
   - 连接错误 → **OLLAMA_SETUP_GUIDE.md**
   - 配置错误 → **CONFIG_PRIORITY.md**
   - AI 错误 → **LLM_ANALYSIS.md**

---

## 📊 文档关系图

```
README.md (入口)
    │
    ├─→ CONFIG_PRIORITY.md (配置目录)
    │       │
    │       └─→ 理解项目配置优先级
    │
    └─→ LLM_USAGE_SUMMARY.md (LLM 总览) ⭐
            │
            ├─→ LLM_ANALYSIS.md (技术细节)
            │       │
            │       └─→ 源代码 (ai.py, prompt.py)
            │
            └─→ OLLAMA_SETUP_GUIDE.md (本地配置)
                    │
                    └─→ 实际操作和问题排查
```

---

## 🎯 核心问题快速索引

| 问题 | 文档 | 章节 |
|------|------|------|
| 如何安装？ | README.md | 快速开始 |
| 配置文件在哪？ | CONFIG_PRIORITY.md | 配置目录优先级 |
| LLM 做什么？ | LLM_USAGE_SUMMARY.md | 核心答案 |
| 支持 Ollama 吗？ | LLM_USAGE_SUMMARY.md | 是否支持本地 Ollama |
| 如何配置 Ollama？ | OLLAMA_SETUP_GUIDE.md | 启动 Ollama 服务 |
| 推荐什么模型？ | OLLAMA_SETUP_GUIDE.md | 推荐模型选择 |
| Ollama 连不上？ | OLLAMA_SETUP_GUIDE.md | 常见问题 |
| 如何切换 LLM？ | LLM_USAGE_SUMMARY.md | 配置选项详解 |
| AI 生成什么内容？ | LLM_USAGE_SUMMARY.md | 4 大类高质量学习内容 |
| 代码如何实现？ | LLM_ANALYSIS.md | 技术实现 |

---

## 📝 文档更新日志

### 2026-02-20
- ✅ 创建 CONFIG_PRIORITY.md
- ✅ 创建 LLM_USAGE_SUMMARY.md
- ✅ 创建 LLM_ANALYSIS.md
- ✅ 创建 OLLAMA_SETUP_GUIDE.md
- ✅ 创建 DOCUMENTATION_INDEX.md

**目的**：解答配置目录和 LLM 功能相关问题

---

## 💡 建议阅读路径

### 新手用户
1. README.md
2. LLM_USAGE_SUMMARY.md
3. OLLAMA_SETUP_GUIDE.md

### 开发者
1. CONFIG_PRIORITY.md
2. LLM_ANALYSIS.md
3. 源代码

### 快速上手
直接看：**LLM_USAGE_SUMMARY.md** ⭐

---

## 🆘 还有问题？

1. 📖 先查阅相关文档
2. 📋 查看 `anki_packager.log` 日志
3. 🔍 搜索日志中的错误信息
4. 🐛 根据错误类型查阅对应文档的"常见问题"章节

---

**祝你使用愉快！** 🎉

