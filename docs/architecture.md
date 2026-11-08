# RepoGuide 架構決策

## 模組化單體與分層

初期以一個 FastAPI 後端提供 API，前端另以 React 呈現。各功能在同一份程式中用模組隔開，先不引入微服務。後續程式執行工作可以交給獨立 worker，共用服務與資料模型。

這是參考 MVC 職責分離的 API 架構：View 是 React；Controller 是 HTTP 路由；Model 的職責再分為資料模型、業務服務與資料存取。Pydantic API schema 與資料庫 model 分開維護。

## 目錄職責

| 路徑 | 責任 | 預計範例 |
| --- | --- | --- |
| backend/app.py | 建立應用、掛載路由與生命週期 | create_app |
| backend/controllers/ | 處理 HTTP 輸入、呼叫 service、回傳結果 | chat.py、workspaces.py |
| backend/schemas/ | API 請求與回應的 Pydantic 型別 | ChatRequest、ChatResponse |
| backend/services/ | 業務流程與使用案例 | 聊天、repo 問答、整理筆記 |
| backend/models/ | 持久化資料模型 | Conversation、Message、Note、Run |
| backend/repositories/ | 資料庫讀寫與查詢 | 對話保存、筆記查詢 |
| backend/integrations/ | 外部系統介接 | LiteLLM、Git、Docker、向量資料庫 |
| backend/core/ | 共用設定與基礎設施初始化 | 環境變數、logging、資料庫連線 |
| frontend/ | 使用者介面，對應 View | React 聊天與編輯器 |

空套件目前只是預留責任位置；不提前建立抽象基底類別或未使用的業務程式。

## 呼叫方向

```text
React → Controller → Service → Repository → SQLite
                            → Integration → 外部服務
```

- Controller 保持簡單，不放模型供應商設定或 SQL。
- Service 協調流程，不依賴 Request、Response 等 HTTP 型別。
- Repository 封裝資料存取；Integration 封裝外部系統。
- app.py 負責組裝，其餘模組不反向 import app.py，避免循環依賴。
- /health 足夠簡單，直接回應，不必建立無作用的 service/repository。

第一個聊天流程預計為：chat controller → chat service → LiteLLM adapter → OpenRouter。成功後再加入對話保存與串流。

## AI 功能如何加入

- Tool calling：後續在 backend/agents/tools/ 建立薄介面，重用 services 的搜尋與讀檔能力。
- Skills：後續在專案 skills/ 保存教學指引，由 Agent runtime 選擇與載入。它們是產品使用的指引，不是本專案開發助理的設定。
- RAG：檢索流程放 services；embedding 與向量庫介接放 integrations；筆記本文由一般資料庫保存。
- 執行環境：HTTP 建立工作，worker 執行受限 Docker job；Run 保存程式版本、stdout、stderr 與 exit code。
- MCP：工具穩定後新增協定入口，重用服務，不另外複製業務邏輯。

以上目錄在實作對應功能時才新增。

## 後續演進

目前以分層目錄幫助理解責任。當聊天、工作區、筆記各自變大，再搬到 backend/modules/chat/ 等功能模組，在模組內保留 controller/service/repository 分工。需要替換外部系統或隔離測試時，再引入少量介面與依賴注入；現階段不套用完整的 Clean Architecture 樣板。

FastAPI 的路由拆分依照官方 APIRouter 文件：
https://fastapi.tiangolo.com/tutorial/bigger-applications/
