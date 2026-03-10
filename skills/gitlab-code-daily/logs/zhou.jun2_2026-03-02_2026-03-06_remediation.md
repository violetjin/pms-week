# 整改清单（周军(苏) / zhou.jun2，2026-03-02~2026-03-06）

口径：按本周期提交涉及仓库进行 gitleaks+semgrep 扫描；清单中给出 **文件/行号 + 该行 blame 的 commit sha（版本）**，便于定位来源与整改。

> 注：blame sha 代表“当前仓库 HEAD 上该行最后修改的提交”，不一定等于本周期 zhou.jun2 的提交（需结合 MR/commit 责任再确认）。

## P0（必须立即核实/整改）：疑似凭证泄露（gitleaks）

1) **[P0] jwt**
- 仓库：cfm-file-download-client
- 文件：`HELP.md` L5:28
- 版本/commit（blame）：`f92d5736be22f5d92faed226b860a70ce46ae4a4`
- 建议：如为真实 token，立即轮换；文档中不要出现可用 token，改为占位符 `xxxxx`。

2) **[P0] jwt**
- 仓库：bdo-pm-confirmation
- 文件：`.../SfHztServiceImpl.java` L335:60
- 版本/commit（blame）：`1a103021b005a5d51897324fbcdd1490d315d105`
- 建议：确认是否硬编码 JWT/密钥；若是，移至配置中心/环境变量，并轮换历史密钥。

3) **[P0] generic-api-key（疑似硬编码 key/secret）**
- 仓库：bdo-pm-confirmation
- 文件：`.../HeaderXmlEncryptUtil.java` L33:42（blame：`dc6d4b968b21d00dbfd3e29471336dc033c97efb`）
- 文件：`.../HeaderXmlEncryptUtil.java` L263:17（blame：`dc6d4b968b21d00dbfd3e29471336dc033c97efb`）
- 建议：将 key/secret 从代码移出；如为加密参数，改为配置注入并做权限隔离。

4) **[P0] generic-api-key（疑似配置/脚本泄露）**
- 仓库：bdo-pm-confirmation
- `docs/v_20251030-fullLink/nacos/readme.txt` L3:6（blame：`fd510647c1ef2ab05a617d05d61ecaaa2b082937`）
- `sonar_scan.sh` L16:14（blame：`412cf3a4b49196cd5d97b651a313b663c0f49467`）
- `sonar_scan.bat` L17:18（blame：`57c68aaf036cc4ba560ce0a0321b684e7ec4fa18`）
- 建议：脚本/文档中不要出现真实 token；如需 CI 扫描，使用 CI 变量注入。

5) **[P0] generic-api-key（疑似配置文档泄露）**
- 仓库：consult-pms-server
- `.../resources/doc/readme` L12:2（blame：`b1fd155386ffdb02b454140f41a88e79e47b75e6`）
- `.../resources/doc/readme` L16:2（blame：`b1fd155386ffdb02b454140f41a88e79e47b75e6`）
- `doc/v_2024_3.29/config/nacos_v_03.29.txt` L7:6（blame：`b1fd155386ffdb02b454140f41a88e79e47b75e6`）
- `doc/v_2024_3.29/config/nacos_v_03.29.txt` L9:6（blame：`b1fd155386ffdb02b454140f41a88e79e47b75e6`）
- `doc/v_2024_3.29/config/德豪/李超超_nacos_v_03.29.txt` L41:4（blame：`b1fd155386ffdb02b454140f41a88e79e47b75e6`）
- `sonar_scan.bat` L17:18（blame：`7c7a6ed5ced89191be78d71363c4f9b999fe0cf3`）
- 建议：配置示例统一脱敏（host/username/password/token），必要时迁移到内网文档系统并加权限。

## P1（安全整改，建议纳入迭代）：加密/反序列化/注入风险（semgrep）

