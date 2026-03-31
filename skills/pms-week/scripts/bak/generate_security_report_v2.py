#!/usr/bin/env python3
"""Generate simplified security scan report for bdo projects only."""

import json
import os
import glob

# Load results
with open('/tmp/gitleaks_full.json') as f:
    gitleaks = json.load(f)

with open('/tmp/semgrep_full.json') as f:
    semgrep_data = json.load(f)
semgrep = semgrep_data.get('results', [])

# Workspace path
workspace = '/home/jinye/.openclaw/workspace'

# Find all bdo-* directories under workspace
bdo_projects = set()
for item in glob.glob(os.path.join(workspace, 'bdo-*')):
    if os.path.isdir(item):
        bdo_projects.add(os.path.basename(item))

# Also check for bdo-* in subdirectories
for root, dirs, files in os.walk(workspace):
    for d in dirs:
        if d.startswith('bdo-'):
            bdo_projects.add(d)
    # Limit search depth
    if root.count(os.sep) > workspace.count(os.sep) + 2:
        dirs.clear()

print(f"Found bdo projects: {sorted(bdo_projects)}")
print()

# Group by repository
def get_repo(file_path):
    if not isinstance(file_path, str):
        return 'unknown'
    # gitleaks returns relative path, semgrep returns absolute
    if not file_path.startswith(workspace):
        file_path = os.path.join(workspace, file_path)
    if not file_path.startswith(workspace):
        return 'unknown'
    rel = file_path[len(workspace)+1:]
    for part in rel.split('/'):
        if part.startswith('bdo-'):
            return part
    return 'unknown'

# Filter findings to only bdo projects
gitleaks_by_repo = {}
for finding in gitleaks:
    file_path = finding.get('File', finding.get('file', ''))
    repo = get_repo(file_path)
    if repo in bdo_projects:
        rule = finding.get('RuleID', finding.get('rule_id', 'unknown'))
        if repo not in gitleaks_by_repo:
            gitleaks_by_repo[repo] = []
        gitleaks_by_repo[repo].append({
            'rule': rule,
            'file': file_path,
            'line': finding.get('StartLine', finding.get('Start_line', '?')),
            'match': finding.get('Match', finding.get('match', ''))[:50]
        })

semgrep_by_repo = {}
for match in semgrep:
    file_path = match.get('path', '')
    repo = get_repo(file_path)
    if repo in bdo_projects:
        metadata = match.get('extra', {}).get('metadata', {})
        semgrep_rule = metadata.get('semgrep.dev', {}).get('rule', {})
        rule_id = semgrep_rule.get('rule_id', 'unknown')
        rule_desc = metadata.get('semgrep.dev', {}).get('rule', {}).get('description', match.get('extra', {}).get('message', ''))
        severity = match.get('extra', {}).get('severity', match.get('severity', 'WARNING'))
        
        if repo not in semgrep_by_repo:
            semgrep_by_repo[repo] = []
        semgrep_by_repo[repo].append({
            'rule': rule_id,
            'desc': rule_desc,
            'severity': severity,
            'file': file_path,
            'line': match.get('start', {}).get('line', '?')
        })

# Output
print("扫描说明：对 7 个涉及仓库做了 gitleaks（密钥）+ semgrep（安全规则）扫描。")
print()

print("### 1) gitleaks（密钥/凭证泄露）")
print()

known_repos = ['bdo-biz-archive', 'bdo-pm-file', 'bdo-pm-report', 'bdo-project-manage']

for repo in sorted(known_repos):
    findings = gitleaks_by_repo.get(repo, [])
    if findings:
        print(f"**{repo}：{len(findings)} 条**")
        for f in findings:
            print(f"- {f['rule']}：{f['file']} 第 {f['line']} 行（匹配：{f['match']}）")
    else:
        print(f"**{repo}：0 条**")

other_repos = set(gitleaks_by_repo.keys()) - set(known_repos)
other_count = sum(len(gitleaks_by_repo.get(r, [])) for r in other_repos)
print(f"**其他项目：{other_count} 条**")
print()

print("### 2) semgrep（安全规则）")
print()

for repo in sorted(known_repos):
    findings = semgrep_by_repo.get(repo, [])
    if findings:
        error_count = sum(1 for f in findings if f['severity'] == 'ERROR')
        warning_count = len(findings) - error_count
        prefix = ""
        if error_count > 0 and warning_count > 0:
            prefix = f"（ERROR {error_count} / WARNING {warning_count}）"
        elif error_count > 0:
            prefix = f"（ERROR {error_count}）"
        elif warning_count > 0:
            prefix = f"（WARNING {warning_count}）"
        
        print(f"**{repo}：{len(findings)} 条{prefix}**")
        
        # Group by rule
        rules = {}
        for f in findings:
            r = f['rule']
            if r not in rules:
                rules[r] = {'desc': f['desc'], 'count': 0, 'examples': []
}
            rules[r]['count'] += 1
            if len(rules[r]['examples']) < 2:
                rules[r]['examples'].append(f"{f['file']} 第 {f['line']} 行")
        
        for rule_id, data in sorted(rules.items(), key=lambda x: x[1]['count'], reverse=True):
            print(f"- `{rule_id}` {data['desc']}（{data['count']} 条）")
            for ex in data['examples']:
                print(f"  - {ex}")
    else:
        print(f"**{repo}：0 条**")

other_semgrep = [f for r in other_repos for f in semgrep_by_repo.get(r, [])]
if other_semgrep:
    print(f"**其他项目：{len(other_semgrep)} 条**")
else:
    print("**其他项目：0 条**")
