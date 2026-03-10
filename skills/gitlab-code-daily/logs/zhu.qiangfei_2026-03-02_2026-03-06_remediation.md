# 整改清单（朱墙飞 / zhu.qiangfei，2026-03-02~2026-03-06）

口径：按本周期提交涉及仓库进行 gitleaks+semgrep 扫描；清单中给出 **文件/行号 + 该行 blame 的 commit sha（版本）**，便于定位来源与整改。

> 注：blame sha 代表“当前仓库 HEAD 上该行最后修改的提交”，不一定等于本周期 zhu.qiangfei 的提交（需结合 MR/commit 责任再确认）。

## P0（必须立即核实/整改）：疑似凭证泄露（gitleaks）

1) **[HIGH] aws-access-token**
- 仓库：sacp__faith-ui__faith-ipo-ui
- 文件：`gitlab/sacp__faith-ui__faith-ipo-ui/resources/libs/bdosnap/js/bdosnap.js` L39:696
- 版本/commit（blame）：`877750a85e0a584e0fed262ab969dce626da5c0c`
- 建议：Identified a pattern that may indicate AWS credentials, risking unauthorized cloud resource access and data breaches on AWS platforms.

2) **[HIGH] aws-access-token**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/Faith/src/main/Faith/assets/js/plugins/bdosnap.1.0.0/static/js/bdosnap.js` L39:696
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Identified a pattern that may indicate AWS credentials, risking unauthorized cloud resource access and data breaches on AWS platforms.

3) **[HIGH] aws-access-token**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/Faith/src/main/Faith/assets/js/plugins/bdosnap.1.0.0/static/js/bdosnap.js.map` L1:6564
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Identified a pattern that may indicate AWS credentials, risking unauthorized cloud resource access and data breaches on AWS platforms.

4) **[HIGH] aws-access-token**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/Faith/src/main/Faith/assets/js/plugins/bdosnap.1.0.0/static/js/demo.js` L32:8112
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Identified a pattern that may indicate AWS credentials, risking unauthorized cloud resource access and data breaches on AWS platforms.

5) **[HIGH] aws-access-token**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/Faith/src/main/Faith/assets/js/plugins/bdosnap.1.0.0/static/js/demo.js.map` L1:1888
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Identified a pattern that may indicate AWS credentials, risking unauthorized cloud resource access and data breaches on AWS platforms.

6) **[HIGH] aws-access-token**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/Faith/src/main/Faith/syncprogram/libs/bdosnap/js/bdosnap.js` L32:6834
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Identified a pattern that may indicate AWS credentials, risking unauthorized cloud resource access and data breaches on AWS platforms.

7) **[HIGH] generic-api-key**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/Faith/src/main/Faith/assets/js/plugins/video/video.min.js` L21:7975
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a Generic API Key, potentially exposing access to various services and sensitive operations.

8) **[HIGH] generic-api-key**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/Faith/src/main/Faith/assets/js/plugins/video/videojs-contrib-hls.min.js` L3:2003
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a Generic API Key, potentially exposing access to various services and sensitive operations.

9) **[HIGH] generic-api-key**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-ipo/faith-ipo-provider/src/main/java/cn/com/bdo/ipo/dao/IpoCustomersubjectDao.java` L114:89
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a Generic API Key, potentially exposing access to various services and sensitive operations.

10) **[HIGH] generic-api-key**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-ipo/faith-ipo-provider/src/main/java/cn/com/bdo/ipo/dao/IpoMerchantdetailDao.java` L30:31
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a Generic API Key, potentially exposing access to various services and sensitive operations.

11) **[HIGH] generic-api-key**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-ipo/faith-ipo-provider/src/main/java/cn/com/bdo/ipo/dao/IpoMerchantdetailDao.java` L59:104
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a Generic API Key, potentially exposing access to various services and sensitive operations.

12) **[HIGH] generic-api-key**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-ipo/faith-ipo-provider/src/main/java/cn/com/bdo/ipo/dao/IpoMerchantrelatedDao.java` L41:111
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a Generic API Key, potentially exposing access to various services and sensitive operations.

13) **[HIGH] generic-api-key**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-ipo/faith-ipo-provider/src/main/java/cn/com/bdo/ipo/dao/IpoMerchantrelatedDao.java` L77:106
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a Generic API Key, potentially exposing access to various services and sensitive operations.

14) **[HIGH] generic-api-key**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-ipo/faith-ipo-provider/src/main/java/cn/com/bdo/ipo/dao/IpoMerchantrelatedDao.java` L90:104
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a Generic API Key, potentially exposing access to various services and sensitive operations.

15) **[HIGH] generic-api-key**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-ipo/faith-ipo-provider/src/main/java/cn/com/bdo/ipo/dao/IpoMerchantrelatedDao.java` L111:104
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a Generic API Key, potentially exposing access to various services and sensitive operations.

16) **[HIGH] generic-api-key**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-ipo/faith-ipo-provider/src/main/java/cn/com/bdo/ipo/dao/IpoMerchantrelatedDao.java` L129:104
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a Generic API Key, potentially exposing access to various services and sensitive operations.

17) **[HIGH] generic-api-key**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/sync_db_struct/load_vars.yml` L7:8
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a Generic API Key, potentially exposing access to various services and sensitive operations.

18) **[HIGH] generic-api-key**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/sync_db_struct/log_vars.yml` L6:8
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a Generic API Key, potentially exposing access to various services and sensitive operations.

19) **[HIGH] generic-api-key**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/sync_db_struct/main_vars.yml` L6:8
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a Generic API Key, potentially exposing access to various services and sensitive operations.

20) **[HIGH] generic-api-key**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-wps/faith-wps-facade/src/main/java/cn/com/bdo/wps/util/WpsLoginUtils.java` L16:39
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a Generic API Key, potentially exposing access to various services and sensitive operations.

21) **[HIGH] jwt**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-core-biz/faith-core-biz-impl/src/main/java/cn/com/bdo/dgCenter/vo/GeneralTableParsingPlatformVo.java` L12:22
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Uncovered a JSON Web Token, which may lead to unauthorized access to web applications and sensitive user data.

22) **[HIGH] jwt**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-core-biz/faith-core-biz-impl/src/main/java/cn/com/bdo/dgCenter/vo/GeneralTableParsingPlatformVo.java` L15:23
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Uncovered a JSON Web Token, which may lead to unauthorized access to web applications and sensitive user data.

23) **[HIGH] jwt**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-core-biz/faith-core-biz-impl/src/main/java/cn/com/bdo/wind/service/WindJobService.java` L814:41
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Uncovered a JSON Web Token, which may lead to unauthorized access to web applications and sensitive user data.

24) **[HIGH] private-key**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/kibana_test_prod/config/kibana.example.org.key` L1:1
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Identified a Private Key, which may compromise cryptographic security and sensitive data encryption.

25) **[HIGH] private-key**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/sacp-prod-uat/nginx/conf/ca/wildcard_bdo_com_cn.key` L1:1
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Identified a Private Key, which may compromise cryptographic security and sensitive data encryption.

## P1（安全整改，建议纳入迭代）：安全规则告警（semgrep）

1) **[WARNING] generic.html-templates.security.unquoted-attribute-var.unquoted-attribute-var**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/Faith/src/main/Faith/bdolx/tpl/form/combo.html` L2:3
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a unquoted template variable as an attribute. If unquoted, a malicious actor could inject custom JavaScript handlers. To fix this, add quotes around the template expression, like this: "{{ expr }}".

2) **[WARNING] generic.html-templates.security.unquoted-attribute-var.unquoted-attribute-var**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/Faith/src/main/Faith/bdolx/tpl/form/combo.html` L15:7
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a unquoted template variable as an attribute. If unquoted, a malicious actor could inject custom JavaScript handlers. To fix this, add quotes around the template expression, like this: "{{ expr }}".

3) **[WARNING] generic.html-templates.security.unquoted-attribute-var.unquoted-attribute-var**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/Faith/src/main/Faith/bdolx/tpl/form/combo.html` L16:7
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a unquoted template variable as an attribute. If unquoted, a malicious actor could inject custom JavaScript handlers. To fix this, add quotes around the template expression, like this: "{{ expr }}".

4) **[WARNING] generic.html-templates.security.unquoted-attribute-var.unquoted-attribute-var**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/Faith/src/main/Faith/bdolx/tpl/form/input.html` L2:3
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a unquoted template variable as an attribute. If unquoted, a malicious actor could inject custom JavaScript handlers. To fix this, add quotes around the template expression, like this: "{{ expr }}".

