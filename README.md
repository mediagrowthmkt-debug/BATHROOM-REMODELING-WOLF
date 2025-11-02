# Wolf Carpenters - Bathroom Remodeling Landing Pages

## Estrutura de Campanhas

Este projeto contém landing pages duplicadas para diferentes campanhas de marketing:

### 📁 Estrutura de Pastas

```
BATHROOM REMODELING/
├── index.html (original)
├── thank-you.html (original)
├── meta/ (Campanha Meta/Facebook)
│   ├── index.html
│   └── thank-you.html
├── google/ (Campanha Google Ads)
│   ├── index.html
│   └── thank-you.html
├── 0 - Brand Logo/
├── 1 - Hero Section - Bathroom Remodeling Introduction/
├── 2 - Before and After Transformation/
├── 3 - Bathroom Portfolio - Finished Projects/
├── 4 - Portfolio Videos - Bathroom Showcase/
├── 5 - Planning Process - Before Construction/
├── 6 - Meet the Team - Wolf Carpenters Crew/
├── 7 - Company Results - Balanced Scorecard/
└── portifolio imagens/
```

### 🎯 URLs das Campanhas

- **Campanha Meta:** `seudominio.com/meta/`
- **Campanha Google:** `seudominio.com/google/`
- **Original:** `seudominio.com/`

### 📊 Rastreamento de Campanhas

Cada versão possui campos ocultos no formulário para identificar a origem:

#### Meta Campaign (`/meta/index.html`)
```html
<input type="hidden" name="campaign" value="Bathroom Remodeling - Meta">
<input type="hidden" name="source" value="Landing Page Meta Campaign">
```

#### Google Campaign (`/google/index.html`)
```html
<input type="hidden" name="campaign" value="Bathroom Remodeling - Google">
<input type="hidden" name="source" value="Landing Page Google Campaign">
```

### 🔗 Recursos Compartilhados

Todas as imagens e recursos (vídeos, logos, etc.) estão localizados na pasta raiz e são compartilhados entre todas as versões usando caminhos relativos (`../`).

### ✅ Funcionalidades

- ✓ Formulários de contato integrados com webhook
- ✓ Redirecionamento para página de agradecimento após submissão
- ✓ Identificação automática de origem da campanha
- ✓ Design responsivo para mobile e desktop
- ✓ Sliders de antes/depois interativos
- ✓ Galeria de portfólio
- ✓ Depoimentos de clientes

### 📝 Notas Importantes

1. Os recursos (imagens, vídeos) estão na pasta raiz e são referenciados com `../` nas páginas dentro das pastas `/meta` e `/google`
2. Cada campanha possui seu próprio identificador no formulário para rastreamento
3. As páginas de agradecimento redirecionam para a página inicial da respectiva campanha

### 🚀 Deploy

Ao fazer upload para o servidor, mantenha toda a estrutura de pastas intacta para garantir que os caminhos relativos funcionem corretamente.
