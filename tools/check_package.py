"""Check candidate package structure and local Markdown links, using the stdlib."""
from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
for name in ['SKILL.md','README.md','LICENSE','PRODUCT_DEFINITION.md','references/gates.md','references/technical-structure.md','evaluation/ACCEPTANCE.md']:
    assert (root/name).is_file(), f'Missing {name}'
skill=(root/'SKILL.md').read_text()
assert skill.startswith('---\nname: sentence-gated-writing\n')
assert len(skill.splitlines())<500
for path in root.rglob('*.md'):
    for target in re.findall(r'\]\(([^)]+)\)',path.read_text()):
        if '://' not in target and not target.startswith('#'):
            assert (path.parent/target.split('#')[0]).exists(), f'{path}: {target}'
print('Package structure and local links OK; this does not measure writing quality.')