5) **[WARNING] generic.html-templates.security.unquoted-attribute-var.unquoted-attribute-var**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/Faith/src/main/Faith/bdolx/tpl/form/input.html` L14:4
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a unquoted template variable as an attribute. If unquoted, a malicious actor could inject custom JavaScript handlers. To fix this, add quotes around the template expression, like this: "{{ expr }}".

6) **[WARNING] generic.html-templates.security.unquoted-attribute-var.unquoted-attribute-var**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/Faith/src/main/Faith/bdolx/tpl/form/input.html` L15:4
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a unquoted template variable as an attribute. If unquoted, a malicious actor could inject custom JavaScript handlers. To fix this, add quotes around the template expression, like this: "{{ expr }}".

7) **[WARNING] generic.html-templates.security.unquoted-attribute-var.unquoted-attribute-var**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/Faith/src/main/Faith/bdolx/tpl/form/input2.html` L3:4
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a unquoted template variable as an attribute. If unquoted, a malicious actor could inject custom JavaScript handlers. To fix this, add quotes around the template expression, like this: "{{ expr }}".

8) **[WARNING] generic.html-templates.security.unquoted-attribute-var.unquoted-attribute-var**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/Faith/src/main/Faith/bdolx/tpl/form/input2.html` L10:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a unquoted template variable as an attribute. If unquoted, a malicious actor could inject custom JavaScript handlers. To fix this, add quotes around the template expression, like this: "{{ expr }}".

9) **[WARNING] generic.html-templates.security.unquoted-attribute-var.unquoted-attribute-var**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/Faith/src/main/Faith/bdolx/tpl/form/input2.html` L11:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a unquoted template variable as an attribute. If unquoted, a malicious actor could inject custom JavaScript handlers. To fix this, add quotes around the template expression, like this: "{{ expr }}".

10) **[WARNING] generic.html-templates.security.unquoted-attribute-var.unquoted-attribute-var**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/Faith/src/main/Faith/bdolx/tpl/form/treecombo.html` L2:3
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a unquoted template variable as an attribute. If unquoted, a malicious actor could inject custom JavaScript handlers. To fix this, add quotes around the template expression, like this: "{{ expr }}".

11) **[WARNING] generic.html-templates.security.unquoted-attribute-var.unquoted-attribute-var**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/Faith/src/main/Faith/bdolx/tpl/form/treecombo.html` L15:7
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a unquoted template variable as an attribute. If unquoted, a malicious actor could inject custom JavaScript handlers. To fix this, add quotes around the template expression, like this: "{{ expr }}".

12) **[WARNING] generic.html-templates.security.unquoted-attribute-var.unquoted-attribute-var**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/Faith/src/main/Faith/bdolx/tpl/form/treecombo.html` L16:7
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a unquoted template variable as an attribute. If unquoted, a malicious actor could inject custom JavaScript handlers. To fix this, add quotes around the template expression, like this: "{{ expr }}".

13) **[WARNING] generic.html-templates.security.unquoted-attribute-var.unquoted-attribute-var**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/Faith/src/main/Faith/ote/html/oteConfDetail.html` L30:14
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a unquoted template variable as an attribute. If unquoted, a malicious actor could inject custom JavaScript handlers. To fix this, add quotes around the template expression, like this: "{{ expr }}".

14) **[WARNING] generic.html-templates.security.unquoted-attribute-var.unquoted-attribute-var**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/Faith/src/main/Faith/ote/html/oteConfDetail.html` L94:14
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a unquoted template variable as an attribute. If unquoted, a malicious actor could inject custom JavaScript handlers. To fix this, add quotes around the template expression, like this: "{{ expr }}".

15) **[WARNING] generic.html-templates.security.unquoted-attribute-var.unquoted-attribute-var**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/Faith/src/main/Faith/ote/html/oteConfDetail.html` L107:14
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a unquoted template variable as an attribute. If unquoted, a malicious actor could inject custom JavaScript handlers. To fix this, add quotes around the template expression, like this: "{{ expr }}".

16) **[WARNING] generic.nginx.security.header-redefinition.header-redefinition**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/nginx_ex_prod/conf/conf.d/static-web.conf` L43:9
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：The 'add_header' directive is called in a 'location' block after headers have been set at the server block. Calling 'add_header' in the location block will actually overwrite the headers defined in the server block, no matter which headers are set. To fix this, explicitly set all headers or set all headers in the server block.

17) **[WARNING] generic.nginx.security.header-redefinition.header-redefinition**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/nginx_ex_prod/conf/conf.d/static-web.conf` L52:9
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：The 'add_header' directive is called in a 'location' block after headers have been set at the server block. Calling 'add_header' in the location block will actually overwrite the headers defined in the server block, no matter which headers are set. To fix this, explicitly set all headers or set all headers in the server block.

18) **[WARNING] generic.nginx.security.header-redefinition.header-redefinition**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/nginx_test_prod/conf/conf.d/static-web.conf` L43:9
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：The 'add_header' directive is called in a 'location' block after headers have been set at the server block. Calling 'add_header' in the location block will actually overwrite the headers defined in the server block, no matter which headers are set. To fix this, explicitly set all headers or set all headers in the server block.

19) **[WARNING] generic.nginx.security.header-redefinition.header-redefinition**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/nginx_test_prod/conf/conf.d/static-web.conf` L52:9
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：The 'add_header' directive is called in a 'location' block after headers have been set at the server block. Calling 'add_header' in the location block will actually overwrite the headers defined in the server block, no matter which headers are set. To fix this, explicitly set all headers or set all headers in the server block.

20) **[WARNING] generic.nginx.security.header-redefinition.header-redefinition**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/sacp-prod-uat/nginx/conf/conf.d/static-web.bdo.com.cn.conf` L43:9
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：The 'add_header' directive is called in a 'location' block after headers have been set at the server block. Calling 'add_header' in the location block will actually overwrite the headers defined in the server block, no matter which headers are set. To fix this, explicitly set all headers or set all headers in the server block.

21) **[WARNING] generic.nginx.security.header-redefinition.header-redefinition**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/sacp-prod-uat/nginx/conf/conf.d/static-web.bdo.com.cn.conf` L52:9
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：The 'add_header' directive is called in a 'location' block after headers have been set at the server block. Calling 'add_header' in the location block will actually overwrite the headers defined in the server block, no matter which headers are set. To fix this, explicitly set all headers or set all headers in the server block.

22) **[WARNING] generic.nginx.security.insecure-redirect.insecure-redirect**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/nginx_ex_prod/conf/conf.d/subconf/sacp.conf` L4:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected an insecure redirect in this nginx configuration. If no scheme is specified, nginx will forward the request with the incoming scheme. This could result in unencrypted communications. To fix this, include the 'https' scheme.

23) **[WARNING] generic.nginx.security.insecure-redirect.insecure-redirect**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/nginx_test_prod/conf/conf.d/subconf/sacp.conf` L4:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected an insecure redirect in this nginx configuration. If no scheme is specified, nginx will forward the request with the incoming scheme. This could result in unencrypted communications. To fix this, include the 'https' scheme.

24) **[WARNING] generic.nginx.security.insecure-redirect.insecure-redirect**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/sacp-prod-uat/nginx/conf/conf.d/subconf/sacp.conf` L4:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected an insecure redirect in this nginx configuration. If no scheme is specified, nginx will forward the request with the incoming scheme. This could result in unencrypted communications. To fix this, include the 'https' scheme.

25) **[WARNING] generic.nginx.security.insecure-redirect.insecure-redirect**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/sacp-prod-uat/nginx/conf/conf.d/subconf_temp/sacp.conf` L4:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected an insecure redirect in this nginx configuration. If no scheme is specified, nginx will forward the request with the incoming scheme. This could result in unencrypted communications. To fix this, include the 'https' scheme.

26) **[WARNING] generic.nginx.security.missing-internal.missing-internal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/nginx_ex_prod/conf/conf.d/subconf/sacp.conf` L89:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：This location block contains a 'proxy_pass' directive but does not contain the 'internal' directive. The 'internal' directive restricts access to this location to internal requests. Without 'internal', an attacker could use your server for server-side request forgeries (SSRF). Include the 'internal' directive in this block to limit exposure.

27) **[WARNING] generic.nginx.security.missing-internal.missing-internal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/nginx_ex_prod/conf/conf.d/subconf/sacp.conf` L110:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：This location block contains a 'proxy_pass' directive but does not contain the 'internal' directive. The 'internal' directive restricts access to this location to internal requests. Without 'internal', an attacker could use your server for server-side request forgeries (SSRF). Include the 'internal' directive in this block to limit exposure.

28) **[WARNING] generic.nginx.security.missing-internal.missing-internal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/nginx_ex_prod/conf/conf.d/subconf/sacp.conf` L126:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：This location block contains a 'proxy_pass' directive but does not contain the 'internal' directive. The 'internal' directive restricts access to this location to internal requests. Without 'internal', an attacker could use your server for server-side request forgeries (SSRF). Include the 'internal' directive in this block to limit exposure.

