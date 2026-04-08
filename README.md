# TekForge

TekForge é um hub de tecnologia que reúne perfil profissional, projetos, materiais de ensino e aplicações.

Este pacote foi preparado para deploy no **Google Cloud Run**, seguindo a mesma linha prática do repositório **catboost_learning_studio**: container com Docker, deploy manual com `gcloud`, opção de **Terraform** e automação com **GitHub Actions**.

## Estrutura de deploy

- `Dockerfile`: imagem pronta para Cloud Run
- `gunicorn.conf.py`: execução de produção com Gunicorn
- `.gcloudignore`: reduz o contexto de build
- `.github/workflows/deploy-cloud-run.yml`: workflow para deploy automatizado
- `terraform/`: base opcional para provisionar Cloud Run e Artifact Registry

## Rodar localmente

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# ou .venv\Scripts\activate no Windows
pip install -r requirements.txt
python app.py
```

## Deploy manual no Google Cloud Run

```bash
gcloud run deploy tekforge   --source .   --region us-central1   --allow-unauthenticated   --set-env-vars ENVIRONMENT=production,APP_VERSION=v12-deploy,SITE_URL=https://tekforge.com.br,SITE_DOMAIN=tekforge.com.br,GITHUB_USERNAME=pedrocnf
```

## Deploy com domínio customizado

Depois do primeiro deploy, faça o mapeamento do domínio para o serviço do Cloud Run e aponte DNS para:

- `tekforge.com.br`
- ou `www.tekforge.com.br`

## GitHub Actions

O workflow usa Workload Identity Federation e espera estes secrets no repositório:

- `GCP_PROJECT_ID`
- `GCP_WIF_PROVIDER`
- `GCP_SERVICE_ACCOUNT`

Opcionalmente, você pode definir estes *Repository Variables*:

- `GCP_REGION` (padrão: `us-central1`)
- `CLOUD_RUN_SERVICE` (padrão: `tekforge`)

## Terraform

A pasta `terraform/` provisiona:

- um repositório no Artifact Registry
- um serviço no Cloud Run

Fluxo sugerido:

```bash
cd terraform
terraform init
terraform plan -var-file=terraform.tfvars
terraform apply -var-file=terraform.tfvars
```

## Health checks

- `/api/health`
- `/api/ready`

## Observação

Se você for publicar pelo GitHub Actions, use a mesma conta de serviço do projeto com permissões para:

- Cloud Run Admin
- Service Account User
- Artifact Registry Writer

## Referência de estilo de deploy

Este pacote foi alinhado ao padrão simples do repositório `pedrocnf/catboost_learning_studio`: README objetivo, `gcloud run deploy --source .`, workflow em `.github/workflows/` e opção de Terraform para infraestrutura.
