import json
from jinja2 import Environment, FileSystemLoader

# Charger les données JSON
with open('snyk_report.json') as f:
    snyk_data = json.load(f)

with open('gitleaks.sarif') as f:
    gitleaks_data = json.load(f)

with open('trivy_report.json') as f:
    trivy_data = json.load(f)

# Configurer Jinja2
env = Environment(loader=FileSystemLoader('report'))
template = env.get_template('template.html')

# Rendu du HTML
html_content = template.render(
    snyk=snyk_data,
    gitleaks=gitleaks_data,
    trivy=trivy_data
)

# Sauvegarder le fichier
with open('report/security_report.html', 'w') as f:
    f.write(html_content)

print("✅ Rapport HTML généré : report/security_report.html")
