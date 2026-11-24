# ChatGPT Ads Performance Skill

A cross-platform Agent Skill for auditing, analyzing, optimizing, monitoring, troubleshooting, and safely creating campaigns with ChatGPT Ads and the OpenAI Advertiser API.

The skill is designed for ChatGPT/Codex and Claude Code. It combines a strict read-first operating model, measurement validation, profitability analysis, experiment discipline, recurring monitoring, and guarded campaign writes.

## What it covers

- Account, campaign, ad-group, ad, review, and serving audits
- Measurement checks for Pixel, CAPI, event settings, deduplication, consent, and oppref
- CTR, CPC, CPM, CVR, CPA, CAC, ROAS, contribution margin, and break-even analysis
- Comparable-period and attribution-aware reporting
- Evidence classification: insufficient, directional, or decision-ready
- Diagnosis across serving, delivery, creative, landing page, tracking, and economics
- Bid, budget, context-hint, creative, platform, location, and product optimization
- Controlled scaling with cooldowns, marginal CPA, and rollback conditions
- Launch, daily, weekly, monthly, experiment, and incident monitoring
- Safe campaign creation with dry-run, approval, verification, and paused-by-default objects
- API freshness checks for changing OpenAI Ads features

## Repository structure

    skill/chatgpt-ads-performance/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── assets/icon.svg
    ├── references/
    │   ├── analysis-framework.md
    │   ├── api-freshness.md
    │   ├── campaign-creation.md
    │   ├── monitoring-playbook.md
    │   ├── optimization-playbook.md
    │   ├── policy-and-safety.md
    │   └── report-contract.md
    └── scripts/analyze_insights.py

## Compatibility

### ChatGPT and Codex

Import or copy the complete skill folder into a supported Skills directory. Invoke it explicitly as:

    $chatgpt-ads-performance

ChatGPT and Codex use agents/openai.yaml for UI metadata. The core SKILL.md, references, and script follow the open Agent Skills format.

### Claude Code

For a personal installation:

    mkdir -p ~/.claude/skills
    cp -R skill/chatgpt-ads-performance ~/.claude/skills/

For a project installation:

    mkdir -p .claude/skills
    cp -R skill/chatgpt-ads-performance .claude/skills/

Invoke it as:

    /chatgpt-ads-performance

Claude Code ignores agents/openai.yaml and uses SKILL.md, references, and scripts normally.

## Requirements

- A configured OpenAI Ads account and Advertiser API key
- The chatgpt-ads-app CLI or an equivalent implementation of the documented commands
- Python 3.10 or newer for scripts/analyze_insights.py
- Permission to access the account and apply any requested changes

Resolve the placeholder CHATGPT_ADS_APP_DIR in SKILL.md during installation, or make the CLI location discoverable in the project.

## Example requests

    Audit my ChatGPT Ads account for the last 30 days and identify the binding constraint.

    Compare the last 14 days with the previous period and propose optimizations without changing anything.

    Check whether this campaign is ready to scale and define the next budget step and rollback rule.

    Monitor my active campaigns, report only material changes, and identify tracking or spend incidents.

    Create a paused campaign plan from this brief, run the dry-run, and wait for approval.

## Deterministic KPI analysis

The bundled script accepts JSON or CSV insight exports:

    python3 skill/chatgpt-ads-performance/scripts/analyze_insights.py \
      current.json \
      --prior prior.json \
      --currency USD \
      --target-cpa 40 \
      --group-by entity_id \
      --format markdown

Run its built-in test:

    python3 skill/chatgpt-ads-performance/scripts/analyze_insights.py --self-test

## Safety model

- Read-only by default
- Measurement before media judgment
- Comparable attribution settings before comparison
- No forced winner on insufficient evidence
- Dry-run and explicit approval before writes
- New objects paused by default
- Budget scaling normally limited to 10–20% per review cycle
- Pause preferred over irreversible archive
- No secrets committed to the repository

## Attribution

