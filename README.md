# RepoGuide

更快讀懂專案，從理解到實作。

單人、本機使用的 repo 學習工作台。採小步實作：聊天 → repo 問答 → 程式執行 → 筆記 → RAG → MCP 與部署。

## 目前進度

已建立後端分層骨架及 `GET /health`。模型串接、資料庫、前端、工具與 Skills 尚未實作。

## 啟動

在專案根目錄執行（需要 Python 3.10+）：

```bash
source .venv/bin/activate
python -m pip install -r backend/requirements.txt
python -m uvicorn backend.app:app --reload
```

若尚未有虛擬環境，先執行 `python3 -m venv .venv`。

- 健康檢查：http://127.0.0.1:8000/health，預期 `{"status":"ok"}`。
- 互動式 API 文件：http://127.0.0.1:8000/docs。

依賴目前使用相容版本範圍；正式部署前再加入 lockfile 固定實際版本。

## 下一個學習任務

實作聊天的 request/response schema，再串起 controller、service 與 LiteLLM/OpenRouter adapter。第一步先完成非串流的一問一答。

架構與各目錄職責請見 [docs/architecture.md](docs/architecture.md)。