29) **[WARNING] generic.nginx.security.missing-internal.missing-internal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/nginx_ex_prod/conf/conf.d/subconf/sacp.conf` L147:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：This location block contains a 'proxy_pass' directive but does not contain the 'internal' directive. The 'internal' directive restricts access to this location to internal requests. Without 'internal', an attacker could use your server for server-side request forgeries (SSRF). Include the 'internal' directive in this block to limit exposure.

30) **[WARNING] generic.nginx.security.missing-internal.missing-internal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/nginx_ex_prod/conf/conf.d/subconf/sacp.conf` L200:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：This location block contains a 'proxy_pass' directive but does not contain the 'internal' directive. The 'internal' directive restricts access to this location to internal requests. Without 'internal', an attacker could use your server for server-side request forgeries (SSRF). Include the 'internal' directive in this block to limit exposure.

31) **[WARNING] generic.nginx.security.missing-internal.missing-internal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/nginx_ex_prod/conf/conf.d/subconf/sacp.conf` L221:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：This location block contains a 'proxy_pass' directive but does not contain the 'internal' directive. The 'internal' directive restricts access to this location to internal requests. Without 'internal', an attacker could use your server for server-side request forgeries (SSRF). Include the 'internal' directive in this block to limit exposure.

32) **[WARNING] generic.nginx.security.missing-internal.missing-internal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/nginx_ex_prod/conf/conf.d/subconf/sacp.conf` L237:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：This location block contains a 'proxy_pass' directive but does not contain the 'internal' directive. The 'internal' directive restricts access to this location to internal requests. Without 'internal', an attacker could use your server for server-side request forgeries (SSRF). Include the 'internal' directive in this block to limit exposure.

33) **[WARNING] generic.nginx.security.missing-internal.missing-internal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/nginx_ex_prod/conf/conf.d/subconf/sacp.conf` L258:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：This location block contains a 'proxy_pass' directive but does not contain the 'internal' directive. The 'internal' directive restricts access to this location to internal requests. Without 'internal', an attacker could use your server for server-side request forgeries (SSRF). Include the 'internal' directive in this block to limit exposure.

34) **[WARNING] generic.nginx.security.missing-internal.missing-internal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/nginx_test_prod/conf/conf.d/subconf/sacp.conf` L81:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：This location block contains a 'proxy_pass' directive but does not contain the 'internal' directive. The 'internal' directive restricts access to this location to internal requests. Without 'internal', an attacker could use your server for server-side request forgeries (SSRF). Include the 'internal' directive in this block to limit exposure.

35) **[WARNING] generic.nginx.security.missing-internal.missing-internal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/nginx_test_prod/conf/conf.d/subconf/sacp.conf` L96:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：This location block contains a 'proxy_pass' directive but does not contain the 'internal' directive. The 'internal' directive restricts access to this location to internal requests. Without 'internal', an attacker could use your server for server-side request forgeries (SSRF). Include the 'internal' directive in this block to limit exposure.

36) **[WARNING] generic.nginx.security.missing-internal.missing-internal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/nginx_test_prod/conf/conf.d/subconf/sacp.conf` L137:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：This location block contains a 'proxy_pass' directive but does not contain the 'internal' directive. The 'internal' directive restricts access to this location to internal requests. Without 'internal', an attacker could use your server for server-side request forgeries (SSRF). Include the 'internal' directive in this block to limit exposure.

37) **[WARNING] generic.nginx.security.missing-internal.missing-internal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/nginx_test_prod/conf/conf.d/subconf/sacp.conf` L158:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：This location block contains a 'proxy_pass' directive but does not contain the 'internal' directive. The 'internal' directive restricts access to this location to internal requests. Without 'internal', an attacker could use your server for server-side request forgeries (SSRF). Include the 'internal' directive in this block to limit exposure.

38) **[WARNING] generic.nginx.security.missing-internal.missing-internal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/sacp-prod-uat/nginx/conf/conf.d/subconf/sacp.conf` L40:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：This location block contains a 'proxy_pass' directive but does not contain the 'internal' directive. The 'internal' directive restricts access to this location to internal requests. Without 'internal', an attacker could use your server for server-side request forgeries (SSRF). Include the 'internal' directive in this block to limit exposure.

39) **[WARNING] generic.nginx.security.missing-internal.missing-internal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/sacp-prod-uat/nginx/conf/conf.d/subconf/sacp.conf` L56:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：This location block contains a 'proxy_pass' directive but does not contain the 'internal' directive. The 'internal' directive restricts access to this location to internal requests. Without 'internal', an attacker could use your server for server-side request forgeries (SSRF). Include the 'internal' directive in this block to limit exposure.

40) **[WARNING] generic.nginx.security.missing-internal.missing-internal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/sacp-prod-uat/nginx/conf/conf.d/subconf/sacp.conf` L88:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：This location block contains a 'proxy_pass' directive but does not contain the 'internal' directive. The 'internal' directive restricts access to this location to internal requests. Without 'internal', an attacker could use your server for server-side request forgeries (SSRF). Include the 'internal' directive in this block to limit exposure.

41) **[WARNING] generic.nginx.security.missing-internal.missing-internal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/sacp-prod-uat/nginx/conf/conf.d/subconf/sacp.conf` L104:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：This location block contains a 'proxy_pass' directive but does not contain the 'internal' directive. The 'internal' directive restricts access to this location to internal requests. Without 'internal', an attacker could use your server for server-side request forgeries (SSRF). Include the 'internal' directive in this block to limit exposure.

42) **[WARNING] generic.nginx.security.missing-internal.missing-internal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/sacp-prod-uat/nginx/conf/conf.d/subconf_temp/sacp.conf` L89:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：This location block contains a 'proxy_pass' directive but does not contain the 'internal' directive. The 'internal' directive restricts access to this location to internal requests. Without 'internal', an attacker could use your server for server-side request forgeries (SSRF). Include the 'internal' directive in this block to limit exposure.

43) **[WARNING] generic.nginx.security.missing-internal.missing-internal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/sacp-prod-uat/nginx/conf/conf.d/subconf_temp/sacp.conf` L110:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：This location block contains a 'proxy_pass' directive but does not contain the 'internal' directive. The 'internal' directive restricts access to this location to internal requests. Without 'internal', an attacker could use your server for server-side request forgeries (SSRF). Include the 'internal' directive in this block to limit exposure.

44) **[WARNING] generic.nginx.security.missing-internal.missing-internal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/sacp-prod-uat/nginx/conf/conf.d/subconf_temp/sacp.conf` L126:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：This location block contains a 'proxy_pass' directive but does not contain the 'internal' directive. The 'internal' directive restricts access to this location to internal requests. Without 'internal', an attacker could use your server for server-side request forgeries (SSRF). Include the 'internal' directive in this block to limit exposure.

45) **[WARNING] generic.nginx.security.missing-internal.missing-internal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/sacp-prod-uat/nginx/conf/conf.d/subconf_temp/sacp.conf` L147:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：This location block contains a 'proxy_pass' directive but does not contain the 'internal' directive. The 'internal' directive restricts access to this location to internal requests. Without 'internal', an attacker could use your server for server-side request forgeries (SSRF). Include the 'internal' directive in this block to limit exposure.

46) **[WARNING] generic.nginx.security.missing-internal.missing-internal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/sacp-prod-uat/nginx/conf/conf.d/subconf_temp/sacp.conf` L200:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：This location block contains a 'proxy_pass' directive but does not contain the 'internal' directive. The 'internal' directive restricts access to this location to internal requests. Without 'internal', an attacker could use your server for server-side request forgeries (SSRF). Include the 'internal' directive in this block to limit exposure.

47) **[WARNING] generic.nginx.security.missing-internal.missing-internal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/sacp-prod-uat/nginx/conf/conf.d/subconf_temp/sacp.conf` L221:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：This location block contains a 'proxy_pass' directive but does not contain the 'internal' directive. The 'internal' directive restricts access to this location to internal requests. Without 'internal', an attacker could use your server for server-side request forgeries (SSRF). Include the 'internal' directive in this block to limit exposure.

48) **[WARNING] generic.nginx.security.missing-internal.missing-internal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/sacp-prod-uat/nginx/conf/conf.d/subconf_temp/sacp.conf` L237:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：This location block contains a 'proxy_pass' directive but does not contain the 'internal' directive. The 'internal' directive restricts access to this location to internal requests. Without 'internal', an attacker could use your server for server-side request forgeries (SSRF). Include the 'internal' directive in this block to limit exposure.

49) **[WARNING] generic.nginx.security.missing-internal.missing-internal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-middleware/docker/sacp-prod-uat/nginx/conf/conf.d/subconf_temp/sacp.conf` L258:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：This location block contains a 'proxy_pass' directive but does not contain the 'internal' directive. The 'internal' directive restricts access to this location to internal requests. Without 'internal', an attacker could use your server for server-side request forgeries (SSRF). Include the 'internal' directive in this block to limit exposure.

50) **[WARNING] java.lang.security.audit.cbc-padding-oracle.cbc-padding-oracle**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-admin/faith-admin-common/src/main/java/cn/com/bdo/base/security/CryptoTools.java` L186:35
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Using CBC with PKCS5Padding is susceptible to padding oracle attacks. A malicious actor could discern the difference between plaintext with valid or invalid padding. Further, CBC mode does not include any integrity checks. Use 'AES/GCM/NoPadding' instead.

