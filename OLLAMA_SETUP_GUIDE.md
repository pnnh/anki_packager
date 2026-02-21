# Ollama 本地服务使用指南

## 📋 问题诊断

从日志发现 Ollama 服务未启动：
```
litellm.APIConnectionError: OllamaException - Cannot connect to host localhost:11434
```

## 🚀 启动 Ollama 服务

### Windows

#### 方法 1：使用桌面应用（推荐）
1. 启动 Ollama Desktop 应用
2. 应用会在后台运行，托盘图标显示
3. 服务自动在 `http://localhost:11434` 监听

#### 方法 2：命令行启动
```powershell
ollama serve
```

### macOS / Linux
```bash
ollama serve
```

---

## ✅ 验证服务运行

### 1. 检查端口
```powershell
# Windows PowerShell
Test-NetConnection -ComputerName localhost -Port 11434

# Linux/macOS
curl http://localhost:11434
```

### 2. 检查进程
```powershell
# Windows
Get-Process ollama

# Linux/macOS
ps aux | grep ollama
```

### 3. 测试 API
```powershell
# Windows PowerShell
Invoke-RestMethod -Uri "http://localhost:11434/api/tags" -Method GET

# Linux/macOS
curl http://localhost:11434/api/tags
```

---

## 📦 安装和拉取模型

### 检查当前模型
```bash
ollama list
```

### 拉取你配置的模型
```bash
# 你的配置使用的模型
ollama pull gemma3:27b

# 或其他推荐模型
ollama pull qwen2.5:14b      # 强大的中英双语模型
ollama pull llama3.1:8b      # 轻量级但强大
ollama pull mistral:7b       # 速度快
```

---

## 🎯 推荐模型选择

### 适合英语学习的模型

| 模型 | 大小 | 特点 | 推荐指数 |
|------|------|------|---------|
| `qwen2.5:14b` | ~9GB | 中英双语优秀，理解文化内涵好 | ⭐⭐⭐⭐⭐ |
| `qwen2.5:7b` | ~5GB | 平衡性能和速度 | ⭐⭐⭐⭐ |
| `gemma2:9b` | ~5GB | Google 出品，质量稳定 | ⭐⭐⭐⭐ |
| `llama3.1:8b` | ~5GB | Meta 出品，通用能力强 | ⭐⭐⭐⭐ |
| `mistral:7b` | ~4GB | 速度快，适合批量处理 | ⭐⭐⭐ |

### 配置示例

```toml
# 推荐：Qwen 2.5（中英双语最佳）
[[MODEL_PARAM]]
model = "ollama/qwen2.5:14b"
api_base = "http://localhost:11434"
rpm = 10

# 或者：Gemma2（平衡选择）
[[MODEL_PARAM]]
model = "ollama/gemma2:9b"
api_base = "http://localhost:11434"
rpm = 15
```

---

## 🔧 配置文件位置

### 当前使用：项目目录
```
E:\Workspace\tools\anki_packager\config\config.toml
```

### 编辑配置
```powershell
notepad E:\Workspace\tools\anki_packager\config\config.toml
```

---

## 🧪 测试流程

### 1. 启动 Ollama
```bash
ollama serve
```

### 2. 确认模型存在
```bash
ollama list
# 如果没有 gemma3:27b，拉取模型
ollama pull gemma3:27b
```

### 3. 运行测试
```bash
cd E:\Workspace\tools\anki_packager
python -m anki_packager
```

### 4. 查看日志
```powershell
Get-Content anki_packager.log | Select-Object -Last 20
```

---

## 🐛 常见问题

### 1. 连接拒绝（Connection Refused）
**原因**：Ollama 服务未启动  
**解决**：
```bash
ollama serve
```

### 2. 模型不存在
**原因**：配置的模型未下载  
**解决**：
```bash
ollama pull gemma3:27b
# 或使用你想用的其他模型
ollama pull qwen2.5:14b
```

