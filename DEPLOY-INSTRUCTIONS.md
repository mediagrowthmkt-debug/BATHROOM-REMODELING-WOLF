# 🚀 Instruções de Deploy - Wolf Carpenters Bathroom Remodeling

## ✅ Estrutura Criada com Sucesso

Foram criadas **3 versões** da landing page:

### 📂 Versões Disponíveis

1. **Original** → `index.html` (raiz do projeto)
2. **Meta/Facebook** → `/meta/index.html`
3. **Google Ads** → `/google/index.html`

---

## 🌐 URLs de Acesso

Após o deploy no servidor, as páginas estarão disponíveis em:

```
https://seudominio.com/                    ← Página Original
https://seudominio.com/meta/               ← Campanha Meta/Facebook
https://seudominio.com/google/             ← Campanha Google Ads
```

---

## 📊 Diferenças Entre as Versões

Todas as páginas são **idênticas visualmente**, mas possuem **rastreamento diferente** no formulário:

### Original (`/index.html`)
```html
<input type="hidden" name="campaign" value="Bathroom Remodeling">
<input type="hidden" name="source" value="Landing Page">
```

### Meta Campaign (`/meta/index.html`)
```html
<input type="hidden" name="campaign" value="Bathroom Remodeling - Meta">
<input type="hidden" name="source" value="Landing Page Meta Campaign">
```

### Google Campaign (`/google/index.html`)
```html
<input type="hidden" name="campaign" value="Bathroom Remodeling - Google">
<input type="hidden" name="source" value="Landing Page Google Campaign">
```

---

## 📦 Como Fazer Upload para o Servidor

### Opção 1: Via FTP/SFTP

1. **Conecte-se ao servidor** usando FileZilla, Cyberduck ou outro cliente FTP
2. **Mantenha a estrutura de pastas exata:**

```
public_html/ (ou www/ ou httpdocs/)
├── index.html
├── thank-you.html
├── meta/
│   ├── index.html
│   └── thank-you.html
├── google/
│   ├── index.html
│   └── thank-you.html
├── 0 - Brand Logo/
├── 1 - Hero Section - Bathroom Remodeling Introduction/
├── 2 - Before and After Transformation/
├── 3 - Bathroom Portfolio - Finished Projects/
├── 4 - Portfolio Videos - Bathroom Showcase/
├── 5 - Planning Process - Before Construction/
├── 6 - Meet the Team - Wolf Carpenters Crew/
└── 7 - Company Results - Balanced Scorecard/
```

3. **Faça upload de TODA a estrutura** de uma vez só

### Opção 2: Via cPanel File Manager

1. Acesse o **cPanel** do seu hosting
2. Vá em **File Manager**
3. Navegue até `public_html` (ou diretório público)
4. Crie um arquivo **ZIP** com todo o conteúdo da pasta "BATHROOM REMODELING"
5. Faça upload do ZIP
6. **Extraia** o arquivo ZIP dentro de `public_html`

---

## ⚠️ IMPORTANTE - Não Modificar

### ❌ NÃO altere:
- Estrutura de pastas
- Caminhos relativos das imagens (`../`)
- Nomes das pastas

### ✅ Pode modificar:
- Conteúdo do texto
- Imagens (mantendo os mesmos nomes)
- Vídeos (mantendo os mesmos nomes)
- Webhook URL do formulário

---

## 🔧 Testar Localmente (Opcional)

Para testar antes de fazer upload:

1. Abra o arquivo `_navigation.html` em um navegador
2. Clique nos botões para navegar entre as versões
3. Teste o envio de formulários

**OU**

Inicie um servidor local:

```bash
# Com Python 3
cd "/Users/bruno/Documents/LPS/CLIENTES/WOLF/BATHROOM REMODELING"
python3 -m http.server 8000

# Acesse: http://localhost:8000
```

---

## 📈 Como Usar nas Campanhas

### Meta Ads / Facebook Ads
- **URL de destino:** `https://seudominio.com/meta/`
- Os leads serão marcados como "Meta Campaign"

### Google Ads
- **URL de destino:** `https://seudominio.com/google/`
- Os leads serão marcados como "Google Campaign"

### Outras Fontes
- **URL de destino:** `https://seudominio.com/`
- Sem identificação específica de campanha

---

## 📧 Webhook Atual

As 3 versões enviam dados para o mesmo webhook:
```
https://hook.us2.make.com/m6c3nxfa5estl25ymykzq44hlvvfnajp
```

O campo `campaign` permite diferenciar a origem no Make.com/Zapier.

---

## ✨ Recursos Incluídos

- ✅ Design responsivo (mobile + desktop)
- ✅ Slider interativo Before/After
- ✅ Galeria de portfólio
- ✅ Depoimentos de clientes (Google Reviews)
- ✅ Formulário de contato integrado
- ✅ Redirecionamento para página de agradecimento
- ✅ Rastreamento por campanha
- ✅ Vídeo hero background
- ✅ Widget flutuante de contato

---

## 🆘 Suporte

Se precisar de ajuda durante o deploy ou tiver dúvidas:

1. Verifique se todos os arquivos foram enviados corretamente
2. Confirme se as pastas `meta/` e `google/` existem no servidor
3. Teste cada URL no navegador
4. Verifique se as imagens estão carregando corretamente

---

**Criado em:** 02/11/2025  
**Versão:** 1.0  
**Cliente:** Wolf Carpenters
