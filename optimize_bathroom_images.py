#!/usr/bin/env python3
"""
Script para otimizar apenas as imagens usadas no index.html do BATHROOM REMODELING
Converte para WebP com alta compressão
"""

import os
from pathlib import Path
from PIL import Image

# Diretório base
BASE_DIR = Path("/Users/bruno/Documents/LPS/CLIENTES/WOLF/BATHROOM REMODELING")

# Lista de imagens usadas no index.html (excluindo vídeos e já convertidas)
ACTIVE_IMAGES = [
    "0 - Brand Logo/logo-wolf-desktop (1).png",
    # As demais já estão em .webp no HTML, mas vamos verificar se precisam otimização
]

def get_file_size_mb(filepath):
    """Retorna o tamanho do arquivo em MB"""
    return os.path.getsize(filepath) / (1024 * 1024)

def optimize_image(image_path):
    """Converte e otimiza imagem para WebP"""
    try:
        if not image_path.exists():
            print(f"✗ Arquivo não encontrado: {image_path}")
            return False
            
        # Abrir imagem
        img = Image.open(image_path)
        
        # Converter para RGB se necessário
        if img.mode in ('RGBA', 'LA', 'P'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            if img.mode in ('RGBA', 'LA'):
                background.paste(img, mask=img.split()[-1])
            else:
                background.paste(img)
            img = background
        elif img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Redimensionar se muito grande
        max_dimension = 1920
        original_size_pixels = img.size
        if max(img.size) > max_dimension:
            ratio = max_dimension / max(img.size)
            new_size = tuple(int(dim * ratio) for dim in img.size)
            img = img.resize(new_size, Image.Resampling.LANCZOS)
            print(f"  📐 Redimensionado: {original_size_pixels} -> {new_size}")
        
        # Criar nome do arquivo WebP
        webp_path = image_path.with_suffix('.webp')
        
        # Se já é WebP, otimizar no lugar
        if image_path.suffix.lower() == '.webp':
            temp_path = image_path.with_stem(image_path.stem + '_temp')
            original_size = get_file_size_mb(image_path)
            img.save(temp_path, 'WEBP', quality=75, method=6)
            new_size = get_file_size_mb(temp_path)
            
            os.remove(image_path)
            temp_path.rename(image_path)
            webp_path = image_path
        else:
            # Converter para WebP
            original_size = get_file_size_mb(image_path)
            img.save(webp_path, 'WEBP', quality=75, method=6)
            new_size = get_file_size_mb(webp_path)
            
            # Remover arquivo original
            os.remove(image_path)
        
        reduction = ((original_size - new_size) / original_size * 100) if original_size > 0 else 0
        print(f"✓ {image_path.name}")
        print(f"  💾 {original_size:.2f}MB -> {new_size:.2f}MB (↓ {reduction:.1f}%)")
        
        return webp_path.relative_to(BASE_DIR)
        
    except Exception as e:
        print(f"✗ Erro ao otimizar {image_path.name}: {e}")
        return False

def optimize_existing_webp():
    """Re-otimiza arquivos WebP existentes se necessário"""
    webp_dirs = [
        "2 - Before and After Transformation",
        "3 - Bathroom Portfolio - Finished Projects",
        "portifolio imagens"
    ]
    
    optimized = 0
    total_original = 0
    total_new = 0
    
    for dir_name in webp_dirs:
        dir_path = BASE_DIR / dir_name
        if not dir_path.exists():
            continue
            
        for webp_file in dir_path.glob("*.webp"):
            print(f"\nRe-otimizando: {webp_file.name}")
            original_size = get_file_size_mb(webp_file)
            total_original += original_size
            
            result = optimize_image(webp_file)
            if result:
                new_size = get_file_size_mb(BASE_DIR / result)
                total_new += new_size
                optimized += 1
    
    return optimized, total_original, total_new

def update_html_references(conversions):
    """Atualiza as referências no index.html"""
    html_file = BASE_DIR / "index.html"
    
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for old_path, new_path in conversions.items():
            if old_path != str(new_path):
                content = content.replace(old_path, str(new_path))
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"\n✓ HTML atualizado com {len(conversions)} referências")
        return True
        
    except Exception as e:
        print(f"✗ Erro ao atualizar HTML: {e}")
        return False

def main():
    """Função principal"""
    print("=" * 70)
    print("🚿 OTIMIZAÇÃO DE IMAGENS - BATHROOM REMODELING")
    print("=" * 70)
    
    conversions = {}
    success_count = 0
    total_original_size = 0
    total_new_size = 0
    
    # Otimizar logo PNG
    print(f"\n📋 Processando logo PNG...\n")
    for i, img_rel_path in enumerate(ACTIVE_IMAGES, 1):
        print(f"[{i}/{len(ACTIVE_IMAGES)}] Processando...")
        img_path = BASE_DIR / img_rel_path
        
        if img_path.exists():
            original_size = get_file_size_mb(img_path)
            total_original_size += original_size
            
            result = optimize_image(img_path)
            
            if result:
                conversions[img_rel_path] = result
                new_path = BASE_DIR / result
                if new_path.exists():
                    new_size = get_file_size_mb(new_path)
                    total_new_size += new_size
                success_count += 1
    
    # Re-otimizar WebPs existentes
    print(f"\n📋 Re-otimizando arquivos WebP existentes...\n")
    webp_count, webp_orig, webp_new = optimize_existing_webp()
    
    total_original_size += webp_orig
    total_new_size += webp_new
    success_count += webp_count
    
    print("\n" + "=" * 70)
    print("📊 RESUMO DA OTIMIZAÇÃO")
    print("=" * 70)
    print(f"✓ Arquivos processados: {success_count}")
    print(f"💾 Tamanho original total: {total_original_size:.2f}MB")
    print(f"💾 Tamanho otimizado total: {total_new_size:.2f}MB")
    
    if total_original_size > 0:
        total_reduction = ((total_original_size - total_new_size) / total_original_size * 100)
        saved_mb = total_original_size - total_new_size
        print(f"📉 Redução total: {saved_mb:.2f}MB ({total_reduction:.1f}%)")
    
    # Atualizar HTML
    if conversions:
        print("\n" + "=" * 70)
        print("📝 ATUALIZANDO REFERÊNCIAS NO HTML")
        print("=" * 70)
        update_html_references(conversions)
    
    print("\n" + "=" * 70)
    print("✅ OTIMIZAÇÃO CONCLUÍDA!")
    print("=" * 70)

if __name__ == "__main__":
    main()