51) **[WARNING] java.lang.security.audit.cbc-padding-oracle.cbc-padding-oracle**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-admin/faith-admin-common/src/main/java/cn/com/bdo/base/security/CryptoTools.java` L205:35
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Using CBC with PKCS5Padding is susceptible to padding oracle attacks. A malicious actor could discern the difference between plaintext with valid or invalid padding. Further, CBC mode does not include any integrity checks. Use 'AES/GCM/NoPadding' instead.

52) **[WARNING] java.lang.security.audit.cbc-padding-oracle.cbc-padding-oracle**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-admin/faith-admin-common/src/main/java/cn/com/bdo/base/security/CryptoTools.java` L223:35
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Using CBC with PKCS5Padding is susceptible to padding oracle attacks. A malicious actor could discern the difference between plaintext with valid or invalid padding. Further, CBC mode does not include any integrity checks. Use 'AES/GCM/NoPadding' instead.

53) **[WARNING] java.lang.security.audit.cbc-padding-oracle.cbc-padding-oracle**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-admin/faith-admin-common/src/main/java/cn/com/bdo/base/security/CryptoTools.java` L241:35
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Using CBC with PKCS5Padding is susceptible to padding oracle attacks. A malicious actor could discern the difference between plaintext with valid or invalid padding. Further, CBC mode does not include any integrity checks. Use 'AES/GCM/NoPadding' instead.

54) **[WARNING] java.lang.security.audit.cbc-padding-oracle.cbc-padding-oracle**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-common/faith-common-base/src/main/java/cn/com/bdo/common/security/CryptoTools.java` L178:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Using CBC with PKCS5Padding is susceptible to padding oracle attacks. A malicious actor could discern the difference between plaintext with valid or invalid padding. Further, CBC mode does not include any integrity checks. Use 'AES/GCM/NoPadding' instead.

55) **[WARNING] java.lang.security.audit.cbc-padding-oracle.cbc-padding-oracle**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-common/faith-common-base/src/main/java/cn/com/bdo/common/security/CryptoTools.java` L212:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Using CBC with PKCS5Padding is susceptible to padding oracle attacks. A malicious actor could discern the difference between plaintext with valid or invalid padding. Further, CBC mode does not include any integrity checks. Use 'AES/GCM/NoPadding' instead.

56) **[WARNING] java.lang.security.audit.cbc-padding-oracle.cbc-padding-oracle**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-common/faith-common-base/src/main/java/cn/com/bdo/common/security/CryptoTools.java` L230:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Using CBC with PKCS5Padding is susceptible to padding oracle attacks. A malicious actor could discern the difference between plaintext with valid or invalid padding. Further, CBC mode does not include any integrity checks. Use 'AES/GCM/NoPadding' instead.

57) **[WARNING] java.lang.security.audit.cbc-padding-oracle.cbc-padding-oracle**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-common/faith-common-base/src/main/java/cn/com/bdo/common/security/CryptoTools.java` L248:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Using CBC with PKCS5Padding is susceptible to padding oracle attacks. A malicious actor could discern the difference between plaintext with valid or invalid padding. Further, CBC mode does not include any integrity checks. Use 'AES/GCM/NoPadding' instead.

58) **[WARNING] java.lang.security.audit.cbc-padding-oracle.cbc-padding-oracle**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-common/faith-common-base/src/main/java/cn/com/bdo/common/utils/AesUtils.java` L27:45
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Using CBC with PKCS5Padding is susceptible to padding oracle attacks. A malicious actor could discern the difference between plaintext with valid or invalid padding. Further, CBC mode does not include any integrity checks. Use 'AES/GCM/NoPadding' instead.

59) **[WARNING] java.lang.security.audit.cbc-padding-oracle.cbc-padding-oracle**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-common/faith-common-base/src/main/java/cn/com/bdo/common/utils/AesUtils.java` L47:45
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Using CBC with PKCS5Padding is susceptible to padding oracle attacks. A malicious actor could discern the difference between plaintext with valid or invalid padding. Further, CBC mode does not include any integrity checks. Use 'AES/GCM/NoPadding' instead.

60) **[WARNING] java.lang.security.audit.cbc-padding-oracle.cbc-padding-oracle**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-core-biz/faith-core-biz-impl/src/main/java/cn/com/bdo/azure/utils/AESCBCUtils.java` L135:52
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Using CBC with PKCS5Padding is susceptible to padding oracle attacks. A malicious actor could discern the difference between plaintext with valid or invalid padding. Further, CBC mode does not include any integrity checks. Use 'AES/GCM/NoPadding' instead.

61) **[WARNING] java.lang.security.audit.cbc-padding-oracle.cbc-padding-oracle**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-core-biz/faith-core-biz-impl/src/main/java/cn/com/bdo/azure/utils/AESCBCUtils.java` L177:52
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Using CBC with PKCS5Padding is susceptible to padding oracle attacks. A malicious actor could discern the difference between plaintext with valid or invalid padding. Further, CBC mode does not include any integrity checks. Use 'AES/GCM/NoPadding' instead.

62) **[WARNING] java.lang.security.audit.cbc-padding-oracle.cbc-padding-oracle**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-jacob2/faith-jacob-server/src/main/java/cn/com/bdo/jacob/utils/CryptoTools.java` L193:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Using CBC with PKCS5Padding is susceptible to padding oracle attacks. A malicious actor could discern the difference between plaintext with valid or invalid padding. Further, CBC mode does not include any integrity checks. Use 'AES/GCM/NoPadding' instead.

63) **[WARNING] java.lang.security.audit.cbc-padding-oracle.cbc-padding-oracle**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-jacob2/faith-jacob-server/src/main/java/cn/com/bdo/jacob/utils/CryptoTools.java` L212:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Using CBC with PKCS5Padding is susceptible to padding oracle attacks. A malicious actor could discern the difference between plaintext with valid or invalid padding. Further, CBC mode does not include any integrity checks. Use 'AES/GCM/NoPadding' instead.

64) **[WARNING] java.lang.security.audit.cbc-padding-oracle.cbc-padding-oracle**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-jacob2/faith-jacob-server/src/main/java/cn/com/bdo/jacob/utils/CryptoTools.java` L230:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Using CBC with PKCS5Padding is susceptible to padding oracle attacks. A malicious actor could discern the difference between plaintext with valid or invalid padding. Further, CBC mode does not include any integrity checks. Use 'AES/GCM/NoPadding' instead.

65) **[WARNING] java.lang.security.audit.cbc-padding-oracle.cbc-padding-oracle**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-jacob2/faith-jacob-server/src/main/java/cn/com/bdo/jacob/utils/CryptoTools.java` L248:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Using CBC with PKCS5Padding is susceptible to padding oracle attacks. A malicious actor could discern the difference between plaintext with valid or invalid padding. Further, CBC mode does not include any integrity checks. Use 'AES/GCM/NoPadding' instead.

66) **[WARNING] java.lang.security.audit.cbc-padding-oracle.cbc-padding-oracle**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-sync-test-env/faith-sync-test-env-provider/src/main/java/cn/com/bdo/sync/utils/CryptoTools.java` L193:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Using CBC with PKCS5Padding is susceptible to padding oracle attacks. A malicious actor could discern the difference between plaintext with valid or invalid padding. Further, CBC mode does not include any integrity checks. Use 'AES/GCM/NoPadding' instead.

67) **[WARNING] java.lang.security.audit.cbc-padding-oracle.cbc-padding-oracle**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-sync-test-env/faith-sync-test-env-provider/src/main/java/cn/com/bdo/sync/utils/CryptoTools.java` L212:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Using CBC with PKCS5Padding is susceptible to padding oracle attacks. A malicious actor could discern the difference between plaintext with valid or invalid padding. Further, CBC mode does not include any integrity checks. Use 'AES/GCM/NoPadding' instead.

68) **[WARNING] java.lang.security.audit.cbc-padding-oracle.cbc-padding-oracle**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-sync-test-env/faith-sync-test-env-provider/src/main/java/cn/com/bdo/sync/utils/CryptoTools.java` L230:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Using CBC with PKCS5Padding is susceptible to padding oracle attacks. A malicious actor could discern the difference between plaintext with valid or invalid padding. Further, CBC mode does not include any integrity checks. Use 'AES/GCM/NoPadding' instead.

