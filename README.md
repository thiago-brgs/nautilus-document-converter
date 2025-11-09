# Nautilus LibreOffice Converter

Uma extensão para o gerenciador de arquivos Nautilus que adiciona um menu de contexto para converter formatos de documentos, planilhas e apresentações usando o poder do LibreOffice.

---

## ✨ Funcionalidades

*   **Integração Nativa:** Adiciona um submenu "Converter com LibreOffice" diretamente no menu de clique com o botão direito do Nautilus.
*   **Conversão Inteligente:** Mostra apenas os formatos de destino relevantes para o tipo de arquivo selecionado (documento, planilha ou apresentação).
*   **Suporte a Múltiplos Formatos:** Converte de e para os formatos mais comuns do Microsoft Office e LibreOffice.
*   **Conversão em Lote:** Selecione vários arquivos da mesma categoria e converta todos de uma só vez.

---

## ⚙️ Dependências

Para que esta extensão funcione, você precisa ter os seguintes programas instalados:

1.  **LibreOffice:** O motor por trás de todas as conversões.
2.  **Python 3 bindings for Nautilus:** O pacote que permite que o Nautilus execute extensões em Python.

---

## 🚀 Instalação

Existem duas maneiras de instalar: uma automática (recomendada) e uma manual.

### Método Automático (Recomendado)

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/thiago-brgs/https://github.com/thiago-brgs/nautilus-document-converter
    cd ~/nautilus-document-converter 
    ```
    
2.  **Execute o script de instalação:**
    ```bash
    ./install.sh
    ```
    O script cuidará de tudo para você.

3.  **Reinicie o Nautilus:**
    ```bash
    nautilus -q
    ```

### Método Manual

1.  **Baixe o arquivo:** Faça o download ou clone o arquivo `LibreOfficeConverter.py` deste repositório.

2.  **Instale as dependências:**
    *   **Debian/Ubuntu:** `sudo apt update && sudo apt install libreoffice python3-nautilus`
    *   **Arch Linux:** `sudo pacman -S libreoffice-fresh python-nautilus`
    *   **Fedora:** `sudo dnf install libreoffice nautilus-python`

3.  **Copie o arquivo da extensão:**
    Crie o diretório se ele não existir e copie o arquivo para lá.
    ```bash
    mkdir -p ~/.local/share/nautilus-python/extensions/
    cp LibreOfficeConverter.py ~/.local/share/nautilus-python/extensions/
    ```

4.  **Reinicie o Nautilus:**
    ```bash
    nautilus -q
    ```

---

## 📖 Uso

Após a instalação e reinicialização do Nautilus:

1.  Abra o gerenciador de arquivos.
2.  Clique com o botão direito em um ou mais arquivos de documento, planilha ou apresentação.
3.  Navegue até o submenu **"Converter com LibreOffice"**.
4.  Clique no formato de destino desejado.

O arquivo convertido será salvo no mesmo diretório do arquivo original.

---

## ⚖️ Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
