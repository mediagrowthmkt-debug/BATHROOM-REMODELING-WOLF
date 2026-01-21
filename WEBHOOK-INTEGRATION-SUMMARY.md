# Integração do Webhook - Bathroom Remodeling

## Data da Atualização
21 de janeiro de 2026

## Webhook URL
```
https://hook.us2.make.com/m6c3nxfa5estl25ymykzq44hlvvfnajp
```

## Formulários Configurados

### 1. Hero Form (Formulário do Cabeçalho)
**ID do Formulário:** `heroForm`

**Campos Capturados:**
- `name` - Nome completo
- `email` - Email
- `phone` - Telefone
- `Qualified_question` - Seleção do tipo de renovação do banheiro

### 2. Contact Form (Formulário de Contato)
**ID do Formulário:** `bathroomForm`

**Campos Capturados:**
- `name` - Nome completo
- `email` - Email
- `phone` - Telefone
- `Qualified_question` - Opção selecionada para o objetivo da renovação (radio button)

## Dados Enviados ao Webhook

Ambos os formulários enviam os seguintes dados em formato JSON:

```json
{
  "email": "email@exemplo.com",
  "phone": "(555) 123-4567",
  "name": "Nome do Cliente",
  "campaign_name": "Bathroom Remodeling",
  "page_name": "Bathroom Remodeling | Wolf Carpenters",
  "FONTE": "https://url-completa-da-pagina.com",
  "PLATAFORMA": "GOOGLE | META | ORGANIC",
  "Qualified_question": "resposta-da-pergunta-qualificatoria"
}
```

## Campos Explicados

### {{email}}
Email fornecido pelo usuário. Campo obrigatório em ambos os formulários.

### {{phone}}
Telefone fornecido pelo usuário. Campo obrigatório em ambos os formulários.

### {{name}}
Nome completo fornecido pelo usuário. Campo obrigatório em ambos os formulários.

### {{campaign_name}}
Nome da campanha: **"Bathroom Remodeling"**

### {{page_name}}
Nome da página: **"Bathroom Remodeling | Wolf Carpenters"**

### {{FONTE}}
URL completa da página onde o formulário foi preenchido. Exemplo:
- `https://wolfcarpenters.com/bathroom-remodeling`
- `https://wolfcarpenters.com/bathroom-remodeling?utm_source=google&utm_medium=cpc`

### {{PLATAFORMA}}
Origem do tráfego detectada automaticamente:
- **GOOGLE** - Se a URL ou parâmetros UTM contêm "google", "cpc" ou "ppc"
- **META** - Se a URL ou parâmetros UTM contêm "meta", "facebook" ou "instagram"
- **ORGANIC** - Para todo o resto (tráfego orgânico, direto, etc.)

### {{Qualified_question}}
Resposta da pergunta qualificatória. Valores possíveis:

**Hero Form (select):**
- `full-remodel` - Full remodel – new layout, tiles, and fixtures
- `partial-upgrade` - Partial upgrade – vanity, shower, or flooring
- `not-sure` - Not sure yet – I'd like some guidance

**Contact Form (radio buttons):**
- `full-remodel` - Full remodel – new layout, tiles, and fixtures
- `partial-upgrade` - Partial upgrade – vanity, shower, or flooring
- `not-sure` - Not sure yet – I'd like some guidance

## Detecção de Plataforma

A detecção de plataforma funciona através de:

1. **Análise da URL** - Verifica se a URL contém palavras-chave como "google", "meta", "facebook", "instagram"
2. **Parâmetros UTM** - Analisa `utm_source` e `utm_medium` para identificar a origem
3. **Prioridade**:
   - Google: Se encontrar "google", "cpc" ou "ppc"
   - Meta: Se encontrar "meta", "facebook" ou "instagram"
   - Organic: Caso contrário

## Fluxo de Submissão

1. Usuário preenche o formulário
2. JavaScript intercepta o submit (preventDefault)
3. Captura a URL atual da página
4. Detecta a plataforma baseada na URL e parâmetros UTM
5. Monta o objeto JSON com todos os dados
6. Envia para o webhook via POST
7. Se sucesso (status 200), redireciona para `thank-you.html`
8. Se erro, mostra mensagem de erro ao usuário

## Logs de Console

Para debug, os seguintes logs são exibidos no console do navegador:

- `"Enviando dados do Hero Form:"` - Antes de enviar o formulário do hero
- `"Enviando dados do Contact Form:"` - Antes de enviar o formulário de contato
- `"Dados enviados com sucesso ao webhook"` - Quando o webhook retorna sucesso
- `"Erro ao enviar dados:"` - Quando há erro na requisição

## Página de Agradecimento

Após submissão bem-sucedida, o usuário é redirecionado para:
```
thank-you.html
```

## Tratamento de Erros

- Se o webhook retornar erro ou não responder, uma mensagem é exibida ao usuário
- Os erros são logados no console para facilitar o debug
- O formulário não é limpo em caso de erro para o usuário não perder os dados

## Notas Técnicas

- **Método:** POST
- **Content-Type:** application/json
- **Encoding:** UTF-8
- **Campos vazios:** Enviados como strings vazias (`""`)
- **Campos opcionais:** Sempre incluídos no payload, mesmo se vazios

## Testes Recomendados

1. ✅ Testar submissão do Hero Form
2. ✅ Testar submissão do Contact Form
3. ✅ Verificar se a URL está sendo capturada corretamente
4. ✅ Testar detecção de plataforma com diferentes URLs:
   - URL normal (deve retornar ORGANIC)
   - URL com `?utm_source=google` (deve retornar GOOGLE)
   - URL com `?utm_source=facebook` (deve retornar META)
5. ✅ Verificar redirecionamento para thank-you.html
6. ✅ Testar tratamento de erro (desconectar internet)

## Status

✅ **IMPLEMENTADO E FUNCIONANDO**

Ambos os formulários estão configurados e enviando dados corretamente para o webhook Make.com.