69) **[WARNING] java.lang.security.audit.cbc-padding-oracle.cbc-padding-oracle**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-sync-test-env/faith-sync-test-env-provider/src/main/java/cn/com/bdo/sync/utils/CryptoTools.java` L248:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Using CBC with PKCS5Padding is susceptible to padding oracle attacks. A malicious actor could discern the difference between plaintext with valid or invalid padding. Further, CBC mode does not include any integrity checks. Use 'AES/GCM/NoPadding' instead.

70) **[WARNING] java.lang.security.audit.cookie-missing-httponly.cookie-missing-httponly**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/Faith/src/main/java/cn/com/bdo/aptView/action/AptViewAction.java` L570:17
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：A cookie was detected without setting the 'HttpOnly' flag. The 'HttpOnly' flag for cookies instructs the browser to forbid client-side scripts from reading the cookie. Set the 'HttpOnly' flag by calling 'cookie.setHttpOnly(true);'

71) **[WARNING] java.lang.security.audit.cookie-missing-httponly.cookie-missing-httponly**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-core-biz/faith-core-biz-impl/src/main/java/cn/com/bdo/cpBase/action/AdminLoginAction.java` L105:21
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：A cookie was detected without setting the 'HttpOnly' flag. The 'HttpOnly' flag for cookies instructs the browser to forbid client-side scripts from reading the cookie. Set the 'HttpOnly' flag by calling 'cookie.setHttpOnly(true);'

72) **[WARNING] java.lang.security.audit.cookie-missing-httponly.cookie-missing-httponly**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-core-biz/faith-core-biz-impl/src/main/java/cn/com/bdo/cpBase/action/LoginAction.java` L1206:17
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：A cookie was detected without setting the 'HttpOnly' flag. The 'HttpOnly' flag for cookies instructs the browser to forbid client-side scripts from reading the cookie. Set the 'HttpOnly' flag by calling 'cookie.setHttpOnly(true);'

73) **[WARNING] java.lang.security.audit.cookie-missing-httponly.cookie-missing-httponly**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-core-biz/faith-core-biz-impl/src/main/java/cn/com/bdo/cpBase/action/LoginAppAction.java` L708:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：A cookie was detected without setting the 'HttpOnly' flag. The 'HttpOnly' flag for cookies instructs the browser to forbid client-side scripts from reading the cookie. Set the 'HttpOnly' flag by calling 'cookie.setHttpOnly(true);'

74) **[WARNING] java.lang.security.audit.cookie-missing-httponly.cookie-missing-httponly**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-core-biz/faith-core-biz-impl/src/main/java/cn/com/bdo/cpBase/action/LoginAppAdminAction.java` L707:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：A cookie was detected without setting the 'HttpOnly' flag. The 'HttpOnly' flag for cookies instructs the browser to forbid client-side scripts from reading the cookie. Set the 'HttpOnly' flag by calling 'cookie.setHttpOnly(true);'

75) **[WARNING] java.lang.security.audit.cookie-missing-httponly.cookie-missing-httponly**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-core-biz/faith-core-biz-impl/src/main/java/cn/com/bdo/cpBase/action/LoginCusAction.java` L650:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：A cookie was detected without setting the 'HttpOnly' flag. The 'HttpOnly' flag for cookies instructs the browser to forbid client-side scripts from reading the cookie. Set the 'HttpOnly' flag by calling 'cookie.setHttpOnly(true);'

76) **[WARNING] java.lang.security.audit.cookie-missing-httponly.cookie-missing-httponly**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-core-biz/faith-core-biz-impl/src/main/java/cn/com/bdo/cpBase/action/LoginOutUserAction.java` L543:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：A cookie was detected without setting the 'HttpOnly' flag. The 'HttpOnly' flag for cookies instructs the browser to forbid client-side scripts from reading the cookie. Set the 'HttpOnly' flag by calling 'cookie.setHttpOnly(true);'

77) **[WARNING] java.lang.security.audit.cookie-missing-secure-flag.cookie-missing-secure-flag**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/Faith/src/main/java/cn/com/bdo/aptView/action/AptViewAction.java` L570:17
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：A cookie was detected without setting the 'secure' flag. The 'secure' flag for cookies prevents the client from transmitting the cookie over insecure channels such as HTTP. Set the 'secure' flag by calling 'cookie.setSecure(true);'

78) **[WARNING] java.lang.security.audit.cookie-missing-secure-flag.cookie-missing-secure-flag**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-core-biz/faith-core-biz-impl/src/main/java/cn/com/bdo/cpBase/action/AdminLoginAction.java` L105:21
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：A cookie was detected without setting the 'secure' flag. The 'secure' flag for cookies prevents the client from transmitting the cookie over insecure channels such as HTTP. Set the 'secure' flag by calling 'cookie.setSecure(true);'

79) **[WARNING] java.lang.security.audit.cookie-missing-secure-flag.cookie-missing-secure-flag**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-core-biz/faith-core-biz-impl/src/main/java/cn/com/bdo/cpBase/action/LoginAction.java` L1206:17
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：A cookie was detected without setting the 'secure' flag. The 'secure' flag for cookies prevents the client from transmitting the cookie over insecure channels such as HTTP. Set the 'secure' flag by calling 'cookie.setSecure(true);'

80) **[WARNING] java.lang.security.audit.cookie-missing-secure-flag.cookie-missing-secure-flag**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-core-biz/faith-core-biz-impl/src/main/java/cn/com/bdo/cpBase/action/LoginAppAction.java` L708:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：A cookie was detected without setting the 'secure' flag. The 'secure' flag for cookies prevents the client from transmitting the cookie over insecure channels such as HTTP. Set the 'secure' flag by calling 'cookie.setSecure(true);'

81) **[WARNING] java.lang.security.audit.cookie-missing-secure-flag.cookie-missing-secure-flag**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-core-biz/faith-core-biz-impl/src/main/java/cn/com/bdo/cpBase/action/LoginAppAdminAction.java` L707:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：A cookie was detected without setting the 'secure' flag. The 'secure' flag for cookies prevents the client from transmitting the cookie over insecure channels such as HTTP. Set the 'secure' flag by calling 'cookie.setSecure(true);'

82) **[WARNING] java.lang.security.audit.cookie-missing-secure-flag.cookie-missing-secure-flag**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-core-biz/faith-core-biz-impl/src/main/java/cn/com/bdo/cpBase/action/LoginCusAction.java` L650:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：A cookie was detected without setting the 'secure' flag. The 'secure' flag for cookies prevents the client from transmitting the cookie over insecure channels such as HTTP. Set the 'secure' flag by calling 'cookie.setSecure(true);'

83) **[WARNING] java.lang.security.audit.cookie-missing-secure-flag.cookie-missing-secure-flag**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-core-biz/faith-core-biz-impl/src/main/java/cn/com/bdo/cpBase/action/LoginOutUserAction.java` L543:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：A cookie was detected without setting the 'secure' flag. The 'secure' flag for cookies prevents the client from transmitting the cookie over insecure channels such as HTTP. Set the 'secure' flag by calling 'cookie.setSecure(true);'

84) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-admin/faith-admin-common/src/main/java/cn/com/bdo/base/security/CryptoTools.java` L165:63
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

85) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-admin/faith-admin-common/src/main/java/cn/com/bdo/base/security/CryptoTools.java` L181:35
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

86) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-admin/faith-admin-common/src/main/java/cn/com/bdo/base/security/CryptoTools.java` L186:35
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

87) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-admin/faith-admin-common/src/main/java/cn/com/bdo/base/security/CryptoTools.java` L202:35
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

88) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-admin/faith-admin-common/src/main/java/cn/com/bdo/base/security/CryptoTools.java` L205:35
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

89) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-admin/faith-admin-common/src/main/java/cn/com/bdo/base/security/CryptoTools.java` L219:35
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

90) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-admin/faith-admin-common/src/main/java/cn/com/bdo/base/security/CryptoTools.java` L223:35
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

91) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-admin/faith-admin-common/src/main/java/cn/com/bdo/base/security/CryptoTools.java` L236:35
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

92) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-admin/faith-admin-common/src/main/java/cn/com/bdo/base/security/CryptoTools.java` L241:35
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

93) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-common/faith-common-base/src/main/java/cn/com/bdo/common/security/CryptoTools.java` L77:72
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

94) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-common/faith-common-base/src/main/java/cn/com/bdo/common/security/CryptoTools.java` L173:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

95) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-common/faith-common-base/src/main/java/cn/com/bdo/common/security/CryptoTools.java` L178:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

96) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-common/faith-common-base/src/main/java/cn/com/bdo/common/security/CryptoTools.java` L209:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

97) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-common/faith-common-base/src/main/java/cn/com/bdo/common/security/CryptoTools.java` L212:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

98) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-common/faith-common-base/src/main/java/cn/com/bdo/common/security/CryptoTools.java` L226:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

99) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-common/faith-common-base/src/main/java/cn/com/bdo/common/security/CryptoTools.java` L230:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

100) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-common/faith-common-base/src/main/java/cn/com/bdo/common/security/CryptoTools.java` L243:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

101) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-common/faith-common-base/src/main/java/cn/com/bdo/common/security/CryptoTools.java` L248:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

102) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-jacob2/faith-jacob-server/src/main/java/cn/com/bdo/jacob/utils/CryptoTools.java` L172:72
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

103) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-jacob2/faith-jacob-server/src/main/java/cn/com/bdo/jacob/utils/CryptoTools.java` L188:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

104) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-jacob2/faith-jacob-server/src/main/java/cn/com/bdo/jacob/utils/CryptoTools.java` L193:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

105) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-jacob2/faith-jacob-server/src/main/java/cn/com/bdo/jacob/utils/CryptoTools.java` L209:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

106) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-jacob2/faith-jacob-server/src/main/java/cn/com/bdo/jacob/utils/CryptoTools.java` L212:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

107) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-jacob2/faith-jacob-server/src/main/java/cn/com/bdo/jacob/utils/CryptoTools.java` L226:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

108) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-jacob2/faith-jacob-server/src/main/java/cn/com/bdo/jacob/utils/CryptoTools.java` L230:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

109) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-jacob2/faith-jacob-server/src/main/java/cn/com/bdo/jacob/utils/CryptoTools.java` L243:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

110) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-jacob2/faith-jacob-server/src/main/java/cn/com/bdo/jacob/utils/CryptoTools.java` L248:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

111) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-sync-test-env/faith-sync-test-env-provider/src/main/java/cn/com/bdo/sync/utils/CryptoTools.java` L172:72
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

112) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-sync-test-env/faith-sync-test-env-provider/src/main/java/cn/com/bdo/sync/utils/CryptoTools.java` L188:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

113) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-sync-test-env/faith-sync-test-env-provider/src/main/java/cn/com/bdo/sync/utils/CryptoTools.java` L193:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

114) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-sync-test-env/faith-sync-test-env-provider/src/main/java/cn/com/bdo/sync/utils/CryptoTools.java` L209:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

115) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-sync-test-env/faith-sync-test-env-provider/src/main/java/cn/com/bdo/sync/utils/CryptoTools.java` L212:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

116) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-sync-test-env/faith-sync-test-env-provider/src/main/java/cn/com/bdo/sync/utils/CryptoTools.java` L226:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

117) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-sync-test-env/faith-sync-test-env-provider/src/main/java/cn/com/bdo/sync/utils/CryptoTools.java` L230:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

118) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-sync-test-env/faith-sync-test-env-provider/src/main/java/cn/com/bdo/sync/utils/CryptoTools.java` L243:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

119) **[WARNING] java.lang.security.audit.crypto.des-is-deprecated.des-is-deprecated**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-sync-test-env/faith-sync-test-env-provider/src/main/java/cn/com/bdo/sync/utils/CryptoTools.java` L248:47
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：DES is considered deprecated. AES is the recommended cipher. Upgrade to use AES. See https://www.nist.gov/news-events/news/2005/06/nist-withdraws-outdated-data-encryption-standard for more information.

120) **[WARNING] java.lang.security.audit.crypto.unencrypted-socket.unencrypted-socket**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-core-biz/faith-core-biz-impl/src/main/java/cn/com/bdo/wind/service/WindToolService.java` L797:22
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected use of a Java socket that is not encrypted. As a result, the traffic could be read by an attacker intercepting the network traffic. Use an SSLSocket created by 'SSLSocketFactory' or 'SSLServerSocketFactory' instead.

121) **[WARNING] java.lang.security.audit.crypto.use-of-md5.use-of-md5**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-admin/faith-admin-common/src/main/java/cn/com/bdo/base/security/SecurityUtils.java` L52:53
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected MD5 hash algorithm which is considered insecure. MD5 is not collision resistant and is therefore not suitable as a cryptographic signature. Use HMAC instead.

122) **[WARNING] java.lang.security.audit.crypto.use-of-md5.use-of-md5**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-admin/faith-admin-common/src/main/java/cn/com/bdo/base/security/SecurityUtils.java` L81:40
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected MD5 hash algorithm which is considered insecure. MD5 is not collision resistant and is therefore not suitable as a cryptographic signature. Use HMAC instead.

123) **[WARNING] java.lang.security.audit.crypto.use-of-md5.use-of-md5**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-common/faith-common-base/src/main/java/cn/com/bdo/common/security/SecurityUtils.java` L51:62
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected MD5 hash algorithm which is considered insecure. MD5 is not collision resistant and is therefore not suitable as a cryptographic signature. Use HMAC instead.

124) **[WARNING] java.lang.security.audit.crypto.use-of-md5.use-of-md5**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-common/faith-common-base/src/main/java/cn/com/bdo/common/security/SecurityUtils.java` L84:52
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected MD5 hash algorithm which is considered insecure. MD5 is not collision resistant and is therefore not suitable as a cryptographic signature. Use HMAC instead.

125) **[ERROR] java.lang.security.audit.formatted-sql-string.formatted-sql-string**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-admin/faith-admin-common/src/main/java/cn/com/bdo/base/dao/GeneralDaoUtils.java` L2412:18
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a formatted string in a SQL statement. This could lead to SQL injection if variables in the SQL statement are not properly sanitized. Use a prepared statements (java.sql.PreparedStatement) instead. You can obtain a PreparedStatement using 'connection.prepareStatement'.

126) **[ERROR] java.lang.security.audit.formatted-sql-string.formatted-sql-string**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-admin/faith-admin-common/src/main/java/cn/com/bdo/base/dao/GeneralDaoUtils.java` L2464:13
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a formatted string in a SQL statement. This could lead to SQL injection if variables in the SQL statement are not properly sanitized. Use a prepared statements (java.sql.PreparedStatement) instead. You can obtain a PreparedStatement using 'connection.prepareStatement'.

127) **[ERROR] java.lang.security.audit.formatted-sql-string.formatted-sql-string**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-admin/faith-admin-common/src/main/java/cn/com/bdo/base/dao/GeneralDaoUtils.java` L2532:18
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a formatted string in a SQL statement. This could lead to SQL injection if variables in the SQL statement are not properly sanitized. Use a prepared statements (java.sql.PreparedStatement) instead. You can obtain a PreparedStatement using 'connection.prepareStatement'.

128) **[ERROR] java.lang.security.audit.formatted-sql-string.formatted-sql-string**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-admin/faith-admin-common/src/main/java/cn/com/bdo/base/dao/GeneralDaoUtils.java` L3029:13
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a formatted string in a SQL statement. This could lead to SQL injection if variables in the SQL statement are not properly sanitized. Use a prepared statements (java.sql.PreparedStatement) instead. You can obtain a PreparedStatement using 'connection.prepareStatement'.

129) **[ERROR] java.lang.security.audit.formatted-sql-string.formatted-sql-string**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-admin/faith-admin-common/src/main/java/cn/com/bdo/base/dao/GeneralDaoUtils.java` L3174:20
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a formatted string in a SQL statement. This could lead to SQL injection if variables in the SQL statement are not properly sanitized. Use a prepared statements (java.sql.PreparedStatement) instead. You can obtain a PreparedStatement using 'connection.prepareStatement'.

130) **[ERROR] java.lang.security.audit.formatted-sql-string.formatted-sql-string**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-admin/faith-admin-common/src/main/java/cn/com/bdo/base/dao/GeneralDaoUtils.java` L3229:20
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a formatted string in a SQL statement. This could lead to SQL injection if variables in the SQL statement are not properly sanitized. Use a prepared statements (java.sql.PreparedStatement) instead. You can obtain a PreparedStatement using 'connection.prepareStatement'.

131) **[ERROR] java.lang.security.audit.formatted-sql-string.formatted-sql-string**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-sync-test-env/faith-sync-test-env-provider/src/main/java/cn/com/bdo/sync/job/SyncDBTask.java` L140:35
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a formatted string in a SQL statement. This could lead to SQL injection if variables in the SQL statement are not properly sanitized. Use a prepared statements (java.sql.PreparedStatement) instead. You can obtain a PreparedStatement using 'connection.prepareStatement'.

132) **[WARNING] java.lang.security.audit.ldap-injection.ldap-injection**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-core-biz/faith-core-biz-impl/src/main/java/cn/com/bdo/cpBase/service/FaithLdapControl.java` L66:2
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected non-constant data passed into an LDAP query. If this data can be controlled by an external user, this is an LDAP injection. Ensure data passed to an LDAP query is not controllable; or properly sanitize the data.

133) **[WARNING] java.lang.security.audit.ldap-injection.ldap-injection**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-core-biz/faith-core-biz-impl/src/main/java/cn/com/bdo/cpBase/service/FaithLdapControl.java` L251:2
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected non-constant data passed into an LDAP query. If this data can be controlled by an external user, this is an LDAP injection. Ensure data passed to an LDAP query is not controllable; or properly sanitize the data.

134) **[WARNING] java.lang.security.audit.ldap-injection.ldap-injection**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-core/src/main/java/cn/com/bdo/base/ldap/LdapControl.java` L132:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected non-constant data passed into an LDAP query. If this data can be controlled by an external user, this is an LDAP injection. Ensure data passed to an LDAP query is not controllable; or properly sanitize the data.

