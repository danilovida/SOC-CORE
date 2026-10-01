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

### Gestão de Inventário de Ativos

O **SOC CORE possui capacidade integrada de Gestão de Inventário de Ativos**, criada para consolidar a visibilidade de ativos relevantes para Segurança da Informação a partir de múltiplas fontes autorizadas em uma única visão operacional.

O inventário pode combinar informações provenientes de plataformas de endpoint/segurança e mecanismos de descoberta de rede, correlacionando observações para reduzir duplicidades e preservar a origem de cada evidência.

Entre as capacidades disponíveis estão:

- descoberta e consolidação de ativos a partir de múltiplas fontes;
- correlação de identidades de dispositivos entre integrações suportadas;
- classificação de endpoints, servidores, infraestrutura de rede, appliances de segurança, impressoras, câmeras, dispositivos de voz e outros tipos observados;
- visão operacional baseada na atividade recente dos ativos;
- visibilidade de hostname, endereço IP, MAC, sistema operacional, fabricante e serviços expostos quando disponibilizados pela fonte;
- identificação da origem das informações, permitindo visualizar ativos observados por uma ou mais integrações;
- pesquisa e filtros por tipo de ativo e fonte;
- visão detalhada por ativo, incluindo identificadores e observações recentes;
- exportação em CSV para apoio operacional, relatórios e auditorias;
- identificação de ativos desconhecidos ou com classificação insuficiente para revisão do analista.

A Gestão de Inventário segue a arquitetura integration-first do SOC CORE. As tecnologias existentes podem continuar sendo a fonte autoritativa de seus próprios dados enquanto o SOC CORE atua como uma **camada de correlação, normalização e visibilidade operacional** entre elas.

> A documentação pública descreve somente a capacidade funcional e o comportamento conceitual da Gestão de Inventário. Listas reais de ativos, endereços internos, hostnames, identificadores de dispositivos, regras de correlação e configurações operacionais não são publicados.

### Cloud Security / CASB

O **SOC CORE possui capacidade CASB (Cloud Access Security Broker) integrada**, voltada à descoberta, visibilidade e governança do uso de aplicações e serviços em nuvem dentro do ambiente corporativo.

A capacidade de Cloud Security pode utilizar telemetria proveniente das integrações já disponíveis no ecossistema de segurança para identificar aplicações utilizadas por usuários e dispositivos, normalizar essas informações e incorporá-las ao contexto operacional do SOC CORE.

Entre as capacidades disponíveis estão:

- **Cloud Discovery**, para identificar aplicações e serviços em nuvem observados no ambiente;
- **Shadow IT**, para destacar aplicações ainda não revisadas, não autorizadas ou fora da governança definida pela organização;
- classificação e categorização de aplicações por contexto de uso;
- acompanhamento de usuários, ativos e volume de eventos relacionados às aplicações identificadas;
- avaliação de risco e priorização de aplicações que exigem análise;
- fluxo de governança para aplicações **não revisadas, permitidas, não autorizadas, bloqueadas ou homologadas**;
- manutenção de uma lista corporativa de aplicações homologadas, conforme decisão da própria organização;
- separação entre aplicações relevantes para governança CASB e telemetria puramente técnica de rede, infraestrutura ou protocolos;
- visão de auditoria por período para apoiar revisões recorrentes do uso de aplicações em nuvem.

A arquitetura do CASB segue o mesmo princípio de integração do SOC CORE: **as decisões de governança permanecem sob controle humano e organizacional**. A plataforma identifica, classifica, contextualiza e apresenta as aplicações para revisão, sem substituir a aprovação formal da empresa.

> A documentação pública apresenta somente a capacidade funcional e a arquitetura conceitual do CASB. Regras internas, integrações de produção, listas corporativas, usuários, endereçamento, credenciais e configurações operacionais não são publicados.

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
- Gestão de Inventário de Ativos
- Descoberta e correlação multi-source de ativos
- Cloud Security / CASB
- Cloud Discovery e Shadow IT
- Governança de aplicações em nuvem
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