This project is an independent, expanded Agent Skill inspired by and designed to operate with [faborsky/chatgpt-ads-app](https://github.com/faborsky/chatgpt-ads-app), created by Jindřich Fáborský and distributed under the MIT License.

The performance-analysis, optimization, monitoring, reporting, and deterministic KPI components in this repository were substantially expanded for cross-platform use.

## License

MIT. See [LICENSE](LICENSE).

---

# Skill ChatGPT Ads Performance — Português do Brasil

Uma Agent Skill multiplataforma para auditar, analisar, otimizar, acompanhar, diagnosticar e criar campanhas com segurança no ChatGPT Ads e na OpenAI Advertiser API.

A skill foi desenvolvida para ChatGPT/Codex e Claude Code. Ela combina operação inicialmente somente leitura, validação da mensuração, análise de rentabilidade, disciplina experimental, acompanhamento recorrente e alterações protegidas por aprovação.

## O que ela cobre

- Auditoria de conta, campanhas, grupos, anúncios, revisão e veiculação
- Verificação de Pixel, CAPI, eventos, deduplicação, consentimento e oppref
- CTR, CPC, CPM, CVR, CPA, CAC, ROAS, margem de contribuição e ponto de equilíbrio
- Relatórios com períodos comparáveis e configurações consistentes de atribuição
- Classificação das evidências: insuficiente, direcional ou pronta para decisão
- Diagnóstico de veiculação, entrega, criativo, landing page, tracking e rentabilidade
- Otimização de lances, orçamento, context hints, criativos, plataformas, regiões e produtos
- Escala controlada com cooldown, CPA marginal e condições de rollback
- Acompanhamento de lançamento, diário, semanal, mensal, experimental e de incidentes
- Criação segura de campanhas com dry-run, aprovação, verificação e objetos inicialmente pausados
- Verificação de atualizações da API do OpenAI Ads

## Estrutura do repositório

    skill/chatgpt-ads-performance/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── assets/icon.svg
    ├── references/
    │   ├── analysis-framework.md
    │   ├── api-freshness.md
    │   ├── campaign-creation.md
    │   ├── monitoring-playbook.md
    │   ├── optimization-playbook.md
    │   ├── policy-and-safety.md
    │   └── report-contract.md
    └── scripts/analyze_insights.py

## Compatibilidade

### ChatGPT e Codex

Importe ou copie a pasta completa da skill para um diretório de Skills compatível. Para chamar explicitamente:

    $chatgpt-ads-performance

O ChatGPT e o Codex utilizam agents/openai.yaml para os metadados da interface. O SKILL.md, as referências e o script seguem o formato aberto Agent Skills.

### Claude Code

Instalação pessoal:

    mkdir -p ~/.claude/skills
    cp -R skill/chatgpt-ads-performance ~/.claude/skills/

Instalação dentro de um projeto:

    mkdir -p .claude/skills
    cp -R skill/chatgpt-ads-performance .claude/skills/

Para chamar:

    /chatgpt-ads-performance

O Claude Code ignora agents/openai.yaml e utiliza normalmente o SKILL.md, as referências e os scripts.

## Requisitos

- Conta do OpenAI Ads configurada e chave da Advertiser API
- CLI chatgpt-ads-app ou uma implementação equivalente dos comandos documentados
- Python 3.10 ou superior para scripts/analyze_insights.py
- Permissão para acessar a conta e aplicar eventuais alterações solicitadas

Durante a instalação, substitua o placeholder CHATGPT_ADS_APP_DIR presente no SKILL.md ou deixe o local da CLI identificável dentro do projeto.

## Exemplos de solicitações

    Audite minha conta do ChatGPT Ads nos últimos 30 dias e identifique a principal limitação.

    Compare os últimos 14 dias com o período anterior e proponha otimizações sem alterar nada.

    Verifique se esta campanha está pronta para escalar e defina o próximo aumento e a regra de rollback.

    Acompanhe minhas campanhas ativas, relate apenas mudanças relevantes e identifique problemas de tracking ou gastos.

    Crie um plano de campanha pausada com base neste briefing, execute o dry-run e aguarde aprovação.

## Análise determinística dos indicadores

O script incluído aceita exportações de insights em JSON ou CSV:

    python3 skill/chatgpt-ads-performance/scripts/analyze_insights.py \
      current.json \
      --prior prior.json \
      --currency BRL \
      --target-cpa 120 \
      --group-by entity_id \
      --format markdown

Para executar o teste interno:

    python3 skill/chatgpt-ads-performance/scripts/analyze_insights.py --self-test

## Modelo de segurança

- Somente leitura por padrão
- Validação da mensuração antes de julgar a mídia
- Comparação apenas com configurações compatíveis de atribuição
- Nenhum vencedor forçado com evidências insuficientes
- Dry-run e aprovação explícita antes de alterações
- Novos objetos criados pausados
- Escala de orçamento normalmente limitada a 10–20% por ciclo
- Pausa preferida ao arquivamento irreversível
- Nenhum segredo salvo no repositório

## Atribuição

Este projeto é uma Agent Skill independente e ampliada, inspirada e desenvolvida para operar com [faborsky/chatgpt-ads-app](https://github.com/faborsky/chatgpt-ads-app), criado por Jindřich Fáborský e distribuído sob a licença MIT.

Os componentes de análise de performance, otimização, acompanhamento, relatórios e cálculo determinístico de indicadores foram significativamente ampliados para uso multiplataforma.

## Licença

MIT. Consulte [LICENSE](LICENSE).