135) **[WARNING] java.lang.security.audit.object-deserialization.object-deserialization**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-admin/faith-admin-common/src/main/java/cn/com/bdo/base/security/CryptoTools.java` L62:4
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Found object deserialization using ObjectInputStream. Deserializing entire Java objects is dangerous because malicious actors can create Java object streams with unintended consequences. Ensure that the objects being deserialized are not user-controlled. If this must be done, consider using HMACs to sign the data stream to make sure it is not tampered with, or consider only transmitting object fields and populating a new object.

136) **[WARNING] java.lang.security.audit.object-deserialization.object-deserialization**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-admin/faith-admin-common/src/main/java/cn/com/bdo/base/utils/BaseBeanUtils.java` L364:4
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Found object deserialization using ObjectInputStream. Deserializing entire Java objects is dangerous because malicious actors can create Java object streams with unintended consequences. Ensure that the objects being deserialized are not user-controlled. If this must be done, consider using HMACs to sign the data stream to make sure it is not tampered with, or consider only transmitting object fields and populating a new object.

137) **[WARNING] java.lang.security.audit.object-deserialization.object-deserialization**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-common/faith-common-base/src/main/java/cn/com/bdo/common/security/CryptoTools.java` L108:13
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Found object deserialization using ObjectInputStream. Deserializing entire Java objects is dangerous because malicious actors can create Java object streams with unintended consequences. Ensure that the objects being deserialized are not user-controlled. If this must be done, consider using HMACs to sign the data stream to make sure it is not tampered with, or consider only transmitting object fields and populating a new object.

138) **[WARNING] java.lang.security.audit.object-deserialization.object-deserialization**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-jacob2/faith-jacob-server/src/main/java/cn/com/bdo/jacob/utils/CryptoTools.java` L69:13
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Found object deserialization using ObjectInputStream. Deserializing entire Java objects is dangerous because malicious actors can create Java object streams with unintended consequences. Ensure that the objects being deserialized are not user-controlled. If this must be done, consider using HMACs to sign the data stream to make sure it is not tampered with, or consider only transmitting object fields and populating a new object.

139) **[WARNING] java.lang.security.audit.object-deserialization.object-deserialization**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-sync-test-env/faith-sync-test-env-provider/src/main/java/cn/com/bdo/sync/utils/CryptoTools.java` L69:13
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Found object deserialization using ObjectInputStream. Deserializing entire Java objects is dangerous because malicious actors can create Java object streams with unintended consequences. Ensure that the objects being deserialized are not user-controlled. If this must be done, consider using HMACs to sign the data stream to make sure it is not tampered with, or consider only transmitting object fields and populating a new object.

140) **[WARNING] java.lang.security.audit.permissive-cors.permissive-cors**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-core/src/main/java/cn/com/bdo/filter/CAFilter.java` L165:9
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：https://find-sec-bugs.github.io/bugs.htm#PERMISSIVE_CORS Permissive CORS policy will allow a malicious application to communicate with the victim application in an inappropriate way, leading to spoofing, data theft, relay and other attacks.

141) **[ERROR] java.lang.security.httpservlet-path-traversal.httpservlet-path-traversal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-admin/faith-admin-common/src/main/java/cn/com/bdo/base/utils/BaseExcel.java` L41:33
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a potential path traversal. A malicious actor could control the location of this file, to include going backwards in the directory with '../'. To address this, ensure that user-controlled variables in file paths are sanitized. You may also consider using a utility method such as org.apache.commons.io.FilenameUtils.getName(...) to only retrieve the file name from the path.

142) **[ERROR] java.lang.security.httpservlet-path-traversal.httpservlet-path-traversal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-admin/faith-admin-common/src/main/java/cn/com/bdo/base/utils/BaseExcel.java` L87:33
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a potential path traversal. A malicious actor could control the location of this file, to include going backwards in the directory with '../'. To address this, ensure that user-controlled variables in file paths are sanitized. You may also consider using a utility method such as org.apache.commons.io.FilenameUtils.getName(...) to only retrieve the file name from the path.

143) **[ERROR] java.lang.security.httpservlet-path-traversal.httpservlet-path-traversal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-core-biz/faith-core-biz-impl/src/main/java/cn/com/bdo/dgCenter/action/DgCenterAction.java` L285:34
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a potential path traversal. A malicious actor could control the location of this file, to include going backwards in the directory with '../'. To address this, ensure that user-controlled variables in file paths are sanitized. You may also consider using a utility method such as org.apache.commons.io.FilenameUtils.getName(...) to only retrieve the file name from the path.

144) **[ERROR] java.lang.security.httpservlet-path-traversal.httpservlet-path-traversal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-core-biz/faith-core-biz-impl/src/main/java/cn/com/bdo/dgCenter/action/DgCenterAction.java` L326:34
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a potential path traversal. A malicious actor could control the location of this file, to include going backwards in the directory with '../'. To address this, ensure that user-controlled variables in file paths are sanitized. You may also consider using a utility method such as org.apache.commons.io.FilenameUtils.getName(...) to only retrieve the file name from the path.

145) **[ERROR] java.lang.security.httpservlet-path-traversal.httpservlet-path-traversal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-core/src/main/java/cn/com/bdo/filter/MaintainFilter.java` L52:12
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a potential path traversal. A malicious actor could control the location of this file, to include going backwards in the directory with '../'. To address this, ensure that user-controlled variables in file paths are sanitized. You may also consider using a utility method such as org.apache.commons.io.FilenameUtils.getName(...) to only retrieve the file name from the path.

146) **[ERROR] java.lang.security.httpservlet-path-traversal.httpservlet-path-traversal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-core/src/main/java/cn/com/bdo/filter/MaintainFilter.java` L54:36
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a potential path traversal. A malicious actor could control the location of this file, to include going backwards in the directory with '../'. To address this, ensure that user-controlled variables in file paths are sanitized. You may also consider using a utility method such as org.apache.commons.io.FilenameUtils.getName(...) to only retrieve the file name from the path.

147) **[ERROR] java.lang.security.httpservlet-path-traversal.httpservlet-path-traversal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-core/src/main/java/cn/com/bdo/filter/MaintainFilter.java` L68:11
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a potential path traversal. A malicious actor could control the location of this file, to include going backwards in the directory with '../'. To address this, ensure that user-controlled variables in file paths are sanitized. You may also consider using a utility method such as org.apache.commons.io.FilenameUtils.getName(...) to only retrieve the file name from the path.

148) **[ERROR] java.lang.security.httpservlet-path-traversal.httpservlet-path-traversal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-core/src/main/java/cn/com/bdo/filter/MaintainFilter.java` L69:35
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a potential path traversal. A malicious actor could control the location of this file, to include going backwards in the directory with '../'. To address this, ensure that user-controlled variables in file paths are sanitized. You may also consider using a utility method such as org.apache.commons.io.FilenameUtils.getName(...) to only retrieve the file name from the path.

149) **[ERROR] java.lang.security.httpservlet-path-traversal.httpservlet-path-traversal**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-web/faith-web-impl/src/main/java/cn/com/bdo/web/controller/DgCenterController.java` L318:63
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a potential path traversal. A malicious actor could control the location of this file, to include going backwards in the directory with '../'. To address this, ensure that user-controlled variables in file paths are sanitized. You may also consider using a utility method such as org.apache.commons.io.FilenameUtils.getName(...) to only retrieve the file name from the path.

150) **[WARNING] java.spring.security.audit.spel-injection.spel-injection**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-common/faith-common-redis/src/main/java/cn/com/bdo/common/redis/utils/BdoSpringExpressionUtil.java` L29:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：A Spring expression is built with a dynamic value. The source of the value(s) should be verified to avoid that unfiltered values fall into this risky code evaluation.

151) **[WARNING] java.spring.security.audit.spel-injection.spel-injection**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-core/src/main/java/cn/com/bdo/base/aop/BaseDataCacheableAspect.java` L104:5
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：A Spring expression is built with a dynamic value. The source of the value(s) should be verified to avoid that unfiltered values fall into this risky code evaluation.

152) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-core-biz/faith-core-biz-impl/src/main/java/cn/com/bdo/controller/JsonController.java` L53:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

153) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-core-biz/faith-core-biz-impl/src/main/java/cn/com/bdo/controller/JsonController.java` L65:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

154) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EDocPublishController.java` L34:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

155) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EDocPublishController.java` L51:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

156) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocArchiveController.java` L28:3
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

157) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocArchiveController.java` L38:3
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

158) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L43:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

159) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L59:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

160) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L75:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

161) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L91:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

162) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L107:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

163) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L124:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

164) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L141:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

165) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L158:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

166) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L175:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

167) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L193:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

168) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L211:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

169) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L228:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

170) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L245:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

171) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L262:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

172) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L279:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

173) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L295:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

174) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L311:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

175) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L327:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

176) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L343:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

177) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L355:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

178) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L373:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

179) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L391:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

180) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L407:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

181) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L423:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

182) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L439:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

183) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L455:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

184) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L471:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

185) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L487:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

186) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L498:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

187) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L514:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

188) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L529:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

189) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocCloudFileController.java` L544:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

190) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocEventController.java` L51:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

191) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocEventController.java` L103:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

192) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocPermanentAuditController.java` L41:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

193) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocPermanentAuditController.java` L66:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

194) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocPermanentAuditController.java` L82:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

195) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocPermanentAuditController.java` L99:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

196) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocPermanentAuditController.java` L116:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

197) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocPermanentAuditController.java` L132:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

198) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocPermanentAuditController.java` L148:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

199) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocPermanentAuditController.java` L164:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

200) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocPermanentAuditController.java` L180:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

201) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocPmController.java` L36:3
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

202) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocPmController.java` L46:3
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

203) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocPmController.java` L56:3
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

204) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocPmController.java` L66:3
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

205) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-edoc/faith-edoc-provider/src/main/java/cn/com/bdo/edoc/controller/EdocPmController.java` L76:3
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

206) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-hb/faith-hb-provider/src/main/java/cn/com/bdo/controller/JsonController.java` L54:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

207) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-hb/faith-hb-provider/src/main/java/cn/com/bdo/controller/JsonController.java` L62:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

208) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-srv/faith-srv-common/src/main/java/cn/com/bdo/controller/JsonController.java` L56:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

209) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-srv/faith-srv-common/src/main/java/cn/com/bdo/controller/JsonController.java` L64:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

210) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te-bak/faith-te-provider/src/main/java/cn/com/bdo/te/controller/FileController.java` L68:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

211) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te-bak/faith-te-provider/src/main/java/cn/com/bdo/te/controller/FileController.java` L109:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

212) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te-bak/faith-te-provider/src/main/java/cn/com/bdo/te/controller/FileController.java` L145:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

213) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te-bak/faith-te-provider/src/main/java/cn/com/bdo/te/controller/TemplateEngineController.java` L67:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

214) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te-bak/faith-te-provider/src/main/java/cn/com/bdo/te/controller/TemplateEngineController.java` L74:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

215) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te-bak/faith-te-provider/src/main/java/cn/com/bdo/te/controller/TemplateEngineController.java` L80:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

216) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te-bak/faith-te-provider/src/main/java/cn/com/bdo/te/controller/TemplateEngineController.java` L86:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

217) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te-bak/faith-te-provider/src/main/java/cn/com/bdo/te/controller/TemplateEngineController.java` L92:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

218) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te-bak/faith-te-provider/src/main/java/cn/com/bdo/te/controller/TemplateEngineController.java` L104:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

219) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te-bak/faith-te-provider/src/main/java/cn/com/bdo/te/controller/TemplateEngineController.java` L110:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

220) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te-bak/faith-te-provider/src/main/java/cn/com/bdo/te/controller/TemplateEngineController.java` L116:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

221) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te-bak/faith-te-provider/src/main/java/cn/com/bdo/te/controller/TemplateEngineController.java` L122:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

222) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te-bak/faith-te-provider/src/main/java/cn/com/bdo/te/controller/TemplateEngineController.java` L127:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

223) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te-bak/faith-te-provider/src/main/java/cn/com/bdo/te/controller/TemplateEngineController.java` L139:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

224) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te-bak/faith-te-provider/src/main/java/cn/com/bdo/te/controller/TemplateEngineController.java` L160:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

225) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te-bak/faith-te-provider/src/main/java/cn/com/bdo/te/controller/TemplateEngineController.java` L173:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

226) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te-bak/faith-te-provider/src/main/java/cn/com/bdo/te/controller/TemplateGroupController.java` L56:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

227) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te/faith-te-provider/src/main/java/cn/com/bdo/te/controller/FileController.java` L67:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

228) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te/faith-te-provider/src/main/java/cn/com/bdo/te/controller/FileController.java` L108:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

229) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te/faith-te-provider/src/main/java/cn/com/bdo/te/controller/FileController.java` L144:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

230) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te/faith-te-provider/src/main/java/cn/com/bdo/te/controller/TemplateEngineController.java` L67:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

231) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te/faith-te-provider/src/main/java/cn/com/bdo/te/controller/TemplateEngineController.java` L75:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

232) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te/faith-te-provider/src/main/java/cn/com/bdo/te/controller/TemplateEngineController.java` L81:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

233) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te/faith-te-provider/src/main/java/cn/com/bdo/te/controller/TemplateEngineController.java` L87:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

234) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te/faith-te-provider/src/main/java/cn/com/bdo/te/controller/TemplateEngineController.java` L93:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

235) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te/faith-te-provider/src/main/java/cn/com/bdo/te/controller/TemplateEngineController.java` L105:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

236) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te/faith-te-provider/src/main/java/cn/com/bdo/te/controller/TemplateEngineController.java` L111:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

237) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te/faith-te-provider/src/main/java/cn/com/bdo/te/controller/TemplateEngineController.java` L117:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

238) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te/faith-te-provider/src/main/java/cn/com/bdo/te/controller/TemplateEngineController.java` L123:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

239) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te/faith-te-provider/src/main/java/cn/com/bdo/te/controller/TemplateEngineController.java` L128:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

240) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te/faith-te-provider/src/main/java/cn/com/bdo/te/controller/TemplateEngineController.java` L140:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

241) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te/faith-te-provider/src/main/java/cn/com/bdo/te/controller/TemplateEngineController.java` L165:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

242) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te/faith-te-provider/src/main/java/cn/com/bdo/te/controller/TemplateEngineController.java` L182:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

243) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-te/faith-te-provider/src/main/java/cn/com/bdo/te/controller/TemplateGroupController.java` L55:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

244) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-web/faith-web-impl/src/main/java/cn/com/bdo/web/controller/AuthController.java` L24:3
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

245) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-web/faith-web-impl/src/main/java/cn/com/bdo/web/controller/BaseController.java` L51:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

246) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-web/faith-web-impl/src/main/java/cn/com/bdo/web/controller/BaseController.java` L257:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

247) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-web/faith-web-impl/src/main/java/cn/com/bdo/web/controller/BdoToteController.java` L49:3
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

248) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-web/faith-web-impl/src/main/java/cn/com/bdo/web/controller/DgCenterController.java` L149:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

249) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-web/faith-web-impl/src/main/java/cn/com/bdo/web/controller/GeneralBaseController.java` L12:3
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

250) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-web/faith-web-impl/src/main/java/cn/com/bdo/web/controller/LoginController.java` L62:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

251) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-web/faith-web-impl/src/main/java/cn/com/bdo/web/controller/LoginController.java` L91:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

252) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-web/faith-web-impl/src/main/java/cn/com/bdo/web/controller/LoginController.java` L117:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

253) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-web/faith-web-impl/src/main/java/cn/com/bdo/web/controller/LoginController.java` L508:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

254) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-web/faith-web-impl/src/main/java/cn/com/bdo/web/controller/LoginController.java` L526:6
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

255) **[WARNING] java.spring.security.unrestricted-request-mapping.unrestricted-request-mapping**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/faith-web/faith-web-impl/src/main/java/cn/com/bdo/web/controller/UsualController.java` L16:3
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected a method annotated with 'RequestMapping' that does not specify the HTTP method. CSRF protections are not enabled for GET, HEAD, TRACE, or OPTIONS, and by default all HTTP methods are allowed when the HTTP method is not explicitly specified. This means that a method that performs state changes could be vulnerable to CSRF attacks. To mitigate, add the 'method' field and specify the HTTP method (such as 'RequestMethod.POST').

256) **[WARNING] javascript.lang.security.detect-eval-with-expression.detect-eval-with-expression**
- 仓库：sacp__faith
- 文件：`gitlab/sacp__faith/Faith/src/main/Faith/bdolx/main/main.js` L1487:24
- 版本/commit（blame）：`c19b6252f457da83d451fae4216a2e67d7851fb5`
- 建议：Detected use of dynamic execution of JavaScript which may come from user-input, which can lead to Cross-Site-Scripting (XSS). Where possible avoid including user-input in functions which dynamically execute user-input.

## 关联说明（本周期 zhu.qiangfei 的提交 sha）

- faith 本周期提交：详见原始 JSON
- faith-ipo-ui 本周期提交：详见原始 JSON
- deploy 本周期提交：详见原始 JSON

> 如需“是否由 zhu.qiangfei 在本周期引入”的归因，可对每个命中文件做 `git log -L`/diff 对比本周期提交范围。