### 3. 响应超时
**原因**：模型太大，生成速度慢  
**解决**：
- 使用更小的模型（如 7B 版本）
- 增加 timeout 设置
- 降低并发数（`rpm`）

### 4. GPU/CPU 内存不足
**原因**：模型加载需要大量内存  
**解决**：
- 使用量化版本（如 `qwen2.5:7b-q4` 而不是 `qwen2.5:14b`）
- 关闭其他占用内存的程序
- 考虑使用云端 API（如 Gemini）

---

## 🔄 切换到云端 API（如果本地资源不足）

### Google Gemini（免费额度）
```toml
[[MODEL_PARAM]]
model = "gemini/gemini-2.0-flash-exp"
api_key = "YOUR_GEMINI_API_KEY"
rpm = 15
```

获取 API Key：https://aistudio.google.com/apikey

### OpenAI Compatible API
```toml
[[MODEL_PARAM]]
model = "openai/gpt-4o-mini"
api_key = "YOUR_API_KEY"
api_base = "https://api.openai.com/v1"
rpm = 50
```

---

## 📊 性能对比

### 本地 Ollama vs 云端 API

| 对比项 | Ollama 本地 | 云端 API |
|--------|------------|---------|
| **成本** | ✅ 免费（硬件成本） | ⚠️ 按量付费 |
| **隐私** | ✅ 完全本地 | ⚠️ 数据上传 |
| **速度** | ⚠️ 取决于硬件 | ✅ 通常更快 |
| **稳定性** | ⚠️ 取决于本地环境 | ✅ 高可用 |
| **质量** | ⚠️ 取决于模型 | ✅ 通常更好 |
| **网络依赖** | ✅ 无需网络 | ❌ 必须联网 |

---

## 🎯 推荐方案

### 方案 1：纯本地（推荐学习/测试）
```toml
[[MODEL_PARAM]]
model = "ollama/qwen2.5:14b"
api_base = "http://localhost:11434"
rpm = 10
```

**优点**：免费、隐私  
**要求**：16GB+ RAM，最好有 GPU

### 方案 2：本地 + 云端混合（推荐生产）
```toml
# 主力：本地 Ollama
[[MODEL_PARAM]]
model = "ollama/qwen2.5:7b"
api_base = "http://localhost:11434"
rpm = 10

# 备用：云端 Gemini
[[MODEL_PARAM]]
model = "gemini/gemini-2.0-flash-exp"
api_key = "YOUR_API_KEY"
rpm = 15
```

**优点**：平衡成本和可靠性  
**说明**：LiteLLM 自动负载均衡和故障转移

### 方案 3：纯云端（推荐企业使用）
```toml
[[MODEL_PARAM]]
model = "gemini/gemini-2.0-flash-exp"
api_key = "YOUR_API_KEY"
rpm = 30
```

**优点**：稳定快速，无需本地资源  
**成本**：Gemini 有免费额度

---

## 📝 快速启动清单

- [ ] 安装 Ollama：https://ollama.ai/download
- [ ] 启动 Ollama 服务：`ollama serve`
- [ ] 拉取模型：`ollama pull qwen2.5:14b`
- [ ] 验证服务：`curl http://localhost:11434`
- [ ] 配置 `config.toml`
- [ ] 测试运行：`python -m anki_packager`
- [ ] 检查生成的卡片

---

## 💡 提示

1. **首次运行会下载模型**，需要等待（几 GB 大小）
2. **建议先用小模型测试**（如 7B），确认流程正常
3. **可以禁用 AI** 功能来测试基础功能：`python -m anki_packager --disable_ai`
4. **查看详细日志**了解问题：`anki_packager.log`

---

## 🆘 需要帮助？

如果遇到问题：
1. 检查 `anki_packager.log` 日志文件
2. 确认 Ollama 服务运行：`ollama list`
3. 测试 API 连接：`curl http://localhost:11434/api/tags`
4. 尝试更小的模型或云端 API

