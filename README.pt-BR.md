# SOC CORE

> **O SOC CORE se adapta ao ecossistema de segurança da empresa, e não o contrário.**

O **SOC CORE** é um projeto de engenharia para operações de segurança focado em reunir **telemetria de segurança, correlação de eventos, enriquecimento com inteligência de ameaças, automação, análise assistida por IA e resposta a incidentes** por meio de uma arquitetura adaptável de integração.

Este repositório é a **documentação técnica pública e portfólio de engenharia** do SOC CORE. Ele intencionalmente não contém código-fonte de produção, credenciais, segredos operacionais, dados de clientes, detalhes internos de rede ou configurações sensíveis.

[English](README.md)

---

## Por que SOC CORE

Ambientes de segurança raramente dependem de um único fabricante.

O SOC CORE foi desenhado com uma abordagem **agnóstica de cloud, fabricante e tecnologia**, permitindo integrações por meio de:

- APIs REST
- Webhooks
- Syslog
- Agentes
- Encaminhamento de logs
- Bancos de dados
- Filas de mensagens
- Arquivos e telemetria
- Outros mecanismos compatíveis de integração

Sempre que uma tecnologia fornecer um mecanismo acessível para consulta, coleta ou encaminhamento de telemetria de segurança, o SOC CORE pode receber uma camada dedicada de integração para **ingerir, normalizar, correlacionar, enriquecer e processar** essas informações.

A viabilidade de integração depende naturalmente dos recursos expostos pela tecnologia de origem, incluindo APIs, autenticação, permissões, licenciamento, qualidade dos dados, conectividade, limites de consumo e demais restrições técnicas.

### Gestão de Vulnerabilidades

O SOC CORE foi projetado para **se adaptar ao ecossistema de Gestão de Vulnerabilidades já existente na organização**. Quando a empresa já possui uma plataforma dedicada de vulnerability management ou scanning, o SOC CORE pode consumir os achados e o contexto disponibilizados por essa tecnologia por meio dos mecanismos de integração suportados, incorporando essas informações aos fluxos de correlação, priorização e operação de segurança.

Quando a organização não dispõe de uma solução dedicada de scanning, o **SOC CORE também possui capacidade integrada de varredura de vulnerabilidades**, permitindo identificar exposições técnicas e utilizar esses achados no mesmo contexto operacional empregado para análise, priorização e resposta.

Dessa forma, a Gestão de Vulnerabilidades pode funcionar tanto como uma **capacidade externa integrada quanto como uma capacidade nativa do SOC CORE**, de acordo com a infraestrutura e o ecossistema de segurança da empresa.

---

### Web Chat / SOC CORE IA

O **SOC CORE possui uma interface Web Chat voltada às operações de Segurança da Informação**, permitindo que o analista interaja com as capacidades da plataforma por meio de perguntas em linguagem natural.

O objetivo do Web Chat é transformar dados técnicos de segurança em uma experiência operacional mais rápida e acessível. Em vez de exigir que o analista navegue manualmente por diferentes fontes para obter contexto, a interface atua como uma camada de interação com o backend do SOC CORE e suas integrações autorizadas.

Entre os casos de uso previstos estão:

- consultar e compreender incidentes e alertas de segurança;
- solicitar contexto sobre vulnerabilidades, CVEs e indicadores de comprometimento (IOCs);
- identificar ativos afetados e evidências relevantes disponíveis no SOC CORE;
- receber resumos objetivos, impacto e ações recomendadas de investigação ou remediação;
- correlacionar informações provenientes das integrações de segurança disponíveis;
- consultar detalhes de incidentes provenientes de plataformas XDR integradas, incluindo referência ao incidente na plataforma de origem quando disponível;
- apoiar o analista durante triagem, investigação e resposta a incidentes.

A **SOC CORE IA é especializada em Segurança da Informação**. A interface foi concebida para apoiar atividades operacionais do SOC e de Gestão de Vulnerabilidades, mantendo o foco em investigação, entendimento técnico, priorização e remediação.

O Web Chat **não substitui as plataformas de segurança integradas nem a decisão do analista**. Ele funciona como uma camada de consulta e assistência sobre os dados que o SOC CORE está autorizado a processar.

> A documentação pública descreve apenas o comportamento funcional da interface. Código de produção, URLs internas, credenciais, tokens, identificadores de ambiente, dados reais de incidentes e detalhes sensíveis do backend não são publicados.

---

## Princípios de Projeto

- Integração em primeiro lugar
- Arquitetura agnóstica de fabricante
- Normalização antes da correlação
- Contexto acima de volume de alertas
- Automação com supervisão humana
- IA como apoio ao analista
- Segurança por design

---

## Segurança da Publicação

Este repositório segue um modelo de publicação com **sanitização por padrão**.

Não são publicados:

- código de produção;
- credenciais, chaves ou tokens;
- IPs e hostnames internos;
- identificadores de tenant, assinatura ou cliente;
- dados de usuários ou colaboradores;
- incidentes reais identificáveis;
- topologia real de produção;
- controles internos que aumentem materialmente a superfície de ataque;
- configurações operacionais proprietárias.

Consulte [Política de Divulgação Pública](docs/PUBLIC-DISCLOSURE-POLICY.md).

---

## Áreas de Engenharia

O SOC CORE explora temas como:

- Security Operations Center (SOC)
- Integração SIEM / XDR
- Detection Engineering
- Correlação de incidentes
- Threat Intelligence
- Enriquecimento de IOC
- Gestão de Vulnerabilidades e scanning integrado
- Segurança de identidade
- Automação e orquestração
- Análise assistida por IA
- Observabilidade de segurança
- Hardening da plataforma

---

## Autor

**Danilo Sincerre Vida**  
Cybersecurity | Security Engineering | Security Operations | Vulnerability Management

GitHub: [@danilovida](https://github.com/danilovida)
