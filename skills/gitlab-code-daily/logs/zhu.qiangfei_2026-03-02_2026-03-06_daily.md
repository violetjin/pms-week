# 个人日报（代码效率&质量）

- 人员：朱墙飞（zhu.qiangfei）
- 时间范围：2026-03-02 ~ 2026-03-06（09:00-19:00）
- 覆盖范围：sacp 组内项目（faith、faith-ui、deploy）

## 一、效率概览（基于提交统计+估时口径）

- 提交次数：52 commits
- 代码变更量（add+del）：39765 LOC
- 估算投入：11.82 小时（combined）
- 效率指标（仅供相对参考）：
  - loc/h：~3365（按 session）
  - commits/h：~4.4（按 session）

> 说明：本周期提交频率较高（日均 ~10 commits），涉及多个模块，包含工程初始化、功能开发、修复与文档更新。

## 二、提交内容概览（按项目）

1) **sacp/faith**
- 合并报表功能迭代（清水对接、索引号覆盖、生成失败修复等）
- junit 测试代码增补（2 次提交）
- 审计平台说明手册撰写（852 LOC 新增）
- 依赖/构建配置优化
- 项目/合同/函证相关模块优化

2) **sacp/faith-ui/faith-ipo-ui**
- Merge develop 远程分支（大量同步，3946 LOC）
- 合并报表相关前端功能开发

3) **sacp/deploy**
- 上线部署相关配置提交

（明细见：`zhu.qiangfei_2026-03-02_2026-03-06.json`）

## 三、代码质量/风险扫描结果

扫描说明：对 faith 和 faith-ipo-ui 两个代码仓库做了 gitleaks（密钥）+ semgrep（安全规则）扫描。deploy 项目无代码文件（仅配置），跳过。

### 1) gitleaks（密钥/凭证泄露）

**sacp/faith：25 条**
- aws-access-token：6 条
- generic-api-key：14 条
- jwt：3 条
- private-key：2 条

**sacp/faith-ui/faith-ipo-ui：2 条**
- aws-access-token：2 条

**建议处置**：
- 将这些密钥/凭证从代码/配置文件中移除；
- 改用环境变量、配置中心或密钥管理服务；
- 对已泄露的凭证进行轮换；
- 若为示例/测试数据，改用占位符并添加 `# 示例，勿直接使用` 注释。

### 2) semgrep（安全规则）

**sacp/faith：256 条（ERROR 16 / WARNING 240）**

Top 规则（按命中次数）：
- `unrestricted-request-mapping`（104 条）：Spring 宽松路径匹配，存在潜在越权风险
- `des-is-deprecated`（36 条）：DES 加密已废弃，建议升级 AES
- `missing-internal`（24 条）：Nginx 配置缺少 `internal` 指令，存在内部路径泄露风险
- `cbc-padding-oracle`（20 条）：CBC + PKCS5Padding 存在填充预言攻击
- `unquoted-attribute-var`（15 条）：HTML 模板变量未加引号，XSS 风险
- `httpservlet-path-traversal`（9 条）：路径遍历风险
- `cookie-missing-httponly`（7 条）：cookie 缺少 httponly 标志
- `cookie-missing-secure-flag`（7 条）：cookie 缺少 secure 标志
- `formatted-sql-string`（7 条）：格式化 SQL 字符串（潜在注入）

**sacp/faith-ui/faith-ipo-ui：0 条**
- semgrep 未命中

**建议处置**：
- 建立基线：将当前告警“冻结”为基线，要求新增代码不得新增告警；
- 分优先级整改：
  - 高优先级：unrestricted-request-mapping、path-traversal、formatted-sql-string
  - 中优先级：DES 弃用、CBC padding oracle、cookie 安全标志
  - 低优先级：Nginx missing-internal、HTML 未引号属性（视场景评估）

## 四、结论（本周期）

- **交付效率**：提交活跃，覆盖功能、测试、文档、配置多个维度，整体偏“全面迭代”。
- **风险点**：
  - 密钥/凭证泄露（gitleaks 27 条）：需立即处置，避免生产环境风险。
  - 安全规则告警（semgrep 256 条）：需分优先级整改，建立安全基线。
- **后续建议**：
  - 将 gitleaks 集成到 CI（如 MR 阶段），拦截密钥提交。
  - 将 semgrep 告警纳入 Code Review check list，新增代码不得新增高危告警。
  - 建议对 `des-is-deprecated`、`cbc-padding-oracle`、`cookie-xxx` 等规则统一做一次“加密/安全配置治理”。
