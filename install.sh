#!/bin/bash

# Script de Instalação para o Nautilus LibreOffice Converter

# --- Variáveis ---
# O nome do arquivo principal da extensão
EXT_SOURCE_FILE="LibreOfficeConverter.py"
# O diretório de destino para as extensões do Nautilus
EXT_DEST_DIR="$HOME/.local/share/nautilus-python/extensions"
# URL do projeto para mensagens de erro
PROJECT_URL="https://github.com/thiago-brgs/nautilus-document-converter"

# --- Funções ---
function print_success() {
    # Imprime em verde
    echo -e "\e[32m$1\e[0m"
}

function print_error() {
    # Imprime em vermelho
    echo -e "\e[31m$1\e[0m"
}

function print_info() {
    # Imprime em amarelo
    echo -e "\e[33m$1\e[0m"
}


# --- Lógica Principal ---
echo "Iniciando a instalação do Nautilus LibreOffice Converter..."
echo ""

# 1. Verifica se as dependências estão instaladas
print_info "Verificando dependências..."
if ! command -v libreoffice &> /dev/null; then
    print_error "ERRO: O comando 'libreoffice' não foi encontrado."
    print_error "Por favor, instale o LibreOffice e tente novamente."
    exit 1
fi
if ! dpkg -s python3-nautilus &>/dev/null && ! pacman -Q python-nautilus &>/dev/null && ! dnf -q list installed nautilus-python &>/dev/null; then
    print_error "ERRO: A dependência 'python-nautilus' não parece estar instalada."
    print_error "Instale-a com o gerenciador de pacotes da sua distribuição e tente novamente."
    print_error "(e.g., sudo apt install python3-nautilus OR sudo pacman -S python-nautilus)"
    exit 1
fi
print_success "Dependências encontradas."
echo ""

# 2. Verifica se o arquivo da extensão está presente
if [ ! -f "$EXT_SOURCE_FILE" ]; then
    print_error "ERRO: O arquivo '$EXT_SOURCE_FILE' não foi encontrado."
    print_error "Certifique-se de que você está executando este script no mesmo diretório que o arquivo da extensão."
    print_error "Se você clonou o repositório, ele deveria estar aqui. Visite $PROJECT_URL para mais ajuda."
    exit 1
fi

# 3. Cria o diretório de destino
if [ ! -d "$EXT_DEST_DIR" ]; then
    print_info "Criando o diretório de extensões em '$EXT_DEST_DIR'..."
    mkdir -p "$EXT_DEST_DIR"
    if [ $? -ne 0 ]; then
        print_error "Falha ao criar o diretório. Verifique as permissões."
        exit 1
    fi
fi

# 4. Copia o script para o diretório do Nautilus
print_info "Copiando '$EXT_SOURCE_FILE' para '$EXT_DEST_DIR'..."
cp -f "$EXT_SOURCE_FILE" "$EXT_DEST_DIR/"
if [ $? -ne 0 ]; then
    print_error "Falha ao copiar o arquivo. Verifique as permissões."
    exit 1
fi
echo ""

# 5. Finalização
print_success "================================================"
print_success "  Instalação concluída com sucesso! 🎉"
print_success "================================================"
echo ""
print_info "Para ativar a extensão, você PRECISA reiniciar o Nautilus."
print_info "Você pode fazer isso executando o seguinte comando no seu terminal:"
echo "nautilus -q"
echo ""

exit 0