1) **[P1] Java 反序列化风险 ObjectInputStream**
- 仓库：consult-pms-server
- 文件：`.../CryptoTools.java` L36:4
- 版本/commit（blame）：`b1fd155386ffdb02b454140f41a88e79e47b75e6`
- 建议：避免对不可信输入进行 Java 原生反序列化；改用安全的白名单方案/JSON 显式映射；必要时增加输入来源校验。

2) **[P1] DES 已废弃 + CBC/PKCS5Padding padding oracle 风险（多处）**
- 仓库：consult-pms-server
- 文件：`.../CryptoTools.java`
  - DES：L135:63、L151:35、L156:35、L172:35、L175:35、L189:35、L193:35、L206:35、L211:35（blame 多为 `b1fd1553...`）
  - CBC padding oracle：L156:35、L175:35、L193:35、L211:35（blame 多为 `b1fd1553...`）
- 建议：统一升级到 AES-GCM（优先）或 AES-CBC + HMAC（次选）；IV 必须随机；避免复用 key/iv。

3) **[P1] MD5 使用（弱哈希）**
- 仓库：consult-pms-server
- 文件：
  - `.../SecurityUtils.java` L53:62（blame：`b1fd1553...`）
  - `.../SecurityUtils.java` L82:52（blame：`b1fd1553...`）
  - `.../StampServiceImpl.java` L858:44
  - `.../BdoMd5Utils.java` L21:86
- 建议：如用于密码/签名/完整性校验，改用 SHA-256/BCrypt/Argon2（按场景选）；如仅用于非安全场景（例如文件指纹），需在代码注释中明确。

4) **[P1] Script Engine Injection**
- 仓库：consult-pms-server
- 文件：`.../ReportNodeProcessLockServiceImpl.java` L132:5（blame：`b1fd1553...`）
- 建议：禁用/限制脚本引擎对外部输入的执行；使用预定义表达式/白名单；对输入做严格校验。

5) **[P1] permissive CORS**
- 仓库：bdo-pm-confirmation
- 文件：
  - `.../HzFeeController.java` L201:5（blame：`5a9853fd24360bdccc72c01f0198a6c92e9d0877`）
  - `.../HzCostRegisterServiceImpl.java` L1473:5、L1661:5
- 建议：限制允许的 Origin（按域名白名单），避免 `*`；并确认是否需要携带凭证。

6) **[P1] Insecure HostnameVerifier（接受任意主机名）**
- 仓库：bdo-pm-confirmation
- 文件：`.../BeanConfig.java` L12:1（blame：`5a9853fd24360bdccc72c01f0198a6c92e9d0877`）
- 建议：禁止在生产环境使用宽松校验；如是测试用途，确保仅在 test profile 生效。

7) **[P1] 静态 IV（no-static-initialization-vector） + CBC padding oracle（AES256Util 多处）**
- 仓库：bdo-pm-confirmation
- 文件：`.../AES256Util.java` L17:1（静态 IV）
- 文件：`.../AES256Util.java` L42/L65/L87/L109/L134/L178 等（CBC padding oracle）
- 建议：IV 每次随机生成并与密文一起存储/传输；优先切到 AES-GCM。

## 关联说明（本周期 zhou.jun2 的提交 sha）

- consult-pms-server 本周期提交：`4c8f5792ecab8bb1284e77e21cfc8c818fb5ef72`
- bdo-pm-confirmation 本周期提交（节选）：`6bf3edf3...`、`1f2ff53f...`、`414b11d1...`、`2274ace3...`、`5b50cb95...`、`95ee7460...`、`07d7dd2c...` 等
- cfm-file-download-client 本周期提交（节选）：`0fde39ff...`、`9cfd2109...`、`e916a902...`、`f92d5736...` 等

> 如需“是否由 zhou.jun2 在本周期引入”的归因：需要对每个命中文件做 `git log -L`/diff 对比本周期提交范围，我可以继续自动化补齐。
